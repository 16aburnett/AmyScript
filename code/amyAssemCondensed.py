# The AmyAssembly Programming Language Interpreter 
# By Amy Burnett
# April 18 2021
#=========================================================================
# Imports

import sys
import re

#=========================================================================
# amy assembly code 

code = """
// AmyAssembly Programming Language
// By Amy Burnett
//========================================================================

// start at main
    jump main

//========================================================================
// converts string range to integer
// param1 - string pointer
// param2 - starting position to read int from
// param3 - end position to stop reading 
stringToInt:
    stackget string 0
    stackget start 1
    stackget end 2
    assign val 0
    assign i start
while00:
    cmp i end
    jge endwhile00

    // shift nums
    multiply val val 10

    cmp string[i] '1'
    jneq notOne
    add val val 1 
    jump continue
notOne:
    cmp string[i] '2'
    jneq notTwo
    add val val 2 
    jump continue
notTwo:
    cmp string[i] '3'
    jneq notThree
    add val val 3 
    jump continue
notThree:
    cmp string[i] '4'
    jneq notFour
    add val val 4 
    jump continue
notFour:
    cmp string[i] '5'
    jneq notFive
    add val val 5 
    jump continue
notFive:
    cmp string[i] '6'
    jneq notSix
    add val val 6 
    jump continue
notSix:
    cmp string[i] '7'
    jneq notSeven
    add val val 7 
    jump continue
notSeven:
    cmp string[i] '8'
    jneq notEight
    add val val 8 
    jump continue
notEight:
    cmp string[i] '9'
    jneq notNine
    add val val 9 
    jump continue
notNine:
    cmp string[i] '0'
    jneq error
    add val val 0 
    jump continue
error:
    print 'e'
    print 'r'
    print 'r'
    print 'o'
    println 'r'
    println string[i]
    halt 
continue:
    add i i 1
    jump while00
endwhile00:
    return val 

//========================================================================

main:
    input line
    // break up line into the two nums
    assign begin1 0
    assign end1 0
while01:
    cmp line[end1] ' '
    jeq endwhile01

    add end1 end1 1 

    jump while01
endwhile01: 

    add begin2 end1 1
    sizeof end2 line

    push end1
    push begin1
    push line
    call stringToInt
    response r
    pop null 
    pop null
    pop null

    push end2
    push begin2
    push line
    call stringToInt
    response s
    pop null 
    pop null
    pop null


    multiply r2 2 s
    subtract r2 r2 r

    println r2 

"""


lines = code.split("\n")


#=========================================================================
# LEXER

WORD = 0
INT = 1
FLOAT = 2
ERROR = 5
MEMORY = 7
CHAR = 8
JUMPPOINT = 9 
DELIMITERS = " \t\n"

#=========================================================================

class CommandComponent:
    def __init__(self, type, value):
        self.type = type 
        self.value = value
class MemoryComponent(CommandComponent):
    def __init__(self, ptrType, ptr, offsetType, offset):
        self.type = MEMORY
        self.pointerType = ptrType
        self.pointer = ptr
        self.offsetType = offsetType
        self.offset = offset
