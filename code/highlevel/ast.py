# Amy Script Compiler - Abstract Syntax Tree
# By Amy Burnett
# April 24 2021
# ========================================================================

# for abstract classes 
from abc import ABC, abstractmethod
from visitor import *

from enum import Enum

class Type(Enum):
    INT = 1
    FLOAT = 2
    CHAR = 3
    BOOL = 4
    STRING = 5
    VOID = 6
    USERTYPE = 7
    UNKNOWN = 8

class Security (Enum):
    PUBLIC = 1
    PRIVATE = 2

# ========================================================================

class Node (ABC):
    @abstractmethod
    def accept (self, visitor):
        pass

# ========================================================================
# type - Type
# id - string

class TypeSpecifierNode (Node):
    
    def __init__(self, type:Type, id, token):
        self.type = type 
        self.id = id
        self.token = token
        self.arrayDimensions = 0

        self.lineNumber = 0
        self.columnNumber = 0

    def __str__(self):
        s = [self.id]
        for i in range(self.arrayDimensions):
            s += ["[]"]
        return "".join(s)

    def accept (self, visitor):
        visitor.visitTypeSpecifierNode (self)

# ========================================================================
# codeunits - List(CodeUnitNode)

class ProgramNode (Node):

    def __init__(self, codeunits):
        self.codeunits = codeunits

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitProgramNode (self)

# ========================================================================

class DeclarationNode (Node):

    def __init__(self, type:TypeSpecifierNode, id, token):
        self.type = type
        self.id = id
        self.token = token

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitDeclarationNode (self)

# ========================================================================

class VariableDeclarationNode (DeclarationNode):

    def __init__(self, type:TypeSpecifierNode, id, token):
        super().__init__(type, id, token)

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitVariableDeclarationNode (self)

# ========================================================================
# id - string

class ParameterNode (DeclarationNode):

    def __init__(self, type:TypeSpecifierNode, id, token):
        super().__init__(type, id, token)

        self.lineNumber = 0
        self.columnNumber = 0

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
    
    def __init__(self, type:TypeSpecifierNode, id, token, params, body):
        self.type = type 
        self.id = id
        self.token = token
        self.params = params
        self.body = body 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitFunctionNode (self)

# ========================================================================
# id - string
# body - CodeBlockNode

class ClassDeclarationNode (CodeUnitNode):
    
    def __init__(self, type, id, token, constructors, fields, methods):
        self.type = type
        self.id = id
        self.token = token
        self.constructors = constructors
        self.fields = fields 
        self.methods = methods 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitClassDeclarationNode (self)

# ========================================================================
# id - string

class FieldDeclarationNode (DeclarationNode):
    
    def __init__(self, security, type, id, token):
        self.security = security
        super().__init__(type, id, token)
        self.parentClass = None

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitFieldDeclarationNode (self)

# ========================================================================
# id - string

class MethodDeclarationNode (DeclarationNode):
    
    def __init__(self, security, type, id, token, params, body):
        self.security = security
        super().__init__(type, id, token)
        self.params = params
        self.body = body 
        self.parentClass = None

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitMethodDeclarationNode (self)

# ========================================================================
# id - string

class ConstructorDeclarationNode (DeclarationNode):
    
    def __init__(self, token, params, body):
        self.token = token
        self.params = params
        self.body = body 
        self.parentClass = None

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitConstructorDeclarationNode (self)

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

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitIfStatementNode (self)

# ========================================================================
# cond - ExpressionNode
# body - StatementNode

class ElifStatementNode (StatementNode):
    
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitElifStatementNode (self)

# ========================================================================
# body - StatementNode

class ElseStatementNode (StatementNode):
    
    def __init__(self, body):
        self.body = body

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitElseStatementNode (self)

# ========================================================================
# init - ExpressionNode
# cond - ExpressionNode
# update - ExpressionNode
# body - CodeUnitNode

class ForStatementNode (StatementNode):
    
    def __init__(self, init, cond, update, body, elseStmt):
        self.init = init
        self.cond = cond
        self.update = update
        self.body = body 
        self.elseStmt = elseStmt
        self.startLabel = ""
        self.breakLabel = ""
        self.endLabel = ""

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitForStatementNode (self)

# ========================================================================
# cond - ExpressionNode
# body - CodeUnitNode

class WhileStatementNode (StatementNode):
    
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body 
        self.startLabel = ""
        self.breakLabel = ""
        self.endLabel = ""

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitWhileStatementNode (self)

# ========================================================================
# expr - ExpressionNode

class ExpressionStatementNode (StatementNode):
    
    def __init__(self, expr=None):
        self.expr = expr  

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitExpressionStatementNode (self)

