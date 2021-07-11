# Amy Script Compiler - Code Generation
# By Amy Burnett
# April 11 2021
# ========================================================================

from ast import *
from visitor import ASTVisitor
from symbolTable import SymbolTable

DIVIDER_LENGTH = 75 
TAB_LENGTH = 3

class CodeGenVisitor (ASTVisitor):

    def __init__(self, lines, srcFilename, libFilename):
        self.parameters = []
        self.lines = lines 
        self.indentation = 0
        self.code = []
        self.lhs = "null"
        self.jumpIndex = 0
        self.shouldComment = True
        self.srcFilename = srcFilename
        self.libFilename = libFilename
        # stack implementation
        # keeps track of containing loop
        # for break and continue statements 
        self.parentLoops = []
        self.pushParent = False

    # === HELPER FUNCTIONS ===============================================

    def printSpaces (self, level):
        if not self.shouldComment:
            return 
            
        while level > 0:
            for i in range(TAB_LENGTH):
                self.code += [" "]
            level -= 1

    def printCode (self, line):
        self.printSpaces (self.indentation)
        self.code += [f"{line}\n"]

    def printComment (self, comment):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        self.code += ["// ", comment, "\n"]

    def printHeader (self, header):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - len (header) - 8
        divider = ["//### "]
        divider += [header, " "]
        for i in range(dividerLength):
            divider += ["#"]
        divider += ["\n"]
        self.code += ["".join(divider)]

    def printDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//"]
        for i in range(dividerLength):
            divider += ["="]
        divider += ["\n"]
        self.code += ["".join(divider)]

    def printSubDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//"]
        for i in range(dividerLength):
            divider += ["-"]
        divider += ["\n"]
        self.code += ["".join(divider)]

    def printNewline (self):
        if not self.shouldComment:
            return 
        self.code += ["\n"]

    # === VISITOR FUNCTIONS ==============================================

    def visitProgramNode (self, node):

        self.printComment ("AmyAssembly compiled from AmyScript")
        self.printComment (f"Filename: {self.srcFilename}")
        self.printDivider ()
        self.printNewline ()

        self.printDivider ()
        self.printHeader ("LIBRARY CODE")
        self.printDivider ()
        self.printNewline ()

        # add library code
        file = open (self.libFilename, "r")
        for line in file.readlines ():
            self.code += [line]

        self.printDivider ()
        self.printHeader ("COMPILED CODE")
        self.printDivider ()
        self.printNewline ()

        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

        self.printDivider ()
        self.printHeader ("END OF CODE")
        self.printDivider ()
        self.printNewline ()

    def visitTypeSpecifierNode (self, node):
        pass

    def visitParameterNode (self, node):
        node.type.accept (self)

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        self.printComment ("Variable Declaration")
        node.type.accept (self)

        self.indentation += 1

        # declare the variable with default value 
        self.printCode (f"ASSIGN {node.id} 0")
        self.lhs = node.id

        self.indentation -= 1

    def visitFunctionNode (self, node):

        self.printDivider ()
        self.printComment (f"Function Declaration - {node.id} {node.type}")
        # add jump to skip over function 
        self.printCode (f"JUMP __end__{node.id}")

        # place function jump-point label 
        self.printCode (node.id + ":")

        self.indentation += 1

        # load parameters 
        self.printComment ("Parameters")
        self.indentation += 1
        for i in range(len(node.params)):
            self.printComment (f"Param: {node.params[i].id}")
            # keep the same parameter name 
            self.printCode (f"STACKGET {node.params[i].id} {i}")
        self.indentation -= 1

        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # extra return statement for if return is not provided 
        self.printCode ("RETURN 0")

        self.indentation -= 1

        self.printCode (f"__end__{node.id}:")

        self.printComment (f"End Function Declaration - {node.id}")
        self.printDivider ()
        self.printNewline ()

    def visitClassDeclarationNode(self, node):

        self.printDivider ()
        self.printComment (f"Class Declaration - {node.id}")

        self.indentation += 1

        i = 0
        for field in node.fields:
            field.parentClass = node
            self.printSubDivider ()
            self.printComment (f"Field - {field.id}")

            fieldIndexVarname = f"__field__{node.id}__{field.id}"
            self.printCode (f"ASSIGN {fieldIndexVarname} {i}")
            i += 1

            self.printSubDivider ()

        # add jump to skip over class dec  
        self.indentation -= 1
        self.printComment ("skip over class methods")
        self.printCode (f"JUMP __endclass__{node.id}")
        self.indentation += 1

        for ctor in node.constructors:
            ctor.parentClass = node
            ctor.accept (self)
        
        for method in node.methods:
            method.parentClass = node
            method.accept (self)

        self.indentation -= 1

        self.printCode (f"__endclass__{node.id}:")

        self.printComment (f"End Class Declaration - {node.id}")
        self.printDivider ()
        self.printNewline ()

    def visitFieldDeclarationNode (self, node):
        pass

    def visitMethodDeclarationNode (self, node):

        self.printSubDivider ()
        self.printComment (f"Method Declaration")

        endLabel = f"__endMethod__{node.parentClass.id}__{node.id}"
        methodLabel = f"__method__{node.parentClass.id}__{node.id}"

        # add jump to skip over function 
        self.printCode (f"JUMP {endLabel}")

        # place function jump-point label 
        self.printCode (methodLabel + ":")

        self.indentation += 1

        # load class instance 
        # first thing on the stack
        self.printComment ("Class Instance")
        self.indentation += 1
        self.printCode ("STACKGET __this 0")
        self.indentation -= 1 

        # load parameters 
        self.printComment ("Parameters")
        self.indentation += 1
        for i in range(1, len(node.params)+1):
            self.printComment (f"Param: {node.params[i-1].id}")
            # keep the same parameter name 
            self.printCode (f"STACKGET {node.params[i-1].id} {i}")
        self.indentation -= 1        

        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # extra return statement for if return is not provided 
        self.printCode ("RETURN 0")

        self.indentation -= 1

        self.printCode (f"{endLabel}:")

        self.printComment (f"End Method Declaration - {methodLabel}")
        self.printSubDivider ()
        self.printNewline ()

    def visitConstructorDeclarationNode (self, node):

        self.printSubDivider ()
        self.printComment (f"Constructor Declaration - {node.parentClass.id} {node.parentClass.type}")

        endLabel = f"__endctor__{node.parentClass.id}"
        ctorLabel = f"{node.parentClass.id}"

        # add jump to skip over function 
        self.printCode (f"JUMP {endLabel}")

        # place function jump-point label 
        self.printCode (ctorLabel + ":")

        self.indentation += 1

        # create class instance 
        self.printComment ("Creating Class Instance")
        self.indentation += 1
        self.printCode (f"MALLOC __this {len(node.parentClass.fields)}")
        # ** maybe initialize entries? or that might be inefficient
        self.indentation -= 1 

        # load parameters 
        self.printComment ("Parameters")
        self.indentation += 1
        for i in range(0, len(node.params)):
            self.printComment (f"Param: {node.params[i].id}")
            # keep the same parameter name 
            self.printCode (f"STACKGET {node.params[i].id} {i}")
        self.indentation -= 1        

        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # return constructed class instance
        self.printCode ("RETURN __this")

        self.indentation -= 1

        self.printCode (f"{endLabel}:")

        self.printComment (f"End Constructor Declaration - {node.parentClass.id}")
        self.printSubDivider ()
        self.printNewline ()
        

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        self.printSubDivider ()
        self.printComment ("If-Statement")

        # unique codes for jump labels 
        ifIndex = self.jumpIndex
        elifIndex = 0
        self.jumpIndex += 1

        elseLabel = f"__else{ifIndex}"
        endLabel = f"__endif{ifIndex}"

        self.indentation += 1

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("POP __cond")

        # jump if false - negation of original condition
        self.printCode ("CMP __cond 0")
        # jump to next elif if there is one 
        if (len(node.elifs) > 0):
            firstElif = f"__elif{ifIndex}x{elifIndex}"
            self.printCode (f"JEQ {firstElif}")
        # no elifs but has an else
        elif node.elseStmt != None:
            self.printCode (f"JEQ {elseLabel}")
        # no elif or else, jump to end of if-chain
        else:
            self.printCode (f"JEQ {endLabel}")
        self.indentation -= 1

        # print the body of if 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add jump to end of if 
        # skips over elifs and else
        self.printCode (f"JUMP {endLabel}")

        # print elifs 
        for i in range(len(node.elifs)):
            elifNode = node.elifs[i]

            self.printSubDivider ()
            self.printComment ("Elif-Statement")
            self.printCode (f"__elif{ifIndex}x{elifIndex}:")
            elifIndex += 1

            self.indentation += 1

            self.printComment ("Condition")
            # condition is an expression 
            # that gets evaluated and the result 
            # should be stored on the stack 
            elifNode.cond.accept (self)

            # get condition result from stack
            self.printCode ("POP __cond")

            # jump if false - negation of original condition
            self.printCode ("CMP __cond 0")
            # jump to next elif if there is one 
            if (i+1 < len(node.elifs)):
                nextElif = f"__elif{ifIndex}x{elifIndex}"
                self.printCode (f"JEQ {nextElif}")
            # no more elifs but has an else
            elif node.elseStmt != None:
                self.printCode (f"JEQ {elseLabel}")
            # no more elif nor else, jump to end of if-chain
            # skips over body 
            else:
                self.printCode (f"JEQ {endLabel}")

            # Body
            self.printComment ("Body")
            elifNode.body.accept (self)

            # add jump to end of if 
            self.printCode (f"JUMP {endLabel}")

            self.indentation -= 1

            self.printSubDivider ()

        # print else 
        if node.elseStmt != None:
            self.printSubDivider ()
            self.printComment ("Else-Statement")
            self.printCode (f"{elseLabel}:")

            node.elseStmt.body.accept (self)

            # jump to endif not necessary since else is always at the end 

            self.printSubDivider ()

        # end of if 
        self.printComment ("End of if")
        self.printCode (f"{endLabel}:")

        self.indentation -= 1

        self.printSubDivider ()

    def visitElifStatementNode (self, node):
        self.printComment ("*** Compiler Error: Elif node should not be used ")

    def visitElseStatementNode (self, node):
        self.printComment ("*** Compiler Error: Else node should not be used ")

    def visitForStatementNode (self, node):
        self.printSubDivider ()
        self.printComment ("For-Loop")

        # unique codes for jump labels 
        forIndex = self.jumpIndex
        self.jumpIndex += 1

        forLabel = f"__for{forIndex}"
        condLabel = f"__forcond{forIndex}"
        elseLabel = f"__forelse{forIndex}"
        endLabel = f"__endfor{forIndex}"

        # save loop info for break and continue statements
        node.startLabel = forLabel
        # break label should be end of loop
        node.breakLabel = endLabel
        # end label should be the location to go 
        # when loop terminates normally
        if (node.elseStmt != None):
            node.endLabel = elseLabel
        else:
            node.endLabel = endLabel
        self.parentLoops += [node]

        # init
        self.printComment ("Init")
        self.indentation += 1
        node.init.accept (self)
        self.indentation -= 1

        # skip over update
        self.printCode (f"JUMP {condLabel}")

        self.printCode (f"{forLabel}:")

        self.indentation += 1

        # perform update
        self.printComment ("Update")
        self.indentation += 1
        node.update.accept (self)
        self.indentation -= 1

        self.printCode (f"{condLabel}:")

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("POP __cond")
        # jump if false - negation of original condition
        self.printCode ("CMP __cond 0")
        if (node.elseStmt != None):
            self.printCode (f"JEQ {elseLabel}")
        else:
            self.printCode (f"JEQ {endLabel}")
        self.indentation -= 1

        # print the body 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add repeating jump
        self.printComment ("Repeat")
        self.printCode (f"JUMP {forLabel}")

        # add else statement if it exists
        if (node.elseStmt != None):
            self.printSubDivider ()
            self.printComment ("For-Else-Statement")
            self.printCode (f"{elseLabel}:")

            node.elseStmt.body.accept (self)

            self.printSubDivider ()

        # end of for 
        self.printComment ("End of For")
        self.printCode (f"{endLabel}:")

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.indentation -= 1

        self.printSubDivider ()

    def visitWhileStatementNode (self, node):
        self.printSubDivider ()
        self.printComment ("While-Loop")

        # unique codes for jump labels 
        whileIndex = self.jumpIndex
        self.jumpIndex += 1

        whileLabel = f"__while{whileIndex}"
        endLabel = f"__endwhile{whileIndex}"

        # save loop info for break and continue statements
        node.startLabel = whileLabel
        node.breakLabel = endLabel
        node.endLabel = endLabel
        self.parentLoops += [node]

        self.printCode (f"{whileLabel}:")

        self.indentation += 1

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("POP __cond")

        # jump if false - negation of original condition
        self.printCode ("CMP __cond 0")
        self.printCode (f"JEQ {endLabel}")

        self.indentation -= 1

        # print the body 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add repeating jump
        self.printCode (f"JUMP {whileLabel}")

        # end of while 
        self.printComment ("End of While")
        self.printCode (f"{endLabel}:")

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.indentation -= 1

        self.printSubDivider ()

    def visitExpressionStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)

    def visitReturnStatementNode (self, node):
        self.printComment ("Return")

        self.indentation += 1
        # if there is a value provided 
        if node.expr != None:
            node.expr.accept (self)

            # get return value 
            self.printCode ("POP __rVal")
            self.printCode (f"RETURN __rVal")
        # no value provided 
        else:
            self.printCode ("RETURN 0")

        self.indentation -= 1

    def visitContinueStatementNode (self, node):
        self.printComment (f"Continue in {self.parentLoops[-1].startLabel}")
        # goes to the start of the loop (aka the condition)
        self.printCode (f"JUMP {self.parentLoops[-1].startLabel}")

    def visitBreakStatementNode (self, node):
        self.printComment (f"Break out of {self.parentLoops[-1].startLabel}")
        # goes to the end of the loop
        self.printCode (f"JUMP {self.parentLoops[-1].breakLabel}")

    def visitCodeBlockNode (self, node):
        # if this is a function body
        # then add the parameters to this scope
        for p in self.parameters:
            p.accept (self)
        self.parameters.clear ()

        # print each codeunit
        for unit in node.codeunits:
            unit.accept (self)

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitAssignExpressionNode (self, node):
        self.printComment ("Assignment")

        self.indentation += 1

        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"POP __rhs")
            self.printCode (f"ASSIGN {node.lhs.id} __rhs")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("LHS")
            self.indentation += 1
            self.printComment ("Subscript assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("OFFSET")
            self.indentation += 1
            node.lhs.offset.accept (self)
            self.indentation -= 1

            self.printCode ("POP __offset")
            self.printCode ("POP __pointer")

            self.indentation -= 1
            self.indentation -= 1

            self.printCode (f"POP __rhs")
            self.printCode (f"ASSIGN __pointer[__offset] __rhs")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.indentation += 1
            self.printComment ("Member Accessor Assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("RHS")
            self.indentation += 1
            # construct field index var 
            fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {fieldIndex}")
            self.indentation -= 1

            self.printCode ("POP __child")
            self.printCode ("POP __parent")

            self.printCode (f"POP __rhs")
            self.printCode (f"ASSIGN __parent[__child] __rhs")

            self.indentation -= 1
            self.indentation -= 1

        
        # assign expressions return result of expression
        # ** this should probably be conditional 
        self.printCode ("PUSH __rhs")
        
        self.indentation -= 1

    def visitLogicalOrExpressionNode (self, node):
        self.printComment ("OR")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")

        self.printCode ("OR __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    # *** might need to edit this for short circuit eval***
    def visitLogicalAndExpressionNode (self, node):
        self.printComment ("AND")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")

        self.printCode ("AND __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitEqualityExpressionNode (self, node):
        if node.op == "==":
            self.printComment ("Equal")
        elif node.op == "!=":
            self.printComment ("Not Equal")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")

        if node.op == "==":
            self.printCode ("EQUAL __res __lhs __rhs")
        elif node.op == "!=":
            self.printCode ("NEQUAL __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitInequalityExpressionNode (self, node):
        if node.op == "<":
            self.printComment ("Less Than")
        elif node.op == "<=":
            self.printComment ("Less Than or Equal to")
        elif node.op == ">":
            self.printComment ("Greater Than")
        elif node.op == ">=":
            self.printComment ("Greater Than or Equal to")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")

        if node.op == "<":
            self.printCode ("LT __res __lhs __rhs")
        elif node.op == "<=":
            self.printCode ("LE __res __lhs __rhs")
        elif node.op == ">":
            self.printCode ("GT __res __lhs __rhs")
        elif node.op == ">=":
            self.printCode ("GE __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitAdditiveExpressionNode (self, node):
        # addition 
        if node.op == "+":
            self.printComment ("Addition")
        # subtraction 
        elif node.op == "-":
            self.printComment ("Subtraction")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")
        
        # addition 
        if node.op == "+":
            self.printCode ("ADD __res __lhs __rhs")
        # subtraction 
        elif node.op == "-":
            self.printCode ("SUBTRACT __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitMultiplicativeExpressionNode (self, node):
        # Multiplication 
        if node.op == "*":
            self.printComment ("Multiplication")
        # division 
        elif node.op == "/":
            self.printComment ("Division")
        # Mod
        elif node.op == "%":
            self.printComment ("Mod")

        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1
        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs and lhs off the stack 
        self.printCode ("POP __rhs")
        self.printCode ("POP __lhs")
    
        # Multiplication 
        if node.op == "*":
            self.printCode ("MULTIPLY __res __lhs __rhs")
        # division 
        elif node.op == "/":
            self.printCode ("DIVIDE __res __lhs __rhs")
        # Mod
        elif node.op == "%":
            self.printCode ("MOD __res __lhs __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1
            
    #  ++ | -- | + | - | ! | ~
    # **INCR and DECR do not save the value
    def visitUnaryLeftExpressionNode (self, node):
        if node.op == "++":
            self.printComment ("Pre-Increment")
            
        elif node.op == "--":
            self.printComment ("Pre-Decrement")
        elif node.op == "+":
            self.printComment ("Positive")
        elif node.op == "-":
            self.printComment ("Negative")
        elif node.op == "!":
            self.printComment ("Negate")
        elif node.op == "~":
            self.printComment ("Bitwise Negation")

        self.indentation += 1

        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs off the stack 
        self.printCode ("POP __rhs")
    
        if node.op == "++":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"ADD {node.rhs.id} {node.rhs.id} 1")
                self.printCode (f"ASSIGN __res {node.rhs.id}")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.indentation += 1
                self.printComment ("Subscript assignment")

                self.indentation += 1

                self.printComment ("LHS")
                self.indentation += 1
                node.rhs.lhs.accept (self)
                self.indentation -= 1

                self.printComment ("OFFSET")
                self.indentation += 1
                node.rhs.offset.accept (self)
                self.indentation -= 1

                self.printCode ("POP __offset")
                self.printCode ("POP __pointer")

                self.indentation -= 1
                self.indentation -= 1

                self.printCode (f"ADD __pointer[__offset] __pointer[__offset] 1")
                self.printCode (f"ASSIGN __res __pointer[__offset]")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.indentation += 1
                self.printComment ("Member Accessor Assignment")

                self.indentation += 1

                self.printComment ("LHS")
                self.indentation += 1
                node.rhs.lhs.accept (self)
                self.indentation -= 1

                self.printComment ("RHS")
                self.indentation += 1
                # construct field index var 
                fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"PUSH {fieldIndex}")
                self.indentation -= 1

                self.printCode ("POP __child")
                self.printCode ("POP __parent")

                self.printCode (f"ADD __parent[__child] __parent[__child] 1")
                self.printCode (f"ASSIGN __res __parent[__child]")

                self.indentation -= 1
                self.indentation -= 1
            else:
                print ("yikes!")
                exit (1)
        elif node.op == "--":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"SUBTRACT {node.rhs.id} {node.rhs.id} 1")
                self.printCode (f"ASSIGN __res {node.rhs.id}")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.indentation += 1
                self.printComment ("Subscript assignment")

                self.indentation += 1

                self.printComment ("LHS")
                self.indentation += 1
                node.rhs.lhs.accept (self)
                self.indentation -= 1

                self.printComment ("OFFSET")
                self.indentation += 1
                node.rhs.offset.accept (self)
                self.indentation -= 1

                self.printCode ("POP __offset")
                self.printCode ("POP __pointer")

                self.indentation -= 1
                self.indentation -= 1

                self.printCode (f"SUBTRACT __pointer[__offset] __pointer[__offset] 1")
                self.printCode (f"ASSIGN __res __pointer[__offset]")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.indentation += 1
                self.printComment ("Member Accessor Assignment")

                self.indentation += 1

                self.printComment ("LHS")
                self.indentation += 1
                node.rhs.lhs.accept (self)
                self.indentation -= 1

                self.printComment ("RHS")
                self.indentation += 1
                # construct field index var 
                fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"PUSH {fieldIndex}")
                self.indentation -= 1

                self.printCode ("POP __child")
                self.printCode ("POP __parent")

                self.printCode (f"SUBTRACT __parent[__child] __parent[__child] 1")
                self.printCode (f"ASSIGN __res __parent[__child]")

                self.indentation -= 1
                self.indentation -= 1
            else:
                print ("yikes!")
                exit (1)
        elif node.op == "+":
            self.printCode ("ASSIGN __res __rhs")
        elif node.op == "-":
            self.printCode ("SUBTRACT __res 0 __rhs")
        elif node.op == "!":
            self.printCode ("NOT __res __rhs")
        elif node.op == "~":
            self.printCode ("NOT __res __rhs")

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitPostIncrementExpressionNode(self, node):
        self.printComment ("Post-Increment")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"ASSIGN __res {node.lhs.id}")
            self.printCode (f"ADD {node.lhs.id} {node.lhs.id} 1")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.indentation += 1
            self.printComment ("Subscript assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("OFFSET")
            self.indentation += 1
            node.lhs.offset.accept (self)
            self.indentation -= 1

            self.printCode ("POP __offset")
            self.printCode ("POP __pointer")

            self.indentation -= 1
            self.indentation -= 1

            self.printCode (f"ASSIGN __res __pointer[__offset]")
            self.printCode (f"ADD __pointer[__offset] __pointer[__offset] 1")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.indentation += 1
            self.printComment ("Member Accessor Assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("RHS")
            self.indentation += 1
            # construct field index var 
            fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {fieldIndex}")
            self.indentation -= 1

            self.printCode ("POP __child")
            self.printCode ("POP __parent")

            self.printCode (f"ASSIGN __res __parent[__child]")
            self.printCode (f"ADD __parent[__child] __parent[__child] 1")

            self.indentation -= 1
            self.indentation -= 1
        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitPostDecrementExpressionNode (self, node):
        self.printComment ("Post-Decrement")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"ASSIGN __res {node.lhs.id}")
            self.printCode (f"SUBTRACT {node.lhs.id} {node.lhs.id} 1")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.indentation += 1
            self.printComment ("Subscript assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("OFFSET")
            self.indentation += 1
            node.lhs.offset.accept (self)
            self.indentation -= 1

            self.printCode ("POP __offset")
            self.printCode ("POP __pointer")

            self.indentation -= 1
            self.indentation -= 1

            self.printCode (f"ASSIGN __res __pointer[__offset]")
            self.printCode (f"SUBTRACT __pointer[__offset] __pointer[__offset] 1")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.indentation += 1
            self.printComment ("Member Accessor Assignment")

            self.indentation += 1

            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.lhs.accept (self)
            self.indentation -= 1

            self.printComment ("RHS")
            self.indentation += 1
            # construct field index var 
            fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {fieldIndex}")
            self.indentation -= 1

            self.printCode ("POP __child")
            self.printCode ("POP __parent")

            self.printCode (f"ASSIGN __res __parent[__child]")
            self.printCode (f"SUBTRACT __parent[__child] __parent[__child] 1")

            self.indentation -= 1
            self.indentation -= 1
        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode ("PUSH __res")

        self.indentation -= 1

    def visitSubscriptExpressionNode (self, node):
        self.printComment ("Subscript")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("OFFSET")
        self.indentation += 1
        node.offset.accept (self)
        self.indentation -= 1

        self.printCode ("POP __offset")
        self.printCode ("POP __pointer")
        self.printCode ("PUSH __pointer[__offset]")

        self.indentation -= 1

    def visitFunctionCallExpressionNode (self, node):
        self.printComment ("Function Call")

        self.indentation += 1

        self.printComment ("Arguments")
        self.indentation += 1
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        # retrieve argument values 
        # values will be popped off the stack in reverse order
        argIndex = len(node.args)-1
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"POP {argName}")
        self.indentation -= 1
        
        # add arguments in reverse order
        self.printComment ("Pushing args in reverse order")
        for i in range(len(node.args)-1, -1, -1):
            self.printCode (f"PUSH __arg{i}")

        # call function
        self.printCode (f"CALL {node.function.id}")

        # remove arguments from stack
        self.printComment ("Remove args")
        for i in range(0, len(node.args)):
            self.printCode (f"POP __null")
        
        # put function's return val on the stack
        self.printCode ("RESPONSE __retval")
        self.printCode ("PUSH __retval")

        self.indentation -= 1

    def visitMemberAccessorExpressionNode (self, node):
        self.printComment ("Member Accessor")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        # construct field index var 
        fieldIndex = f"__field__{node.lhs.type.id}__{node.rhs.id}"
        self.printCode (f"PUSH {fieldIndex}")
        self.indentation -= 1

        self.printCode ("POP __child")
        self.printCode ("POP __parent")
        self.printCode ("PUSH __parent[__child]")

        self.indentation -= 1

    def visitFieldAccessorExpressionNode (self, node):
        self.printComment ("Field Accessor")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        # construct field index var 
        fieldIndex = f"__field__{node.lhs.type.id}__{node.rhs.id}"
        self.printCode (f"PUSH {fieldIndex}")
        self.indentation -= 1

        self.printCode ("POP __child")
        self.printCode ("POP __parent")
        self.printCode ("PUSH __parent[__child]")

        self.indentation -= 1

    def visitMethodAccessorExpressionNode (self, node):
        self.printComment ("Method Call")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        # construct field index var 
        methodName = f"__method__{node.lhs.type.id}__{node.rhs.id}"
        self.indentation -= 1


        self.printComment ("Arguments")
        self.indentation += 1
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        argIndex = len(node.args)-1
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"POP {argName}")
        self.indentation -= 1
        
        # parent object should be on the stack
        # *happens after args incase args uses __obj
        # in another method call
        self.printCode ("POP __obj")

        # add arguments in reverse order
        self.printComment ("Pushing args in reverse order")
        for i in range(len(node.args)-1, -1, -1):
            self.printCode (f"PUSH __arg{i}")

        # push parent object instance last
        self.printCode (f"PUSH __obj")

        # call function
        self.printCode (f"CALL {methodName}")

        # remove parent object instance
        self.printCode (f"PUSH __null")

        # remove arguments from stack
        self.printComment ("Remove args")
        for i in range(0, len(node.args)):
            self.printCode (f"POP __null")
                
        # put function's return val on the stack
        self.printCode ("RESPONSE __retval")
        self.printCode ("PUSH __retval")

        self.indentation -= 1

    def visitThisExpressionNode (self, node):
        self.printComment (f"This keyword")
        self.indentation += 1
        self.printCode (f"PUSH __this")
        self.indentation -= 1

    def visitIdentifierExpressionNode (self, node):
        self.printComment (f"Identifier")
        self.indentation += 1
        self.printCode (f"PUSH {node.id}")
        self.indentation -= 1

    def visitArrayAllocatorExpressionNode (self, node):
        self.printComment ("Array Allocator")

        self.indentation += 1
        for d in node.dimensions:
            d.accept (self)
        
        # ** maybe make a large array for multiple dimensions
        self.printCode (f"POP __size")
        self.printCode (f"MALLOC __ptr __size")

        self.printCode (f"PUSH __ptr")

        self.indentation -= 1

    def visitConstructorCallExpressionNode (self, node):
        self.printComment ("Constructor Call")

        self.indentation += 1

        self.printComment ("Arguments")
        self.indentation += 1
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        # retrieve values in reverse order
        argIndex = len(node.args)-1
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"POP {argName}")
        self.indentation -= 1
        
        # add arguments in reverse order
        self.printComment ("Pushing args in reverse order")
        for i in range(len(node.args)-1, -1, -1):
            self.printCode (f"PUSH __arg{i}")

        # call function
        self.printCode (f"CALL {node.type.id}")

        # remove arguments from stack
        self.printComment ("Remove args")
        for i in range(0, len(node.args)):
            self.printCode (f"POP __null")
        
        # put function's return val on the stack
        self.printCode ("RESPONSE __retval")
        self.printCode ("PUSH __retval")

        self.indentation -= 1

    def visitIntLiteralExpressionNode (self, node):
        self.printComment ("Literal")
        self.indentation += 1
        self.printCode (f"PUSH {node.value}")
        self.indentation -= 1

    def visitFloatLiteralExpressionNode (self, node):
        self.printComment ("Literal")
        self.indentation += 1
        self.printCode (f"PUSH {node.value}")
        self.indentation -= 1

    def visitCharLiteralExpressionNode (self, node):
        self.printComment ("Literal")
        self.indentation += 1
        self.printCode (f"PUSH {node.value}")
        self.indentation -= 1

    def visitStringLiteralExpressionNode (self, node):
        self.printComment ("Literal")
        self.indentation += 1
        # create string on heap as char[]
        self.printCode (f"MALLOC __str {len(node.value)-2}")
        for i in range(1, len(node.value)-1):
            self.printCode (f"ASSIGN __str[{i-1}] '{node.value[i]}'")
        self.printCode ("PUSH __str")
        self.indentation -= 1

    def visitListConstructorExpressionNode (self, node):

        self.printComment ("Array Constructor")

        self.indentation += 1

        # evaluate each element
        # elements could be list constructors 
        #  so we don't want to pop values into variables yet
        self.printComment ("Elements")
        for elem in node.elems:
            elem.accept (self)
            
        elemIndex = len(node.elems)-1
        # retrieve values in reverse order
        for elem in node.elems:
            # save element 
            elemName = f"__elem{elemIndex}"
            elemIndex -= 1
            self.printCode (f"POP {elemName}")

        self.printCode (f"MALLOC __list {len(node.elems)}")

        # add elements to list in correct order
        for i in range(len(node.elems)):
            self.printCode (f"ASSIGN __list[{i}] __elem{i}")

        # push array onto stack
        self.printCode ("PUSH __list")

        self.indentation -= 1
        


# ========================================================================