# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

from ast import *
from visitor import ASTVisitor
from symbolTable import SymbolTable

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
            decl = self.typesTable.lookup (node.id)
            # variable has no declaration
            if (decl == None):
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
        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        # grab params so that the body can use them
        for p in node.params:
            self.parameters += [p]

        node.body.accept (self)

    def visitClassDeclarationNode(self, node):
        wasSuccessful = self.typesTable.insert (node)

        # save the current containing class
        self.containingClass += [node]

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.typesTable.lookup (varname)
            print (f"Semantic Error: Redeclaration of '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        # class will have its own scope 
        self.table.enterScope ()
        self.typesTable.enterScope ()

        # eval fields first to add to scope 
        for field in node.fields:
            field.accept (self)

        for ctor in node.constructors:
            ctor.accept (self)
        
        for method in node.methods:
            method.accept (self)

        self.table.exitScope ()
        self.typesTable.exitScope ()

        # remove current containing class (going out of scope)
        self.containingClass.pop ()

    def visitFieldDeclarationNode (self, node):
        node.type.accept (self)
        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of Field '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

    def visitMethodDeclarationNode (self, node):
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

        # grab params so that the body can use them
        for p in node.params:
            self.parameters += [p]

        node.body.accept (self)

    def visitConstructorDeclarationNode (self, node):
        # grab params so that the body can use them
        for p in node.params:
            self.parameters += [p]

        node.body.accept (self)
        

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)
        # print elifs 
        for e in node.elifs:
            e.accept (self)
        # print else 
        if node.elseStmt != None:
            node.elseStmt.accept (self)

    def visitElifStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)

    def visitElseStatementNode (self, node):
        node.body.accept (self)

    def visitForStatementNode (self, node):
        node.init.accept (self)
        node.cond.accept (self)
        node.update.accept (self)
        node.body.accept (self)

    def visitWhileStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)

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
        if (node.lhs.type.type != node.rhs.type.type \
            or node.lhs.type.arrayDimensions != node.rhs.type.arrayDimensions):
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

        node.type = node.lhs.type

        # ensure types work
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
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
        
        node.type = node.lhs.type

        # ensure types work
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
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
        
        node.type = node.lhs.type

        # ensure types work 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)
                or node.lhs.type.arrayDimensions > 0
                or node.rhs.type.arrayDimensions > 0):
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
        
        node.type = node.lhs.type

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

        node.function.accept (self)

        # search for function
        decl = self.table.lookup (node.function.id)
        # make sure the function declaration exists and its a function
        if (decl == None or not isinstance (decl, FunctionNode)):
            print (f"Semantic Error: '{node.function.id}' is not a function")
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

        # save declaration with function call
        node.decl = decl 

        # ensure the correct number of parameters 
        if (len(node.args) != len(decl.params)):
            print (f"Semantic Error: Invalid number of parameters")
            print (f"   Expected: {len(decl.params)}")
            print (f"   But got:  {len(node.args)}")
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

        # ensure each argument type matches the function's types
        for i in range(len(node.args)):
            # check for mismatched type
            if (node.args[i].type.type != decl.params[i].type.type
                or node.args[i].type.arrayDimensions != decl.params[i].type.arrayDimensions):
                print (f"Semantic Error: Parameter types in function call do not match function declaration")
                print (f"   Expected: {node.function.id}(", end="")
                if len(decl.params) > 0:
                    print (f"{decl.params[0].type}", end="")
                for i in range(1, len(decl.params)):
                    print (f", {decl.params[i].type}", end="")
                print (")")

                print (f"   But got:  {node.function.id}(", end="")
                if len(node.args) > 0:
                    print (f"{node.args[0].type}", end="")
                for i in range(1, len(node.args)):
                    print (f", {node.args[i].type}", end="")
                print (")")
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

        node.type = node.function.type 


    # not evaluated at this stage 
    def visitMemberAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.typesTable.lookup (node.lhs.type.id)
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

    def visitFieldAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        lhsdecl = self.typesTable.lookup (node.lhs.type.id)
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
                    node.methodDecl = method
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

        # ensure the correct number of parameters 
        if (len(node.args) != len(node.methodDecl.params)):
            print (f"Semantic Error: Invalid number of parameters in method call")
            print (f"   Expected: {len(node.methodDecl.params)}")
            print (f"   But got:  {len(node.args)}")
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

        # ensure each argument type matches the function's types
        for i in range(len(node.args)):
            # check for mismatched type
            if (node.args[i].type.type != node.methodDecl.params[i].type.type
                or node.args[i].type.arrayDimensions != node.methodDecl.params[i].type.arrayDimensions):
                print (f"Semantic Error: Parameter types in method call do not match method declaration")
                print (f"   Expected: {node.methodDecl.id}(", end="")
                if len(node.methodDecl.params) > 0:
                    print (f"{node.methodDecl.params[0].type}", end="")
                for i in range(1, len(node.methodDecl.params)):
                    print (f", {node.methodDecl.params[i].type}", end="")
                print (")")

                print (f"   But got:  {node.methodDecl.id}(", end="")
                if len(node.args) > 0:
                    print (f"{node.args[0].type}", end="")
                for i in range(1, len(node.args)):
                    print (f", {node.args[i].type}", end="")
                print (")")
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

    def visitArrayAllocatorExpressionNode (self, node):
        node.type.accept (self)
        for d in node.dimensions:
            d.accept (self)

    def visitConstructorCallExpressionNode (self, node):
        node.type.accept (self)

        # take the first constructor declaration
        node.decl = self.typesTable.lookup (node.id).constructors[0]

        for a in node.args:
            # ensure arguments match 
            a.accept (self)

        # ensure the correct number of parameters 
        if (len(node.args) != len(node.decl.params)):
            print (f"Semantic Error: Invalid number of parameters in constructor call")
            print (f"   Expected: {len(node.decl.params)}")
            print (f"   But got:  {len(node.args)}")
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

        # ensure each argument type matches the function's types
        for i in range(len(node.args)):
            # check for mismatched type
            if (node.args[i].type.type != node.decl.params[i].type.type
                or node.args[i].type.arrayDimensions != node.decl.params[i].type.arrayDimensions):
                print (f"Semantic Error: Parameter types in constructor call do not match constructor declaration")
                print (f"   Expected: {node.id}(", end="")
                if len(node.decl.params) > 0:
                    print (f"{node.decl.params[0].type}", end="")
                for i in range(1, len(node.decl.params)):
                    print (f", {node.decl.params[i].type}", end="")
                print (")")

                print (f"   But got:  {node.id}(", end="")
                if len(node.args) > 0:
                    print (f"{node.args[0].type}", end="")
                for i in range(1, len(node.args)):
                    print (f", {node.args[i].type}", end="")
                print (")")
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


# ========================================================================