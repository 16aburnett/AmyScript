# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

if __name__ == "semanticAnalyzer":
    from ast import *
    from visitor import ASTVisitor
    from symbolTable import SymbolTable
else:
    from .ast import *
    from .visitor import ASTVisitor
    from .symbolTable import SymbolTable

# ========================================================================

class SymbolTableVisitor (ASTVisitor):

    def __init__(self, lines):
        self.table = SymbolTable ()
        self.typesTable = SymbolTable ()
        self.parameters = []
        self.lines = lines 
        self.wasSuccessful = True
        self.checkDeclaration = True
        # works as a stack for nested class declarations
        self.containingClass = []

    def visitProgramNode (self, node):
        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

    def visitTypeSpecifierNode (self, node):
        # if type spec is not primitive
        if (node.type == Type.USERTYPE):
            # make sure type exists 
            # and save with the type spec for later lookup 
            node.decl = self.typesTable.lookup (node.id)
            # variable has no declaration
            if (node.decl == None):
                print (f"Semantic Error: '{node.id}' does not name a type")
                print (f"   Located on line {node.token.line}: column {node.token.column}")
                print (f"   line:")
                print (f"      {self.lines[node.token.line-1][:-1]}")
                print (f"      ",end="")
                for i in range(node.token.column-1):
                    print (" ", end="")
                print ("^")
                print ()
                self.wasSuccessful = False

    def visitParameterNode (self, node):
        node.type.accept (self)
        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of Param '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        node.type.accept (self)
        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

    def visitFunctionNode (self, node):
        node.type.accept (self)

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)
            self.parameters += [p]

        # create signature for node
        signature = [f"{node.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            originalDec = self.table.lookup (node.id, node.params)
            print (f"Semantic Error: Redeclaration of function '{node.signature}'")
            print (f"   Originally on line {originalDec.token.line}: column {originalDec.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        node.body.accept (self)


    def visitClassDeclarationNode(self, node):
        wasSuccessful = self.typesTable.insert (node)

        # save the current containing class
        self.containingClass += [node]

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.typesTable.lookup (varname)
            print (f"Semantic Error: Redeclaration of class '{varname}'")
            print (f"   Originally on line {originalDec.token.line}: column {originalDec.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        # Check for parent 
        if node.parent != "":
            # print (node.id, "inherits", node.parent)
            pDecl = self.typesTable.lookup (node.parent)
            if pDecl == None:
                print (f"Semantic Error: '{node.parent}' does not name a type")
                print (f"   On line {node.token.line}: column {node.token.column}")
                print ()
                self.wasSuccessful = False
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
        # self.typesTable.enterScope ()

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
        # self.typesTable.exitScope ()

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

    def visitFieldDeclarationNode (self, node):
        node.type.accept (self)

        # create signature for node
        node.signature = f"{node.parentClass.id}::{node.id}"

        wasSuccessful = self.table.insert (node, node.signature)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of Field '{varname}'")
            print (f"   Originally on line {originalDec.token.line}: column {originalDec.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

    def visitMethodDeclarationNode (self, node):
        node.type.accept (self)

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)
            self.parameters += [p]

        # create signature for node
        signature = [f"{node.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signatureNoScope = signature

        signature = [f"{node.parentClass.id}::{node.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        wasSuccessful = self.table.insert (node, f"{node.parentClass.id}::{node.id}")

        if (not wasSuccessful):
            originalDec = self.table.lookup (f"{node.parentClass.id}::{node.id}", node.params)
            print (f"Semantic Error: Redeclaration of Method '{node.signature}'")
            print (f"   Originally on line {originalDec.token.line}: column {originalDec.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        if not node.isInherited:
            node.body.accept (self)

    def visitConstructorDeclarationNode (self, node):

        # grab params so that the body can use them
        for p in node.params:
            # visit type to ensure valid type 
            p.type.accept (self)
            self.parameters += [p]

        # create signature for node
        signature = [f"{node.parentClass.id}::{node.parentClass.id}("]
        if len(node.params) > 0:
            signature += [node.params[0].type.__str__()]
        for i in range(1, len(node.params)):
            signature += [f", {node.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        node.signature = signature

        wasSuccessful = self.table.insert (node, f"{node.parentClass.id}::{node.parentClass.id}")

        if (not wasSuccessful):
            originalDec = self.table.lookup (f"{node.parentClass.id}::{node.parentClass.id}", node.params)
            print (f"Semantic Error: Redeclaration of ctor, '{node.signature}'")
            print (f"   Originally on line {originalDec.token.line}: column {originalDec.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        node.body.accept (self)
        

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()
        self.typesTable.enterScope ()

        node.cond.accept (self)
        node.body.accept (self)
        
        # exit scope before reaching elifs and else
        self.typesTable.exitScope ()
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
        self.typesTable.enterScope ()

        node.cond.accept (self)
        node.body.accept (self)

        # exit scope before reaching elifs and else
        self.typesTable.exitScope ()
        self.table.exitScope ()

    def visitElseStatementNode (self, node):
        node.body.accept (self)

    def visitForStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()
        self.typesTable.enterScope ()

        node.init.accept (self)
        node.cond.accept (self)
        node.update.accept (self)
        node.body.accept (self)

        if node.elseStmt:
            node.elseStmt.accept (self)

        self.typesTable.exitScope ()
        self.table.exitScope ()

    def visitWhileStatementNode (self, node):
        # create scope to include variables in condition 
        self.table.enterScope ()
        self.typesTable.enterScope ()

        node.cond.accept (self)
        node.body.accept (self)

        self.typesTable.exitScope ()
        self.table.exitScope ()

    def visitExpressionStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)

    def visitReturnStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)
        # *** make sure the type is that same as a function
        # *** make sure it is in a function

    def visitContinueStatementNode (self, node):
        # *** make sure it is in a loop
        # *** save loop's jump point in loop node ***
        pass

    def visitBreakStatementNode (self, node):
        # *** make sure it is in a loop
        pass

    def visitCodeBlockNode (self, node):
        self.table.enterScope ()
        self.typesTable.enterScope ()

        # if this is a function body
        # then add the parameters to this scope
        for p in self.parameters:
            p.accept (self)
        self.parameters.clear ()

        # print each codeunit
        for unit in node.codeunits:
            unit.accept (self)

        self.table.exitScope ()
        self.typesTable.exitScope ()

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
        isDiffType = node.lhs.type.type.__str__() != node.rhs.type.type.__str__()
        isDiffDimensions = node.lhs.type.arrayDimensions != node.rhs.type.arrayDimensions 
        isArrayNullOp = node.lhs.type.arrayDimensions > 0 and node.rhs.type.type == Type.NULL
        isObjectNullOp = node.lhs.type.type == Type.USERTYPE and node.lhs.type.arrayDimensions == 0 and node.rhs.type.type == Type.NULL
        # lhs is object 
        isSubtype = False 
        if node.lhs.type.type == Type.USERTYPE and node.rhs.type.type == Type.USERTYPE:
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
            if not isSubtype:
                # print ("not a subtype")
                isDiffType = True
        if (not isArrayNullOp and not isObjectNullOp and (isDiffType or isDiffDimensions)):
            print (f"Semantic Error: mismatching types in assign")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"Semantic Error: mismatching types in ||")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"Semantic Error: mismatching types in &&")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
                or node.lhs.type.arrayDimensions != node.rhs.type.arrayDimensions)):
            print (f"Semantic Error: mismatching types in equality")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
            print (f"Semantic Error: mismatching types in inequality")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False

    def visitAdditiveExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # **this might need to be changed if we allow char[] + int or int + char[]
        node.type = node.lhs.type

        # ensure types work for add/sub
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
            print (f"Semantic Error: mismatching types in additive")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False

    def visitMultiplicativeExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

        # ensure types work for mult/div/mod 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
            print (f"Semantic Error: mismatching types in multiplicative")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   {node.lhs.type} != {node.rhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   type: {node.lhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   type: {node.lhs.type}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False

    def visitSubscriptExpressionNode (self, node):
        if self.checkDeclaration:
            node.lhs.accept (self)

            # ensure lhs is an array 
            if (node.lhs.type.arrayDimensions == 0):
                print (f"Semantic Error: lhs must be an array")
                print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
                print (f"   type: {node.lhs.type}")
                print (f"   line:")
                print (f"      {self.lines[node.lineNumber-1][:-1]}")
                print (f"      ",end="")
                for i in range(node.columnNumber-1):
                    print (" ", end="")
                print ("^")
                print ()
                self.wasSuccessful = False

        # the type for this is lhs - 1 dimension
        node.type = TypeSpecifierNode (node.lhs.type.type, node.lhs.type.id, None)

        node.type.arrayDimensions = node.lhs.type.arrayDimensions - 1

        node.offset.accept (self)

    def visitFunctionCallExpressionNode (self, node):
        # eval arguments to get types 
        for arg in node.args:
            arg.accept (self)

        # search for function
        # create signature for node
        signature = [f"{node.function.id}("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        decl = self.table.lookup (node.function.id, node.args)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, FunctionNode)):
            print (f"Semantic Error: No function matching signature {signature}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.type


    # not evaluated at this stage 
    def visitMemberAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.typesTable.lookup (node.lhs.type.id)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            print (f"   LHS Type: {node.lhs.type}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False

        # check rhs 
        self.checkDeclaration = False
        node.rhs.accept (self)
        self.checkDeclaration = True

    def visitFieldAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.typesTable.lookup (node.lhs.type.id)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            print (f"   LHS Type: {node.lhs.type}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False

        # check rhs 
        self.checkDeclaration = False
        node.rhs.accept (self)
        self.checkDeclaration = True

    def visitMethodAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.typesTable.lookup (node.lhs.type.id)
        # make sure lhs is a class dec
        if not isinstance (lhsdecl, ClassDeclarationNode):
            print (f"Semantic Error: LHS of dot operator must be of class type")
            print (f"   LHS Type: {node.lhs.type}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
                    node.decl = method
                    break
        if not isMember:
            print (f"Semantic Error: '{rhsid}' is not a member of '{lhsdecl.id}'")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
        signature = [f"{lhsdecl.type.id}::{node.rhs.id}("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        # decl = self.table.lookup (signature)
        decl = self.table.lookup (f"{lhsdecl.type.id}::{node.rhs.id}", node.args)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, MethodDeclarationNode)):
            print (f"Semantic Error: No method matching signature {signature}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.type

    def visitThisExpressionNode (self, node):
        # ensure there is a containing class
        if (len(self.containingClass) == 0):
                print (f"Semantic Error: 'this' keyword used outside of class")
                print (f"   Located on line {node.token.line}: column {node.token.column}")
                print (f"   line:")
                print (f"      {self.lines[node.lineNumber-1][:-1]}")
                print (f"      ",end="")
                for i in range(node.columnNumber-1):
                    print (" ", end="")
                print ("^")
                print ()
                self.wasSuccessful = False
                return
        
        # ** make sure this is in a constructor or method

        decl = self.typesTable.lookup (self.containingClass[-1].id)
        # save declaration's type info
        node.type = decl.type
        # save declaration 
        node.decl = decl 

    def visitIdentifierExpressionNode (self, node):
        if (self.checkDeclaration):
            decl = self.table.lookup (node.id)
            # variable has no declaration
            if (decl == None):
                print (f"Semantic Error: '{node.id}' was not declared in this scope")
                print (f"   Located on line {node.token.line}: column {node.token.column}")
                print (f"   line:")
                print (f"      {self.lines[node.lineNumber-1][:-1]}")
                print (f"      ",end="")
                for i in range(node.columnNumber-1):
                    print (" ", end="")
                print ("^")
                print ()
                self.wasSuccessful = False
            # variable has declaration
            else:
                # save declaration's type info
                node.type = decl.type
                # save declaration 
                node.decl = decl 

    def visitArrayAllocatorExpressionNode (self, node):
        node.type.accept (self)
        for d in node.dimensions:
            d.accept (self)

    def visitConstructorCallExpressionNode (self, node):
        node.type.accept (self)

        # take the first constructor declaration
        node.decl = self.typesTable.lookup (node.id).constructors[0]

        for a in node.args:
            a.accept (self)

        # search for function
        # create signature for node
        signature = [f"{node.id}::{node.id}("]
        if len(node.args) > 0:
            signature += [node.args[0].type.__str__()]
        for i in range(1, len(node.args)):
            signature += [f", {node.args[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)

        decl = self.table.lookup (f"{node.id}::{node.id}", node.args)

        # save declaration with function call
        node.decl = decl 

        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, ConstructorDeclarationNode)):
            print (f"Semantic Error: No method matching signature {signature}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False
            return 

        node.type = node.decl.parentClass.type
    
    def visitSizeofExpressionNode(self, node):
        node.rhs.accept (self)
        # ensure RHS is an array
        if node.rhs.type.arrayDimensions == 0:
            print (f"Semantic Error: Sizeof requires an array")
            print (f"   Expected: <type>[]")
            print (f"   But got:  {node.rhs.type}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
            print ()
            self.wasSuccessful = False
            return 
    
    def visitFreeExpressionNode (self, node):
        node.rhs.accept (self)
        # ensure RHS is an array
        if node.rhs.type.arrayDimensions == 0 and node.rhs.type.type != Type.USERTYPE:
            print (f"Semantic Error: Free requires an array or object")
            print (f"   Expected: <type>[] or <userType>")
            print (f"   But got:  {node.rhs.type}")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
        pass

    def visitListConstructorExpressionNode (self, node):
        for elem in node.elems:
            elem.accept (self)

        if len(node.elems) == 0:
            print (f"Semantic Error: Empty list constructor")
            print (f"   List constructor needs at least one value")
            print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
            print (f"   line:")
            print (f"      {self.lines[node.lineNumber-1][:-1]}")
            print (f"      ",end="")
            for i in range(node.columnNumber-1):
                print (" ", end="")
            print ("^")
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
                print (f"   Located on line {node.lineNumber}: column {node.columnNumber}")
                print (f"   line:")
                print (f"      {self.lines[node.lineNumber-1][:-1]}")
                print (f"      ",end="")
                for i in range(node.columnNumber-1):
                    print (" ", end="")
                print ("^")
                print ()
                self.wasSuccessful = False
                return 


    def visitNullExpressionNode (self, node):
        pass


# ========================================================================