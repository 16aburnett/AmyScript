# The Amy Programming Language Interpreter 
# By Amy Burnett
# November 5 2020
##########################################################################
# Imports

import sys
from lexer import *
from memory import Heap
from memory import printheap
from stack import Record, RecordInstance

##########################################################################
# Globals/Constants

##########################################################################

# ensure file was provided 
if len(sys.argv) != 2:
    print("Please provide a file_name")
    exit()

# read code from file 
file_name = sys.argv[1]
lines = []
with open(file_name, "r") as file:
    lines = file.readlines()

# remove any comments and empty lines
for i in range(len(lines)-1, -1, -1):
    lines[i] = lines[i].strip()
    if lines[i].startswith("//"):
        lines.pop(i)
    elif lines[i] == "":
        lines.pop(i)

# index start and end points for blocks of code 

# lex each line
code = []
for line in lines:
    lexer = Lexer(line)
    components = []
    while lexer.hasToken():
        component = lexer.getToken()

        # report errors in parsing
        if component.type == ERROR:
            print(component.value)
            exit()

        components += [component]
    code += [components]


heap = Heap()
stack = []

# build the record for main
main = Record(0, "__main__")
main.variables = {"ARGV" : sys.argv}
maininstance = main.getInstance()
stack.append(maininstance)

