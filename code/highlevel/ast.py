# Amy Script Compiler - Abstract Syntax Tree
# By Amy Burnett
# April 24 2021
# ========================================================================

# for abstract classes 
from abc import ABC, abstractmethod
from visitor import *

# ========================================================================

class Node (ABC):
    @abstractmethod
    def accept (self, visitor):
        pass

# ========================================================================
# codeunits - List(CodeUnitNode)

class ProgramNode (Node):

    def __init__(self, codeunits):
        self.codeunits = codeunits

    def accept (self, visitor):
        visitor.visitProgramNode (self)

# ========================================================================
# id - string

class ParameterNode (Node):

    def __init__(self, id):
        self.id = id

    def accept (self, visitor):
        visitor.visitParameterNode (self)

# ========================================================================

class CodeUnitNode (Node):
    
    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitCodeUnitNode (self)

# ========================================================================
# id - string
# params - List(ParameterNode)
# body - CodeBlockNode

class FunctionNode (CodeUnitNode):
    
    def __init__(self, id, params, body):
        self.id = id
        self.params = params
        self.body = body 

    def accept (self, visitor):
        visitor.visitFunctionNode (self)

# ========================================================================

class StatementNode (CodeUnitNode):
    
    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitStatementNode (self)

# ========================================================================
# cond - ExpressionNode
# body - StatementNode
# elifs - List(ElifStatementNode)
# elseStmt - ElseStatementNode

class IfStatementNode (StatementNode):
    
    def __init__(self, cond, body, elifs=[], elseStmt=None):
        self.cond = cond
        self.body = body
        self.elifs = elifs
        self.elseStmt = elseStmt 

    def accept (self, visitor):
        visitor.visitIfStatementNode (self)

# ========================================================================
# cond - ExpressionNode
# body - StatementNode

class ElifStatementNode (StatementNode):
    
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

    def accept (self, visitor):
        visitor.visitElifStatementNode (self)

# ========================================================================
# body - StatementNode

class ElseStatementNode (StatementNode):
    
    def __init__(self, body):
        self.body = body

    def accept (self, visitor):
        visitor.visitElseStatementNode (self)

# ========================================================================
# init - ExpressionNode
# cond - ExpressionNode
# update - ExpressionNode
# body - CodeUnitNode

class ForStatementNode (StatementNode):
    
    def __init__(self, init, cond, update, body):
        self.init = init
        self.cond = cond
        self.update = update
        self.body = body 

    def accept (self, visitor):
        visitor.visitForStatementNode (self)

# ========================================================================
# cond - ExpressionNode
# body - CodeUnitNode

class WhileStatementNode (StatementNode):
    
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body 

    def accept (self, visitor):
        visitor.visitWhileStatementNode (self)

# ========================================================================
# expr - ExpressionNode

class ExpressionStatementNode (StatementNode):
    
    def __init__(self, expr=None):
        self.expr = expr  

    def accept (self, visitor):
        visitor.visitExpressionStatementNode (self)

# ========================================================================
# expr - ExpressionNode

class ReturnStatementNode (StatementNode):
    
    def __init__(self, expr):
        self.expr = expr 

    def accept (self, visitor):
        visitor.visitReturnStatementNode (self)

# ========================================================================

class ContinueStatementNode (StatementNode):
    
    def __init__(self):
        pass 

    def accept (self, visitor):
        visitor.visitContinueStatementNode (self)

# ========================================================================

class BreakStatementNode (StatementNode):
    
    def __init__(self):
        pass 

    def accept (self, visitor):
        visitor.visitBreakStatementNode (self)

# ========================================================================
# codeunits - List(CodeUnitNode)

class CodeBlockNode (StatementNode):
    
    def __init__(self, codeunits):
        self.codeunits = codeunits

    def accept (self, visitor):
        visitor.visitCodeBlockNode (self)

# ========================================================================

class ExpressionNode (Node):

    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode 
# rhs - ExpressionNode

class TupleExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitTupleExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - AssignOp 
# rhs - ExpressionNode

class AssignExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitAssignExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalOrExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitLogicalOrExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalAndExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitLogicalAndExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - equality op  
# rhs - ExpressionNode

class EqualityExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitEqualityExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - inequality op  
# rhs - ExpressionNode

class InequalityExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitInequalityExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - additive op  
# rhs - ExpressionNode

class AdditiveExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitAdditiveExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - multiplicative op  
# rhs - ExpressionNode

class MultiplicativeExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitMultiplicativeExpressionNode (self)

# ========================================================================
# op  - unaryleft op  
# rhs - ExpressionNode

class UnaryLeftExpressionNode (ExpressionNode):

    def __init__(self, op, rhs):
        self.op = op
        self.rhs = rhs 

    def accept (self, visitor):
        visitor.visitUnaryLeftExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode

class PostIncrementExpressionNode (ExpressionNode):

    def __init__(self, lhs):
        self.lhs = lhs 

    def accept (self, visitor):
        visitor.visitPostIncrementExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode

class PostDecrementExpressionNode (ExpressionNode):

    def __init__(self, lhs):
        self.lhs = lhs 

    def accept (self, visitor):
        visitor.visitPostDecrementExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# offset - ExpressionNode

class SubscriptExpressionNode (ExpressionNode):

    def __init__(self, lhs, offset):
        self.lhs = lhs 
        self.offset = offset

    def accept (self, visitor):
        visitor.visitSubscriptExpressionNode (self)

# ========================================================================
# function - ExpressionNode
# args - list[ExpressionNode]

class FunctionCallExpressionNode (ExpressionNode):

    def __init__(self, function, args):
        self.function = function
        self.args = args 

    def accept (self, visitor):
        visitor.visitFunctionCallExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class MemberAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def accept (self, visitor):
        visitor.visitMemberAccessorExpressionNode (self)

# ========================================================================
# id - string

class IdentifierExpressionNode (ExpressionNode):

    def __init__(self, id):
        self.id = id

    def accept (self, visitor):
        visitor.visitIdentifierExpressionNode (self)

# ========================================================================
# value - int

class IntLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:int):
        self.value = value

    def accept (self, visitor):
        visitor.visitIntLiteralExpressionNode (self)

# ========================================================================
# value - float

class FloatLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:float):
        self.value = value

    def accept (self, visitor):
        visitor.visitFloatLiteralExpressionNode (self)

# ========================================================================
# value - char

class CharLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:chr):
        self.value = value

    def accept (self, visitor):
        visitor.visitCharLiteralExpressionNode (self)

# ========================================================================
# value - string

class StringLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:str):
        self.value = value

    def accept (self, visitor):
        visitor.visitStringLiteralExpressionNode (self)

# ========================================================================
# elems - list[ExpressionNode]

class ListConstructorExpressionNode (ExpressionNode):

    def __init__(self, elems:list):
        self.elems = elems

    def accept (self, visitor):
        visitor.visitListConstructorExpressionNode (self)

# ========================================================================