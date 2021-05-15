# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

from ast import *
from visitor import ASTVisitor
from symbolTable import SymbolTable

class SymbolTableVisitor (ASTVisitor):

    def __init__(self):
        self.table = SymbolTable ()
        self.parameters = []
        self.wasSuccessful = True

    def visitProgramNode (self, node):
        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

    def visitTypeSpecifierNode (self, node):
        # if type spec is not primitive
        if (node.type == Type.USERTYPE):
            # make sure type exists 
            decl = self.table.lookup (node.id)
            # variable has no declaration
            if (decl == None):
                print (f"Semantic Error: '{node.id}' does not name a type")
                print (f"   Located on line {node.token.line}: column {node.token.column}")
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
        wasSuccessful = self.table.insert (node)

        if (not wasSuccessful):
            varname = node.id 
            originalDec = self.table.lookup (varname)
            print (f"Semantic Error: Redeclaration of '{varname}'")
            print (f"   Originally on line {node.token.line}: column {node.token.column}")
            print (f"   Redeclaration on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False

        # class will have its own scope 
        self.table.enterScope ()

        # eval fields first to add to scope 
        for field in node.fields:
            field.accept (self)

        for ctor in node.constructors:
            ctor.accept (self)
        
        for method in node.methods:
            method.accept (self)

        self.table.exitScope ()

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

    def visitContinueStatementNode (self, node):
        pass

    def visitBreakStatementNode (self, node):
        pass

    def visitCodeBlockNode (self, node):
        self.table.enterScope ()

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
        if (node.lhs.type.type != node.rhs.type.type):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitLogicalOrExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

        # ensure types work
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitLogicalAndExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        node.type = node.lhs.type

        # ensure types work
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitEqualityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        node.type = node.lhs.type

        # ensure types work 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitInequalityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        node.type = node.lhs.type

        # ensure types work 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitAdditiveExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        node.type = node.lhs.type

        # ensure types work for add/sub
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitMultiplicativeExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

        # ensure types work for mult/div/mod 
        if (node.lhs.type.type != node.rhs.type.type
            or (node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False
            

    def visitUnaryLeftExpressionNode (self, node):
        node.rhs.accept (self)
        node.type = node.rhs.type 

        # ensure types work 
        if ((node.rhs.type.type != Type.INT
                and node.rhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitPostIncrementExpressionNode(self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

        # ensure types work for ++
        if ((node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitPostDecrementExpressionNode (self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

        # ensure types work for --
        if ((node.lhs.type.type != Type.INT
                and node.lhs.type.type != Type.FLOAT)):
            print (f"Semantic Error: mismatching types")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

    def visitSubscriptExpressionNode (self, node):
        node.lhs.accept (self)

        # ensure lhs is an array 
        if (node.lhs.type.arrayDimensions == 0):
            print (f"Semantic Error: lhs must be an array")
            print (f"   Located on line X: column Y")
            print ()
            self.wasSuccessful = False

        # the type for this is lhs - 1 dimension
        node.type = TypeSpecifierNode (node.lhs.type.type, node.lhs.type.id, None)
        node.type.arrayDimensions = node.lhs.type.arrayDimensions - 1

        node.offset.accept (self)

    def visitFunctionCallExpressionNode (self, node):
        node.function.accept (self)

        node.type = node.function.type 

        for arg in node.args:
            arg.accept (self)

    # not evaluated at this stage 
    def visitMemberAccessorExpressionNode (self, node):
        # node.lhs.accept (self)
        # node.rhs.accept (self)
        pass

    def visitIdentifierExpressionNode (self, node):
        decl = self.table.lookup (node.id)
        # variable has no declaration
        if (decl == None):
            print (f"Semantic Error: '{node.id}' was not declared in this scope")
            print (f"   Located on line {node.token.line}: column {node.token.column}")
            print ()
            self.wasSuccessful = False
        # variable has declaration
        else:
            # save declaration's type info
            node.type = decl.type

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