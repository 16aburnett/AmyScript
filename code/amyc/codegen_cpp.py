# Amy Script Compiler - Code Generation
# By Amy Burnett
# December 2022
# ========================================================================

import os 
from sys import exit

if __name__ == "codegen_cpp":
    from amyAST import *
    from visitor import ASTVisitor
    from symbolTable import SymbolTable
else:
    from .amyAST import *
    from .visitor import ASTVisitor
    from .symbolTable import SymbolTable

# ========================================================================

DIVIDER_LENGTH = 75 
TAB_LENGTH = 4

LIB_FILENAME = os.path.dirname(__file__) + "/AmyScriptBuiltinLib_cpp.cpp"

# ========================================================================

class CodeGenVisitor_cpp (ASTVisitor):

    def __init__(self, lines):
        self.parameters = []
        self.lines = lines 
        self.indentation = 0
        self.code = []
        self.lhs = "null"
        self.jumpIndex = 0
        self.shouldComment = True
        # stack implementation
        # keeps track of containing loop
        # for break and continue statements 
        self.parentLoops = []
        self.pushParent = False
        self.scopeNames = ["__main"]

    # === HELPER FUNCTIONS ===============================================

    def printIndent (self):
        self.printSpaces (self.indentation)

    def printSpaces (self, level):
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
        self.code += ["".join(divider)]
        self.printNewline ()

    def printDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//="]
        for i in range(dividerLength):
            divider += ["="]
        self.code += ["".join(divider)]
        self.printNewline ()

    def printSubDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//-"]
        for i in range(dividerLength):
            divider += ["-"]
        self.code += ["".join(divider)]
        self.printNewline ()

    def printNewline (self):
        self.code += ["\n"]

    def enterScope (self, name):
        self.scopeNames += [f"__{name}"]

    def exitScope (self):
        self.scopeNames.pop ()

    # === VISITOR FUNCTIONS ==============================================

    def visitProgramNode (self, node):

        self.printComment ("Generated C++ code compiled from AmyScript")
        self.printDivider ()
        self.printNewline ()

        self.printDivider ()
        self.printHeader ("LIBRARY CODE")
        self.printDivider ()
        self.printNewline ()

        # add library code
        file = open (LIB_FILENAME, "r")
        for line in file.readlines ():
            self.code += [line]

        self.printDivider ()
        self.printHeader ("SETUP EXPRESSION RESULT STACK")
        self.printDivider ()
        self.printNewline ()
        
        # expression result stack stores values from expressions 
        self.printComment ("This stack is used to store results of expressions")
        self.printCode ("stack = []")
        self.printNewline ()

        self.printDivider ()
        self.printHeader ("COMPILED CODE")
        self.printDivider ()
        self.printNewline ()

        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

        self.printNewline ()
        self.printDivider ()
        self.printHeader ("END OF CODE")
        self.printDivider ()
        self.printNewline ()

    def visitTypeSpecifierNode (self, node):
        pass

    def visitParameterNode (self, node):
        node.type.accept (self)
        node.scopeName = "".join (self.scopeNames) + "__" + node.id

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        node.type.accept (self)

        # variable names are modified by its scope 
        scopeName = "".join (self.scopeNames) + "__" + node.id

        # declare the variable with default value 
        self.printCode (f"{scopeName} = 0")
        self.lhs = node.id
        node.scopeName = scopeName

    def visitFunctionNode (self, node):

        # variable names are modified by its scope 
        scopeName = ["".join (self.scopeNames), "____", node.id]
        # add template parameters if there are any 
        if len(node.templateParams) > 0:
            scopeName += [f"__{node.templateParams[0].id}"]
            # add array dimensions
            if node.templateParams[0].arrayDimensions > 0:
                scopeName += [f"__{node.templateParams[0].arrayDimensions}"]
            # add rest of template params 
            for i in range(1, len(node.templateParams)):
                scopeName += [f"__{node.templateParams[i].id}"]
                # add array dimensions
                if node.templateParams[i].arrayDimensions > 0:
                    scopeName += [f"__{node.templateParams[i].arrayDimensions}"]
            scopeName += ["__"]
        # add signature to scopeName for overloaded functions
        if len(node.params) > 0:
            scopeName += [f"__{node.params[0].type.id}"]
            # param template types
            if len(node.params[0].type.templateParams) > 0:
                 scopeName += [f"__tparam{0}__{node.params[0].type.templateParams[0].id}"]
            for i in range(1, len(node.params[0].type.templateParams)):
                 scopeName += [f"__tparam{i}__{node.params[0].type.templateParams[i].id}"]
            # add array dimensions
            if node.params[0].type.arrayDimensions > 0:
                scopeName += [f"__{node.params[0].type.arrayDimensions}"]
            for i in range(1, len(node.params)):
                scopeName += [f"__{node.params[i].type.id}"]
                # param template types
                if len(node.params[i].type.templateParams) > 0:
                    scopeName += [f"__tparam{0}__{node.params[i].type.templateParams[0].id}"]
                for j in range(1, len(node.params[i].type.templateParams)):
                    scopeName += [f"__tparam{j}__{node.params[i].type.templateParams[j].id}"]
                # add array dimensions
                if node.params[i].type.arrayDimensions > 0:
                    scopeName += [f"__{node.params[i].type.arrayDimensions}"]
        node.scopeName = "".join(scopeName)

        # AD HOC CENTRAL!!
        # fill in prereferences with scopename 
        for i in range(len(self.code)):
            if f"${node.signature}" in self.code[i]:
                self.code[i] = self.code[i].replace(f"${node.signature}", node.scopeName)

        # create new scope level 
        self.scopeNames += [f"__{node.id}"]

        self.printDivider ()
        self.printComment (f"Function Declaration - {node.signature} -> {node.type}")

        # parameters
        params = []
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (node.params[i].scopeName)
        self.printCode (f"def {node.scopeName} ({', '.join(params)}):")

        self.indentation += 1
        self.printComment ("Body")
        node.body.accept (self)
        self.indentation -= 1

        self.printComment (f"End Function Declaration - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

    def visitClassDeclarationNode(self, node):

        # variable names are modified by its scope 
        scopeName = ["__", node.id]
        # add template parameters if there are any 
        if len(node.templateParams) > 0:
            scopeName += [f"__{node.templateParams[0].id}"]
            # add array dimensions
            if node.templateParams[0].arrayDimensions > 0:
                scopeName += [f"__{node.templateParams[0].arrayDimensions}"]
            # add rest of template params 
            for i in range(1, len(node.templateParams)):
                scopeName += [f"__{node.templateParams[i].id}"]
                # add array dimensions
                if node.templateParams[i].arrayDimensions > 0:
                    scopeName += [f"__{node.templateParams[i].arrayDimensions}"]
        node.scopeName = "".join(scopeName)

        # create new scope level 
        self.scopeNames += [f"__{node.scopeName}"]

        node.scopeName = "".join(self.scopeNames)

        self.printDivider ()
        if node.pDecl != None:
            self.printComment (f"Class Declaration - {node.scopeName} inherits {node.pDecl.scopeName}")
        else: 
            self.printComment (f"Class Declaration - {node.scopeName}")

        # create scope names for methods
        for method in node.methods:
            # variable names are modified by its scope 
            scopeName = ["__method__", "".join (self.scopeNames), "____", method.id]
            # add signature to scopeName for overloaded functions
            if len(method.params) > 0:
                scopeName += [f"__{method.params[0].type.id}"]
                # add array dimensions
                if method.params[0].type.arrayDimensions > 0:
                    scopeName += [f"__{method.params[0].type.arrayDimensions}"]
            for i in range(1, len(method.params)):
                scopeName += [f"__{method.params[i].type.id}"]
                # add array dimensions
                if method.params[i].type.arrayDimensions > 0:
                    scopeName += [f"__{method.params[i].type.arrayDimensions}"]
            method.scopeName = "".join(scopeName)
        # create scope names for ctors 
        for ctor in node.constructors:
            # variable names are modified by its scope 
            scopeName = ["__ctor__", "".join (self.scopeNames), "____", ctor.parentClass.id]
            # add signature to scopeName for overloaded functions
            if len(ctor.params) > 0:
                scopeName += [f"__{ctor.params[0].type.id}"]
                # add array dimensions
                if ctor.params[0].type.arrayDimensions > 0:
                    scopeName += [f"__{ctor.params[0].type.arrayDimensions}"]
            for i in range(1, len(ctor.params)):
                scopeName += [f"__{ctor.params[i].type.id}"]
                # add array dimensions
                if ctor.params[i].type.arrayDimensions > 0:
                    scopeName += [f"__{ctor.params[i].type.arrayDimensions}"]
            ctor.scopeName = "".join(scopeName)

        # create dispatch table 
        self.printComment ("Creating Dispatch Table (will be populated later)")
        node.dtableScopeName = "__dtable__" + "".join (self.scopeNames)
        self.printCode (f"{node.dtableScopeName} = []")

        # create scope names for fields 
        for field in node.fields:
            # variable names are modified by its scope 
            fieldScopeName = "__field__" + "".join (self.scopeNames) + "____" + field.id
            field.scopeName = fieldScopeName

        # dispatch table pointer is at i = 0 
        i = 1
        for field in node.fields:
            field.parentClass = node
            field.index = i 
            field.accept (self)
            i += 1

        for ctor in node.constructors:
            ctor.parentClass = node
            ctor.accept (self)

        for method in node.methods:
            method.parentClass = node
            method.accept (self)
        
        self.printComment ("Populate Dispatch Table")
        # populate dispatch table
        funcpointers = []
        for i in range(len(node.functionPointerList)):
            funcpointers.append (node.functionPointerList[i].scopeName)
        self.printCode (f"{node.dtableScopeName} = [{', '.join(funcpointers)}]")

        self.printComment (f"End Class Declaration - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

    def visitFieldDeclarationNode (self, node):
        self.printSubDivider ()
        self.printComment (f"Field - {node.type} {node.signature}")
        if node.isInherited:
            self.printComment (f"Inherited from {node.parentClass.pDecl.id}")

        # fieldIndexVarname = f"__field__{node.id}__{field.id}"
        self.printCode (f"{node.scopeName} = {node.index}")

        self.printSubDivider ()

    def visitMethodDeclarationNode (self, node):

        # create new scope level 
        self.scopeNames += [f"__{node.id}"]

        self.printSubDivider ()
        self.printComment (f"Method Declaration - {node.signature} -> {node.type}")
        if node.isInherited:
            self.printComment (f"Inherited from {node.parentClass.pDecl.id}")

        endLabel = f"__end{node.scopeName}"
        methodLabel = node.scopeName

        # ensure we start with the object instance param
        # parameters
        params = ['']
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (node.params[i].scopeName)
        self.printCode (f"def {methodLabel} (this{', '.join(params)}):")

        self.indentation += 1

        # inherited methods
        if node.isInherited:
            self.printComment (f"Jump to {node.inheritedMethod.parentClass.id}'s version")
            self.printCode (f"__retval = {node.inheritedMethod.scopeName} (this{', '.join(params)})")
            self.printCode (f"return __retval")
        else:
            self.printComment ("Body")
            node.body.accept (self)

            # extra return statement for if return is not provided 
            self.printCode ("return 0")

        self.indentation -= 1

        self.printComment (f"End Method Declaration - {methodLabel}")
        self.printSubDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

    def visitConstructorDeclarationNode (self, node):

        # create new scope level 
        self.scopeNames += [f"__{node.parentClass.id}"]

        self.printSubDivider ()
        self.printComment (f"Constructor Declaration - {node.signature} -> {node.parentClass.type}")

        endLabel = f"__end{node.scopeName}"
        ctorLabel = f"{node.scopeName}"

        # AD HOC CENTRAL!!
        # fill in prereferences with scopename 
        for i in range(len(self.code)):
            if f"${node.signature}" in self.code[i]:
                self.code[i] = self.code[i].replace(f"${node.signature}", node.scopeName)

        # parameters
        params = []
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (node.params[i].scopeName)
        self.printCode (f"def {ctorLabel} ({', '.join(params)}):")

        self.indentation += 1

        # create class instance 
        self.printComment ("Creating Class Instance")
        # +1 because all classes start with a dispatch table 
        self.printCode (f"this = [0] * {len(node.parentClass.fields)+1}")

        # add dispatch table to instance
        self.printComment ("Add Dispatch Table")
        self.printCode (f"this[0] = {node.parentClass.dtableScopeName}")

        # ** maybe initialize entries? or that might be inefficient
        
        # *** are we supposed to support inherited ctors?
        self.printComment ("Body")
        node.body.accept (self)

        # return constructed class instance
        self.printComment ("Return the constructed instance")
        self.printCode ("return this")

        self.indentation -= 1

        self.printComment (f"End Constructor Declaration - {node.scopeName}")
        self.printSubDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

    def visitEnumDeclarationNode (self, node):

        self.printSubDivider ()
        self.printComment (f"Enum Declaration - {node.scopeName}")

        self.indentation += 1

        i = 0
        for field in node.fields:
            # variable names are modified by its scope 
            scopeName = ["__enum__", "".join (self.scopeNames), "____", node.id, "____", field.id]
            field.scopeName = "".join(scopeName)
            self.printCode (f"ASSIGN {field.scopeName} {i}")
            i += 1

        self.indentation -= 1

        self.printComment (f"End Enum Declaration - {node.scopeName}")
        self.printSubDivider ()
        self.printNewline ()

    def visitFunctionTemplateNode (self, node):
        self.printDivider ()
        self.printComment (f"Function Template - {node.scopeName}")

        for instance in node.instantiations:
            node.instantiations[instance].accept (self)

        self.printComment (f"End Function Template - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

    def visitClassTemplateDeclarationNode (self, node):
        self.printDivider ()
        self.printComment (f"Class Template - {node.scopeName}")

        for instance in node.instantiations:
            node.instantiations[instance].accept (self)

        self.printComment (f"End Class Template - {node.scopeName}")
        self.printDivider ()
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

        elseLabel = f"__else__{ifIndex}"
        endLabel = f"__endif__{ifIndex}"

        # create new scope level 
        self.scopeNames += [f"__if__{ifIndex}"]

        self.printComment ("Precomputing all if/elif conditions and give unique names")
        self.printComment ("bc we can't have code between if and elif")
        self.printComment ("Condition")
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        self.printCode (f"__if__{ifIndex}__cond = stack.pop ()")
        for i in range(len(node.elifs)):
            self.printComment (f"Condition for elif #{i}")
            node.elifs[i].cond.accept (self)
            self.printCode (f"__elif__{ifIndex}x{elifIndex}__cond = stack.pop ()")
            elifIndex += 1
        elifIndex = 0

        self.printComment ("get condition from stack")
        self.printCode (f"if (__if__{ifIndex}__cond):")

        # print the body of if 
        self.indentation += 1
        self.printComment ("Body")
        node.body.accept (self)
        self.indentation -= 1

        # exit if scope
        self.scopeNames.pop ()

        # print elifs 
        for i in range(len(node.elifs)):
            elifNode = node.elifs[i]

            self.printSubDivider ()
            self.printComment ("Elif-Statement")

            # create new scope level 
            self.scopeNames += [f"__elif__{ifIndex}x{elifIndex}"]

            self.printComment ("Condition")
            # condition is an expression 
            # that gets evaluated and the result 
            # should be stored on the stack 
            # elifNode.cond.accept (self)

            # get condition result from stack
            # ***this wont work bc it would separate if and elif
            # self.printCode ("__cond = stack.pop ()")

            self.printCode (f"elif (__elif__{ifIndex}x{elifIndex}__cond):")
            elifIndex += 1

            # Body
            self.indentation += 1
            self.printComment ("Body")
            elifNode.body.accept (self)
            self.indentation -= 1

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

        # print else 
        if node.elseStmt != None:
            self.printSubDivider ()
            self.printComment ("Else-Statement")

            # create new scope level 
            self.scopeNames += [elseLabel]

            self.printCode ("else:")

            self.indentation += 1
            node.elseStmt.body.accept (self)
            self.indentation -= 1

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

        # end of if 
        self.printComment ("End of if")

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

        forLabel = f"__for__{forIndex}"
        condLabel = f"__forcond__{forIndex}"
        elseLabel = f"__forelse__{forIndex}"
        endLabel = f"__endfor__{forIndex}"

        # create new scope level 
        self.scopeNames += [forLabel]

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
        node.init.accept (self)

        self.printComment ("Using an infinite loop so we can write a separate multi-line condition")
        self.printCode ("while (1):")

        self.indentation += 1

        self.printComment ("Condition")
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("__cond = stack.pop ()")
        # jump if false - negation of original condition
        self.printComment ("break out of loop if condition is false")
        self.printCode ("if (__cond == 0): break")

        # print the body 
        self.printComment ("Body")
        node.body.accept (self)


        # perform update
        self.printComment ("Update")
        node.update.accept (self)

        self.indentation -= 1

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.printSubDivider ()

        # exit scope
        self.scopeNames.pop ()

    def visitWhileStatementNode (self, node):
        self.printSubDivider ()
        self.printComment ("While-Loop")

        # unique codes for jump labels 
        whileIndex = self.jumpIndex
        self.jumpIndex += 1

        whileLabel = f"__while__{whileIndex}"
        endLabel = f"__endwhile__{whileIndex}"

        # create new scope level 
        self.scopeNames += [whileLabel]

        # save loop info for break and continue statements
        node.startLabel = whileLabel
        node.breakLabel = endLabel
        node.endLabel = endLabel
        self.parentLoops += [node]

        self.printComment ("Using an infinite loop so we can write a separate multi-line condition")
        self.printCode ("while (1):")

        self.indentation += 1

        self.printComment ("Condition")
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("__cond = stack.pop ()")
        # jump if false - negation of original condition
        self.printComment ("break out of loop if condition is false")
        self.printCode ("if (__cond == 0): break")

        # print the body 
        self.printComment ("Body")
        node.body.accept (self)

        self.indentation -= 1

        # end of while 
        self.printComment ("End of While")

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.printSubDivider ()

        # exit scope 
        self.scopeNames.pop ()

    def visitExpressionStatementNode (self, node):
        # ignore variable decl
        # int x; should not translate to anything
        if node.expr != None and not isinstance(node.expr, VariableDeclarationNode):
            self.printComment ("Statement")
            node.expr.accept (self)
            # don't need stack value from statement
            # in some cases, this extra value on the stack can break things
            self.printComment ("Statement results can be ignored")
            self.printCode ("stack.pop ()")
            self.printComment ("End Statement")
            self.printNewline ()

    def visitReturnStatementNode (self, node):
        self.printComment ("Return")
        # if there is a value provided 
        if node.expr != None:
            node.expr.accept (self)
            # get return value 
            self.printCode ("__rVal = stack.pop ()")
            self.printCode (f"return __rVal")
        # no value provided 
        else:
            self.printCode ("return")

    def visitContinueStatementNode (self, node):
        self.printComment (f"Continue in {self.parentLoops[-1].startLabel}")
        # for loops need to inject the update
        if isinstance (self.parentLoops[-1], ForStatementNode):
            self.parentLoops[-1].update.accept (self)
        # goes to the start of the loop (aka the condition)
        self.printCode (f"continue")

    def visitBreakStatementNode (self, node):
        self.printComment (f"Break out of {self.parentLoops[-1].startLabel}")
        # goes to the end of the loop
        self.printCode (f"break")

    def visitCodeBlockNode (self, node):
        self.printSubDivider ()
        self.printComment ("Code Block")

        # create new scope level 
        self.scopeNames += [f"__block__{self.jumpIndex}"]
        self.jumpIndex += 1

        # if this is a function body
        # then add the parameters to this scope
        for p in self.parameters:
            p.accept (self)
        self.parameters.clear ()

        # print each codeunit
        for unit in node.codeunits:
            unit.accept (self)

        # exit scope
        self.scopeNames.pop ()

        self.printSubDivider ()

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitAssignExpressionNode (self, node):
        self.printComment (f"Assignment - '{node.op.lexeme}'")

        self.printComment ("RHS")
        node.rhs.accept (self)

        # simple assign 
        if node.overloadedFunctionCall == None:

            if isinstance(node.lhs, VariableDeclarationNode):
                self.printComment ("LHS")
                node.lhs.accept (self)
                self.printCode (f"__rhs = stack.pop()")
                lhsStr = f"{node.lhs.scopeName}"

            elif isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
                self.printCode (f"__rhs = stack.pop()")
                lhsStr = f"{node.lhs.decl.scopeName}"

            elif isinstance(node.lhs, SubscriptExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.lhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.lhs.offset.accept (self)

                self.printCode (f"__offset = stack.pop()")
                self.printCode (f"__pointer = stack.pop()")

                self.printCode (f"__rhs = stack.pop()")
                lhsStr = f"__pointer[__offset]"

            elif isinstance (node.lhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.lhs.lhs.accept (self)

                self.printComment ("RHS")
                # # construct field index var 
                # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
                self.printCode (f"stack.append({node.lhs.decl.scopeName})")

                self.printCode (f"__child = stack.pop()")
                self.printCode (f"__parent = stack.pop()")

                self.printCode (f"__rhs = stack.pop()")
                
                lhsStr = f"__parent[__child]"
                
            # =
            if node.op.type == "ASSIGN":
                self.printCode (f"{lhsStr} = __rhs")
            # +=
            elif node.op.type == "ASSIGN_ADD":
                self.printCode (f"{lhsStr} = {lhsStr} + __rhs")
            # -=
            elif node.op.type == "ASSIGN_SUB":
                self.printCode (f"{lhsStr} = {lhsStr} - __rhs")
            # *=
            elif node.op.type == "ASSIGN_MUL":
                self.printCode (f"{lhsStr} = {lhsStr} * __rhs")
            # /=
            elif node.op.type == "ASSIGN_DIV":
                self.printCode (f"{lhsStr} = {lhsStr} / __rhs")
            # %=
            elif node.op.type == "ASSIGN_MOD":
                self.printCode (f"{lhsStr} = {lhsStr} % __rhs")

            self.printCode (f"stack.append ({lhsStr})")
        

    def visitLogicalOrExpressionNode (self, node):
        self.printComment ("OR")
        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop ()")
        self.printCode ("__lhs = stack.pop ()")
        self.printCode ("__res = __lhs or __rhs")
        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitLogicalAndExpressionNode (self, node):
        self.printComment ("AND")
        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop ()")
        self.printCode ("__lhs = stack.pop ()")
        self.printCode ("__res = __lhs and __rhs")
        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitEqualityExpressionNode (self, node):
        if node.op.lexeme == "==":
            self.printComment ("Equal")
        elif node.op.lexeme == "!=":
            self.printComment ("Not Equal")

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop ()")
        self.printCode ("__lhs = stack.pop ()")

        if node.op.lexeme == "==":
            self.printCode ("__res = __lhs == __rhs")
        elif node.op.lexeme == "!=":
            self.printCode ("__res = __lhs != __rhs")

        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitInequalityExpressionNode (self, node):
        if node.op.lexeme == "<":
            self.printComment ("Less Than")
        elif node.op.lexeme == "<=":
            self.printComment ("Less Than or Equal to")
        elif node.op.lexeme == ">":
            self.printComment ("Greater Than")
        elif node.op.lexeme == ">=":
            self.printComment ("Greater Than or Equal to")

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop ()")
        self.printCode ("__lhs = stack.pop ()")

        if node.op.lexeme == "<":
            self.printCode ("__res = __lhs < __rhs")
        elif node.op.lexeme == "<=":
            self.printCode ("__res = __lhs <= __rhs")
        elif node.op.lexeme == ">":
            self.printCode ("__res = __lhs > __rhs")
        elif node.op.lexeme == ">=":
            self.printCode ("__res = __lhs >= __rhs")

        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitAdditiveExpressionNode (self, node):
        # addition 
        if node.op.lexeme == "+":
            self.printComment ("Addition")
        # subtraction 
        elif node.op.lexeme == "-":
            self.printComment ("Subtraction")

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop()")
        self.printCode ("__lhs = stack.pop()")
        
        # simple additive 
        if node.overloadedFunctionCall == None:
            # addition
            if node.op.lexeme == "+":
                self.printCode ("__res = __lhs + __rhs")
            # subtraction 
            elif node.op.lexeme == "-":
                self.printCode ("__res = __lhs - __rhs")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"__res = {node.overloadedFunctionCall.decl.scopeName} (__lhs, __rhs)")

        # push result to the stack
        self.printCode ("stack.append(__res)")

    def visitMultiplicativeExpressionNode (self, node):
        if node.op.lexeme == "*":
            self.printComment ("Multiplication")
        elif node.op.lexeme == "/":
            self.printComment ("Division")
        elif node.op.lexeme == "%":
            self.printComment ("Modulus")

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.pop()")
        self.printCode ("__lhs = stack.pop()")
        
        # simple 
        if node.overloadedFunctionCall == None:
            # mul
            if node.op.lexeme == "*":
                self.printCode ("__res = __lhs * __rhs")
            # div 
            elif node.op.lexeme == "/":
                # integer division
                if node.lhs.type.type == Type.INT:
                    self.printCode (f"__res = __lhs // __rhs")
                else:
                    self.printCode (f"__res = __lhs / __rhs")
            # mod
            elif node.op.lexeme == "%":
                self.printCode ("__res = __lhs % __rhs")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"__res = {node.overloadedFunctionCall.decl.scopeName} (__lhs, __rhs)")

        # push result to the stack
        self.printCode ("stack.append(__res)")
            
    #  ++ | -- | + | - | ! | ~
    def visitUnaryLeftExpressionNode (self, node):
        if node.op.lexeme == "++":
            self.printComment ("Pre-Increment")
        elif node.op.lexeme == "--":
            self.printComment ("Pre-Decrement")
        elif node.op.lexeme == "+":
            self.printComment ("Positive")
        elif node.op.lexeme == "-":
            self.printComment ("Negative")
        elif node.op.lexeme == "!":
            self.printComment ("Negate")
        elif node.op.lexeme == "~":
            self.printComment ("Bitwise Negation")

        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs off the stack 
        self.printCode ("__rhs = stack.pop ()")
        # ** i think this could be a potential bug because we pop rhs before visiting lhs and offset
    
        if node.op.lexeme == "++":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"{node.rhs.decl.scopeName} = {node.rhs.decl.scopeName} + 1")
                self.printCode (f"__res = {node.rhs.decl.scopeName}")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.rhs.offset.accept (self)

                self.printCode ("__offset = stack.pop ()")
                self.printCode ("__pointer = stack.pop ()")

                self.printCode (f"__pointer[__offset] = __pointer[__offset] + 1")
                self.printCode (f"__res = __pointer[__offset]")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("RHS")
                # construct field index var 
                # fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"stack.append ({node.rhs.decl.scopeName})")

                self.printCode ("__child = stack.pop ()")
                self.printCode ("__parent = stack.pop ()")

                self.printCode (f"__parent[__child] = __parent[__child] + 1")
                self.printCode (f"__res = __parent[__child]")
            else:
                print ("yikes!")
                exit (1)
        elif node.op.lexeme == "--":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"{node.rhs.decl.scopeName} = {node.rhs.decl.scopeName} - 1")
                self.printCode (f"__res = {node.rhs.decl.scopeName}")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.rhs.offset.accept (self)

                self.printCode ("__offset = stack.pop ()")
                self.printCode ("__pointer = stack.pop ()")

                self.printCode (f"__pointer[__offset] = __pointer[__offset] - 1")
                self.printCode (f"__res = __pointer[__offset]")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("RHS")
                # construct field index var 
                # fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"stack.append ({node.rhs.decl.scopeName})")

                self.printCode ("__child = stack.pop ()")
                self.printCode ("__parent = stack.pop ()")

                self.printCode (f"__parent[__child] = __parent[__child] - 1")
                self.printCode (f"__res = __parent[__child]")
            else:
                print ("yikes!")
                exit (1)
        elif node.op.lexeme == "+":
            self.printCode ("__res = __rhs")
        elif node.op.lexeme == "-":
            self.printCode ("__res = -__rhs")
        elif node.op.lexeme == "!":
            self.printCode ("__res = not __rhs")
        elif node.op.lexeme == "~":
            self.printCode ("__res = ~__rhs")

        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitPostIncrementExpressionNode(self, node):
        self.printComment ("Post-Increment")

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"__res = {node.lhs.decl.scopeName}")
            self.printCode (f"{node.lhs.decl.scopeName} = {node.lhs.decl.scopeName} + 1")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.printComment ("Subscript assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("OFFSET")
            node.lhs.offset.accept (self)

            self.printCode ("__offset = stack.pop ()")
            self.printCode ("__pointer = stack.pop ()")

            self.printCode (f"__res = __pointer[__offset]")
            self.printCode (f"__pointer[__offset] = __pointer[__offset] + 1")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.printComment ("Member Accessor Assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("RHS")
            # construct field index var 
            # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"stack.append ({node.lhs.decl.scopeName})")

            self.printCode ("__child = stack.pop ()")
            self.printCode ("__parent = stack.pop ()")

            self.printCode (f"__res = __parent[__child]")
            self.printCode (f"__parent[__child] = __parent[__child] + 1")
        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitPostDecrementExpressionNode (self, node):
        self.printComment ("Post-Decrement")

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"__res = {node.lhs.decl.scopeName}")
            self.printCode (f"{node.lhs.decl.scopeName} = {node.lhs.decl.scopeName} - 1")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.printComment ("Subscript assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("OFFSET")
            node.lhs.offset.accept (self)

            self.printCode ("__offset = stack.pop ()")
            self.printCode ("__pointer = stack.pop ()")

            self.printCode (f"__res = __pointer[__offset]")
            self.printCode (f"__pointer[__offset] = __pointer[__offset] - 1")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.printComment ("Member Accessor Assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("RHS")
            # construct field index var 
            # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"stack.append ({node.lhs.decl.scopeName})")

            self.printCode ("__child = stack.pop ()")
            self.printCode ("__parent = stack.pop ()")

            self.printCode (f"__res = __parent[__child]")
            self.printCode (f"__parent[__child] = __parent[__child] - 1")
        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode ("stack.append (__res)")

    def visitSubscriptExpressionNode (self, node):
        self.printComment ("Subscript")

        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("OFFSET")
        node.offset.accept (self)

        self.printCode ("__offset = stack.pop ()")
        self.printCode ("__pointer = stack.pop ()")

        # simple subscript  
        if node.overloadedFunctionCall == None:
            self.printCode ("stack.append (__pointer[__offset])")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"__res = {node.overloadedFunctionCall.decl.scopeName} (__pointer, __offset)")
            self.printCode (f"stack.append (__res)")

    def visitFunctionCallExpressionNode (self, node):
        self.printComment (f"Function Call - {node.decl.signature} -> {node.decl.type}")

        self.printComment ("Arguments")
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        argIndex = len(node.args)-1
        args = []
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"{argName} = stack.pop ()")
            args.insert (0, argName)

        # call function
        self.printComment (f"*** {node.function.id}")
        funcname = ""
        if node.decl.scopeName == "":
            # x = sum([1 if '\n' in s else 0 for s in self.code])
            # print (f"[code-gen] Error: no scope name for {node.function.id} {[t.type.__str__() for t in node.args]} {node.lineNumber} {x}")
            # print (f"   this could have happened due to a template using a class that was defined after the template")
            # print (f"   temporary fix: move the class declaration to above the template class that uses it")
            # solution! extremely ad hoc 
            funcname = node.decl.signature
            # exit (1)
        else:
            funcname = node.decl.scopeName

        self.printCode (f"__res = {funcname} ({', '.join(args)})")
        
        # put function's return val on the stack
        self.printCode ("stack.append (__res) # function call result")

    def visitMemberAccessorExpressionNode (self, node):

        # static calls 
        # lhs is not an identifier 
        if node.isstatic:
            # enum 
            self.printComment (f"Enum Member Accessor - {node.lhs.id}.{node.rhs.id}")
            self.indentation += 1
            self.printCode (f"PUSH {node.decl.scopeName}")
            self.indentation -= 1
            return 

        self.printComment ("Member Accessor")

        self.printComment ("LHS")
        node.lhs.accept (self)

        self.printComment ("RHS")
        if node.decl.scopeName == "":
            x = sum([1 if '\n' in s else 0 for s in self.code])
            print (f"[code-gen] [member-accessor] Error: no scope name for '{node.decl.id}' on line {node.lineNumber}")
            print (f"   this could have happened due to a cyclic reference/composition with template classes")
            print (f"   cyclic references are not yet supported")
            exit (1)
        self.printCode (f"stack.append ({node.decl.scopeName})")

        self.printCode ("__child = stack.pop ()")
        self.printCode ("__parent = stack.pop ()")
        self.printCode ("stack.append (__parent[__child])")

    def visitFieldAccessorExpressionNode (self, node):
        pass

    def visitMethodAccessorExpressionNode (self, node):
        if node.decl.isVirtual:
            self.printComment (f"Virtual Method Call - {node.decl.signatureNoScope} -> {node.decl.type}")
        else:
            self.printComment (f"Method Call - {node.decl.signature} -> {node.decl.type}")

        self.printComment ("LHS")
        node.lhs.accept (self)

        self.printComment ("RHS")
        # construct field index var 
        # methodName = f"__method__{node.lhs.type.id}__{node.rhs.id}"

        self.printComment ("Arguments")
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        argIndex = len(node.args)-1
        args = ['']
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"{argName} = stack.pop ()")
            args.insert (1, argName)
        
        # parent object should be on the stack
        # *happens after args incase args uses __obj
        # in another method call
        self.printCode ("__obj = stack.pop ()")

        # if virtual function
        if node.decl.isVirtual:
            # call the appropriate function 
            self.printComment (f"Virtual Function Dispatch")
            # find dispatch table index 
            # by locating the matching virtual function 
            index = 0 
            for i in range(len(node.decl.parentClass.virtualMethods)):
                if node.decl.signatureNoScope == node.decl.parentClass.virtualMethods[i].signatureNoScope:
                    # found index 
                    index = i 
                    break 
            else:
                print (f"Error: Dispatch Function not found")
            # call proper dispatch function 
            self.printCode (f"__dtable = __obj[0]")
            self.printCode (f"__retval = __dtable[{i}] (__obj{', '.join(args)})")

        # otherwise, call function normally
        else:
            self.printCode (f"__retval = {node.decl.scopeName} (__obj{', '.join(args)})")
                
        # put function's return val on the stack
        self.printCode ("stack.append (__retval)")

    def visitThisExpressionNode (self, node):
        self.printCode (f"stack.append(this)")

    def visitIdentifierExpressionNode (self, node):
        self.printCode (f"stack.append({node.decl.scopeName})")

    def visitArrayAllocatorExpressionNode (self, node):
        node.dimensions[0].accept (self)
        self.printCode (f"__dim = stack.pop ()")
        # this is probably not ideal and will likely cause problems
        self.printCode (f"__res = [None] * __dim")
        self.printCode ("stack.append (__res)")

    def visitConstructorCallExpressionNode (self, node):
        self.printComment (f"Constructor Call - {node.decl.signature} -> {node.decl.parentClass.type}")

        self.printComment ("Arguments")
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        # retrieve values
        argIndex = len(node.args)-1
        args = []
        for arg in node.args:
            # save argument 
            argName = f"__arg{argIndex}"
            argIndex -= 1
            self.printCode (f"{argName} = stack.pop ()")
            args.insert (0, argName)

        # call function
        self.printCode (f"__retval = {node.decl.scopeName} ({', '.join(args)})")
        
        # put function's return val on the stack
        self.printCode ("stack.append (__retval)")
    
    def visitSizeofExpressionNode(self, node):
        node.rhs.accept (self)
        self.printCode ("__arr = stack.pop ()")
        self.printCode ("__res = len (__arr)")
        self.printCode ("stack.append (__res)")
    
    def visitFreeExpressionNode (self, node):
        # nothing to do, python has its own garbage collector ;)
        # for now, i am just calling the builtin free function which will do nothing
        node.rhs.accept (self)
        self.printCode ("__arr = stack.pop ()")
        self.printCode ("__builtin__free (__arr)")
        self.printCode ("stack.append (0)")

    def visitIntLiteralExpressionNode (self, node):
        self.printComment ("Int Literal")
        self.printCode (f"stack.append({node.value})")

    def visitFloatLiteralExpressionNode (self, node):
        self.printComment ("Float Literal")
        self.printCode (f"stack.append({node.value})")

    def visitCharLiteralExpressionNode (self, node):
        self.printComment ("Char Literal")
        self.printCode (f"stack.append('{node.value}')")

    def visitStringLiteralExpressionNode (self, node):
        self.printComment ("String Literal")
        self.printCode (f"stack.append({node.value})")

    def visitListConstructorExpressionNode (self, node):
        self.printComment ("Array Constructor")

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
        

    def visitNullExpressionNode (self, node):
            
        self.printComment ("Null Literal")
        self.printCode ("stack.append (None)")


# ========================================================================