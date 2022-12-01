# The Amy Programming Language Lexer
# By Amy Burnett
# November 5 2020
##########################################################################
# Imports

import re

##########################################################################

WORD = 0
INT = 1
FLOAT = 2
ERROR = 5
MEMORY = 7
CHAR = 8
JUMPPOINT = 9 
DELIMITERS = " \t\n"

##########################################################################

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
                while self.index < len(self.source) and not (self.source[self.index] == "\'"):
                    token += [self.source[self.index]]
                    # skip escaped characters
                    if self.source[self.index] == '\\':
                        token += [self.source[self.index+1]]
                        self.index += 2
                    else:
                        self.index += 1
                # no ending quotation marks
                if self.index >= len(self.source):
                    return ERROR, f"Syntax Error: Line ended without closing quotation mark in {self.source}"
                # index should be at the ending quotation mark
                self.index += 1
                # ensure next position is whitespace or the end
                if self.index < len(self.source) and self.source[self.index] not in DELIMITERS:
                    return ERROR, f"Syntax Error: Unexpected {self.source[self.index]} for line \n {self.source}"
                # string successfully matched
                return CHAR, "".join(token)

            self.index += 1
        return ERROR, f"Syntax Error: Unexpected {self.source[self.index]} for line \n {self.source}"

    def hasToken(self) -> bool:
        return self.index < len(self.source)

