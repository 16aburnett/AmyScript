# The Amy Programming Language Interpreter 
# By Amy Burnett
# October 29 2020
##########################################################################
# Imports

import sys
import shlex
import re
from memory import Heap
from memory import printheap

##########################################################################
# Globals/Constants

##########################################################################


WORD = 0
INT = 1
FLOAT = 2
BOOL = 3
STRING = 4
ERROR = 5
NAMESPACE = 6
MEMORY = 7
DELIMITERS = " \t\n"

class CommandComponent:
    def __init__(self, type, value):
        self.type = type 
        self.value = value
class MemoryComponent(CommandComponent):
    def __init__(self, ptr, offset):
        self.type = MEMORY
        self.pointer = ptr
        self.offset = offset
class Lexer:
    def __init__(self, source:str):
        self.source = source.strip()
        self.index = 0
    def getToken(self) -> CommandComponent:
        # grab next component
        while self.index < len(self.source):
            # possibly a word or boolean value
            if re.match("[a-zA-Z_]", self.source[self.index]):
                token = [self.source[self.index]]
                self.index += 1
                # read alphanumerics
                while self.index < len(self.source) and re.match("[a-zA-Z0-9_]", self.source[self.index]):
                    token += [self.source[self.index]]
                    self.index += 1
                # memory accessor
                if self.index < len(self.source) and self.source[self.index] == "[":
                    self.index += 1 
                    # possibly a word
                    if self.index < len(self.source) and re.match("[a-zA-Z_]", self.source[self.index]):
                        offset = [self.source[self.index]]
                        self.index += 1
                        # grab other letters for var
                        while self.index < len(self.source) and re.match("[a-zA-Z0-9_]", self.source[self.index]):
                            offset += [self.source[self.index]]
                            self.index += 1
                        # ensure next thing is ]
                        if self.index >= len(self.source) or self.source[self.index] != "]":
                            return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                        self.index += 1
                        # ensure next is space - if there is next
                        if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                            return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                        return MemoryComponent("".join(token), "".join(offset))
                    # possibly an int
                    if self.index < len(self.source) and re.match("[0-9-]", self.source[self.index]):
                        offset = [self.source[self.index]]
                        self.index += 1
                        # grab other letters for var
                        while self.index < len(self.source) and re.match("[0-9]", self.source[self.index]):
                            offset += [self.source[self.index]]
                            self.index += 1
                        # ensure next thing is ]
                        if self.index >= len(self.source) or self.source[self.index] != "]":
                            return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                        self.index += 1
                        # ensure next is space - if there is next
                        if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                            return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                        return MemoryComponent("".join(token), int("".join(offset)))
                # ensure next is space - if there is next
                if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                    return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                token = "".join(token)
                # boolean 
                if token == "true" or token == "false":
                    return CommandComponent(BOOL, bool(token))
                # return word component
                return CommandComponent(WORD, token)

            # possibly a number 
            if re.match("[0-9-]", self.source[self.index]):
                token = [self.source[self.index]]
                self.index += 1
                # grab left of decimal
                while self.index < len(self.source) and re.match("[0-9_]", self.source[self.index]):
                    token += [self.source[self.index]]
                    self.index += 1
                # float
                if self.index < len(self.source) and self.source[self.index] == ".":
                    token += ["."]
                    self.index += 1
                    # grab right of decimal
                    while self.index < len(self.source) and re.match("[0-9_]", self.source[self.index]):
                        token += [self.source[self.index]]
                        self.index += 1
                    return CommandComponent(FLOAT, float("".join(token)))
                # ensure next is space
                if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                    return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                # ensure that the only thing captured wasnt '-'
                if "".join(token) == '-':
                    return CommandComponent(ERROR, f"Unexpected '-' for line '{self.source}'")
                return CommandComponent(INT, int("".join(token)))
            
            # strings
            if self.source[self.index] == "\"":
                token = []
                self.index += 1
                while self.index < len(self.source) and self.source[self.index] != "\"":
                    token += [self.source[self.index]]
                    self.index += 1
                # no ending quotation marks
                if self.index >= len(self.source):
                    return CommandComponent(ERROR, f"Line ended without closing double quotes in {self.source}")
                # index should be at the ending quotation mark
                self.index += 1
                # ensure next position is whitespace or the end
                if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                    return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")
                # string successfully matched
                return CommandComponent(STRING, "".join(token))

            self.index += 1
        return CommandComponent(ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}")

    def hasToken(self) -> bool:
        return self.index < len(self.source)


##########################################################################

class RecordInstance:

    def __init__(self, start_index:int):
        self.index = start_index
        self.variables = {}
        self.records = {}
        self.numParams = 0
        self.paramlabels = []

class Record:

    def __init__(self, start_index:int, function_name):
        self.start_index = start_index
        self.variables = {}
        self.records = {
            function_name : self
        }
        self.numParams = 0
        self.paramlabels = []
        self.returnedToVar = None
    
    def getInstance(self):
        ri = RecordInstance(self.start_index)
        ri.variables = dict(self.variables)
        ri.records = dict(self.records)
        ri.numParams = self.numParams
        ri.paramlabels = list(self.paramlabels)
        return ri 

##########################################################################

# ensure file was provided 
if len(sys.argv) != 2:
    print("Please provide a file_name")

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

    stack[-1].index += 1




print("*** End of program ***")

##########################################################################
