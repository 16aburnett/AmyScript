# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

from enum import Enum
from sys import exit

if __name__ == "symbolTable":
    from amyAST import *
    from template import TemplateVisitor
else:
    from .amyAST import *  
    from .template import TemplateVisitor

# ========================================================================

class Symbol:
    def __init__(self):
        self.id = ""
        self.typeDec = {}
        self.varDec = None 
        self.funDec = {0:[]} 

class Kind(Enum):
    TYPE = 0
    VAR  = 1
    FUNC = 2


# ========================================================================

class SymbolTable:

    def __init__(self):
        self.nestLevel = 0
        # list of dictionaries
        self.table = [{}]
        self.lines = []

    def enterScope (self):
        self.table.append ({})
        self.nestLevel += 1

    def exitScope (self):
        self.table.pop ()
        self.nestLevel -= 1

    # table [
    #   scope0 : {
    #       add : Symbol {
    #           typeDec : None,
    #           varDec : None,
    #           funDec : templates {
    #              0 template params : overloads[]
    #              1 template param  : TemplateFunction()
    #                  instances[]
    #              2 template params : TemplateFunction()
    #                  instances[]
    #           }
    #       }   
    #       vector : Symbol {
    #           typeDec : templates {
    #               0 template params : ClassDec
    #               1 template param  : TemplateClass()
    #                   instances[
    #                       vector<int>
    #                       vector<float>
    #                   ]
    #           }
    #           varDec : None,
    #           funDec : None
    #       }
    #       vector<int>::push_back : Symbol {
    #           typeDec : None
    #           varDec  : None,
    #           funDec  : templates {
    #               0 template params : overloads[]
    #           }
    #       }
    # 
    # ]
    def insert (self, decl, name, kind):
        # print (f"[SymbolTable] [insert] '{name}' as {kind}")

        # TYPES (CLASS, CLASSTEMP, ENUM)
        if kind == Kind.TYPE:
            # ** ensure decl is a type 
            # ensure type wasnt already declared in this scope
            if (name in self.table[-1] and self.table[-1][name].typeDec != {}):

                # CLASS TEMPLATES
                if isinstance (decl, ClassTemplateDeclarationNode):
                    # print (f"  {decl.templateParams}")
                    # ensure there isnt already a template with the same amount of template params 
                    if len(decl.templateParams) in self.table[-1][name].typeDec:
                        originalDec = self.table[-1][name].typeDec[len(decl.templateParams)].type
                        print (f"Semantic Error: Redeclaration of class template '{decl.id}' with {len(decl.templateParams)} template parameters")
                        print (f"   Original:")
                        print (f"      in file {originalDec.token.originalFilename}")
                        print (f"      on line {originalDec.token.originalLine}:{originalDec.token.column}")
                        print (f"      {self.lines[originalDec.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(originalDec.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print (f"   Redeclaration:")
                        print (f"      in file {decl._class.token.originalFilename}")
                        print (f"      on line {decl._class.token.originalLine}:{decl._class.token.column}")
                        print (f"      {self.lines[decl._class.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(decl._class.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print ()
                        return False
                # CLASS & ENUM
                else:
                    if 0 in self.table[-1][name].typeDec:
                        originalDec = self.table[-1][name].typeDec[0].type
                        print (f"Semantic Error: Redeclaration of class/enum '{decl.id}'")
                        print (f"   Original:")
                        print (f"      in file {originalDec.token.originalFilename}")
                        print (f"      on line {originalDec.token.originalLine}:{originalDec.token.column}")
                        print (f"      {self.lines[originalDec.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(originalDec.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print (f"   Redeclaration:")
                        print (f"      in file {decl.type.token.originalFilename}")
                        print (f"      on line {decl.type.token.originalLine}:{decl.type.token.column}")
                        print (f"      {self.lines[decl.type.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(decl.type.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print ()
                        return False

            # ensure symbol is in table 
            if (name not in self.table[-1]):
                self.table[-1][name] = Symbol ()

            # CLASS TEMPLATE
            if isinstance (decl, (ClassTemplateDeclarationNode)):
                # insert new type
                self.table[-1][name].typeDec[len(decl.templateParams)] = decl
            # CLASS & ENUM
            else:
                # insert new type
                self.table[-1][name].typeDec[0] = decl

            return True
        
        # VARIABLES, FIELDS
        elif kind == Kind.VAR:
            # ** ensure decl is a VAR 
            # ensure VAR wasnt already declared in this scope
            if (name in self.table[-1] and self.table[-1][name].varDec != None):
                # Ensure field is not shadowing an inherited field 
                if isinstance(decl, FieldDeclarationNode) and isinstance(self.table[-1][name].varDec, FieldDeclarationNode) \
                    and self.table[-1][name].varDec.isInherited:
                    pass
                # no inherited field shadowing 
                else:
                    return False

            # ensure symbol is in table 
            if (name not in self.table[-1]):
                self.table[-1][name] = Symbol ()

            # insert new VAR
            self.table[-1][name].varDec = decl
            return True

        
        # FUNCTIONS, METHODS, CONSTRUCTORS
        elif kind == Kind.FUNC:
            # ** ensure decl is a FUNC 
            # ensure FUNC wasnt already declared in this scope
            if (name in self.table[-1]):
                # Ensure function overload doesnt already exist
                if (isinstance (decl,(FunctionNode, MethodDeclarationNode, ConstructorDeclarationNode))):
                    # ensure that parameters dont match
                    for overload in self.table[-1][name].funDec[0]:
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
                # functions can be overloaded by the number of template parameters
                elif isinstance (decl, FunctionTemplateDeclarationNode):
                    # print (f"  {decl.types}")
                    # ensure there isnt already a template with the same amount of template params 
                    if len(decl.types) in self.table[-1][name].funDec:
                        originalDec = self.table[-1][name].funDec[len(decl.types)].type
                        print (f"Semantic Error: Redeclaration of template function '{decl.id}' with {len(decl.types)} template parameters")
                        print (f"   Original:")
                        print (f"      in file {originalDec.token.originalFilename}")
                        print (f"      on line {originalDec.token.originalLine}:{originalDec.token.column}")
                        print (f"      {self.lines[originalDec.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(originalDec.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print (f"   Redeclaration:")
                        print (f"      in file {decl.type.token.originalFilename}")
                        print (f"      on line {decl.type.token.originalLine}:{decl.type.token.column}")
                        print (f"      {self.lines[decl.type.token.line-1]}")
                        print (f"      ",end="")
                        for i in range(decl.type.token.column-1):
                            print (" ", end="")
                        print ("^")
                        print ()
                        return False
            # reaches here if not a redeclaration 

            # ensure symbol is in table 
            if (name not in self.table[-1]):
                self.table[-1][name] = Symbol ()

            # add function to overload list in table
            if isinstance (decl, (FunctionNode, MethodDeclarationNode, ConstructorDeclarationNode)):
                # add to overload list 
                self.table[-1][name].funDec[0].append (decl)
                return True

            # add function template to template overloads 
            elif isinstance (decl, FunctionTemplateDeclarationNode):
                # add template function
                self.table[-1][name].funDec[len(decl.types)] = decl 
                return True

        return False

    def lookup (self, name, kind, params=[], templateParams=[], visitor=None):

        # print (f"[SymbolTable] [lookup] {name}",end="")
        # if len(templateParams) > 0:
        #     print (f"<:{templateParams[0]}",end="")
        #     for i in range(1, len(templateParams)):
        #         print (f", {templateParams[i]}",end="")
        #     print(":>",end="")
        # print ()


        # for each scope
        # march through the scopes 
        # use closes suitable match 
        for i in range(len(self.table)-1, -1, -1):
            # ensure var is in this scope 
            if (name not in self.table[i]):
                continue

            # TYPES (CLASS, CLASSTEMP, ENUM)
            if (kind == Kind.TYPE):
                # CLASS TEMP
                if len(templateParams) > 0:
                    # ensure template params match 
                    if len(templateParams) not in self.table[i][name].typeDec:
                        continue 

                    # create template instance if DNE
                    tempSignature = [f"<:{templateParams[0]}"]
                    for j in range(1, len(templateParams)):
                        tempSignature += [f", {templateParams[j]}"]
                    tempSignature += [f":>"]
                    tempSignature = "".join(tempSignature)
                    if tempSignature not in self.table[i][name].typeDec[len(templateParams)].instantiations:
                        # print ("creating template instance...")
                        # print (name, tempSignature)
                        # create instance
                        _class = self.table[i][name].typeDec[len(templateParams)]._class.copy()
                        self.table[i][name].typeDec[len(templateParams)].instantiations[tempSignature] = _class
                        # overrite template aliases with their new types 
                        _class.templateParams = templateParams
                        _class.type.templateParams = templateParams
                        templateVisitor = TemplateVisitor (self.table[i][name].typeDec[len(templateParams)].templateParams, templateParams)
                        _class.accept (templateVisitor)
                        # analyze new instance 
                        visitor.insertFunc = False
                        oldWasSuccessful = visitor.wasSuccessful
                        visitor.wasSuccessful = True
                        _class.accept (visitor)
                        if not visitor.wasSuccessful:
                            print (f"**From instantiation of class '{_class.id+tempSignature}'", end="\n\n")
                            exit (1)
                        # restore previous success
                        visitor.wasSuccessful = visitor.wasSuccessful and oldWasSuccessful
                        visitor.insertFunc = True
                    return self.table[i][name].typeDec[len(templateParams)].instantiations[tempSignature]

                # CLASS & ENUM
                else:
                    # ensure symbol is a variable
                    if 0 not in self.table[i][name].typeDec:
                        continue
                    return self.table[i][name].typeDec[0]
            
            # VARIABLES, FIELDS
            elif (kind == Kind.VAR):
                # ensure symbol is a variable
                if self.table[i][name].varDec == None:
                    continue
                return self.table[i][name].varDec
                
            # FUNCTIONS, METHODS, CONSTRUCTORS, FUNCTION TEMPLATE
            elif (kind == Kind.FUNC):

                # FUNCTION TEMPLATE
                if len(templateParams) > 0 and isinstance (self.table[i][name].funDec, dict):
                    # ensure num template params match 
                    if len(templateParams) not in self.table[i][name].funDec:
                        continue
                    # find matching instance
                    # ** currently, overloading template functions with normal parameters is not supported 
                    tempSignature = [f"<:{templateParams[0].__str__()}"]
                    for j in range(1, len(templateParams)):
                        tempSignature += [f", {templateParams[j].__str__()}"]
                    tempSignature += [f":>"]
                    tempSignature = "".join(tempSignature)
                    # print (tempSignature)
                    # create template instance if it DNE
                    if tempSignature not in self.table[i][name].funDec[len(templateParams)].instantiations:
                        # print ("creating function template instance...")
                        # create instance
                        func = self.table[i][name].funDec[len(templateParams)].function.copy()
                        self.table[i][name].funDec[len(templateParams)].instantiations[tempSignature] = func
                        # overrite template aliases with their new types 
                        templateVisitor = TemplateVisitor (self.table[i][name].funDec[len(templateParams)].types, templateParams)
                        func.accept (templateVisitor)
                        # analyze new instance 
                        visitor.insertFunc = False
                        func.templateParams = templateParams
                        oldWasSuccessful = visitor.wasSuccessful
                        visitor.wasSuccessful = True
                        func.accept (visitor)
                        if not visitor.wasSuccessful:
                            print (f"**From instantiation of function '{func.signature}'", end="\n\n")
                        # restore previous success
                        visitor.wasSuccessful = visitor.wasSuccessful and oldWasSuccessful
                        visitor.insertFunc = True 
                    func = self.table[i][name].funDec[len(templateParams)].instantiations[tempSignature]
                    # ensure num params match 
                    if len(params) != len(func.params):
                        print (f"Semantic Error: Invalid number of parameters for template instance of '{func.id}'")
                        print (f"   Desired:    {func.signature}")
                        print (f"   Got:        {func.id}{tempSignature}(", end="")
                        if len(params) > 0:
                            print (f"{params[0].type}", end="")
                            for j in range(1, len(params)):
                                print (f", {params[j].type}", end="")
                        print (f")")
                        print ()
                        return None
                    # ensure type of params match 
                    for j in range(len(params)):
                        if params[j].type.__str__() != func.params[j].type.__str__():
                            # make sure types are not related 
                            isObject = func.params[j].type.type == Type.USERTYPE
                            isArray = func.params[j].type.arrayDimensions > 0
                            if params[j].type.id == "null" and (isObject or isArray):
                                continue
                            # ensure array dim match
                            if params[j].type.arrayDimensions != func.params[j].type.arrayDimensions:
                                break 
                            # ensure types are objects; for checking subtypes 
                            if func.params[j].type.type != Type.USERTYPE or params[j].type.type != Type.USERTYPE:
                                break 
                            # make sure lhs is not a subtype of rhs 
                            # get class declaration
                            parent = params[j].type.decl.pDecl 
                            match = False 
                            while parent != None:
                                # print (" ", parent.type, overload.params[j].type)
                                # check ids instead of __str__ because overload could be array but the parent type wouldn't be 
                                if parent.type.id == func.params[j].type.id:
                                    match = True
                                    break
                                parent = parent.pDecl 
                            # found matching parent class
                            # params[j] is of the same type as overload.params[j]
                            if match:
                                continue 
                            break
                    # all parameters are satisfactory 
                    else: 
                        return self.table[i][name].funDec[len(templateParams)].instantiations[tempSignature]
                    # reaches here if parameters dont match 
                    print (f"Semantic Error: Bad parameter types for template instance of '{func.id}'")
                    print (f"   Desired:    {func.signature}")
                    print (f"   Got:        {func.id}{tempSignature}(", end="")
                    if len(params) > 0:
                        print (f"{params[0].type}", end="")
                        for j in range(1, len(params)):
                            print (f", {params[j].type}", end="")
                    print (f")")
                    return None

                # FUNCTION, METHOD, CONSTRUCTOR 
                elif (isinstance (self.table[i][name].funDec, dict)):
                    # check each overload and determine initial candidates 
                    candidates = []
                    for overload in self.table[i][name].funDec[0]:
                        # check the number of parameters 
                        if (len(params) != len(overload.params)):
                            continue
                        # check parameter types 
                        # steps is the number of steps up from the derived class arguments to the overload's parameters 
                        # For example:
                        # C inherits B, B inherits A 
                        #   functioncall func(C, C);
                        # with:
                        #   declaration func(A, A); // 2 steps, 2 steps -> 4 total steps (C->B->A, C->B->A)
                        #   declaration func(B, B); // 1 step , 1 step  -> 2 total steps (C->B, C->B)
                        steps = 0
                        for j in range(len(params)):
                            # check if param type does not match
                            # print (params[j].type, overload.params[j].type)
                            if params[j].type.__str__() != overload.params[j].type.__str__():
                                # make sure types are not related 
                                isObject = overload.params[j].type.type == Type.USERTYPE
                                isArray = overload.params[j].type.arrayDimensions > 0
                                if params[j].type.id == "null" and (isObject or isArray):
                                    continue
                                # ensure array dim match
                                if params[j].type.arrayDimensions != overload.params[j].type.arrayDimensions:
                                    break 
                                # ensure types are objects; for checking subtypes 
                                if overload.params[j].type.type != Type.USERTYPE or params[j].type.type != Type.USERTYPE:
                                    break 
                                # make sure lhs is not a subtype of rhs 
                                # get class declaration
                                parent = params[j].type.decl.pDecl 
                                match = False 
                                steps += 1
                                while parent != None:
                                    # print (" ", parent.type, overload.params[j].type)
                                    # check ids instead of __str__ because overload could be array but the parent type wouldn't be 
                                    if parent.type.id == overload.params[j].type.id:
                                        match = True
                                        break
                                    parent = parent.pDecl 
                                    steps += 1
                                # found matching parent class
                                # params[j] is of the same type as overload.params[j]
                                if match:
                                    continue 
                                break
                        # all param types match - found a viable function decl overload
                        else: 
                            candidates += [(overload, steps)]
                        # check next overload 
                    # check if viable overloads were found 
                    if len(candidates) == 0:
                        # no viable overloads found at this scope
                        print (f"no viable candidates")
                        # return None 
                        continue
                    # found viable overloads 
                    # check for best viable overload 
                    # best viable overload is the one with the least number of steps 
                    # throws an ambiguity error if there are multiple 
                    maxVal = float("inf")
                    maxI = [0]
                    for j in range(len(candidates)):
                        if candidates[j][1] < maxVal:
                            maxVal = candidates[j][1]
                            maxI = [j]
                        # same steps 
                        elif candidates[j][1] == maxVal:
                            maxI += [j]
                    # check for ambiguity 
                    if len(maxI) > 1:
                        print (f"Semantic Error: Ambiguity in function lookup")
                        print (f"   Desired:    {name}(", end="")
                        if len(params) > 0:
                            print (f"{params[0].type}", end="")
                        for j in range(1, len(params)):
                            print (f", {params[j].type}",end="")
                        print (f")")
                        for j in maxI:
                            print (f"   Candidate:  {candidates[j][0].signature}")
                            print (f"      Steps: {candidates[j][1]}")
                        return None
                    # no ambiguity -> found viable candidate
                    return candidates[maxI[0]][0]
                    # reaches here if no overloads match 
                
        # reaches here if no matching declaration was found
        return None

# ========================================================================