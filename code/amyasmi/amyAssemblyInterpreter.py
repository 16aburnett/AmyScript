# The Amy Programming Language Interpreter 
# By Amy Burnett
# November 30 2020
##########################################################################
# Imports

import sys
from sys import exit

if __name__ == "__main__":
    from lexer import *
    from memory import Heap
    from memory import printheap
    from memory import MEMORY_NULL
else:
    from .lexer import *
    from .memory import Heap
    from .memory import printheap
    from .memory import MEMORY_NULL

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
OPCODE_PRINTLN     = 9
OPCODE_INPUT       = 10
OPCODE_HALT        = 11
OPCODE_CALL        = 12
OPCODE_RETURN      = 13
OPCODE_RESPONSE    = 14
OPCODE_JUMP        = 15
OPCODE_JUMPLT      = 16
OPCODE_JUMPLE      = 17
OPCODE_JUMPEQ      = 18
OPCODE_JUMPNEQ     = 19
OPCODE_JUMPGE      = 20
OPCODE_JUMPGT      = 21
OPCODE_EQUAL       = 22
OPCODE_NEQUAL      = 23
OPCODE_LT          = 24
OPCODE_LE          = 25
OPCODE_GT          = 26
OPCODE_GE          = 27
OPCODE_COMPARE     = 28
OPCODE_AND         = 29
OPCODE_OR          = 30
OPCODE_NOT         = 31
OPCODE_SIZEOF      = 32
OPCODE_PUSH        = 33
OPCODE_POP         = 34
OPCODE_STACKGET    = 35
OPCODE_FtoI        = 36 # float to int
OPCODE_ItoF        = 37 # int to float
OPCODE_STRING      = 38 # int/float to string
OPCODE_StoF        = 39 # string to float
OPCODE_StoI        = 40 # string to int 
OPCODE_CtoI        = 41 # char to int 
toOpCode = {
    "assign"      : OPCODE_ASSIGN,
    "malloc"      : OPCODE_MALLOC,
    "free"        : OPCODE_FREE,
    "add"         : OPCODE_ADD,
    "subtract"    : OPCODE_SUBTRACT,
    "multiply"    : OPCODE_MULTIPLY,
    "divide"      : OPCODE_DIVIDE,
    "mod"         : OPCODE_MOD,
    "print"       : OPCODE_PRINT,
    "input"       : OPCODE_INPUT,
    "halt"        : OPCODE_HALT,
    "call"        : OPCODE_CALL,
    "return"      : OPCODE_RETURN,
    "response"    : OPCODE_RESPONSE,
    "jump"        : OPCODE_JUMP,
    "jlt"         : OPCODE_JUMPLT,
    "jle"         : OPCODE_JUMPLE,
    "jeq"         : OPCODE_JUMPEQ,
    "jneq"        : OPCODE_JUMPNEQ,
    "jge"         : OPCODE_JUMPGE,
    "jgt"         : OPCODE_JUMPGT,
    "equal"       : OPCODE_EQUAL,
    "nequal"      : OPCODE_NEQUAL,
    "lt"          : OPCODE_LT,
    "le"          : OPCODE_LE,
    "gt"          : OPCODE_GT,
    "ge"          : OPCODE_GE,
    "cmp"         : OPCODE_COMPARE,
    "println"     : OPCODE_PRINTLN,
    "sizeof"      : OPCODE_SIZEOF,
    "and"         : OPCODE_AND,
    "or"          : OPCODE_OR,
    "not"         : OPCODE_NOT,
    "push"        : OPCODE_PUSH,
    "pop"         : OPCODE_POP,
    "stackget"    : OPCODE_STACKGET,
    "ftoi"        : OPCODE_FtoI,
    "itof"        : OPCODE_ItoF,
    "string"      : OPCODE_STRING,
    "stof"        : OPCODE_StoF,
    "stoi"        : OPCODE_StoI,
    "ctoi"        : OPCODE_CtoI
}

