# Amy Script Compiler - Abstract Syntax Tree
# By Amy Burnett
# April 24 2021
# ========================================================================

# for abstract classes 
from abc import ABC, abstractmethod
from enum import Enum
from sys import exit

if __name__ == "amyAST":
    from visitor import *
else:
    from .visitor import *

# ========================================================================

class Type(Enum):
    INT = 1
    FLOAT = 2
    CHAR = 3
    BOOL = 4
    STRING = 5
    VOID = 6
    USERTYPE = 7
    NULL = 8
    UNKNOWN = 9

class Security (Enum):
    PUBLIC = 1
    PRIVATE = 2

# ========================================================================

class Node (ABC):
    @abstractmethod
    def accept (self, visitor):
        pass

    @abstractmethod
    def copy (self):
        pass


# ========================================================================
# type - Type
# id - string

class TypeSpecifierNode (Node):
    
    def __init__(self, type:Type, id, token, templateParams=[]):
        self.type = type 
        self.id = id
        self.token = token
        self.arrayDimensions = 0

        self.templateParams = templateParams

        self.decl = None

        self.isGeneric = False

        self.lineNumber = 0
        self.columnNumber = 0

    def __str__(self):
        s = [self.id]
        if len(self.templateParams) > 0:
            s += ["<:", self.templateParams[0].__str__()]
            for i in range(1, len(self.templateParams)):
                s += [f", {self.templateParams[i].__str__()}"]
            s += [":>"]
        for i in range(self.arrayDimensions):
            s += ["[]"]
        return "".join(s)

    def accept (self, visitor):
        visitor.visitTypeSpecifierNode (self)

    def copy (self):
        node = TypeSpecifierNode (self.type, self.id, self.token)
        node.arrayDimensions = self.arrayDimensions
        node.decl = self.decl
        node.isGeneric = self.isGeneric
        node.templateParams = [t.copy() for t in self.templateParams]
        return node

# ========================================================================
# codeunits - List(CodeUnitNode)

class ProgramNode (Node):

    def __init__(self, codeunits):
        self.codeunits = codeunits

        self.lineNumber = 0
        self.columnNumber = 0

        self.localVariables = []
        self.floatLiterals = []
        self.stringLiterals = []

    def accept (self, visitor):
        visitor.visitProgramNode (self)

    def copy (self):
        node = ProgramNode (None)
        for codeunit in self.codeunits:
            node.codeunits += [codeunit.copy ()]
        node.localVariables = [n.copy() for n in self.localVariables]
        return node

# ========================================================================

class DeclarationNode (Node):

    def __init__(self, type:TypeSpecifierNode, id, token):
        self.type = type
        self.id = id
        self.token = token

        self.scopeName = "<unset-scope-name>"

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitDeclarationNode (self)

    def copy (self):
        node = DeclarationNode (self.type.copy(), self.id, self.token)
        node.scopeName = self.scopeName
        return node

# ========================================================================

class VariableDeclarationNode (DeclarationNode):

    def __init__(self, type:TypeSpecifierNode, id, token):
        super().__init__(type, id, token)

        self.lineNumber = 0
        self.columnNumber = 0

        # x86 fields
        self.stackOffset = 0

    def accept (self, visitor):
        visitor.visitVariableDeclarationNode (self)

    def copy (self):
        node = VariableDeclarationNode (self.type.copy(), self.id, self.token)
        node.stackOffset = self.stackOffset
        return node

# ========================================================================

class ParameterNode (DeclarationNode):

    def __init__(self, type:TypeSpecifierNode, id, token):
        super().__init__(type, id, token)

        self.lineNumber = 0
        self.columnNumber = 0

        # x86 fields
        self.stackOffset = 0

    def accept (self, visitor):
        visitor.visitParameterNode (self)

    def copy (self):
        node = ParameterNode (self.type.copy(), self.id, self.token)
        node.stackOffset = self.stackOffset
        return node

# ========================================================================

class GenericDeclarationNode (DeclarationNode):

    def __init__(self, type:TypeSpecifierNode, id, token):
        super().__init__(type, id, token)

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitGenericDeclarationNode (self)

    def copy (self):
        node = GenericDeclarationNode (self.type.copy(), self.id, self.token)
        return node