# ========================================================================
# expr - ExpressionNode

class ReturnStatementNode (StatementNode):
    
    def __init__(self, expr):
        self.expr = expr 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitReturnStatementNode (self)

# ========================================================================

class ContinueStatementNode (StatementNode):
    
    def __init__(self):

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitContinueStatementNode (self)

# ========================================================================

class BreakStatementNode (StatementNode):
    
    def __init__(self):

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitBreakStatementNode (self)

# ========================================================================
# codeunits - List(CodeUnitNode)

class CodeBlockNode (StatementNode):
    
    def __init__(self, codeunits):
        self.codeunits = codeunits

        self.lineNumber = 0
        self.columnNumber = 0

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

    def __init__(self, lhs, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitTupleExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - AssignOp 
# rhs - ExpressionNode

class AssignExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitAssignExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalOrExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitLogicalOrExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalAndExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitLogicalAndExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - equality op  
# rhs - ExpressionNode

class EqualityExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitEqualityExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - inequality op  
# rhs - ExpressionNode

class InequalityExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitInequalityExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - additive op  
# rhs - ExpressionNode

class AdditiveExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitAdditiveExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# op  - multiplicative op  
# rhs - ExpressionNode

class MultiplicativeExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMultiplicativeExpressionNode (self)

# ========================================================================
# op  - unaryleft op  
# rhs - ExpressionNode

class UnaryLeftExpressionNode (ExpressionNode):

    def __init__(self, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitUnaryLeftExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode

class PostIncrementExpressionNode (ExpressionNode):

    def __init__(self, lhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitPostIncrementExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode

class PostDecrementExpressionNode (ExpressionNode):

    def __init__(self, lhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitPostDecrementExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode
# offset - ExpressionNode

class SubscriptExpressionNode (ExpressionNode):

    def __init__(self, lhs, offset, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 
        self.offset = offset

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitSubscriptExpressionNode (self)

# ========================================================================
# function - ExpressionNode
# args - list[ExpressionNode]

class FunctionCallExpressionNode (ExpressionNode):

    def __init__(self, function, args, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.function = function
        self.args = args 
        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitFunctionCallExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class MemberAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs
        # id is the assembly representation of the function 
        # for class method calls 
        self.id = ""

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMemberAccessorExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class FieldAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitFieldAccessorExpressionNode (self)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class MethodAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, rhs, args, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.rhs = rhs
        self.args = args
        self.methodDecl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMethodAccessorExpressionNode (self)

# ========================================================================

class ThisExpressionNode (ExpressionNode):

    def __init__(self, token, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.token = token

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitThisExpressionNode (self)

# ========================================================================
# id - string

class IdentifierExpressionNode (ExpressionNode):

    def __init__(self, id, token, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.id = id
        self.token = token

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitIdentifierExpressionNode (self)

# ========================================================================

class ArrayAllocatorExpressionNode (ExpressionNode):

    def __init__(self, type, dimensions, line, column):
        self.type = type
        self.dimensions = dimensions

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitArrayAllocatorExpressionNode (self)

# ========================================================================

class ConstructorCallExpressionNode (ExpressionNode):

    def __init__(self, type, id, args, line, column):
        self.type = type
        self.id = id
        self.args = args
        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitConstructorCallExpressionNode (self)

# ========================================================================

class SizeofExpressionNode (ExpressionNode):

    def __init__(self, type, rhs, line, column):
        self.type = type
        self.rhs = rhs

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitSizeofExpressionNode (self)

# ========================================================================
# value - int

class IntLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:int):
        self.type = TypeSpecifierNode (Type.INT, "int", None)
        self.value = value

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitIntLiteralExpressionNode (self)

# ========================================================================
# value - float

class FloatLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:float):
        self.type = TypeSpecifierNode (Type.FLOAT, "float", None)
        self.value = value

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitFloatLiteralExpressionNode (self)

# ========================================================================
# value - char

class CharLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:chr):
        self.type = TypeSpecifierNode (Type.CHAR, "char", None)
        self.value = value

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitCharLiteralExpressionNode (self)

# ========================================================================
# value - string

class StringLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:str):
        # char[] instead of string
        self.type = TypeSpecifierNode (Type.CHAR, "char", None)
        self.type.arrayDimensions = 1
        self.value = value

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitStringLiteralExpressionNode (self)

# ========================================================================
# elems - list[ExpressionNode]

class ListConstructorExpressionNode (ExpressionNode):

    def __init__(self, elems:list, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.elems = elems

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitListConstructorExpressionNode (self)

# ========================================================================