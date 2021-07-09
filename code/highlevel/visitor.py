# Amy Script Compiler - AST Visitors
# By Amy Burnett
# April 24 2021
# ========================================================================

# for abstract classes 
from abc import ABC, abstractmethod

# ========================================================================

class ASTVisitor (ABC):

    @abstractmethod
    def visitProgramNode (self, node):
        pass

    @abstractmethod
    def visitTypeSpecifierNode (self, node):
        pass

    @abstractmethod
    def visitParameterNode (self, node):
        pass

    @abstractmethod
    def visitCodeUnitNode (self, node):
        pass

    @abstractmethod
    def visitVariableDeclarationNode (self, node):
        pass

    @abstractmethod
    def visitFunctionNode (self, node):
        pass

    @abstractmethod
    def visitClassDeclarationNode (self, node):
        pass

    @abstractmethod
    def visitStatementNode (self, node):
        pass

    @abstractmethod
    def visitIfStatementNode (self, node):
        pass

    @abstractmethod
    def visitElifStatementNode (self, node):
        pass

    @abstractmethod
    def visitElseStatementNode (self, node):
        pass

    @abstractmethod
    def visitForStatementNode (self, node):
        pass

    @abstractmethod
    def visitWhileStatementNode (self, node):
        pass

    @abstractmethod
    def visitExpressionStatementNode (self, node):
        pass

    @abstractmethod
    def visitReturnStatementNode (self, node):
        pass

    @abstractmethod
    def visitContinueStatementNode (self, node):
        pass

    @abstractmethod
    def visitBreakStatementNode (self, node):
        pass

    @abstractmethod
    def visitCodeBlockNode (self, node):
        pass

    @abstractmethod
    def visitExpressionNode (self, node):
        pass

    @abstractmethod
    def visitTupleExpressionNode (self, node):
        pass

    @abstractmethod
    def visitAssignExpressionNode (self, node):
        pass

    @abstractmethod
    def visitLogicalOrExpressionNode (self, node):
        pass

    @abstractmethod
    def visitLogicalAndExpressionNode (self, node):
        pass

    @abstractmethod
    def visitEqualityExpressionNode (self, node):
        pass

    @abstractmethod
    def visitInequalityExpressionNode (self, node):
        pass

    @abstractmethod
    def visitAdditiveExpressionNode (self, node):
        pass

    @abstractmethod
    def visitMultiplicativeExpressionNode (self, node):
        pass

    @abstractmethod
    def visitUnaryLeftExpressionNode (self, node):
        pass

    @abstractmethod
    def visitPostIncrementExpressionNode (self, node):
        pass

    @abstractmethod
    def visitPostDecrementExpressionNode (self, node):
        pass

    @abstractmethod
    def visitSubscriptExpressionNode (self, node):
        pass

    @abstractmethod
    def visitFunctionCallExpressionNode (self, node):
        pass

    @abstractmethod
    def visitMemberAccessorExpressionNode (self, node):
        pass

    @abstractmethod
    def visitFieldAccessorExpressionNode (self, node):
        pass

    @abstractmethod
    def visitMethodAccessorExpressionNode (self, node):
        pass

    @abstractmethod
    def visitThisExpressionNode (self, node):
        pass

    @abstractmethod
    def visitIdentifierExpressionNode (self, node):
        pass

    @abstractmethod
    def visitArrayAllocatorExpressionNode (self, node):
        pass

    @abstractmethod
    def visitIntLiteralExpressionNode (self, node):
        pass

    @abstractmethod
    def visitFloatLiteralExpressionNode (self, node):
        pass

    @abstractmethod
    def visitCharLiteralExpressionNode (self, node):
        pass

    @abstractmethod
    def visitStringLiteralExpressionNode (self, node):
        pass

    @abstractmethod
    def visitListConstructorExpressionNode (self, node):
        pass

# ========================================================================