# ========================================================================

class CodeUnitNode (Node):
    
    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitCodeUnitNode (self)

    def copy (self):
        node = CodeUnitNode ()
        return node

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

        self.signature = ""

        self.scopeName = ""
        self.label = ""
        self.endLabel = ""

        self.templateParams = []

        self.lineNumber = 0
        self.columnNumber = 0

        self.localVariables = []

    def accept (self, visitor):
        visitor.visitFunctionNode (self)

    def copy (self):
        node = FunctionNode (self.type.copy(), self.id, self.token, [param.copy() for param in self.params], self.body.copy())
        node.signature = self.signature
        node.scopeName = self.scopeName
        node.label = self.label
        node.endLabel = self.endLabel
        node.localVariables = [n.copy() for n in self.localVariables]
        return node

# ========================================================================
# id - string
# body - CodeBlockNode

class ClassDeclarationNode (CodeUnitNode):
    
    def __init__(self, type, id, token, parent, pToken, constructors, fields, virtualMethods, methods):
        self.type = type
        self.type.decl = self 
        self.id = id
        self.token = token
        self.parent = parent 
        self.pToken = pToken
        self.pDecl = None 
        self.constructors = constructors
        self.fields = fields 
        self.methods = methods 

        self.templateParams = []

        self.children = []

        self.virtualMethods = [] 
        self.functionPointerList = [] 

        self.scopeName = ""
        self.dtableScopeName = ""

        self.signature = ""
        self.signatureNoScope = ""

        self.isForwardDeclaration = False 

        # x86 dispatch table offset
        self.stackOffset = 0

        # x86 this keyword offset
        self.thisStackOffset = 0

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitClassDeclarationNode (self)

    def copy (self):
        node = ClassDeclarationNode (self.type.copy(), self.id, self.token, self.parent, self.pToken, [c.copy() for c in self.constructors], [f.copy() for f in self.fields], [v.copy() for v in self.virtualMethods], [m.copy() for m in self.methods])
        node.children = [child.copy () for child in self.children]
        node.functionPointerList = [fptr.copy() for fptr in self.functionPointerList]
        node.scopeName = self.scopeName
        node.dtableScopeName = self.dtableScopeName
        node.isForwardDeclaration = self.isForwardDeclaration
        return node

# ========================================================================
# id - string

class FieldDeclarationNode (DeclarationNode):
    
    def __init__(self, security, type, id, token):
        self.security = security
        super().__init__(type, id, token)
        self.parentClass = None
        self.index = 0

        self.scopeName = ""
        self.signature = ""
        self.signatureNoScope = ""

        self.isInherited = False 

        # x86 fields
        self.stackOffset = 0

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitFieldDeclarationNode (self)

    def copy (self):
        node = FieldDeclarationNode (self.security, self.type.copy(), self.id, self.token)
        if self.parentClass != None:
            node.parentClass = self.parentClass.copy ()
        node.index = self.index 
        node.isInherited = self.isInherited
        return node

# ========================================================================
# id - string

class MethodDeclarationNode (DeclarationNode):
    
    def __init__(self, security, type, id, token, params, body, isVirtual=False):
        self.security = security
        super().__init__(type, id, token)
        self.params = params
        self.body = body 
        self.parentClass = None

        self.scopeName = ""

        self.signature = ""
        self.signatureNoScope = ""

        self.isVirtual = isVirtual
        self.isInherited = False 
        self.inheritedMethod = None
        self.isOverride = False 

        self.lineNumber = 0
        self.columnNumber = 0

        self.localVariables = []

    def accept (self, visitor):
        visitor.visitMethodDeclarationNode (self)

    def copy (self):
        node = MethodDeclarationNode (self.security, self.type.copy(), self.id, self.token, [p.copy() for p in self.params], self.body.copy (), self.isVirtual)
        
        if self.parentClass != None:
            node.parentClass = self.parentClass.copy ()

        node.scopeName = self.scopeName

        node.signature = self.signature
        node.signatureNoScope = self.signatureNoScope

        node.isVirtual = self.isVirtual
        node.isInherited = self.isInherited 
        if self.inheritedMethod != None:
            node.inheritedMethod = self.inheritedMethod.copy()
        node.isOverride = self.isOverride 
        return node

