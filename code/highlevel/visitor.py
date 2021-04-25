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
    def visitParameterNode (self, node):
        pass

    @abstractmethod
    def visitCodeUnitNode (self, node):
        pass

    @abstractmethod
    def visitFunctionNode (self, node):
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
    def visitIdentifierExpressionNode (self, node):
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

    def visitParameterNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Parameter: {node.id}\n"]

    def visitCodeUnitNode (self, node):
        pass

    def visitFunctionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Function: {node.id}\n"]

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
        self.outputstrings += ["Condition:\n"]

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
        self.outputstrings += ["Condition:\n"]

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
        self.outputstrings += ["Init:\n"]
        self.level += 1
        node.init.accept (self)
        self.level -= 1

        # print cond 
        self.printSpaces (self.level)
        self.outputstrings += ["Condition:\n"]
        self.level += 1
        node.cond.accept (self)
        self.level -= 1

        # print update 
        self.printSpaces (self.level)
        self.outputstrings += ["Update:\n"]
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
        self.outputstrings += ["Condition:\n"]
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
            self.level += 1
            node.expr.accept (self)
            self.level -= 1

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
        self.outputstrings += [f"Tuple:\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitAssignExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"AssignExpression: {node.op}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitLogicalOrExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"LogicalOR Expression: ||\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitLogicalAndExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"LogicalAND Expression: &&\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitEqualityExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"EqualityExpression: {node.op}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitInequalityExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"InequalityExpression: {node.op}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitAdditiveExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"AdditiveExpression: {node.op}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitMultiplicativeExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"MultiplicativeExpression: {node.op}\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitUnaryLeftExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"UnaryLeftExpression: {node.op}\n"]

        self.level += 1

        node.rhs.accept (self)

        self.level -= 1

    def visitPostIncrementExpressionNode(self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"PostIncrement:\n"]

        self.level += 1

        node.lhs.accept (self)

        self.level -= 1

    def visitPostDecrementExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"PostDecrement:\n"]

        self.level += 1

        node.lhs.accept (self)

        self.level -= 1

    def visitSubscriptExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Subscript Operator:\n"]

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
        self.outputstrings += [f"Function Call:\n"]

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
        self.outputstrings += [f"Member Accessor:\n"]

        self.level += 1

        node.lhs.accept (self)
        node.rhs.accept (self)

        self.level -= 1

    def visitIdentifierExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Identifier: {node.id}\n"]

    def visitIntLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Int Literal: {node.value}\n"]

    def visitFloatLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Float Literal: {node.value}\n"]

    def visitCharLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"Char Literal: {node.value}\n"]

    def visitStringLiteralExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"String Literal: {node.value}\n"]

    def visitListConstructorExpressionNode (self, node):
        self.printSpaces (self.level)
        self.outputstrings += [f"List Constructor:\n"]
        
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
            self.outputstrings += ["  "]
            level -= 1

# ========================================================================