class Lexer:
    def __init__(self, source:str):
        self.source = source.strip()
        self.index = 0
    def getNumber(self):
        # ensure valid index
        if self.index >= len(self.source):
            return ERROR, "No number"
        # ensure it starts with 0 - 9 or '-' minus 
        if not re.match("[0-9-]", self.source[self.index]):
            return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"

        token = [self.source[self.index]]
        self.index += 1

        # grab left of decimal
        while self.index < len(self.source) and re.match("[0-9]", self.source[self.index]):
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
            return FLOAT, float("".join(token))
        # ensure that the only thing captured wasnt '-'
        if "".join(token) == '-':
            return ERROR, f"Unexpected '-' for line '{self.source}'"
        # Success return int
        return INT, int("".join(token))
        
    def getWord(self):
        # ensure valid index
        if self.index >= len(self.source):
            return ERROR, "No word"
        # ensure first is is alpha 
        if not re.match("[a-zA-Z_]", self.source[self.index]):
            return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"
        token = [self.source[self.index]]
        self.index += 1
        # read alphanumerics
        while self.index < len(self.source) and re.match("[a-zA-Z0-9_]", self.source[self.index]):
            token += [self.source[self.index]]
            self.index += 1
        
        # return word component
        return WORD, "".join(token)
        
    def getToken(self) -> CommandComponent:
        # grab next component
        while self.index < len(self.source):
            # possibly a word 
            if re.match("[a-zA-Z_]", self.source[self.index]):
                status, value = self.getWord()
                # skip over whitespace
                while self.index < len(self.source) and self.source[self.index] in DELIMITERS:
                    self.index += 1
                # try to match jump point label 
                if self.index < len(self.source) and self.source[self.index] == ':':
                    return JUMPPOINT, value 
                # try to match subscript 
                if status != ERROR and self.index < len(self.source) and self.source[self.index] == '[':
                    self.index += 1
                    
                    # subscript is var
                    if self.index < len(self.source) and re.match("[a-zA-Z_]", self.source[self.index]):
                        status, subscript = self.getWord()
                        # ensure matched word
                        if status == ERROR:
                            return ERROR, subscript
                        # ensure next thing is ]
                        if self.index >= len(self.source) or self.source[self.index] != "]":
                            return ERROR, f"Expected ']' at index {self.index} for line \n {self.source}"
                        self.index += 1
                        # ensure next is space - if there is next
                        if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                            return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"
                        self.index += 1
                        # return word component
                        return MEMORY, WORD, value, WORD, subscript
                    # subscript is immediate number
                    if self.index < len(self.source) and re.match("[0-9-]", self.source[self.index]):
                        status, subscript = self.getNumber()
                        # ensure matched word
                        if status == ERROR:
                            return ERROR, subscript
                        # ensure num is INT
                        if status != INT:
                            return ERROR, f"Memory addresses should be integers"
                        # ensure next thing is ]
                        if self.index >= len(self.source) or self.source[self.index] != "]":
                            return ERROR, f"Expected ']' at index {self.index} for line \n {self.source}"
                        self.index += 1
                        # ensure next is space - if there is next
                        if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                            return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"
                        self.index += 1
                        # return word component
                        return MEMORY, WORD, value, INT, subscript

                return status, value
            # possibly a number 
            if re.match("[0-9-]", self.source[self.index]):
                return self.getNumber()

            # characters
            if self.source[self.index] == "\'":
                token = []
                self.index += 1
                while self.index < len(self.source) and self.source[self.index] != "\'":
                    token += [self.source[self.index]]
                    self.index += 1
                # no ending quotation marks
                if self.index >= len(self.source):
                    return ERROR, f"Line ended without closing double quotes in {self.source}"
                # index should be at the ending quotation mark
                self.index += 1
                # ensure next position is whitespace or the end
                if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                    return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"
                # string successfully matched
                return CHAR, "".join(token)

            self.index += 1
        return ERROR, f"Unexpected {self.source[self.index]} for line \n {self.source}"

    def hasToken(self) -> bool:
        return self.index < len(self.source)

#=========================================================================
# HEAP 

class BlockHeader:
    def __init__(self, prevBlock, payloadSize:int, isAlloc:bool):
        self.prevBlock = prevBlock
        self.payloadSize = payloadSize
        self.isAlloc = isAlloc

