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

# OPCODES
OPCODE_ASSIGN      = 0
OPCODE_MALLOC      = 1
OPCODE_FREE        = 2
OPCODE_ADD         = 3
OPCODE_SUBTRACT    = 4
OPCODE_MULTIPLY    = 5
OPCODE_DIVIDE      = 6
OPCODE_MOD         = 7
OPCODE_PRINT       = 8
OPCODE_INPUT       = 9
OPCODE_HALT        = 10
OPCODE_FUNCTION    = 11
OPCODE_ENDFUNCTION = 12
OPCODE_CALL        = 13
OPCODE_RETURN      = 14
OPCODE_RESPONSE    = 15
OPCODE_IF          = 16
OPCODE_ELIF        = 17
OPCODE_ELSE        = 18
OPCODE_ENDIF       = 19
OPCODE_JUMP        = 20
OPCODE_EQUAL       = 21
OPCODE_PRINTLN     = 22
OPCODE_AND         = 23
OPCODE_OR          = 24
OPCODE_NOT         = 25
toOpCode = {
    "ASSIGN"      : OPCODE_ASSIGN,
    "MALLOC"      : OPCODE_MALLOC,
    "FREE"        : OPCODE_FREE,
    "ADD"         : OPCODE_ADD,
    "SUBTRACT"    : OPCODE_SUBTRACT,
    "MULTIPLY"    : OPCODE_MULTIPLY,
    "DIVIDE"      : OPCODE_DIVIDE,
    "MOD"         : OPCODE_MOD,
    "PRINT"       : OPCODE_PRINT,
    "INPUT"       : OPCODE_INPUT,
    "HALT"        : OPCODE_HALT,
    "FUNCTION"    : OPCODE_FUNCTION,
    "ENDFUNCTION" : OPCODE_ENDFUNCTION,
    "CALL"        : OPCODE_CALL,
    "RETURN"      : OPCODE_RETURN,
    "RESPONSE"    : OPCODE_RESPONSE,
    "IF"          : OPCODE_IF,
    "ELIF"        : OPCODE_ELIF,
    "ELSE"        : OPCODE_ELSE,
    "ENDIF"       : OPCODE_ENDIF,
    "EQUAL"       : OPCODE_EQUAL,
    "PRINTLN"     : OPCODE_PRINTLN,
    "AND"         : OPCODE_AND,
    "OR"          : OPCODE_OR,
    "NOT"         : OPCODE_NOT
}

# PARAM MODES
MODE_IMMEDIATE = 0 # value represent data
MODE_STACK     = 1 # value is a stack address (aka a variable/function)
MODE_MEMORY    = 2 # value is a heap address 
MODE_STRING    = 3 # value is a string literal

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

### Convert to IntCode ###################################################
# this translates each line into a list of integers
#  to more easily parse each line

# Variable name to Int mapping
# This does not care about scope 
wordToInt = {}
wordId = 0
code = []
for line in lines:
    lexer = Lexer(line)
    code_line = []

    # all lines start with a command
    # convert to opcode
    type, value = lexer.getToken()
    if type != WORD:
        print(f"lines should start with a word \n {line}")
        exit(1)
    # ensure valid command
    if value not in toOpCode:
        print(f"'{value}' is not a command")
        exit(1)
    code_line += [toOpCode[value]]

    # convert the arguments to integers
    while lexer.hasToken():
        type, *values = lexer.getToken()

        # report errors in parsing
        if type == ERROR:
            print(values[0])
            exit()
        # immediate
        if type == INT or type == FLOAT:
            code_line += [MODE_IMMEDIATE, values[0]]
        # string literal
        elif type == STRING:
            code_line += [MODE_STRING, values[0]]
        # var/func
        elif type == WORD:
            # var DNE
            if values[0] not in wordToInt:
                wordToInt[values[0]] = wordId
                wordId += 1
            code_line += [MODE_STACK, wordToInt[values[0]]]
        # memory 
        elif type == MEMORY:
            code_line += [MODE_MEMORY]
            # pointer is immediate
            if values[0] == INT or values[0] == FLOAT:
                code_line += [MODE_IMMEDIATE, values[1]]
                # offset is immediate
                if values[2] == INT or values[2] == FLOAT:
                    code_line += [MODE_IMMEDIATE, values[3]]
                else:
                    # var DNE
                    if values[3] not in wordToInt:
                        wordToInt[values[3]] = wordId
                        wordId += 1
                    code_line += [MODE_STACK, wordToInt[values[3]]]
            # pointer is a var
            else:
                # var DNE
                if values[1] not in wordToInt:
                    wordToInt[values[1]] = wordId
                    wordId += 1
                code_line += [MODE_STACK, wordToInt[values[1]]]
                # offset is immediate
                if values[2] == INT or values[2] == FLOAT:
                    code_line += [MODE_IMMEDIATE, values[3]]
                else:
                    # var DNE
                    if values[3] not in wordToInt:
                        wordToInt[values[3]] = wordId
                        wordId += 1
                    code_line += [MODE_STACK, wordToInt[values[3]]]
    # add line to code list
    code += [code_line]