# ========================================================================
# id - string

class ConstructorDeclarationNode (DeclarationNode):
    
    def __init__(self, token, params, body):
        self.type = None
        self.id = ""
        self.token = token
        self.params = params
        self.body = body 
        self.parentClass = None

        self.scopeName = ""

        self.lineNumber = 0
        self.columnNumber = 0

        self.localVariables = []

    def accept (self, visitor):
        visitor.visitConstructorDeclarationNode (self)

    def copy (self):
        node = ConstructorDeclarationNode (self.token, [p.copy() for p in self.params], self.body.copy ())
        
        if self.parentClass != None:
            node.parentClass = self.parentClass.copy ()

        node.scopeName = self.scopeName

        return node

# ========================================================================

class EnumDeclarationNode (CodeUnitNode):
    
    def __init__(self, type, id, token, fields):
        self.type = type
        self.type.decl = self 
        self.id = id
        self.token = token
        self.fields = fields 
        
        self.parent = "Enum"
        self.pDecl = None 

        self.scopeName = ""
        self.dtableScopeName = ""

        self.isForwardDeclaration = False 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitEnumDeclarationNode (self)

    def copy (self):
        node = EnumDeclarationNode (self.type.copy(), self.id, self.token, [field.copy() for field in self.fields])
        return node

# ========================================================================

class FunctionTemplateDeclarationNode (CodeUnitNode):
    
    def __init__(self, type, id, token, types, function):
        self.type = type
        self.id = id
        self.token = token

        # template parameter names 
        self.types = types 

        # function declaration for the template 
        self.function = function

        # map of (string(templateParams), functionDeclaration)
        self.instantiations = {}

        self.scopeName = ""
        self.dtableScopeName = ""

        self.isForwardDeclaration = False 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitFunctionTemplateNode (self)

    def copy (self):
        node = FunctionTemplateDeclarationNode (self.type.copy(), self.id, self.token, [type for type in self.types], self.function.copy())
        return node

# ========================================================================

class ClassTemplateDeclarationNode (CodeUnitNode):
    
    def __init__(self, type, id, token, templateParams, _class):
        self.type = type
        self.id = id
        self.token = token

        # template parameter names 
        self.templateParams = templateParams 

        # class declaration for the template 
        self._class = _class

        # map of (string(templateParams), classDeclarationNodes)
        self.instantiations = {}

        self.scopeName = ""
        self.dtableScopeName = ""

        self.isForwardDeclaration = False 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitClassTemplateDeclarationNode (self)

    def copy (self):
        return ClassTemplateDeclarationNode (self.type.copy(), self.id, self.token, [type for type in self.templateParams], self._class.copy())

# ========================================================================

class StatementNode (CodeUnitNode):
    
    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitStatementNode (self)

    def copy (self):
        return StatementNode ()

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

    def copy (self):
        return IfStatementNode (self.cond.copy(), self.body.copy(), [e.copy() for e in self.elifs], None if self.elseStmt == None else self.elseStmt.copy())

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

    def copy (self):
        return ElifStatementNode (self.cond.copy(), self.body.copy())

# ========================================================================
# body - StatementNode

class ElseStatementNode (StatementNode):
    
    def __init__(self, body):
        self.body = body

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitElseStatementNode (self)

    def copy (self):
        return ElseStatementNode (self.body.copy())

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

    def copy (self):
        return ForStatementNode (self.init.copy(), self.cond.copy(), self.update.copy(), self.body.copy(), self.elseStmt.copy() if self.elseStmt else None)

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

    def copy (self):
        return WhileStatementNode (self.cond.copy(), self.body.copy())

# ========================================================================
# expr - ExpressionNode

class ExpressionStatementNode (StatementNode):
    
    def __init__(self, expr=None):
        self.expr = expr  

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitExpressionStatementNode (self)

    def copy (self):
        return ExpressionStatementNode (self.expr.copy() if self.expr != None else None)

# ========================================================================
# expr - ExpressionNode

class ReturnStatementNode (StatementNode):
    
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr 

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitReturnStatementNode (self)

    def copy (self):
        return ReturnStatementNode (self.token, self.expr.copy() if self.expr != None else None)