class Heap:
    def __init__(self):
        initialSize = 12
        self.memory = [0 for _ in range(initialSize)]
        # set up first free block
        # mem[0] is reserved for NULLPTR
        self.memory[1] = BlockHeader(None, initialSize-2, False)

    def malloc(self, size:int) -> int:
        """allocates space for given size and returns the pointer to 
        the starting position"""
        # Search for sufficient mem block
        i = 1
        header = None
        while i < len(self.memory):
            # get header
            header = self.memory[i]
            # ensure it is free
            if header.isAlloc:
                i += header.payloadSize + 1
                continue
            # if sufficient 
            if header.payloadSize == size:
                # allocate 
                header.isAlloc = True
                # return pointer to first payload pos
                return i + 1
            # if sufficient
            if header.payloadSize > size:
                # split payload
                secondPayload = header.payloadSize - size - 1
                secondAddress = i+size+1
                # modify this payload
                header.payloadSize = size
                header.isAlloc = True
                # if second split has >0 payload
                # *** removed if because caused error 
                # if secondPayload > 0:
                    # create new payload
                self.memory[secondAddress] = BlockHeader(header, secondPayload, False)
                # coalesce 
                self.coallese(secondAddress)
                # assign second split's next's prev to the second split
                if secondAddress+secondPayload+1 < len(self.memory):
                    self.memory[secondAddress+secondPayload+1].prevBlock = self.memory[secondAddress]
                # ****
                # return pointer to first payload pos
                return i + 1
            i += header.payloadSize + 1
        # Reachs here if no sufficient free blocks were found
        # Lets add one
        self.memory += [BlockHeader(header, size, True)]
        self.memory += [0 for _ in range(size)]
        # return pointer to first payload pos
        return i + 1

    def free(self, address:int):
        """Frees the block containing the address"""
        self.memory[address-1].isAlloc = False
        self.coallese(address-1)
    
    def coallese(self, address:int):
        """Merges the free block at given address with
        adjacent free blocks"""
        # combine with free block after
        nextBlockAddr = address+self.memory[address].payloadSize+1
        if nextBlockAddr < len(self.memory) and not self.memory[nextBlockAddr].isAlloc:
            # clear second split
            temp = self.memory[nextBlockAddr].payloadSize
            self.memory[nextBlockAddr] = 0
            # add space to this block
            # + 1 for the space that used to have the header
            self.memory[address].payloadSize += temp+1
            # assign this to the prev of the next header
            newNextBlockAddr = address+self.memory[address].payloadSize+1
            if newNextBlockAddr < len(self.memory):
                self.memory[newNextBlockAddr].prevBlock = self.memory[address]
        # Combine with free block before
        if self.memory[address].prevBlock != None and not self.memory[address].prevBlock.isAlloc:
            # add this space to the prev block payload
            self.memory[address].prevBlock.payloadSize += 1+self.memory[address].payloadSize
            # assign this next to the prev
            # if there is a next
            if address+self.memory[address].payloadSize+1 < len(self.memory):
                self.memory[address+self.memory[address].payloadSize+1].prevBlock = self.memory[address].prevBlock
            # delete header
            self.memory[address] = 0

    def sizeof(self, address):
        """Returns the payload size for a given pointer

        Pre-condition: pointer must be allocated and not offset 
        from the start of the block
        """
        return self.memory[address-1].payloadSize

def printheap(heap):
    for i in range(len(heap.memory)):
        if isinstance(heap.memory[i], BlockHeader):
            print(f"{i} {heap.memory[i].payloadSize} {heap.memory[i].isAlloc}")
            # if heap.memory[i].prevBlock != None:
            #     print(f"\t{heap.memory[i].prevBlock.payloadSize} {heap.memory[i].prevBlock.isAlloc}")
        else:
            print(f"{i} {heap.memory[i]}")


#=========================================================================
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
OPCODE_COMPARE     = 23
OPCODE_AND         = 24
OPCODE_OR          = 25
OPCODE_NOT         = 26
OPCODE_SIZEOF      = 27
OPCODE_PUSH        = 28
OPCODE_POP         = 29
OPCODE_STACKGET    = 30
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
    "cmp"         : OPCODE_COMPARE,
    "println"     : OPCODE_PRINTLN,
    "sizeof"      : OPCODE_SIZEOF,
    "and"         : OPCODE_AND,
    "or"          : OPCODE_OR,
    "not"         : OPCODE_NOT,
    "push"        : OPCODE_PUSH,
    "pop"         : OPCODE_POP,
    "stackget"    : OPCODE_STACKGET
}