### Add Control Flow Jumps ###############################################

def addControlFlowJumps(i, awaiting_endif=[]):

    prev_if = i-1

    while (i < len(code)):

        # print(f"[{i}] {code[i]} {lines[i]}")

        if code[i][0] == OPCODE_IF:
            # print("found if")
            i = addControlFlowJumps (i+1)
        elif code[i][0] == OPCODE_ELIF:
            # print("found elif")
            # add finishing jump for endif 
            code.insert(i, [OPCODE_JUMP])
            lines.insert(i, "JUMP")
            i += 1
            # save this elif position to prev if/elif
            code[prev_if] += [MODE_IMMEDIATE, i]
            return addControlFlowJumps(i+1, awaiting_endif+[i-1])
        elif code[i][0] == OPCODE_ELSE:
            # print("found else")
            # add finishing jump for endif 
            code.insert(i, [OPCODE_JUMP])
            lines.insert(i, "JUMP")
            i += 1
            # save this elif position to prev if/elif
            code[prev_if] += [MODE_IMMEDIATE, i]
            return addControlFlowJumps(i+1, awaiting_endif+[i-1])
        elif code[i][0] == OPCODE_ENDIF:
            # print("found end")
            # add this position to all awaiting terminal jumps
            for j in awaiting_endif:
                code[j] += [MODE_IMMEDIATE, i]
                lines[j] += " to " + str(i)
            # save this elif position to prev if/elif/else
            code[prev_if] += [MODE_IMMEDIATE, i]
            return i
        i += 1
    
    return i 

addControlFlowJumps(0)


### Print Code ###########################################################

# print("=== Code ========================================================")
# for i in range(len(code)):
#     print(f"[{i}] {code[i]} {lines[i]}")

### Save IntCode #########################################################

def padzeros(i, maxdigits):
    stri = str(i)
    while len(stri) < maxdigits:
        stri = "".join(["0",stri])
    return stri

with open(file_name+"c", "w") as outfile:
    maxdigits = len(str(len(code)))
    for i in range(len(code)):
        outfile.write(f"{padzeros(i, maxdigits)} {code[i]} {lines[i]}\n")

with open(file_name+"i", "w") as outfile:
    for i in range(len(code)):
        outfile.write(f"{code[i][0]}")
        for j in range(1, len(code[i])):
            if isinstance(code[i][j], str):
                outfile.write(f", \"{code[i][j]}\"")
            else:
                outfile.write(f", {code[i][j]}")
        outfile.write("\n")

### Set up the stack and heap ############################################

heap = Heap()
stack = []

# build the record for main
main = Record(0, "__main__")
main.variables = {"ARGV" : sys.argv}
maininstance = main.getInstance()
stack.append(maininstance)

### Execute The Code #####################################################

def getVariableValue(stack, var):

    # Ensure variable exists
    if var not in stack[-1].variables:
        print(f"variable referenced before assignment - '{var}'")
        exit(1)
    
    return stack[-1].variables[var]

def getMemAddress(stack, pmode, pointer, omode, offset) -> int:

    # Ensure pointer mode is stack variable
    if pmode != MODE_STACK:
        print("pmode must be stack variable")
        exit(1)

    # grab pointer value
    address = getVariableValue(stack, pointer)

    # add offset
    if omode == MODE_STACK:
        
        address += getVariableValue(stack, offset)
    else:
        address += offset
    
    return address

def getNextValue(heap, stack, params, i, reject=[]):
    """Returns the next parameter value whether the parameter mode
    is MODE_MEMORY, MODE_STACK, MODE_IMMEDIATE, or MODE_STRING

    Params:
    - heap - the heap for getting memory values
    - stack - the stack for getting variable values
    - params - a list of code parameters to parse the next value out of
    - reject - a list of modes to reject if they are found next 
    """
    # Case 1: Memory
    if params[i] == MODE_MEMORY and MODE_MEMORY not in reject:
        # next 4 nums make up the pointer and offset
        pmode, pointer, omode, offset = params[i+1:i+5]
        address = getMemAddress(stack, pmode, pointer, omode, offset)
        return heap.memory[address], i+5
    
    # Case 2: Stack variable
    elif params[i] == MODE_STACK and MODE_STACK not in reject:
        return getVariableValue(stack, params[i+1]), i+2
    
    # Case 3: Immediate Variable
    elif params[i] == MODE_IMMEDIATE and MODE_IMMEDIATE not in reject:
        return params[i+1], i+2

    # Case 4: String Literal
    elif params[i] == MODE_STRING and MODE_STRING not in reject:
        # treat it as an immediate value 
        #   for now
        return params[i+1], i+2

        # # Allocate space on heap for string
        # string = params[i+1]
        # string_address = heap.malloc(len(string)+1)
        # # copy string into memory
        # for j in range(len(string)):
        #     heap.memory[string_address+j] = string[j]
        # # Null terminated 
        # heap.memory[string_address + len(string)] = "\0"
        # return string_address, i+2
    # Case 5: Unknown mode
    print("Bad Parameter Mode")
    exit(1)

