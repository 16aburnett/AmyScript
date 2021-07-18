# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

if __name__ == "symbolTable":
    from ast import *
else:
    from .ast import *  

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

    def insert (self, decl, name=""):
        if name == "":
            name = decl.id
        # ensure variable wasnt already declared
        if (name in self.table[-1]):
            # functions of the same name can have multiple overloads 
            if isinstance (self.table[-1][name], list):
                # check that parameters dont match
                for overload in self.table[-1][name]:
                    # params dont match if nParams is different
                    if len(overload.params) != len(decl.params):
                        continue
                    # check if param types match
                    for i in range(len(overload.params)):
                        # found nonmatching param
                        if overload.params[i].type.__str__() != decl.params[i].type.__str__():
                            # param types do not match
                            break
                    # param types match 
                    else:
                        return False 
                # reaches here if no overloads match 
            else:
                return False
        # add function to overload list in table
        if isinstance (decl, (FunctionNode, MethodDeclarationNode, ConstructorDeclarationNode)):
            # create overload list if DNE
            if name not in self.table[-1]:
                self.table[-1][name] = []
            # add to overload list 
            self.table[-1][name].append (decl)
            return True
        # add normal variable to table 
        self.table[-1][name] = decl
        return True

    def lookup (self, name, paramTypes=[]):
        for i in range(len(self.table)-1, -1, -1):
            # check scope for var 
            if (name in self.table[i]):
                # for matching functions 
                if (isinstance (self.table[i][name], list)):
                    # check each overload 
                    for overload in self.table[i][name]:
                        # check the number of parameters 
                        if (len(paramTypes) != len(overload.params)):
                            continue
                        # check parameter types 
                        for j in range(len(paramTypes)):
                            # check if param type does not match
                            if paramTypes[j] != overload.params[j].type.__str__():
                                # make sure types are not related 
                                isObject = overload.params[j].type.type == Type.USERTYPE
                                isArray = overload.params[j].type.arrayDimensions > 0
                                if paramTypes[j] == "null" and (isObject or isArray):
                                    continue
                                break
                        # all param types match - found desired function decl overload
                        else: 
                            return overload
                        # reaches here if overload's params dont match
                        # check next overload 
                    # reaches here if no overloads match 
                # for matching variables 
                else:
                    return self.table[i][name]
                
        # reaches here if no matching variable declaration was found
        return None

# ========================================================================