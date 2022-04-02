# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

from sys import exit
if __name__ == "semanticAnalyzer":
    from tokenizer import printToken
    from amyAST import *
    from visitor import ASTVisitor
    from symbolTable import *
else:
    from .tokenizer import printToken
    from .amyAST import *
    from .visitor import ASTVisitor
    from .symbolTable import *

# ========================================================================

class SymbolTableVisitor (ASTVisitor):

    def __init__(self, lines):
        self.table = SymbolTable ()

        self.parameters = []
        self.isFunctionBody = False

        self.lines = lines 
        self.table.lines = self.lines

        self.wasSuccessful = True
        self.checkDeclaration = True
        # works as a stack for nested class declarations
        self.containingClass = []
        self.containingFunction = [] 
        self.containingLoop = []

        # keeps track of the root 
        self.programNode = None

        self.insertFunc = True 

    def visitProgramNode (self, node):
        # keep track of the root node 
        self.programNode = node

        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

    def visitTypeSpecifierNode (self, node):
        # print (f"[typespec] {node}")
        # if type spec is not primitive
        if (node.type == Type.USERTYPE):
            # make sure type exists 
            # and save with the type spec for later lookup 
            node.decl = self.table.lookup (node.id, Kind.TYPE, [], node.templateParams, self)
            # variable has no declaration
            if (node.decl == None):
                print (f"Semantic Error: '{node}' does not name a type")
                if node.token != None:
                    printToken (node.token)
                print ()
                self.wasSuccessful = False
                node.type = Type.UNKNOWN
            # check template parameter types 
            # for tparam in node.templateParams:
            #     tparam.accept (self)

    def visitParameterNode (self, node):
        node.type.accept (self)
        wasSuccessful = self.table.insert (node, node.id, Kind.VAR)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname, Kind.VAR)
            print (f"Semantic Error: Redeclaration of Param '{varname}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        # print (f"checking type of {node.id} {node.type}")
        node.type.accept (self)
        # print (f"finished checking type {node.id} {node.type}")

        wasSuccessful = self.table.insert (node, node.id, Kind.VAR)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname, Kind.VAR)
            print (f"Semantic Error: Redeclaration of variable '{varname}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

        # save a reference to this variable for the function header
        if len(self.containingFunction) > 0:
            self.containingFunction[-1].localVariables += [node]
        # if global code, save to global localVariables 
        else:
            self.programNode.localVariables += [node]


    def visitFunctionNode (self, node):
        node.type.accept (self)

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)
            self.parameters += [p]

        # create signature for node
        signature = [f"{node.id}"]
        # add template params 
        if len(node.templateParams) > 0:
            signature += [f"<:"]
            signature += [f"{node.templateParams[0].__str__()}"]
            for i in range(1, len(node.templateParams)):
                signature += [f", {node.templateParams[i]}"]
            signature += [f":>"]
        signature += [f"("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        # this is for checking template instances 
        if self.insertFunc:
            wasSuccessful = self.table.insert (node, node.id, Kind.FUNC)

            if (not wasSuccessful):
                originalDec = self.table.lookup (node.id, Kind.FUNC, node.params)
                print (f"Semantic Error: Redeclaration of function '{node.signature}'")
                print (f"   Original:")
                printToken (originalDec.token, "      ")
                print (f"   Redeclaration:")
                printToken (node.token, "      ")
                print ()
                self.wasSuccessful = False
        else:
            self.insertFunc = True

        # containing function keeps track of what function 
        # we're currently in 
        # this is helpful for ensuring RETURN is in a function
        # and for ensuring the value being returned matches the function's return type 
        self.containingFunction += [node]
        # since we are now in a function, 
        # we want outer loops to be ignored 
        # so clear the containing loop state and restore it after the function
        containingLoop = self.containingLoop
        self.containingLoop = []

        self.isFunctionBody = True
        node.body.accept (self)
        self.isFunctionBody = False

        self.containingFunction.pop ()
        # restore containing loop state
        self.containingLoop = containingLoop


    def visitClassDeclarationNode(self, node):
        # save the current containing class
        self.containingClass += [node]
        # since we are now in a class, 
        # we want outer loops to be ignored 
        # so clear the containing loop state and restore it after the class
        containingLoop = self.containingLoop
        self.containingLoop = []

        if self.insertFunc:
            wasSuccessful = self.table.insert (node, node.id, Kind.TYPE)

            if (not wasSuccessful):
                varname = node.id 
                originalDec = self.table.lookup (varname, Kind.TYPE)
                print (f"Semantic Error: Redeclaration of class '{varname}'")
                print (f"   Original:")
                printToken (originalDec.token, "      ")
                print (f"   Redeclaration:")
                printToken (node.token, "      ")
                print ()
                self.wasSuccessful = False
        else:
            self.insertFunc = True

        # Check for parent 
        if node.parent != "":
            # print (node.id, "inherits", node.parent)
            pDecl = self.table.lookup (node.parent, Kind.TYPE)
            if pDecl == None:
                print (f"Semantic Error: '{node.parent}' does not name a type")
                printToken (node.pToken)
                print ()
                self.wasSuccessful = False
                return
            # save parent decl 
            node.pDecl = pDecl 
            # save self as a child to parent 
            pDecl.children += [node]

            # add parent fields to this fields
            fields = []
            for field in pDecl.fields: 
                fields += [FieldDeclarationNode (field.security, field.type, field.id, field.token)]
                fields[-1].isInherited = True
            # add current fields
            for field in node.fields:
                fields += [field]
            node.fields = fields

            # print (f"{node.id} inherits {node.parent}")

            # add non-overridden parent methods 
            methods = []
            for pMethod in pDecl.methods:
                # ensure method is not overridden
                # a method is overridden if the name and parameter types match 
                # otherwise, they are two separate functions 
                for method in node.methods:
                    # name matches 
                    if pMethod.id == method.id:
                        # ensure same num params  
                        if len(pMethod.params) == len(method.params):
                            # check each parameter 
                            for i in range (len(method.params)):
                                # check if param type is different 
                                if pMethod.params[i].type.__str__() != method.params[i].type.__str__():
                                    # non-matching param => non-matching signatures 
                                    break
                            # all params match => signatures match 
                            else:
                                # stop checking these methods because we know parent method is overridden 
                                # mark method as an override 
                                method.isOverride = True 
                                break 
                        # otherwise, params dont match, move on 
                    # name doesnt match, move on

                # method is not overridden 
                else: 
                    # create reference method to parent method
                    params = []
                    for p in pMethod.params:
                        params += [p]
                    m = MethodDeclarationNode (pMethod.security, pMethod.type, pMethod.id, pMethod.token, params, None, pMethod.isVirtual)
                    # mark method as inherited 
                    m.isInherited = True
                    # save parent method 
                    m.inheritedMethod = pMethod 
                    methods += [m]
            
            # add these methods 
            for method in node.methods:
                methods += [method]
            # save methods 
            node.methods = methods
        
        # class will have its own scope 
        # class does not have a scope atm
        # self.table.enterScope ()

        # eval fields first to add to scope 
        for field in node.fields:
            field.parentClass = node
            field.accept (self)

        for ctor in node.constructors:
            ctor.parentClass = node
            ctor.accept (self)
        
        for method in node.methods:
            method.parentClass = node
            method.accept (self)

        # self.table.exitScope ()

        # visit method bodies
        for method in node.methods:
            if not method.isInherited:
                for p in method.params:
                    self.parameters += [p]
                # containing function keeps track of what function 
                # we're currently in 
                # this is helpful for ensuring RETURN is in a function
                # and for ensuring the value being returned matches the function's return type 
                self.containingFunction += [method]
                method.body.accept (self)
                self.containingFunction.pop ()

        # visit ctor bodies
        for ctor in node.constructors:
            for p in ctor.params:
                self.parameters += [p]
            self.containingFunction += [ctor]
            ctor.body.accept (self)
            self.containingFunction.pop ()

        # Generating Dispatch table entries and their order 

        # any function in this class who's signature matches a function in parentVirtual 
        # print ("  Overridden Virtual Functions:")
        overriddenVirtual = [method for method in node.methods if method.isOverride]
        # for method in overriddenVirtual: print (f"    {method.signatureNoScope} -> {method.signature}")


        # print ("  New Virtual Functions:")
        newVirtual = [method for method in node.methods if not method.isOverride and not method.isInherited]
        # for method in newVirtual: print (f"    {method.signatureNoScope}")


        totalVirtual = []

        # save parent's order for virtual methods 
        node.virtualMethods = [m for m in pDecl.virtualMethods]
        node.functionPointerList = [m for m in pDecl.functionPointerList]
        # override parent's function pointers for this class 
        for method in overriddenVirtual:
            for i in range(len(node.virtualMethods)):
                if method.signatureNoScope == node.virtualMethods[i].signatureNoScope:
                    # override parent's method 
                    node.functionPointerList[i] = method 
                    # stop checking, found override 
                    break 
        
        # add new virtual methods and their corresponding methods
        for method in newVirtual:
            node.virtualMethods += [method]
            node.functionPointerList += [method]

        # print ("  Total Virtual Functions:")
        # for method in node.virtualMethods: print (f"    {method.signatureNoScope}")

        # print ("  Total Function Pointers:")
        # for method in node.functionPointerList: print (f"    {method.signature}")
        

        # print ()
        # print ()


        # remove current containing class (going out of scope)
        self.containingClass.pop ()
        # restore containing loop state
        self.containingLoop = containingLoop

    def visitFieldDeclarationNode (self, node):
        node.type.accept (self)

        # create signature for node
        node.signature = f"{node.parentClass.type}::{node.id}"

        wasSuccessful = self.table.insert (node, node.signature, Kind.VAR)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (node.signature, Kind.VAR)
            print (f"Semantic Error: Redeclaration of Field, '{varname}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

    def visitMethodDeclarationNode (self, node):
        node.type.accept (self)

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)

        # create signature for node
        signature = [f"{node.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signatureNoScope = signature

        signature = [f"{node.parentClass.type}::{node.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        wasSuccessful = self.table.insert (node, f"{node.parentClass.type}::{node.id}", Kind.FUNC)

        if (not wasSuccessful):
            originalDec = self.table.lookup (f"{node.parentClass.type}::{node.id}", Kind.FUNC, node.params)
            print (f"Semantic Error: Redeclaration of Method, '{node.signature}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

        # body is explored in class dec 

    def visitConstructorDeclarationNode (self, node):
        node.type = node.parentClass.type

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)

        # create signature for node
        signature = [f"{node.parentClass.type}::{node.parentClass.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        # print (f"adding {node.parentClass.type}::{node.parentClass.id} to the table ")
        wasSuccessful = self.table.insert (node, f"{node.parentClass.type}::{node.parentClass.id}", Kind.FUNC)

        if (not wasSuccessful):
            originalDec = self.table.lookup (f"{node.parentClass.type}::{node.parentClass.id}", Kind.FUNC, node.params)
            print (f"Semantic Error: Redeclaration of Constructor, '{node.signature}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

        # body is explored in class dec

    def visitEnumDeclarationNode (self, node):

        wasSuccessful = self.table.insert (node, node.id, Kind.TYPE)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname, Kind.TYPE)
            print (f"Semantic Error: Redeclaration of Enum, '{varname}'")
            print (f"   Original:")
            printToken (originalDec.token, "      ")
            print (f"   Redeclaration:")
            printToken (node.token, "      ")
            print ()
            self.wasSuccessful = False

        # *** enums currently cannot inherit from other enums/classes
        pDecl = self.table.lookup (node.parent, Kind.TYPE)
        if pDecl == None:
            print (f"Semantic Error: '{node.parent}' does not name a type")
            printToken (node.token)
            print ()
            self.wasSuccessful = False
        # save parent decl 
        node.pDecl = pDecl 
        
        # *** ensure each enum value is unique 

    def visitFunctionTemplateNode (self, node):

        # add template function to scope 
        wasSuccessful = self.table.insert (node, node.id, Kind.FUNC)
        if not wasSuccessful:
            self.wasSuccessful = False 

        # **ensure template types are unique 

        # add template typenames to scope 
        self.table.enterScope ()

        for t in node.types:
            self.table.insert (t, t.id, Kind.TYPE)

        # check the function 
        # node.function.accept (self)

        # exit scope 
        self.table.exitScope ()

    def visitClassTemplateDeclarationNode (self, node):

        # add template class to scope 
        wasSuccessful = self.table.insert (node, node.id, Kind.TYPE)
        if not wasSuccessful:
            self.wasSuccessful = False

        # **ensure template types are unique 

        # add template typenames to scope 
        self.table.enterScope ()

        for t in node.templateParams:
            self.table.insert (t, t.id, Kind.TYPE)

        # check the function 
        # node.function.accept (self)

        # exit scope 
        self.table.exitScope ()

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()

        node.cond.accept (self)
        node.body.accept (self)
        
        # exit scope before reaching elifs and else
        self.table.exitScope ()

        # print elifs 
        for e in node.elifs:
            e.accept (self)
        # print else 
        if node.elseStmt != None:
            node.elseStmt.accept (self)

    def visitElifStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()

        node.cond.accept (self)
        node.body.accept (self)

        # exit scope before reaching elifs and else
        self.table.exitScope ()

    def visitElseStatementNode (self, node):
        node.body.accept (self)

    def visitForStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()

        node.init.accept (self)
        node.cond.accept (self)
        node.update.accept (self)

        # containing loop keeps track of what loop we're currently in 
        # this is helpful for ensuring CONTINUE and BREAK are in a loop
        self.containingLoop += [node]
        node.body.accept (self)
        self.containingLoop.pop ()

        if node.elseStmt:
            node.elseStmt.accept (self)

        self.table.exitScope ()

    def visitWhileStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()

        node.cond.accept (self)

        # containing loop keeps track of what loop we're currently in 
        # this is helpful for ensuring CONTINUE and BREAK are in a loop
        self.containingLoop += [node]
        node.body.accept (self)
        self.containingLoop.pop ()

        self.table.exitScope ()

    def visitExpressionStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)

    def visitReturnStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)
        # ensure return statement is in a function
        if len(self.containingFunction) == 0:
            print (f"Semantic Error: Return statement must be in a function or method")
            printToken (node.token)
            print ()
            self.wasSuccessful = False 
            return 
        # ensure there is no return value if in a constructor 
        if isinstance (self.containingFunction[-1], ConstructorDeclarationNode) and node.expr != None:
            print (f"Semantic Error: Cannot return a value in a constructor")
            printToken (node.token)
            print ()
            self.wasSuccessful = False 
            return 
        # ensure return value matches the return type of the function 
        # this also checks for array/object vs null
        # and inheritance subtypes 
        if node.expr != None:
            # ensure types work 
            isDiffType = self.containingFunction[-1].type.__str__() != node.expr.type.__str__()
            isDiffDimensions = self.containingFunction[-1].type.arrayDimensions != node.expr.type.arrayDimensions 
            isArrayNullOp = self.containingFunction[-1].type.arrayDimensions > 0 and node.expr.type.type == Type.NULL
            isObjectNullOp = self.containingFunction[-1].type.type == Type.USERTYPE and self.containingFunction[-1].type.arrayDimensions == 0 and node.expr.type.type == Type.NULL
            # lhs is object 
            isSubtype = False 
            if self.containingFunction[-1].type.type == Type.USERTYPE and node.expr.type.type == Type.USERTYPE:
                parent = node.expr.type.decl
                # print (parent.type.id, self.containingFunction[-1].type.id)
                if parent.type.id == self.containingFunction[-1].type.id:
                    # print ("match!")
                    isSubtype = True
                    parent = None
                else:
                    parent = parent.pDecl 
                while parent != None:
                    # print (parent.type.id, self.containingFunction[-1].type.id)
                    if parent.type.id == self.containingFunction[-1].type.id:
                        # print ("match!")
                        isSubtype = True
                        break 
                    parent = parent.pDecl
                isDiffType = not isSubtype
            if (not isArrayNullOp and not isObjectNullOp and (isDiffType or isDiffDimensions)):
                print (f"Semantic Error: Return value does not match function's return type")
                printToken (node.token)
                print (f"   Expected: {self.containingFunction[-1].type}")
                print (f"   Got:      {node.expr.type}")
                print ()
                self.wasSuccessful = False 
                return 

    def visitContinueStatementNode (self, node):
        # ensure continue is in a loop
        if len(self.containingLoop) == 0:
            print (f"Semantic Error: Continue statement must be in a loop body")
            printToken (node.token)
            print ()
            self.wasSuccessful = False 
            return 

    def visitBreakStatementNode (self, node):
        # ensure break is in a loop
        if len(self.containingLoop) == 0:
            print (f"Semantic Error: Break statement must be in a loop body")
            printToken (node.token)
            print ()
            self.wasSuccessful = False 
            return 

    def visitCodeBlockNode (self, node):

        # determine scope type
        # this is used to determine number of dynamic links to follow
        scopeType = ScopeType.OTHER
        if self.isFunctionBody:
            scopeType = ScopeType.FUNCTION
            self.isFunctionBody = False

        self.table.enterScope (scopeType)

        # if this is a function body
        # then add the parameters to this scope
        for p in self.parameters:
            p.accept (self)
        self.parameters.clear ()

        # print each codeunit
        for unit in node.codeunits:
            unit.accept (self)

        self.table.exitScope ()

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitAssignExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

        # ensure types work 
        isDiffType = node.lhs.type.__str__() != node.rhs.type.__str__()
        isDiffDimensions = node.lhs.type.arrayDimensions != node.rhs.type.arrayDimensions 
        isArrayNullOp = node.lhs.type.arrayDimensions > 0 and node.rhs.type.type == Type.NULL
        isObjectNullOp = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and node.rhs.type.type == Type.NULL
        # lhs is object 
        isSubtype = False 
        # ensure both are objects and that rhs isn't Object
        if node.lhs.type.type == Type.USERTYPE and node.rhs.type.type == Type.USERTYPE and node.rhs.type.decl != None:
            parent = node.rhs.type.decl
            # print (parent.type.id, node.lhs.type.id)
            if parent.type.id == node.lhs.type.id:
                # print ("match!")
                isSubtype = True
                parent = None
            else:
                parent = parent.pDecl 
            while parent != None:
                # print (parent.type.id, node.lhs.type.id)
                if parent.type.id == node.lhs.type.id:
                    # print ("match!")
                    isSubtype = True
                    break 
                parent = parent.pDecl
            isDiffType = not isSubtype
        if (not isArrayNullOp and not isObjectNullOp and (isDiffType or isDiffDimensions)):
            print (f"Semantic Error: mismatching types in assign, \"{node.op.lexeme}\"")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitLogicalOrExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

        # ensure types work
        isLHSArray = node.lhs.type.arrayDimensions > 0
        isRHSArray = node.rhs.type.arrayDimensions > 0
        isLHSObject = node.lhs.type.type == Type.USERTYPE
        isRHSObject = node.rhs.type.type == Type.USERTYPE
        if (not isLHSArray and not isRHSArray and  not isLHSObject and not isRHSObject and (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0)):
            print (f"Semantic Error: invalid/mismatching types types in ||")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitLogicalAndExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

        # ensure types work
        isLHSArray = node.lhs.type.arrayDimensions > 0
        isRHSArray = node.rhs.type.arrayDimensions > 0
        isLHSObject = node.lhs.type.type == Type.USERTYPE
        isRHSObject = node.rhs.type.type == Type.USERTYPE
        if (not isLHSArray and not isRHSArray and not isLHSObject and not isRHSObject and (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0)):
            print (f"Semantic Error: invalid/mismatching types types in &&")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitEqualityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

        # ensure types work 
        isArrayNullOp = node.lhs.type.arrayDimensions > 0 and node.rhs.type.type == Type.NULL
        isObjectNullOp = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and node.rhs.type.type == Type.NULL
        if (not isArrayNullOp and not isObjectNullOp and (node.lhs.type.type != node.rhs.type.type
                or node.lhs.type.arrayDimensions != node.rhs.type.arrayDimensions
                or node.lhs.type.id != node.rhs.type.id)):
            print (f"Semantic Error: invalid/mismatching types in equality")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitInequalityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

        # ensure types work 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT
                and node.lhs.type.type != Type.CHAR)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
            print (f"Semantic Error: invalid/mismatching types in inequality")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitAdditiveExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # **this might need to be changed if we allow char[] + int or int + char[]
        node.type = node.lhs.type

        # ensure types work for add/sub
        if node.op.lexeme == '+':
            overloadedFunctionName = "__add__"
        elif node.op.lexeme == '-':
            overloadedFunctionName = "__sub__"
        hasOverloadedMethod = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs]) != None
        hasOverloadedFunction = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs]) != None
        # print (f"__add__({node.lhs.type.__str__()}, {node.rhs.type.__str__()})", hasOverloadedMethod)
        if ((node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
            or node.lhs.type.arrayDimensions > 0
            or node.rhs.type.arrayDimensions > 0)
            and not hasOverloadedMethod
            and not hasOverloadedFunction):
            print (f"Semantic Error: invalid/mismatching types for \"{node.op.lexeme}\"")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False
            
        # function operator overload 
        elif hasOverloadedFunction and not hasOverloadedMethod:
            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode (overloadedFunctionName, node.op, 0, 0), [node.lhs, node.rhs], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs])
        
        # method operator overload
        elif hasOverloadedMethod and not hasOverloadedFunction:
            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode (f"{node.lhs.type}::{overloadedFunctionName}", node.op, 0, 0), [node.lhs, node.rhs], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs])
        
        # ambiguous 
        elif hasOverloadedFunction and hasOverloadedMethod:
            overloadedMethodDecl = self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs])
            overloadedFunctionDecl = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs])
            print (f"Semantic Error: Ambiguous overload for subscript operator")
            printToken (node.op)
            print (f"   Candidate: {overloadedMethodDecl.signature}")
            printToken (overloadedMethodDecl.token)
            print (f"   Candidate: {overloadedFunctionDecl.signature}")
            printToken (overloadedFunctionDecl.token)
            print ()
            self.wasSuccessful = False

    def visitMultiplicativeExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

        # ensure types work for mult/div/mod 
        if node.op.lexeme == '*':
            overloadedFunctionName = "__mult__"
        elif node.op.lexeme == '/':
            overloadedFunctionName = "__div__"
        elif node.op.lexeme == '%':
            overloadedFunctionName = "__mod__"

        hasOverloadedMethod = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs]) != None
        hasOverloadedFunction = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs]) != None

        if ((node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
            or node.lhs.type.arrayDimensions > 0
            or node.rhs.type.arrayDimensions > 0)
            and not hasOverloadedMethod
            and not hasOverloadedFunction):
            print (f"Semantic Error: invalid/mismatching types for \"{node.op.lexeme}\"")
            printToken (node.op)
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print ()
            self.wasSuccessful = False
            
        # function operator overload 
        elif hasOverloadedFunction and not hasOverloadedMethod:
            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode (overloadedFunctionName, node.op, 0, 0), [node.lhs, node.rhs], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs])
        
        # method operator overload
        elif hasOverloadedMethod and not hasOverloadedFunction:
            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode (f"{node.lhs.type}::{overloadedFunctionName}", node.op, 0, 0), [node.lhs, node.rhs], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs])
        
        # ambiguous 
        elif hasOverloadedFunction and hasOverloadedMethod:
            overloadedMethodDecl = self.table.lookup (f"{node.lhs.type}::{overloadedFunctionName}", Kind.FUNC, [node.rhs])
            overloadedFunctionDecl = self.table.lookup (overloadedFunctionName, Kind.FUNC, [node.lhs, node.rhs])
            print (f"Semantic Error: Ambiguous overload for \"{overloadedFunctionName}\" operator")
            printToken (node.op)
            print (f"   Candidate: {overloadedMethodDecl.signature}")
            printToken (overloadedMethodDecl.token)
            print (f"   Candidate: {overloadedFunctionDecl.signature}")
            printToken (overloadedFunctionDecl.token)
            print ()
            self.wasSuccessful = False

    def visitUnaryLeftExpressionNode (self, node):
        node.rhs.accept (self)
        node.type = node.rhs.type 

        # ensure types work 
        if ((node.rhs.type.type != Type.INT
                and node.rhs.type.type != Type.FLOAT)
                or node.rhs.type.arrayDimensions > 0):
            print (f"Semantic Error: invalid type for unary left operator")
            printToken (node.op)
            print (f"   RHS type: {node.rhs.type}")
            print ()
            self.wasSuccessful = False

    def visitPostIncrementExpressionNode(self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

        # ensure types work for ++
        if ((node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0):
            print (f"Semantic Error: invalid type for increment operator")
            printToken (node.op)
            print (f"   LHS type: {node.lhs.type}")
            print ()
            self.wasSuccessful = False

    def visitPostDecrementExpressionNode (self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

        # ensure types work for --
        if ((node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0):
            print (f"Semantic Error: invalid type for decrement operator")
            printToken (node.op)
            print (f"   LHS type: {node.lhs.type}")
            print ()
            self.wasSuccessful = False

    def visitSubscriptExpressionNode (self, node):

        # *** implement multiple offsets for overloads

        if self.checkDeclaration:
            node.lhs.accept (self)

            # ensure lhs is an array 
            hasOverloadedMethod = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and self.table.lookup (f"{node.lhs.type}::__subscript__", Kind.FUNC, [node.offset]) != None
            hasOverloadedFunction = self.table.lookup ("__subscript__", Kind.FUNC, [node.lhs, node.offset]) != None
            if (node.lhs.type.arrayDimensions == 0
               and not hasOverloadedMethod
               and not hasOverloadedFunction):
                print (f"Semantic Error: lhs must be an array")
                printToken (node.op)
                print (f"   LHS type: {node.lhs.type}")
                print ()
                self.wasSuccessful = False

        # nonoverloaded 
        if not hasOverloadedFunction and not hasOverloadedMethod:
            # the type for this is lhs - 1 dimension
            node.type = node.lhs.type.copy ()

            node.type.arrayDimensions = node.lhs.type.arrayDimensions - 1

            node.type.accept (self)
            node.offset.accept (self)

            # ensure offset is type int or enum 
            isInt = node.offset.type.type == Type.INT and node.offset.type.arrayDimensions == 0
            isEnum = False
            typedecl = self.table.lookup(node.offset.type.id, Kind.TYPE)
            isEnum = typedecl and isinstance (typedecl, EnumDeclarationNode)
            if not (isInt or isEnum):
                print (f"Semantic Error: Offset of subscript operator must be an integer or enum")
                printToken (node.op)
                print (f"   Offset type: {node.offset.type}")
                print ()
                self.wasSuccessful = False
        # overloaded method
        elif hasOverloadedMethod and not hasOverloadedFunction:
            overloadedFunctionDecl = self.table.lookup (f"{node.lhs.type}::__subscript__", Kind.FUNC, [node.offset])

            # this type would be the return type of the overloaded call 
            node.type = overloadedFunctionDecl.type.copy ()

            node.type.accept (self)
            node.offset.accept (self)

            # just using a function call for simplicity
            # NOTE: implicit object parameter is also passed as an arg
            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode (f"{node.lhs.type}::__subscript__", node.op, 0, 0), [node.lhs, node.offset], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = overloadedFunctionDecl
        # overloaded function
        elif hasOverloadedFunction and not hasOverloadedMethod:
            overloadedFunctionDecl = self.table.lookup ("__subscript__", Kind.FUNC, [node.lhs, node.offset])

            # this type would be the return type of the overloaded call 
            node.type = overloadedFunctionDecl.type.copy ()

            node.type.accept (self)
            node.offset.accept (self)

            node.overloadedFunctionCall = FunctionCallExpressionNode (IdentifierExpressionNode ("__subscript__", node.op, 0, 0), [node.lhs, node.offset], [], node.op, 0, 0)
            node.overloadedFunctionCall.decl = overloadedFunctionDecl
        # ambiguous 
        elif hasOverloadedFunction and hasOverloadedMethod:
            overloadedMethodDecl = self.table.lookup (f"{node.lhs.type}::__subscript__", Kind.FUNC, [node.offset])
            overloadedFunctionDecl = self.table.lookup ("__subscript__", Kind.FUNC, [node.lhs, node.offset])
            print (f"Semantic Error: Ambiguous overload for \"__subscript__\" operator")
            printToken (node.op)
            print (f"   Candidate: {overloadedMethodDecl.signature}")
            printToken (overloadedMethodDecl.token)
            print (f"   Candidate: {overloadedFunctionDecl.signature}")
            printToken (overloadedFunctionDecl.token)
            print ()
            self.wasSuccessful = False

    def visitFunctionCallExpressionNode (self, node):
        # eval arguments to get types 
        for arg in node.args:
            arg.accept (self)
        
        # ensure any template parameters are valid types 
        for tparam in node.templateParams:
            tparam.accept (self)

        # search for function
        # create signature for node
        signature = [f"{node.function.id}"]
        # add template parameters
        if len(node.templateParams) > 0:
            signature += [f"<:{node.templateParams[0].__str__()}"]
            for i in range(1, len(node.templateParams)):
                signature += [f", {node.templateParams[i].__str__()}"]
            signature += [":>"]
        signature += ["("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        decl = self.table.lookup (node.function.id, Kind.FUNC, node.args, node.templateParams, self)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function or constructor 
        if (decl == None or not isinstance (decl,(FunctionNode, ConstructorDeclarationNode))):
            print (f"Semantic Error: No function matching signature {signature}")
            printToken (node.op)
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.type


    # not evaluated at this stage 
    def visitMemberAccessorExpressionNode (self, node):

        # check if lhs is a typename 
        if isinstance (node.lhs, IdentifierExpressionNode):
            typedecl = self.table.lookup (node.lhs.id, Kind.TYPE)
            # lhs is not a variable - its a type 
            if typedecl:
                # mark this as a static access
                node.isstatic = True 
                # print ("LHS IS A TYPENAME")
                # enums 
                if isinstance (typedecl, EnumDeclarationNode):
                    # the result of the enum member access is the enum
                    node.type = typedecl.type 
                    # ensure rhs is an identifier
                    if not isinstance (node.rhs, IdentifierExpressionNode):
                        print (f"Semantic Error: RHS of dot operator must be an indentifier")
                        printToken (node.op)
                        print ()
                        self.wasSuccessful = False
                        return
                    # ensure rhs is a valid member of the enum 
                    for field in typedecl.fields:
                        # found matching member
                        if field.id == node.rhs.id:
                            # print (f"{node.rhs.id} is a valid member of {node.lhs.id}")
                            # save member declaration 
                            node.decl = field 
                            break
                    # did not find member
                    else:
                        print (f"Semantic Error: '{node.rhs.id}' is not a member of '{node.lhs.id}'")
                        printToken (node.op)
                        print ()
                        self.wasSuccessful = False
                        return
                    return 
                elif isinstance (typedecl, ClassDeclarationNode):
                    print (f"ERROR: STATIC CLASS MEMBER ACCESS NOT IMPLEMENTED YET")
                    self.wasSuccessful = False
                    return 

        # non-static access

        node.lhs.accept (self)
        lhsdecl = self.table.lookup (node.lhs.type.id, Kind.TYPE, [], node.lhs.type.templateParams)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            printToken (node.op)
            print (f"   LHS Type: {node.lhs.type}")
            print (f"   LHS Decl: {lhsdecl}")
            print ()
            self.wasSuccessful = False
            return

        rhsid = None
        if (isinstance(node.rhs, IdentifierExpressionNode)):
            rhsid = node.rhs.id
        elif (isinstance(node.rhs, SubscriptExpressionNode)):
            rhsid = node.rhs.lhs.id
        else:
            print (f"Invalid member accessor")
            return
        # make sure rhs is a member of lhs
        isMember = False
        for field in lhsdecl.fields:
            if (field.id == rhsid):
                isMember = True
                node.type = field.type
                node.rhs.type = node.type
                node.decl = field
                break
        # check if it is a method
        if not isMember:
            for method in lhsdecl.methods:
                if (method.id == rhsid):
                    isMember = True
                    node.type = method.type
                    node.rhs.type = node.type
                    node.decl = method
                    break
        if not isMember:
            print (f"Semantic Error: '{rhsid}' is not a member of '{lhsdecl.id}'")
            printToken (node.op)
            print ()
            self.wasSuccessful = False

        # check rhs 
        self.checkDeclaration = False
        node.rhs.accept (self)
        self.checkDeclaration = True

    def visitFieldAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.table.lookup (node.lhs.type.id, Kind.TYPE, [], node.lhs.type.templateParams)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            printToken (node.op)
            print (f"   LHS Type: {node.lhs.type}")
            print ()
            self.wasSuccessful = False
            return
        rhsid = None
        if (isinstance(node.rhs, IdentifierExpressionNode)):
            rhsid = node.rhs.id
        elif (isinstance(node.rhs, SubscriptExpressionNode)):
            rhsid = node.rhs.lhs.id
        else:
            print (f"Invalid member accessor")
            return
        # make sure rhs is a member of lhs
        isMember = False
        for field in lhsdecl.fields:
            if (field.id == rhsid):
                isMember = True
                node.type = field.type
                node.rhs.type = node.type
                break
        # check if it is a method
        if not isMember:
            for method in lhsdecl.methods:
                if (method.id == rhsid):
                    isMember = True
                    node.type = method.type
                    node.rhs.type = node.type
                    break
        if not isMember:
            print (f"Semantic Error: '{rhsid}' is not a member of '{lhsdecl.id}'")
            printToken (node.op)
            print ()
            self.wasSuccessful = False

        # check rhs 
        self.checkDeclaration = False
        node.rhs.accept (self)
        self.checkDeclaration = True

    def visitMethodAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.table.lookup (node.lhs.type.id, Kind.TYPE, [], node.lhs.type.templateParams)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            printToken (node.op)
            print (f"   LHS Type: {node.lhs.type}")
            print ()
            self.wasSuccessful = False
            return
        rhsid = None
        if (isinstance(node.rhs, IdentifierExpressionNode)):
            rhsid = node.rhs.id
        elif (isinstance(node.rhs, SubscriptExpressionNode)):
            rhsid = node.rhs.lhs.id
        else:
            print (f"Semantic Error: Invalid RHS of dot operator")
            printToken (node.op)
            return
        # make sure rhs is a member of lhs
        isMember = False
        # check if it is a method
        if not isMember:
            for method in lhsdecl.methods:
                if (method.id == rhsid):
                    isMember = True
                    node.type = method.type
                    node.rhs.type = node.type
                    node.decl = method
                    break
        if lhsdecl.isForwardDeclaration:
            print (f"'{lhsdecl.id}' is incomplete")
        if not isMember:
            print (f"Semantic Error: '{rhsid}' is not a member of '{lhsdecl.id}'")
            printToken (node.op)
            print ()
            self.wasSuccessful = False

        # check rhs 
        self.checkDeclaration = False
        node.rhs.accept (self)
        self.checkDeclaration = True

        # eval arguments to get types 
        for arg in node.args:
            arg.accept (self)

        # search for function
        # create signature for node
        signature = [f"{lhsdecl.type}::{node.rhs.id}("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        # decl = self.table.lookup (signature)
        decl = self.table.lookup (f"{lhsdecl.type}::{node.rhs.id}", Kind.FUNC, node.args)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, MethodDeclarationNode)):
            print (f"Semantic Error: No method matching signature {signature}")
            printToken (node.op)
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.type

    def visitThisExpressionNode (self, node):
        # ensure there is a containing class
        if (len(self.containingClass) == 0):
            print (f"Semantic Error: 'this' keyword used outside of class")
            printToken (node.token)
            print ()
            self.wasSuccessful = False
            return
        
        # ** make sure this is in a constructor or method

        decl = self.table.lookup (self.containingClass[-1].id, Kind.TYPE, [], self.containingClass[-1].templateParams)
        # save declaration's type info
        node.type = decl.type
        # save declaration 
        node.decl = decl 

    def visitIdentifierExpressionNode (self, node):
        if (self.checkDeclaration):
            decl = self.table.lookup (node.id, Kind.VAR)
            # variable has no declaration
            if (decl == None):
                print (f"Semantic Error: '{node.id}' was not declared in this scope")
                printToken (node.token)
                print ()
                self.wasSuccessful = False
            # variable has declaration
            else:
                # save declaration's type info
                node.type = decl.type
                # save declaration 
                node.decl = decl 
                # print(f"==> {node.decl.id} : linksFollowed={self.table.linksFollowed}")

    def visitArrayAllocatorExpressionNode (self, node):
        node.type.accept (self)
        for d in node.dimensions:
            d.accept (self)

    def visitConstructorCallExpressionNode (self, node):
        # print (f"checking type of constructor call")
        node.type.accept (self)

        for a in node.args:
            a.accept (self)

        # search for function
        # create signature for node
        signature = [f"{node.type}::{node.type.id}("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        decl = self.table.lookup (f"{node.type}::{node.type.id}", Kind.FUNC, node.args, [], self)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, ConstructorDeclarationNode)):
            print (f"Semantic Error: No method matching signature {signature}")
            printToken (node.op)
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.parentClass.type
    
    def visitSizeofExpressionNode(self, node):
        node.rhs.accept (self)
        # ensure RHS is an array
        if node.rhs.type.arrayDimensions == 0:
            print (f"Semantic Error: Sizeof requires an array")
            printToken (node.op)
            print (f"   Expected: <type>[]")
            print (f"   But got:  {node.rhs.type}")
            print ()
            self.wasSuccessful = False
            return 
    
    def visitFreeExpressionNode (self, node):
        node.rhs.accept (self)
        # ensure RHS is an array
        if node.rhs.type.arrayDimensions == 0 and node.rhs.type.type != Type.USERTYPE:
            print (f"Semantic Error: Free requires an array or object")
            printToken (node.op)
            print (f"   Expected: <type>[] or <userType>")
            print (f"   But got:  {node.rhs.type}")
            print ()
            self.wasSuccessful = False
            return 

    def visitIntLiteralExpressionNode (self, node):
        pass

    def visitFloatLiteralExpressionNode (self, node):
        pass

    def visitCharLiteralExpressionNode (self, node):
        pass

    def visitStringLiteralExpressionNode (self, node):
        # FOR X86-64
        # save with program node so these can be added to the data section
        self.programNode.stringLiterals += [node]

    def visitListConstructorExpressionNode (self, node):
        for elem in node.elems:
            elem.accept (self)

        if len(node.elems) == 0:
            print (f"Semantic Error: Empty list constructor")
            printToken (node.token)
            print (f"   List constructor needs at least one value")
            print ()
            self.wasSuccessful = False
            return 

        # save type 
        firstType = node.elems[0].type
        node.type = TypeSpecifierNode(node.elems[0].type.type, node.elems[0].type.id, None)
        node.type.arrayDimensions = firstType.arrayDimensions + 1

        # ensure each element has the same type
        for elem in node.elems:
            if elem.type.type != firstType.type or elem.type.arrayDimensions != firstType.arrayDimensions:
                print (f"Semantic Error: All elements in a list constructor must have the same type")
                printToken (node.op)
                print ()
                self.wasSuccessful = False
                return 


    def visitNullExpressionNode (self, node):
        pass


# ========================================================================