# evaluate lines
while stack[-1].index < len(code):

    print(f"{stack[-1].index} {lines[stack[-1].index]}")

    # command name not first 
    if code[stack[-1].index][0].type != WORD:
        print("Lines must start with a Command Name")

    elif code[stack[-1].index][0].value == "ASSIGN":
        # parse components
        cmd, varname, value = code[stack[-1].index]

        # ensure varname is a word
        if varname.type != WORD and varname.type != MEMORY:
            print("Expected <word> but got", varname.type)
            print(code[stack[-1].index])
            exit()

        # Case 1: value is another variable 
        if value.type == WORD:
            # Ensure it is a valid variable
            if value.value not in stack[-1].variables:
                print(f"{value.value} referenced before assignment\nLine: {lines[stack[-1].index]}") 
                exit()
            # assign value to varname
            # Case 1: varname is var
            if varname.type == WORD:
                stack[-1].variables[varname.value] = stack[-1].variables[value.value]
            # Case 2: varname is memory addr
            elif varname.type == MEMORY:
                heap.memory[stack[-1].variables[varname.pointer]+varname.offset] = stack[-1].variables[value.value]

        # Case 2: value is immediate data
        else:
            # Case 1: varname is var
            if varname.type == WORD:
                stack[-1].variables[varname.value] = value.value
            # Case 2: varname is memory addr
            elif varname.type == MEMORY:
                heap.memory[stack[-1].variables[varname.pointer]+varname.offset] = value.value

    elif code[stack[-1].index][0].value == "ADD":
        cmd, varname1, varname2, into, varname3 = code[stack[-1].index]

        # ensure into keyword
        if into.type != WORD or into.value != "INTO":
            print("Expected INTO keyword but got", into.value)
            print(code[stack[-1].index])
            exit()

        # ensure varname3 is a word
        if varname3.type != WORD:
            print("Expected <word> but got", varname.type)
            print(code[stack[-1].index])
            exit()

        # Case 1: varname1 is a var
        if varname1.type == WORD:
            # ensure varname1 is a valid var
            if varname1.value not in stack[-1].variables:
                print(f"{varname1.value} referenced before assignment\nLine: {lines[stack[-1].index]}") 
                exit()
            # Case 1a: varname2 is a var
            if varname2.type == WORD:
                # ensure varname2 is a valid var
                if varname2.value not in stack[-1].variables:
                    print(f"{varname2.value} referenced before assignment\nLine: {lines[stack[-1].index]}") 
                    exit()
                # perform add
                stack[-1].variables[varname3.value] = stack[-1].variables[varname1.value] + stack[-1].variables[varname2.value]
            # Case 1b: varname2 is immediate
            else:
                stack[-1].variables[varname3.value] = stack[-1].variables[varname1.value] + varname2.value

        # Case 2: varname1 is immediate data
        else:
            # Case 2a: varname2 is a var
            if varname2.type == WORD:
                # ensure varname2 is a valid var
                if varname2.value not in stack[-1].variables:
                    print(f"{varname2.value} referenced before assignment\nLine: {lines[stack[-1].index]}") 
                    exit()
                # perform add
                stack[-1].variables[varname3.value] = varname1.value + stack[-1].variables[varname2.value]
            # Case 2b: varname2 is immediate
            else:
                stack[-1].variables[varname3.value] = varname1.value + varname2.value

    elif code[stack[-1].index][0].value == "PRINT":
        cmd, varname = code[stack[-1].index]

        # Case 1: varname is var
        if varname.type == WORD:
            # ensure var exists
            if varname.value not in stack[-1].variables:
                print(f"{varname.value} referenced before assignment\nLine: {lines[stack[-1].index]}")  
                exit()
            print(stack[-1].variables[varname.value])
        # Case 2: varname is immediate 
        else:
            print(varname.value)

    # function definitions
    elif code[stack[-1].index][0].value == "FUNCTION":
        cmd, fname, *params = code[stack[-1].index]

        # build record for new function
        record = Record(stack[-1].index, fname.value)

        # Ensure all parameters are words

        # count and add parameter labels
        record.numParams = len(params)
        plabels = []
        for param in params:
            plabels += [param.value]
        record.paramlabels = plabels

        # add function to this record
        stack[-1].records[fname.value] = record

        # skip through definition - dont eval code
        print("... Skipping Function Definition ...")
        while stack[-1].index < len(code) and code[stack[-1].index][0].value != "ENDFUNCTION":
            stack[-1].index += 1
        
        # ensure end of function was found
        if stack[-1].index >= len(code):
            print(f"function '{fname.value}' does not have a matching 'endfunction'")
            exit()

    # calling functions
    elif code[stack[-1].index][0].value == "CALL":
        cmd, fname, *args = code[stack[-1].index]

        # Ensure function exists
        if fname.value not in stack[-1].records:
            print(f"function '{fname.value}' is not defined")  

        # get function's record
        record = stack[-1].records[fname.value]

        # ensure INTO keyword
        params = []
        retvar = None
        i = 0
        while i < len(args):
            if args[i].value == "INTO":
                retvar = args[i+1]
                break
            else:
                params += [args[i]]
            i+=1

        # assign stacks awaiting var 
        stack[-1].returnedToVar = retvar.value
        
        # Ensure the corrent number of parameters
        if len(params) != record.numParams:
            print(f"Incorrect number of parameters,\nexpected {record.numParams} but got {len(params)} for line\n {lines[stack[-1].index]}")
            exit()

        # Generate record instance
        instance = record.getInstance()
        
        # Add parameters to record instance
        for i in range(len(params)):
            # param is var
            if params[i].type == WORD:
                instance.variables[instance.paramlabels[i]] = stack[-1].variables[params[i].value]
            # Immediate 
            else:
                instance.variables[instance.paramlabels[i]] = params[i].value

        # push record instance onto the stack
        stack.append(instance)

    # returning from functions
    elif code[stack[-1].index][0].value == "RETURN":
        cmd, retval = code[stack[-1].index]

        returnedValue = 0

        # Case 1: retval is var
        if retval.type == WORD:
            # ensure retval exists
            if retval.value not in stack[-1].variables:
                print(f"{varname.value} referenced before assignment\nLine: {lines[stack[-1].index]}")
                exit()
            
            returnedValue = stack[-1].variables[retval.value]
        
        # Case 2: retval is immediate
        else:
            returnedValue = retval.value

        # pop off the stack 
        # to return to where the function was called
        stack.pop()

        # ensure caller was expecting a value
        if stack[-1].returnedToVar != None:
            stack[-1].variables[stack[-1].returnedToVar] = returnedValue

    # allocating data on heap
    elif code[stack[-1].index][0].value == "MALLOC":
        cmd, varname, size = code[stack[-1].index]

        # allocate space on heap 
        stack[-1].variables[varname.value] = heap.malloc(size.value)

        printheap(heap)

    # deallocating data on heap
    elif code[stack[-1].index][0].value == "FREE":
        cmd, varname = code[stack[-1].index]

        # allocate space on heap 
        heap.free(stack[-1].variables[varname.value])

    else:
        print("UNKNOWN command! Yikes there bud!")
        exit()

    stack[-1].index += 1




print("*** End of program ***")

##########################################################################
