# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

if __name__ == "symbolTable":
    from ast import FunctionNode   
else:
    from .ast import FunctionNode   

# ========================================================================

class SymbolTable:

    def __init__(self):
        self.nestLevel = 0
        # list of dictionaries
        self.table = [{}]

    def enterScope (self):
        self.table.append ({})
        self.nestLevel += 1

    def exitScope (self):
        self.table.pop ()
        self.nestLevel -= 1

    def insert (self, decl):
        name = decl.id
        # ensure variable wasnt already declared
        if (name in self.table[-1]):
            return False
        # add declaration to table
        self.table[-1][name] = decl
        return True

    def lookup (self, name, paramTypes=[]):
        for i in range(len(self.table)-1, -1, -1):
            # check scope for var 
            if (name in self.table[i]):
                # for matching functions 
                if (isinstance (self.table[i], FunctionNode)):
                    # check the number of parameters 
                    if (len(paramTypes) != len(self.table[i][name].params)):
                        continue
                    # check parameter types 
                    for i in range(len(paramTypes)):
                        # check if param type does not match
                        if paramTypes[i] != self.table[i][name].params[i].type.type:
                            break
                    # all param types match 
                    else: 
                        return self.table[i][name]
                    # reaches here if params dont match
                else:
                    return self.table[i][name]
                
        # reaches here if no matching variable declaration was found
        return None

# ========================================================================