# PARAM MODES
MODE_IMMEDIATE = 0 # value represent data
MODE_STACK     = 1 # value is a stack address (aka a variable/function)
MODE_MEMORY    = 2 # value is a heap address 
MODE_JUMPPOINT = -1

##########################################################################

class AmyAssemblyInterpreter:

    def __init__(self, file_name=""):
        self.file_name = file_name
        self.output_combined = False
        self.output_intcode = False
        self.debug = False

    def execute (self, inputCode):

        def padzeros(i, maxdigits):
            stri = str(i)
            while len(stri) < maxdigits:
                stri = "".join(["0",stri])
            return stri

        # read code from file 
        # file_name = sys.argv[1]
        lines = inputCode.splitlines ()
        # with open(file_name, "r") as file:
        #     lines = file.readlines()

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
        # this holds the reverse mapping 
        # for outputting the variable's string name in error messages 
        intToWord = {}
        wordId = 0
        # stores all the jump points (label, instruction)
        # this populates the initial stack frame 
        # and treats the labels as variables that store their instruction pointer
        jumpPoints = {}
        code = []
        lineNo = -1
        for line in lines:
            # advance lineNo
            lineNo += 1

            # tokenize line
            lexer = Lexer(line)
            code_line = []

            type, value = lexer.getToken()
            # save jump points before executing code 
            # allows for jumps to labels that weren't executed yet 
            if type == JUMPPOINT:
                # var DNE
                if value not in wordToInt:
                    wordToInt[value] = wordId
                    intToWord[wordId] = value 
                    wordId += 1
                # jump point already exists 
                elif wordToInt[value] in jumpPoints:
                    print (f"Error: Duplicate jump point '{value}'")
                    exit (1)
                jumpPoints[wordToInt[value]] = len(code)
                code += [[MODE_JUMPPOINT, wordToInt[value], len(code)]]
                continue
            elif type != WORD:
                print(f"lines should start with a word or jump point label \n {line}")
                exit(1)
            # ensure valid command
            if value.lower() not in toOpCode:
                print(f"'{value}' is not a command")
                exit(1)
            code_line += [toOpCode[value.lower()]]

            # convert the arguments to integers
            while lexer.hasToken():
                type, *values = lexer.getToken()

                # report errors in parsing
                if type == ERROR:
                    print(values[0])
                    exit()
                # immediate
                if type == INT or type == FLOAT or type == CHAR:
                    code_line += [MODE_IMMEDIATE, values[0]]
                # var/func
                elif type == WORD:
                    # var DNE
                    if values[0] not in wordToInt:
                        wordToInt[values[0]] = wordId
                        intToWord[wordId] = values[0]
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
                                intToWord[wordId] = values[3]
                                wordId += 1
                            code_line += [MODE_STACK, wordToInt[values[3]]]
                    # pointer is a var
                    else:
                        # var DNE
                        if values[1] not in wordToInt:
                            wordToInt[values[1]] = wordId
                            intToWord[wordId] = values[1]
                            wordId += 1
                        code_line += [MODE_STACK, wordToInt[values[1]]]
                        # offset is immediate
                        if values[2] == INT or values[2] == FLOAT:
                            code_line += [MODE_IMMEDIATE, values[3]]
                        else:
                            # var DNE
                            if values[3] not in wordToInt:
                                wordToInt[values[3]] = wordId
                                intToWord[wordId] = values[3]
                                wordId += 1
                            code_line += [MODE_STACK, wordToInt[values[3]]]
            # add line to code list
            code += [code_line]

        ### Print Code ###########################################################

        # print("=== Code ========================================================")
        # for i in range(len(code)):
        #     print(f"[{i}] {code[i]} {lines[i]}")

        ### Save Combined ########################################################

        if self.output_combined:
            with open(self.file_name+"c", "w") as outfile:
                maxdigits = len(str(len(code)))
                for i in range(len(code)):
                    outfile.write(f"{padzeros(i, maxdigits)} {code[i]} {lines[i]}\n")

        ### Save IntCode #########################################################

        if self.output_intcode:
            with open(self.file_name+"i", "w") as outfile:
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
        # create the stack 
        # starts with the program arguments
        # and variable scope for main 
        # for each stack frame, the base_pointer should point
        # to the variable dictionary 
        stack = []
        sys.argv.reverse()
        for arg in sys.argv:
            # allocate string on heap
            ptr = heap.malloc(len(arg))
            # copy string to heap 
            for i in range(len(arg)):
                heap.memory[ptr+i] = arg[i]
            # put ptr on stack 
            stack += [ptr]
        # add the first stack frame 
        #   populated with the jumpPoints 
        stack += [len(sys.argv), -1, -1, jumpPoints]
        instruction_pointer = 0
        base_pointer = len(stack)-1
        return_value = 0
        # flag states 
        lessThanFlag = 0
        equalFlag = 0
        greaterThanFlag = 0

        ### Execute The Code #####################################################
        ### Helper Functions #####################################################

        def getVariableValue(stack, var):

            # Ensure variable exists in the current scope or parent scopes
            bptr = base_pointer
            # top scope will have prev base pointer of -1
            while bptr != -1:
                # found variable in bptr's scope
                if var in stack[bptr]:
                    if isinstance(stack[bptr][var], str) and stack[bptr][var][0] == '\\':
                        return stack[bptr][var].replace ("\\n", "\n").replace ("\\t", "\t").replace ("\\r", "\r").replace ("\\b", "\b")
                    return stack[bptr][var]
                bptr = stack[bptr-1]
            
            print(f"Error: variable referenced before assignment - '{intToWord[var]}'")
            exit(1)

        def getMemAddress(stack, pmode, pointer, omode, offset) -> int:
            """Gets the absolute memory address including any offset

            """
            # Ensure pointer mode is stack variable
            if pmode != MODE_STACK:
                print("Error: ptr mode must be stack variable")
                exit(1)

            # grab pointer value
            address = getVariableValue(stack, pointer)

            # make sure pointer is not null 
            if (address == MEMORY_NULL):
                print (f"Error: Cannot read from null address")
                exit (1)

            # add offset
            if omode == MODE_STACK:
                offset = getVariableValue(stack, offset)

            # make sure offset isn't outside of address' block
            if (offset >= heap.sizeof (address)):
                # print (heap.memory[address-15:address+15], heap.memory[address])
                print (f"Error: Index out of bounds.")
                exit (1)
            
            return address+offset

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
                address = getVariableValue(stack, pointer)
                if omode == MODE_STACK:
                    offset = getVariableValue(stack, offset)

                # make sure offset isn't outside of address' block
                if (offset >= heap.sizeof (address)):
                    # print (heap.memory[address-15:address+15], "'"+heap.memory[address]+"'")
                    print (f"Error: Index out of bounds.")
                    exit (1)

                # heap address must be int
                if isinstance(address, int):
                    # make sure pointer is not null 
                    if (address == MEMORY_NULL):
                        print (f"Error: Cannot read from null address")
                        exit (1)
                    return heap.memory[address+offset], i+5
                # float is invalid
                if isinstance(address, float):
                    print("Error: float is not an address")
                    exit(1)
                # strings and lists
                else:
                    return address[offset], i+5
            
            # Case 2: Stack variable
            elif params[i] == MODE_STACK and MODE_STACK not in reject:
                return getVariableValue(stack, params[i+1]), i+2
            
            # Case 3: Immediate Variable
            elif params[i] == MODE_IMMEDIATE and MODE_IMMEDIATE not in reject:
                # convert special characters for output
                if isinstance(params[i+1], str) and params[i+1][0] == '\\':
                    # literal_eval will essentially output the string 
                    # which will convert \ chars to actual newlines, tabs, etc
                    import ast
                    params[i+1] = ast.literal_eval ("'"+params[i+1]+"'")
                    return params[i+1].replace ("\\n", "\n").replace ("\\t", "\t").replace ("\\r", "\r").replace ("\\b", "\b"), i+2
                return params[i+1], i+2

            # Case 5: Unknown mode
            print("Error: Bad Parameter Mode")
            exit(1)

        ### Evaluate Lines #######################################################

        # evaluate lines
        while instruction_pointer < len(code):

            cmd, *params = code[instruction_pointer] 
            
            # print debug output 
            if self.debug:
                print ("====================================================")
                # print ("[heap]", heap.memory, end="\n\n\n")
                # printheap (heap)
                print ("[stack]", stack, end="\n\n\n")
                print (f"[base-pointer]", base_pointer)
                # print (f"[less-than-flag]", lessThanFlag)
                # print (f"[equal-to-flag]", equalFlag)
                # print (f"[greater-than-flag]", greaterThanFlag)
                print (f"[current-instruction] {instruction_pointer} {code[instruction_pointer]} | {lines[instruction_pointer]}")
                print ("====================================================")

            if cmd == OPCODE_ASSIGN:
                # ASSIGN dest src
                # Case 1: Dest is Memory
                if params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    # Assign dest to src
                    heap.memory[address], i = getNextValue(heap, stack, params, 5)
                # Case 2: Dest is Stack variable
                elif params[0] == MODE_STACK:
                    # Assign dest to src 
                    stack[base_pointer][params[1]], i = getNextValue(heap, stack, params, 2)
                # Case 3: Dest is Invalid param type
                else:
                    print(f"Error: Can only assign a value to a stack variable or memory address")
                    exit(1)
            elif cmd == OPCODE_ADD:
                # ADD dest src1 src2
                # Case 1: Dest is Memory
                if params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = src1 + src2
                # Case 2: Dest is Stack variable
                elif params[0] == MODE_STACK:
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = src1 + src2
                # Case 3: Dest is Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
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
                    stack[base_pointer][params[1]] = src1 - src2
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
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
                    stack[base_pointer][params[1]] = src1 * src2
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
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
                    # integer division
                    if isinstance(src1, int) and isinstance (src2, int):
                        heap.memory[address] = src1 // src2
                    else:
                        heap.memory[address] = src1 / src2
                # Case 2: Stack variable
                elif params[0] == MODE_STACK:
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    # integer division
                    if isinstance(src1, int) and isinstance (src2, int):
                        stack[base_pointer][params[1]] = src1 // src2
                    else:
                        stack[base_pointer][params[1]] = src1 / src2
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
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
                    stack[base_pointer][params[1]] = src1 % src2
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
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
            elif cmd == OPCODE_INPUT:
                # INPUT dest 

                # Read in line 
                try:
                    line = input () + '\n' + '\0'
                except EOFError:
                    line = 0

                # put in memory 
                if line != 0:
                    lineAddress = heap.malloc(len(line))
                    for i in range(len(line)):
                        heap.memory[lineAddress+i] = line[i]
                else:
                    # set to null
                    lineAddress = 0

                # Case 1: Memory
                if params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    heap.memory[address] = lineAddress
                # Case 2: Stack variable
                elif params[0] == MODE_STACK:
                    stack[base_pointer][params[1]] = lineAddress
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            # calling functions
            elif cmd == OPCODE_CALL:
                # CALL funcPtr
                # print (f"[interpreter] Function call {lines[instruction_pointer]}")

                funcPtr, _ = getNextValue (heap, stack, params, 0)

                # push return address 
                stack.append(instruction_pointer)

                # push previous base pointer
                stack.append(base_pointer)

                # move stack base pointer to after return address 
                base_pointer = len(stack)

                # add new variable scope 
                stack.append({})

                # jump to function start
                instruction_pointer = funcPtr

            # returning from functions
            elif cmd == OPCODE_RETURN:
                # RETURN value
                return_value, i = getNextValue(heap, stack, params, 0)
                # restore instruction pointer
                instruction_pointer = stack[base_pointer-2]
                # pop off function's scope 
                # this does not work if there are extra values on the stack
                # stack.pop()

                # new pop off function's scope 
                stack = stack[:base_pointer]

                # restore base_pointer
                base_pointer = stack[base_pointer-1]
                # pop off base_pointer
                stack.pop()
                # pop off return address
                stack.pop()
                # top of stack should be at the params now 
            elif cmd == OPCODE_RESPONSE:
                # RESPONSE dest
                # Case 1 : Stack variable
                if params[0] == MODE_STACK:
                    stack[base_pointer][params[1]] = return_value
                # Case 2 : Memory address
                elif params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    heap.memory[address] = return_value
                # Case 3 : Bad token
                else:
                    print(f"Error: RESPONSE requires a stack variable or a memory address")
                    exit(1)
            # allocating data on heap
            elif cmd == OPCODE_MALLOC:
                # MALLOC ptrDest size 
                # Pointer Case1 : variable
                if params[0] == MODE_STACK:
                    size, _ = getNextValue(heap, stack, params, 2, reject=[])
                    stack[base_pointer][params[1]] = heap.malloc(size)
                # Pointer Case2 : memory
                elif params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    size, _ = getNextValue(heap, stack, params, 5, reject=[])
                    heap.memory[address] = heap.malloc(size)
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
                # printheap(heap)
            # deallocating data on heap
            elif cmd == OPCODE_FREE:
                # FREE pointer
                pointer, _ = getNextValue(heap, stack, params, 0)
                # allocate space on heap 
                heap.free(pointer)
            elif cmd == OPCODE_SIZEOF:
                # SIZEOF dest pointer
                # Case1 : variable
                if params[0] == MODE_STACK:
                    pointer, _ = getNextValue(heap, stack, params, 2)
                    stack[base_pointer][params[1]] = heap.sizeof(pointer)
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    # next 4 nums make up the pointer and offset
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    pointer, _ = getNextValue(heap, stack, params, 5)
                    heap.memory[address] = heap.sizeof(pointer)
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_COMPARE:
                # COMPARE src1 src2
                # sets the appropriate comparision flag 
                src1, i = getNextValue(heap, stack, params, 0)
                src2, i = getNextValue(heap, stack, params, i)
                # set flags 
                if isinstance (src1, str):
                    src1 = ord(src1)
                if isinstance (src2, str):
                    src2 = ord(src2)
                lessThanFlag = 1 if src1 < src2 else 0
                equalFlag = 1 if src1 == src2 else 0
                greaterThanFlag = 1 if src1 > src2 else 0
            elif cmd == OPCODE_JUMP:
                # JUMP dest
                # unconditional jump 
                # move to jump point
                instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPLT:
                # JUMPLT dest
                # jump if less than flag is true
                if lessThanFlag == 1:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPLE:
                # JUMPLE dest
                # jump if less than or equal to flags are true 
                if lessThanFlag == 1 or equalFlag == 1:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPEQ:
                # JUMPEQ dest
                # jump if equal to flag is true 
                if equalFlag == 1:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPNEQ:
                # JUMPNEQ dest
                # jump if equal to flag is false 
                if equalFlag == 0:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPGE:
                # JUMPGE dest
                # jump if greater than or equal to flags are true
                if equalFlag == 1 or greaterThanFlag == 1:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_JUMPGT:
                # JUMPGT dest
                # jump if greater than flag is true 
                if greaterThanFlag == 1:
                    instruction_pointer, _ = getNextValue (heap, stack, params, 0)
            elif cmd == OPCODE_EQUAL:
                # EQUAL dest src1 src2 
                # dest = src1 == src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 == src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 == src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_NEQUAL:
                # NEQUAL dest src1 src2 
                # dest = src1 != src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 != src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 != src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_LT:
                # LT dest src1 src2 
                # dest = src1 < src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 < src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 < src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_LE:
                # LE dest src1 src2 
                # dest = src1 <= src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 <= src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 <= src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_GT:
                # GT dest src1 src2 
                # dest = src1 > src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 > src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 > src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_GE:
                # GE dest src1 src2 
                # dest = src1 >= src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 >= src2 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 >= src2 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_AND:
                # AND dest src1 src2 
                # dest = src1 && src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 != 0 and src2 != 0 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 != 0 and src2 != 0 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_OR:
                # OR dest src1 src2 
                # dest = src1 || src2
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src1, i = getNextValue(heap, stack, params, 2)
                    src2, i = getNextValue(heap, stack, params, i)
                    stack[base_pointer][params[1]] = 1 if src1 != 0 or src2 != 0 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src1, i = getNextValue(heap, stack, params, 5)
                    src2, i = getNextValue(heap, stack, params, i)
                    heap.memory[address] = 1 if src1 != 0 or src2 != 0 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_NOT:
                # NOT dest src
                # dest = ~src
                # Case1 : variable
                if params[0] == MODE_STACK:
                    # variable is allowed to not exist for assigning 
                    src, i = getNextValue(heap, stack, params, 2)
                    stack[base_pointer][params[1]] = 1 if src == 0 else 0
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    heap.memory[address] = 1 if src == 0 else 0
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_PUSH:
                # PUSH src 
                src, i = getNextValue(heap, stack, params, 0)
                stack.append(src)
            elif cmd == OPCODE_POP:
                # POP dest 
                # ensure base_pointer (scope) isnt getting popped
                if base_pointer == len(stack)-1:
                    print (f"[error] [pop] Nothing to pop off of stack")
                    exit(1)
                # Case1 : variable
                if params[0] == MODE_STACK:
                    stack[base_pointer][params[1]] = stack[-1]
                    stack.pop()
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    heap.memory[address] = stack[-1] 
                    stack.pop()
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_STACKGET:
                # STACKGET dest offset 
                # Case1 : variable
                if params[0] == MODE_STACK:
                    offset, i = getNextValue(heap, stack, params, 2)
                    # -3 initially because
                    # first argument <--- base pointer - 3
                    # return address <--- base pointer - 2
                    # old base pointer <- base pointer - 1
                    # variables <-------- base pointer
                    stack[base_pointer][params[1]] = stack[base_pointer-3-offset]
                # Case2 : memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    offset, i = getNextValue(heap, stack, params, 5)
                    # -3 initially because
                    # first argument <--- base pointer - 3
                    # return address <--- base pointer - 2
                    # old base pointer <- base pointer - 1
                    # variables <-------- base pointer
                    heap.memory[address] = stack[base_pointer-3-offset]
                # Case 3: Invalid param type
                else:
                    print(f"Error: Dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_FtoI:
                # FTOI dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    # ensure src is float
                    if not isinstance (src, float):
                        print (f"Error FTOI - src should be of type float")
                        exit (1)
                    stack[base_pointer][params[1]] = int(src)
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    # ensure src is float
                    if not isinstance (src, float):
                        print (f"Error FTOI - src should be of type float")
                        exit (1)
                    heap.memory[address] = int(src)
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_ItoF:
                # ITOF dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    # ensure src is int
                    if not isinstance (src, int):
                        print (f"Error ITOF - src should be of type int")
                        exit (1)
                    stack[base_pointer][params[1]] = float(src)
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    # ensure src is int
                    if not isinstance (src, int):
                        print (f"Error ITOF - src should be of type int")
                        exit (1)
                    heap.memory[address] = float(src)
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_STRING:
                # STRING dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    s = str(src) + '\0'
                    # create string on heap
                    ptr = heap.malloc (len(s))
                    # add characters to heap block
                    for i in range(len(s)):
                        heap.memory[ptr+i] = s[i]
                    # give user the ptr to the string 
                    stack[base_pointer][params[1]] = ptr
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    s = str(src) + '\0'
                    # create string on heap
                    ptr = heap.malloc (len(s))
                    # add characters to heap block
                    for i in range(len(s)):
                        heap.memory[ptr+i] = s[i]
                    # give user the ptr to the string 
                    heap.memory[address] = ptr
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_StoF:
                # STOF dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    # ensure src is address (int)
                    if not isinstance (src, int):
                        print (f"Error STOF - src should be a memory address (int)")
                        exit (1)
                    # accumulate characters 
                    s = []
                    size = heap.sizeof (src)
                    # -1 to ignore null char
                    for i in range(size-1):
                        s += [heap.memory[src+i]]
                    s = "".join(s)
                    stack[base_pointer][params[1]] = float (s)
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    # ensure src is address (int)
                    if not isinstance (src, int):
                        print (f"Error STOF - src should be a memory address (int)")
                        exit (1)
                    # accumulate characters 
                    s = []
                    size = heap.sizeof (src)
                    # -1 to ignore null char
                    for i in range(size-1):
                        s += [heap.memory[src+i]]
                    s = "".join(s)
                    heap.memory[address] = float (s)
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_StoI:
                # STOI dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    # ensure src is address (int)
                    if not isinstance (src, int):
                        print (f"Error STOI - src should be a memory address (int)")
                        exit (1)
                    # accumulate characters 
                    s = []
                    size = heap.sizeof (src)
                    # protection for chars (since python chars a strings)
                    if size == 1: 
                        size += 1
                    # -1 to ignore null char for strings
                    else:
                        # strlen 
                        j = 0
                        while j < size and heap.memory[src+j] != '\0':
                            j += 1
                        size = j+1
                    for i in range(size-1):
                        s += [heap.memory[src+i]]
                    s = "".join(s)
                    # print ("'"+s+"'", size)
                    # print (heap.memory[src-10:src+10])
                    stack[base_pointer][params[1]] = int (s)
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    # ensure src is address (int)
                    if not isinstance (src, int):
                        print (f"Error STOI - src should be a memory address (int)")
                        exit (1)
                    # accumulate characters 
                    s = []
                    size = heap.sizeof (src)
                    # protection for chars (since python chars a strings)
                    if size == 1: 
                        size += 1
                    # -1 to ignore null char for strings
                    else:
                        # strlen 
                        j = 0
                        while j < size and heap.memory[src+j] != '\0':
                            j += 1
                        size = j+1
                    for i in range(size-1):
                        s += [heap.memory[src+i]]
                    s = "".join(s)
                    # print ("'"+s+"'", size)
                    # print (heap.memory[src-10:src+10])
                    heap.memory[address] = int (s)
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_CtoI:
                # CTOI dest src 
                # Case1 : dest variable
                if params[0] == MODE_STACK:
                    src, i = getNextValue(heap, stack, params, 2)
                    stack[base_pointer][params[1]] = int (src)
                # Case2 : dest memory
                elif params[0] == MODE_MEMORY:
                    pmode, pointer, omode, offset = params[1:5]
                    address = getMemAddress(stack, pmode, pointer, omode, offset)
                    src, i = getNextValue(heap, stack, params, 5)
                    heap.memory[address] = int (src)
                # Case 3: Invalid param type
                else:
                    print(f"Error: dest should be memory or stack")
                    exit(1)
            elif cmd == OPCODE_HALT:
                break
            #  jump point line
            elif cmd == MODE_JUMPPOINT:
                pass
            else:
                print(f"Error: '{lines[instruction_pointer][0]}' is not a valid command")
                exit(1)

            instruction_pointer += 1


        # print ("=======================================")
        # printheap(heap)
        # print (heap.allocatedMemory)

        # print("*** End of program ***")

##########################################################################


if __name__ == "__main__":
    # ensure file was provided 
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<file-name>")
        exit()

    # read code from file 
    file_name = sys.argv[1]
    lines = []
    with open(file_name, "r") as file:
        lines = file.readlines()

    interpreter = AmyAssemblyInterpreter (file_name)
    # interpreter = AmyAssemblyInterpreter ("")

    interpreter.execute ("".join(lines))
    # interpreter.execute (code)
    