# PARAM MODES
MODE_IMMEDIATE = 0 # value represent data
MODE_STACK     = 1 # value is a stack address (aka a variable/function)
MODE_MEMORY    = 2 # value is a heap address 
MODE_JUMPPOINT = -1

##########################################################################

# ensure file was provided 
# if len(sys.argv) < 2:
#     print("Please provide a file_name")
#     exit()

# read code from file 
# file_name = sys.argv[1]
# lines = []
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
wordId = 0
# stores all the jump points (label, instruction)
jumpPoints = {}
code = []
for line in lines:
    lexer = Lexer(line)
    code_line = []

    type, value = lexer.getToken()
    # jump points
    if type == JUMPPOINT:
        # var DNE
        if value not in wordToInt:
            wordToInt[value] = wordId
            wordId += 1
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

# with open(file_name+"c", "w") as outfile:
#     maxdigits = len(str(len(code)))
#     for i in range(len(code)):
#         outfile.write(f"{padzeros(i, maxdigits)} {code[i]} {lines[i]}\n")

# with open(file_name+"i", "w") as outfile:
#     for i in range(len(code)):
#         outfile.write(f"{code[i][0]}")
#         for j in range(1, len(code[i])):
#             if isinstance(code[i][j], str):
#                 outfile.write(f", \"{code[i][j]}\"")
#             else:
#                 outfile.write(f", {code[i][j]}")
#         outfile.write("\n")

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
stack += [len(sys.argv), -1, -1, {}]
instruction_pointer = 0
base_pointer = len(stack)-1
return_value = 0
# flag states 
lessThanFlag = 0
equalFlag = 0
greaterThanFlag = 0

### Execute The Code #####################################################

def getVariableValue(stack, var):

    # Ensure variable exists in the current scope 
    if var not in stack[base_pointer]:
        print(f"variable referenced before assignment - '{var}'")
        exit(1)
    
    return stack[base_pointer][var]

def getMemAddress(stack, pmode, pointer, omode, offset) -> int:
    """Gets the absolute memory address including any offset

    """
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
        address = getVariableValue(stack, pointer)
        if omode == MODE_STACK:
            offset = getVariableValue(stack, offset)
        # heap address must be int
        if isinstance(address, int):
            return heap.memory[address+offset], i+5
        # float is invalid
        if isinstance(address, float):
            print("float is not subscriptable")
            exit(1)
        # strings and lists
        else:
            return address[offset], i+5
    
    # Case 2: Stack variable
    elif params[i] == MODE_STACK and MODE_STACK not in reject:
        return getVariableValue(stack, params[i+1]), i+2
    
    # Case 3: Immediate Variable
    elif params[i] == MODE_IMMEDIATE and MODE_IMMEDIATE not in reject:
        return params[i+1], i+2

    # Case 5: Unknown mode
    print("Bad Parameter Mode")
    exit(1)