class PrintVisitor (ASTVisitor):

    def __init__(self):
        self.level = 0
        self.outputstrings = [] 

    def visitProgramNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += ["ProgramNode:\n"]

        self.level += 1

        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

        self.level -= 1

    def visitTypeSpecifierNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Type: {node.type} {node.id}"]

        for i in range(node.arrayDimensions):
            self.outputstrings += ["[]"]
        self.outputstrings += ["\n"]

    def visitParameterNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Parameter: \n"]

        self.level += 1

        node.type.accept (self)

        self.printSpaces (self.level)
        self.outputstrings += [f"Name: {node.id}\n"]

        self.level -= 1

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"VariableDeclaration: \n"]

        self.level += 1

        node.type.accept (self)

        self.printSpaces (self.level)
        self.outputstrings += [f"Name: {node.id}\n"]

        self.level -= 1

    def visitFunctionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Function: {node.id} "]

        if (len(node.params) == 0):
            self.outputstrings += ["void"]
        else:
            self.outputstrings += [f"{node.params[0].type}"]
            for i in range(1, len(node.params)):
                self.outputstrings += [f":{node.params[i].type}"]
        self.outputstrings += [f"->{node.type}\n"]

        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += ["ReturnType:\n"]
        self.level += 1
        node.type.accept (self)
        self.level -= 1

        # print parameters 
        for param in node.params:
            param.accept (self)

        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        if node.body != None:
            node.body.accept (self)

        self.level -= 2

    def visitClassDeclarationNode(self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Class: {node.id}\n"]

        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += ["Constructors:\n"]

        self.level += 1
        for ctor in node.constructors:
            ctor.accept (self)
        self.level -= 1

        self.printSpaces (self.level)
        self.outputstrings += ["Fields:\n"]

        self.level += 1
        for field in node.fields:
            field.accept (self)
        self.level -= 1

        self.printSpaces (self.level)
        self.outputstrings += ["Methods:\n"]

        self.level += 1
        for method in node.methods:
            method.accept (self)
        self.level -= 1

        self.level -= 1

    def visitFieldDeclarationNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Field: \n"]

        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += [f"Security: {node.security}\n"]

        node.type.accept (self)
        
        self.printSpaces (self.level)
        self.outputstrings += [f"Name: {node.id}\n"]

        self.level -= 1

    def visitMethodDeclarationNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Method: {node.id} "]

        if (len(node.params) == 0):
            self.outputstrings += ["void"]
        else:
            self.outputstrings += [f"{node.params[0].type}"]
            for i in range(1, len(node.params)):
                self.outputstrings += [f":{node.params[i].type}"]
        self.outputstrings += [f"->{node.type}\n"]

        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += [f"Security: {node.security}\n"]
        
        self.printSpaces (self.level)
        self.outputstrings += ["ReturnType:\n"]
        self.level += 1
        node.type.accept (self)
        self.level -= 1

        self.printSpaces (self.level)
        self.outputstrings += [f"Name: {node.id}\n"]

        # print parameters 
        for param in node.params:
            param.accept (self)

        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        if node.body != None:
            node.body.accept (self)

        self.level -= 2

    def visitConstructorDeclarationNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Constructor: \n"]

        self.level += 1

        # print parameters 
        for param in node.params:
            param.accept (self)

        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        if node.body != None:
            node.body.accept (self)

        self.level -= 2

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"If:\n"]

        self.level += 1

        # print condition 
        self.printSpaces (self.level)
        self.outputstrings += [f"Condition: {node.cond.type.type}\n"]

        self.level += 1
        node.cond.accept (self)
        self.level -= 1

        # print body 
        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        node.body.accept (self)
        self.level -= 1

        # print elifs 
        for e in node.elifs:
            e.accept (self)

        # print else 
        if node.elseStmt != None:
            node.elseStmt.accept (self)

        self.level -= 1
        

    def visitElifStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Elif:\n"]

        self.level += 1

        # print condition 
        self.printSpaces (self.level)
        self.outputstrings += [f"Condition: {node.cond.type.type}\n"]

        self.level += 1
        node.cond.accept (self)
        self.level -= 1

        # print body 
        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        node.body.accept (self)
        self.level -= 1

        self.level -= 1
        

    def visitElseStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Else:\n"]

        self.level += 1

        # print body 
        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]

        self.level += 1
        node.body.accept (self)
        self.level -= 1

        self.level -= 1

    def visitForStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"For:\n"]

        self.level += 1

        # print init 
        self.printSpaces (self.level)
        self.outputstrings += [f"Init: {node.init.type.type}\n"]
        self.level += 1
        node.init.accept (self)
        self.level -= 1

        # print cond 
        self.printSpaces (self.level)
        self.outputstrings += [f"Condition: {node.cond.type.type}\n"]
        self.level += 1
        node.cond.accept (self)
        self.level -= 1

        # print update 
        self.printSpaces (self.level)
        self.outputstrings += [f"Update: {node.update.type.type}\n"]
        self.level += 1
        node.update.accept (self)
        self.level -= 1

        # print body 
        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]
        self.level += 1
        node.body.accept (self)
        self.level -= 1

        self.level -= 1

    def visitWhileStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"While:\n"]

        self.level += 1

        # print cond 
        self.printSpaces (self.level)
        self.outputstrings += [f"Condition: {node.cond.type.type}\n"]
        self.level += 1
        node.cond.accept (self)
        self.level -= 1

        # print body 
        self.printSpaces (self.level)
        self.outputstrings += ["Body:\n"]
        self.level += 1
        node.body.accept (self)
        self.level -= 1

        self.level -= 1

    def visitExpressionStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"ExpressionStatement:\n"]

        self.level += 1

        # print expr 
        if node.expr != None:
            node.expr.accept (self)

        self.level -= 1

    def visitReturnStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"ReturnStatement:\n"]

        self.level += 1

        # print expr 
        if node.expr != None:
            self.level += 1
            node.expr.accept (self)
            self.level -= 1

        self.level -= 1

    def visitContinueStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"ContinueStatement:\n"]

    def visitBreakStatementNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"BreakStatement:\n"]

    def visitCodeBlockNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"CodeBlock:\n"]

        self.level += 1

        # print each codeunit
        for unit in node.codeunits:
            unit.accept (self)

        self.level -= 1

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Tuple: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitAssignExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"AssignExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.type.accept (self)
        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitLogicalOrExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"LogicalOR Expression: || {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitLogicalAndExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"LogicalAND Expression: && {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitEqualityExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"EqualityExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitInequalityExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"InequalityExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitAdditiveExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"AdditiveExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitMultiplicativeExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"MultiplicativeExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitUnaryLeftExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"UnaryLeftExpression: {node.op} {node.type}\n"]

        self.level += 1

        node.rhs.accept (self)

        self.level -= 1

    def visitPostIncrementExpressionNode(self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"PostIncrement: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)

        self.level -= 1

    def visitPostDecrementExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"PostDecrement: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)

        self.level -= 1

    def visitSubscriptExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Subscript Operator: {node.type}\n"]

        self.level += 1
        
        self.printSpaces (self.level)
        self.outputstrings += ["Array:\n"]
        self.level += 1
        node.lhs.accept (self)
        self.level -= 1

        self.printSpaces (self.level)
        self.outputstrings += ["Offset:\n"]
        self.level += 1
        node.offset.accept (self)
        self.level -= 1

        self.level -= 1

    def visitFunctionCallExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Function Call: {node.type}\n"]

        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += ["Function Name:\n"]
        self.level += 1
        node.function.accept (self)
        self.level -= 1

        self.printSpaces (self.level)
        self.outputstrings += ["Arguments:\n"]
        self.level += 1
        for arg in node.args:
            arg.accept (self)
        self.level -= 1

        self.level -= 1

    def visitMemberAccessorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Member Accessor: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitFieldAccessorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Field Accessor: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitMethodAccessorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Method Accessor: {node.type}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)
        for arg in node.args:
            arg.accept (self)

        self.level -= 1

    def visitThisExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"This: {node.type}\n"]

    def visitIdentifierExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Identifier: {node.id} {node.type}\n"]

    def visitArrayAllocatorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"ArrayAllocator: {node.type}\n"]
        self.level += 1
        self.printSpaces (self.level)
        self.outputstrings += [f"Dimensions: \n"]
        self.level += 1
        for d in node.dimensions:
            d.accept (self)
        self.level -= 2

    def visitConstructorCallExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"ConstructorCall: {node.type}\n"]
        self.level += 1
        self.printSpaces (self.level)
        self.outputstrings += [f"Args: \n"]
        self.level += 1
        for a in node.args:
            a.accept (self)
        self.level -= 2

    def visitIntLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Int Literal: {node.value} {node.type}\n"]

    def visitFloatLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Float Literal: {node.value} {node.type}\n"]

    def visitCharLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Char Literal: {node.value} {node.type}\n"]

    def visitStringLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"String Literal: {node.value} {node.type}\n"]

    def visitListConstructorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"List Constructor: {node.type}\n"]
        
        self.level += 1

        self.printSpaces (self.level)
        self.outputstrings += ["Elements:\n"]
        self.level += 1
        for elem in node.elems:
            elem.accept (self)
        self.level -= 1

        self.level -= 1
    
    def printSpaces (self, level):
        while level > 0:
            self.outputstrings += ["|   "]
            level -= 1

# ========================================================================