# ========================================================================

class ContinueStatementNode (StatementNode):
    
    def __init__(self, token):
        self.token = token

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitContinueStatementNode (self)

    def copy (self):
        return ContinueStatementNode (self.token)

# ========================================================================

class BreakStatementNode (StatementNode):
    
    def __init__(self, token):
        self.token = token

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitBreakStatementNode (self)

    def copy (self):
        return BreakStatementNode (self.token)

# ========================================================================
# codeunits - List(CodeUnitNode)

class CodeBlockNode (StatementNode):
    
    def __init__(self, codeunits):
        self.codeunits = codeunits

        self.lineNumber = 0
        self.columnNumber = 0

    def accept (self, visitor):
        visitor.visitCodeBlockNode (self)

    def copy (self):
        return CodeBlockNode ([codeunit.copy() for codeunit in self.codeunits])

# ========================================================================

class ExpressionNode (Node):

    def __init__(self):
        pass

    def accept (self, visitor):
        visitor.visitExpressionNode (self)

    def copy (self):
        return ExpressionNode()

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

    def copy (self):
        return TupleExpressionNode(self.lhs.copy(), self.rhs.copy(), self.lineNumber, self.columnNumber)

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

        self.overloadedFunctionCall = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitAssignExpressionNode (self)

    def copy (self):
        return AssignExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalOrExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitLogicalOrExpressionNode (self)

    def copy (self):
        return LogicalOrExpressionNode(self.lhs.copy(), self.rhs, self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode
# rhs - ExpressionNode

class LogicalAndExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs 

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitLogicalAndExpressionNode (self)

    def copy (self):
        return LogicalAndExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

    def copy (self):
        return EqualityExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

    def copy (self):
        return InequalityExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

        self.overloadedFunctionCall = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitAdditiveExpressionNode (self)

    def copy (self):
        return AdditiveExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

        self.overloadedFunctionCall = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMultiplicativeExpressionNode (self)

    def copy (self):
        return MultiplicativeExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

    def copy (self):
        return UnaryLeftExpressionNode(self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode

class PostIncrementExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 
        self.op = op

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitPostIncrementExpressionNode (self)

    def copy (self):
        return PostIncrementExpressionNode(self.lhs.copy(), self.op, self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode

class PostDecrementExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 
        self.op = op

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitPostDecrementExpressionNode (self)

    def copy (self):
        return PostDecrementExpressionNode(self.lhs.copy(), self.op, self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode
# offset - ExpressionNode

class SubscriptExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, offset, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs 
        self.op = op
        self.offset = offset

        self.overloadedFunctionCall = None
        self.overloadedMethodCall = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitSubscriptExpressionNode (self)

    def copy (self):
        return SubscriptExpressionNode(self.lhs.copy(), self.op, self.offset.copy(), self.lineNumber, self.columnNumber)

# ========================================================================
# function - ExpressionNode
# args - list[ExpressionNode]

class FunctionCallExpressionNode (ExpressionNode):

    def __init__(self, function, args, templateParams, op, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.function = function
        self.args = args 
        self.op = op

        self.templateParams = templateParams 

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitFunctionCallExpressionNode (self)

    def copy (self):
        return FunctionCallExpressionNode(self.function.copy(), [arg.copy() for arg in self.args], [tempParam.copy() for tempParam in self.templateParams], self.op, self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class MemberAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
        # id is the assembly representation of the function 
        # for class method calls 
        self.id = ""

        self.isstatic = False

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMemberAccessorExpressionNode (self)

    def copy (self):
        return MemberAccessorExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class FieldAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitFieldAccessorExpressionNode (self)

    def copy (self):
        return FieldAccessorExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

# ========================================================================
# lhs - ExpressionNode - must be class type 
# rhs - ExpressionNode  - must be a valid member  

class MethodAccessorExpressionNode (ExpressionNode):

    def __init__(self, lhs, op, rhs, args, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
        self.args = args

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitMethodAccessorExpressionNode (self)

    def copy (self):
        return MethodAccessorExpressionNode(self.lhs.copy(), self.op, self.rhs.copy(), [arg.copy() for arg in self.args], self.lineNumber, self.columnNumber)

# ========================================================================

class ThisExpressionNode (ExpressionNode):

    def __init__(self, token, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.token = token

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitThisExpressionNode (self)

    def copy (self):
        return ThisExpressionNode(self.token, self.lineNumber, self.columnNumber)

# ========================================================================
# id - string

class IdentifierExpressionNode (ExpressionNode):

    def __init__(self, id, token, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.id = id
        self.token = token

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitIdentifierExpressionNode (self)

    def copy (self):
        return IdentifierExpressionNode(self.id, self.token, self.lineNumber, self.columnNumber)

# ========================================================================

class ArrayAllocatorExpressionNode (ExpressionNode):

    def __init__(self, type, dimensions, templateParams, line, column):
        self.type = type
        self.dimensions = dimensions

        self.templateParams = templateParams

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitArrayAllocatorExpressionNode (self)

    def copy (self):
        return ArrayAllocatorExpressionNode(self.type.copy(), [d.copy() for d in self.dimensions], [t.copy() for t in self.templateParams], self.lineNumber, self.columnNumber)

# ========================================================================

class ConstructorCallExpressionNode (ExpressionNode):

    def __init__(self, type, id, op, args, templateParams, line, column):
        self.type = type
        self.id = id
        self.op = op
        self.args = args

        self.templateParams = templateParams

        self.decl = None

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitConstructorCallExpressionNode (self)

    def copy (self):
        return ConstructorCallExpressionNode(self.type.copy(), self.id, self.op, [a.copy() for a in self.args], [t.copy() for t in self.templateParams], self.lineNumber, self.columnNumber)

# ========================================================================

class SizeofExpressionNode (ExpressionNode):

    def __init__(self, type, op, rhs, line, column):
        self.type = type
        self.op = op
        self.rhs = rhs

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitSizeofExpressionNode (self)

    def copy (self):
        return SizeofExpressionNode(self.type.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

# ========================================================================

class FreeExpressionNode (ExpressionNode):

    def __init__(self, type, op, rhs, line, column):
        self.type = type
        self.op = op
        self.rhs = rhs

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitFreeExpressionNode (self)

    def copy (self):
        return FreeExpressionNode(self.type.copy(), self.op, self.rhs.copy(), self.lineNumber, self.columnNumber)

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

    def copy (self):
        return IntLiteralExpressionNode(self.value)

# ========================================================================
# value - float

class FloatLiteralExpressionNode (ExpressionNode):

    def __init__(self, value:float):
        self.type = TypeSpecifierNode (Type.FLOAT, "float", None)
        self.value = value

        self.lineNumber = 0
        self.columnNumber = 0
        
        # x86
        self.label = "<ERROR:LABEL NOT SET>"

    def accept (self, visitor):
        visitor.visitFloatLiteralExpressionNode (self)

    def copy (self):
        return FloatLiteralExpressionNode(self.value)

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

    def copy (self):
        return CharLiteralExpressionNode(self.value)

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

        # x86
        self.label = "<ERROR:LABEL NOT SET>"

    def accept (self, visitor):
        visitor.visitStringLiteralExpressionNode (self)

    def copy (self):
        return StringLiteralExpressionNode(self.value)

# ========================================================================
# elems - list[ExpressionNode]

class ListConstructorExpressionNode (ExpressionNode):

    def __init__(self, op, elems:list, line, column):
        self.type = TypeSpecifierNode (Type.UNKNOWN, "", None)
        self.op = op
        self.elems = elems

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitListConstructorExpressionNode (self)

    def copy (self):
        return ListConstructorExpressionNode(self.op, [e.copy() for e in self.elems], self.lineNumber, self.columnNumber)

# ========================================================================

class NullExpressionNode (ExpressionNode):

    def __init__(self, line, column):
        self.type = TypeSpecifierNode (Type.NULL, "null", None)
        self.value = 0

        self.lineNumber = line
        self.columnNumber = column

    def accept (self, visitor):
        visitor.visitNullExpressionNode (self)

    def copy (self):
        return NullExpressionNode(self.lineNumber, self.columnNumber)

# ========================================================================