# evaluate lines
while stack[-1].index < len(code):

    # print(f"[{stack[-1].index}] {code[stack[-1].index]} {lines[stack[-1].index]}")

    cmd, *params = code[stack[-1].index] 


    if cmd == OPCODE_ASSIGN:
        # ASSIGN dest src
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            # Assign src to dest 
            heap.memory[address], i = getNextValue(heap, stack, params, 5)
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            # Assign src to dest
            stack[-1].variables[params[1]], i = getNextValue(heap, stack, params, 2)
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_ADD:
        # ADD dest src1 src2
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = src1 + src2
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = src1 + src2
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_SUBTRACT:
        # SUBTRACT dest src1 src2
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = src1 - src2
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = src1 - src2
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_MULTIPLY:
        # MULTIPLY dest src1 src2
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = src1 * src2
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = src1 * src2
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_DIVIDE:
        # DIVIDE dest src1 src2
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = src1 / src2
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = src1 / src2
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_MOD:
        # MOD dest src1 src2
        # Case 1: Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = src1 % src2
        # Case 2: Stack variable
        elif params[0] == MODE_STACK:
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = src1 % src2
        # Case 3: Invalid param type
        else:
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_PRINT:
        # Only One Parameter
        value, _ = getNextValue(heap, stack, params, 0)
        print(value, end="")
    elif cmd == OPCODE_PRINTLN:
        # PRINTLN 
        # PRINTLN value
        if len(params) == 0:
            print()
        else:
            value, _ = getNextValue(heap, stack, params, 0)
            print(value)
    # function definitions
    elif cmd == OPCODE_FUNCTION:

        if params[0] != MODE_STACK:
            print(f"function name must be a stack variable")
            exit(1)

        fname = params[1]

        # build record for new function
        record = Record(stack[-1].index, fname)

        # Ensure all parameters are words

        # add parameter labels
        record.numParams = 0
        plabels = []
        i = 2
        while i < len(params):
            # ensure param mode is stack var
            if params[i] != MODE_STACK:
                print(f"function def must have variable names")
                exit(1)
            plabels += [params[i+1]]
            i += 2
            record.numParams += 1
        record.paramlabels = plabels

        # add capture value of surrounding scope
        # this copies all values seen before the function def
        # however, if a variable is modified after function def,
        # then the variable is not updated for the function
        # **this should be changed to match C++
        # -> existing vars are updated 
        for param_name in stack[-1].variables:
            record.variables[param_name] = stack[-1].variables[param_name]

        # add function to this record
        stack[-1].records[fname] = record

        # skip through definition - dont eval code
        # print("... Skipping Function Definition ...")
        while stack[-1].index < len(code) and (code[stack[-1].index][0] != OPCODE_ENDFUNCTION or code[stack[-1].index][2] != fname):
            stack[-1].index += 1
        
        # ensure end of function was found
        if stack[-1].index >= len(code):
            print(f"function '{fname}' does not have a matching 'endfunction'")
            exit()

    # calling functions
    elif cmd == OPCODE_CALL:

        if params[0] != MODE_STACK:
            print(f"function name must be a stack variable")
            exit(1)

        fname = params[1]

        # Ensure function exists
        if fname not in stack[-1].records:
            print(f"function '{fname}' is not defined")  

        # get function's record
        record = stack[-1].records[fname]

        # Generate record instance
        instance = record.getInstance()
        
        # Add parameters to record instance
        j = 2
        for i in range(len(instance.paramlabels)):
            
            # ensure there are enough parameters
            if j > len(params):
                print(f"Not enough parameters : function needs {len(instance.paramlabels)} parameters")
                exit(1)

            instance.variables[instance.paramlabels[i]], j = getNextValue(heap, stack, params, j)

        # ensure there weren't too many parameters
        if j < len(params):
            print(f"Too many parameters : function needs {len(instance.paramlabels)} parameters {j}")
            exit(1)

        # push record instance onto the stack
        stack.append(instance)

    # returning from functions
    elif cmd == OPCODE_RETURN:
        # RETURN value
        returnedValue, i = getNextValue(heap, stack, params, 0)
        # pop off the stack 
        # to return to where the function was called
        stack.pop()
        # give caller the return value 
        stack[-1].returnedValue = returnedValue
    elif cmd == OPCODE_RESPONSE:
        # RESPONSE dest
        # Case 1 : Stack variable
        if params[0] == MODE_STACK:
            stack[-1].variables[params[1]] = stack[-1].returnedValue
        # Case 2 : Memory address
        elif params[0] == MODE_MEMORY:
            heap.memory[params[1]] = stack[-1].returnedValue
        # Case 3 : Bad token
        else:
            print(f"RESPONSE requires a stack variable or a memory address")
            exit(1)
    # allocating data on heap
    elif cmd == OPCODE_MALLOC:
        # ensure param1 is var or mem address
        if params[0] != MODE_STACK and params[0] != MODE_MEMORY:
            print(f"Expected variable or memory address - line {lines[stack[-1].index]}")
            exit(1)
        # Pointer Case1 : variable
        if params[0] == MODE_STACK:
            # variable is allowed to not exist for assigning 
            size, _ = getNextValue(heap, stack, params, 2, reject=[MODE_STRING])
            stack[-1].variables[params[1]] = heap.malloc(size)
        # Pointer Case2 : memory
        elif params[0] == MODE_MEMORY:
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            size, _ = getNextValue(heap, stack, params, 5, reject=[MODE_STRING])
            heap.memory[address] = heap.malloc(size)
        # printheap(heap)
    # deallocating data on heap
    elif cmd == OPCODE_FREE:
        # FREE pointer
        pointer, _ = getNextValue(heap, stack, params, 0)
        # allocate space on heap 
        heap.free(pointer)
    # Control flow
    elif cmd == OPCODE_IF:
        # IF cond destIfFalse
        cond, i = getNextValue(heap, stack, params, 0)
        destIfFalse, i = getNextValue(heap, stack, params, i)
        # condition is false
        if cond == 0:
            # jump to next elif or else
            stack[-1].index = destIfFalse
            continue
        # if condition passes - just continue execution
    elif cmd == OPCODE_ELIF:
        # ELIF cond destIfFalse
        cond, i = getNextValue(heap, stack, params, 0)
        destIfFalse, i = getNextValue(heap, stack, params, i)
        # condition is false
        if cond == 0:
            # jump to next elif or else
            stack[-1].index = destIfFalse
            continue
        # if condition passes - just continue execution
    elif cmd == OPCODE_ELSE:
        # ELSE 
        # if reached - just execute block
        pass
    elif cmd == OPCODE_ENDIF:
        # if reached - just move on 
        pass
    elif cmd == OPCODE_JUMP:
        # JUMP dest
        dest, _ = getNextValue(heap, stack, params, 0)
        stack[-1].index = dest
    elif cmd == OPCODE_EQUAL:
        # EQUAL dest src1 src2 
        # dest = src1 == src2
        # Case1 : variable
        if params[0] == MODE_STACK:
            # variable is allowed to not exist for assigning 
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = 1 if src1 == src2 else 0
        # Case2 : memory
        elif params[0] == MODE_MEMORY:
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = 1 if src1 == src2 else 0
    elif cmd == OPCODE_AND:
        # AND dest src1 src2 
        # dest = src1 && src2
        # Case1 : variable
        if params[0] == MODE_STACK:
            # variable is allowed to not exist for assigning 
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = 1 if src1 != 0 and src2 != 0 else 0
        # Case2 : memory
        elif params[0] == MODE_MEMORY:
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = 1 if src1 != 0 and src2 != 0 else 0
    elif cmd == OPCODE_OR:
        # OR dest src1 src2 
        # dest = src1 || src2
        # Case1 : variable
        if params[0] == MODE_STACK:
            # variable is allowed to not exist for assigning 
            src1, i = getNextValue(heap, stack, params, 2)
            src2, i = getNextValue(heap, stack, params, i)
            stack[-1].variables[params[1]] = 1 if src1 != 0 or src2 != 0 else 0
        # Case2 : memory
        elif params[0] == MODE_MEMORY:
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src1, i = getNextValue(heap, stack, params, 5)
            src2, i = getNextValue(heap, stack, params, i)
            heap.memory[address] = 1 if src1 != 0 or src2 != 0 else 0
    elif cmd == OPCODE_NOT:
        # OR dest src
        # dest = ~src
        # Case1 : variable
        if params[0] == MODE_STACK:
            # variable is allowed to not exist for assigning 
            src, i = getNextValue(heap, stack, params, 2)
            stack[-1].variables[params[1]] = 1 if src == 0 else 0
        # Case2 : memory
        elif params[0] == MODE_MEMORY:
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            src, i = getNextValue(heap, stack, params, 5)
            heap.memory[address] = 1 if src == 0 else 0
    elif cmd == OPCODE_HALT:
        break
    else:
        print("UNKNOWN command! Yikes there bud!")
        exit(1)

    stack[-1].index += 1


# printheap(heap)

# print("*** End of program ***")

##########################################################################