# evaluate lines
while instruction_pointer < len(code):

    cmd, *params = code[instruction_pointer] 

    # print (f"{code[instruction_pointer]} | {lines[instruction_pointer]}")
    # print (heap.memory)
    # print("\n\n")
    # print (stack, end="\n\n\n")

    if cmd == OPCODE_ASSIGN:
        # ASSIGN dest src
        # Case 1: Dest is Memory
        if params[0] == MODE_MEMORY:
            # next 4 nums make up the pointer and offset
            pmode, pointer, omode, offset = params[1:5]
            address = getMemAddress(stack, pmode, pointer, omode, offset)
            # Assign src to dest 
            heap.memory[address], i = getNextValue(heap, stack, params, 5)
        # Case 2: Dest is Stack variable
        elif params[0] == MODE_STACK:
            # Assign src to dest
            stack[base_pointer][params[1]], i = getNextValue(heap, stack, params, 2)
        # Case 3: Dest is Invalid param type
        else:
            print(f"Can only assign a value to a stack variable or memory address")
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
            stack[base_pointer][params[1]] = src1 - src2
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
            stack[base_pointer][params[1]] = src1 * src2
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
            stack[base_pointer][params[1]] = src1 / src2
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
            stack[base_pointer][params[1]] = src1 % src2
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
    elif cmd == OPCODE_INPUT:
        # INPUT dest

        # Read in line 
        line = input()
        # put in memory 
        lineAddress = heap.malloc(len(line))
        for i in range(len(line)):
            heap.memory[lineAddress+i] = line[i]

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
            print(f"Dest should be memory or stack")
            exit(1)
    # calling functions
    elif cmd == OPCODE_CALL:

        if params[0] != MODE_STACK:
            print(f"function name must be a stack variable")
            exit(1)

        fname = params[1]

        # Ensure function exists 
        if fname not in jumpPoints:
            print(f"jump point '{fname}' is not defined")  
            exit(1)

        # push return address 
        stack.append(instruction_pointer)

        # push previous base pointer
        stack.append(base_pointer)

        # move stack base pointer to after return address 
        base_pointer = len(stack)

        # add new variable scope 
        stack.append({})

        # jump to function start
        instruction_pointer = jumpPoints[fname]

    # returning from functions
    elif cmd == OPCODE_RETURN:
        # RETURN value
        return_value, i = getNextValue(heap, stack, params, 0)
        # restore instruction pointer
        instruction_pointer = stack[base_pointer-2]
        # pop off function's scope 
        stack.pop()
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
            print(f"RESPONSE requires a stack variable or a memory address")
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
            print(f"Dest should be memory or stack")
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
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_COMPARE:
        # COMPARE src1 src2
        # sets the appropriate comparision flag 
        src1, i = getNextValue(heap, stack, params, 0)
        src2, i = getNextValue(heap, stack, params, i)
        # set flags 
        lessThanFlag = 1 if src1 < src2 else 0
        equalFlag = 1 if src1 == src2 else 0
        greaterThanFlag = 1 if src1 > src2 else 0
    elif cmd == OPCODE_JUMP:
        # JUMP dest
        # unconditional jump 
        # ensure it is a var 
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPLT:
        # JUMPLT dest
        # jump if less than flag is true 
        # ensure it is a var 
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if lessThanFlag == 1:
            instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPLE:
        # JUMPLE dest
        # jump if less than or equal to flags are true 
        # ensure it is a var
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if lessThanFlag == 1 or equalFlag == 1:
            instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPEQ:
        # JUMPEQ dest
        # jump if equal to flag is true 
        # ensure it is a var
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if equalFlag == 1:
            instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPNEQ:
        # JUMPNEQ dest
        # jump if equal to flag is false 
        # ensure it is a var
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if equalFlag == 0:
            instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPGE:
        # JUMPGE dest
        # jump if greater than or equal to flags are true 
        # ensure it is a var
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if equalFlag == 1 or greaterThanFlag == 1:
            instruction_pointer = jumpPoints[params[1]]
    elif cmd == OPCODE_JUMPGT:
        # JUMPGT dest
        # jump if greater than flag is true 
        # ensure it is a var
        if params[0] != MODE_STACK:
            print("can only jump to a jump point")
            exit(1)
        # move to jump point
        if greaterThanFlag == 1:
            instruction_pointer = jumpPoints[params[1]]
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
            print(f"Dest should be memory or stack")
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
            print(f"Dest should be memory or stack")
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
            print(f"Dest should be memory or stack")
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
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_PUSH:
        # PUSH src 
        src, i = getNextValue(heap, stack, params, 0)
        stack.append(src)
    elif cmd == OPCODE_POP:
        # POP dest 
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
            print(f"Dest should be memory or stack")
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
            print(f"Dest should be memory or stack")
            exit(1)
    elif cmd == OPCODE_HALT:
        break
    #  jump point line
    elif cmd == MODE_JUMPPOINT:
        pass
    else:
        print(f"UNKNOWN command! Yikes there bud! {cmd}")
        exit(1)

    instruction_pointer += 1


# printheap(heap)

# print("*** End of program ***")

##########################################################################
