# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

if __name__ == "symbolTable":
    from ast import *
    from template import TemplateVisitor
else:
    from .ast import *  
    from .template import TemplateVisitor

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
        # print (f"**insert {name}**")
        # ensure variable wasnt already declared
        if (name in self.table[-1]):
            # functions of the same name can have multiple overloads
            if isinstance (decl, (FunctionNode, MethodDeclarationNode, ConstructorDeclarationNode)) and isinstance (self.table[-1][name], dict):
                # ensure that parameters dont match
                for overload in self.table[-1][name][0]:
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
                if len(decl.types) in self.table[-1][name]:
                    print (f"Semantic Error: Redeclaration of template function '{decl.id}' with {len(decl.types)} num template parameters")
                    print (f"   Original on line {self.table[-1][name][len(decl.types)].type.token.line} and column {self.table[-1][name][len(decl.types)].type.token.column}")
                    print (f"   Redeclaration on line {decl.type.token.line} and column {decl.type.token.column}")
                    return False
            # ensure field is not inherited from parent 
            elif isinstance (self.table[-1][name], FieldDeclarationNode) and isinstance (decl, FieldDeclarationNode) and self.table[-1][name].isInherited:
                # override if it is inherited and being overridden
                # this shadows/hides overridden parent fields 
                self.table[-1][name] = decl 
            # forward declaration 
            elif isinstance (self.table[-1][name], ClassDeclarationNode) and self.table[-1][name].isForwardDeclaration:
                # replace the forward declaration 
                self.table[-1][name] = decl
            else:
                return False
        # add function to overload list in table
        if isinstance (decl, (FunctionNode, MethodDeclarationNode, ConstructorDeclarationNode)):
            # create overload list if DNE
            if name not in self.table[-1]:
                # create template dict 
                self.table[-1][name] = {}
                # create overload dict 
                self.table[-1][name][0] = []
            # add to overload list 
            self.table[-1][name][0].append (decl)
            return True
        # add template function to template overloads 
        elif isinstance (decl, FunctionTemplateDeclarationNode):
            # create overload if DNE
            if name not in self.table[-1]:
                # create template dict
                self.table[-1][name] = {}
            # add template function
            self.table[-1][name][len(decl.types)] = decl 
            return True
        # add normal variable to table 
        self.table[-1][name] = decl
        return True

    def lookup (self, name, params=[], templateParams=[], visitor=None):
        # print (f"**lookup {name}**")
        for i in range(len(self.table)-1, -1, -1):
            # check scope for var 
            if (name in self.table[i]):
                # for matching templated functions 
                if len(templateParams) > 0 and isinstance (self.table[i][name], dict):
                    # ensure template has the correct number of template parameters 
                    if len(templateParams) not in self.table[i][name]:
                        # print ("template not found")
                        continue
                    # find matching instantiation 
                    # ** currently, overloading template functions with normal parameters is not supported 
                    tempSignature = [f"<:{templateParams[0].__str__()}"]
                    for j in range(1, len(templateParams)):
                        tempSignature += [f", {templateParams[j].__str__()}"]
                    tempSignature += [f":>"]
                    tempSignature = "".join(tempSignature)
                    # print (tempSignature)
                    # create template instance if it DNE
                    if tempSignature not in self.table[i][name][len(templateParams)].instantiations:
                        # print ("creating template instance...")
                        # create instance
                        func = self.table[i][name][len(templateParams)].function.copy()
                        self.table[i][name][len(templateParams)].instantiations[tempSignature] = func
                        # overrite template aliases with their new types 
                        templateVisitor = TemplateVisitor (self.table[i][name][len(templateParams)].types, templateParams)
                        func.accept (templateVisitor)
                        # analyze new instance 
                        visitor.insertFunc = False
                        func.templateParams = templateParams
                        oldWasSuccessful = visitor.wasSuccessful
                        visitor.wasSuccessful = True
                        func.accept (visitor)
                        if not visitor.wasSuccessful:
                            print (f"**From instantiation of '{func.signature}'", end="\n\n")
                        # restore previous success
                        visitor.wasSuccessful = visitor.wasSuccessful and oldWasSuccessful
                        visitor.insertFunc = True 
                    func = self.table[i][name][len(templateParams)].instantiations[tempSignature]
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
                        return self.table[i][name][len(templateParams)].instantiations[tempSignature]
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

                # for matching function overloads
                elif (isinstance (self.table[i][name], dict)):
                    # check each overload and determine initial candidates 
                    candidates = []
                    for overload in self.table[i][name][0]:
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
                        # no viable overloads found 
                        return None 
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
                # for matching variables 
                else:
                    return self.table[i][name]
                
        # reaches here if no matching variable declaration was found
        return None

# ========================================================================