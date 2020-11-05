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
BOOL = 3
STRING = 4
ERROR = 5
NAMESPACE = 6
MEMORY = 7
DELIMITERS = " \t\n"

##########################################################################

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

