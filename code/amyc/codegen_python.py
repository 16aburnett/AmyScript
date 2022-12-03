# Amy Script Compiler - Code Generation
# By Amy Burnett
# April 11 2021
# ========================================================================

import os 
from sys import exit

if __name__ == "codegen_python":
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

LIB_FILENAME = os.path.dirname(__file__) + "/AmyScriptBuiltinLib_python.py"

# ========================================================================

class CodeGenVisitor_python (ASTVisitor):

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
        self.code += [f"{line}"]

    def printComment (self, comment):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        self.code += ["# ", comment]
        self.printNewline ()

    def printHeader (self, header):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - len (header) - 8
        divider = ["#### "]
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
        divider = ["#="]
        for i in range(dividerLength):
            divider += ["="]
        self.code += ["".join(divider)]
        self.printNewline ()

    def printSubDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["#-"]
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

        self.printComment ("Python compiled from AmyScript")
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
        self.printCode (node.scopeName)

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        node.type.accept (self)

        # variable names are modified by its scope 
        scopeName = "".join (self.scopeNames) + "__" + node.id

        # declare the variable with default value 
        self.printCode (f"{scopeName}")
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

        self.printIndent ()
        self.printCode (f"def {node.scopeName} (")
        # parameters
        if len(node.params) != 0:
            node.params[0].accept (self)
        for i in range(1, len(node.params)):
            self.printCode (", ")
            node.params[i].accept (self)
        self.printCode ("):")
        self.printNewline ()

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
        self.printIndent ()
        self.printCode (f"{node.dtableScopeName} = []")
        self.printNewline ()

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
        self.printIndent ()
        self.printCode (f"{node.dtableScopeName} = [")
        # populate dispatch table
        if len(node.functionPointerList) != 0:
            self.printCode (f"{node.functionPointerList[0].scopeName}")
        for i in range(1, len(node.functionPointerList)):
            self.printCode (f", {node.functionPointerList[i].scopeName}")
        self.printCode ("]")
        self.printNewline ()

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
        self.printIndent ()
        self.printCode (f"{node.scopeName} = {node.index}")
        self.printNewline ()

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
        self.printIndent ()
        self.printCode (f"def {methodLabel} (this")
        # parameters
        for i in range(len(node.params)):
            self.printCode (", ")
            node.params[i].accept (self)
        self.printCode ("):")   
        self.printNewline ()

        self.indentation += 1

        # inherited methods
        if node.isInherited:
            self.printComment (f"Jump to {node.inheritedMethod.parentClass.id}'s version")
            self.printCode (f"JUMP {node.inheritedMethod.scopeName}")
        else:
            self.printComment ("Body")
            node.body.accept (self)

            # extra return statement for if return is not provided 
            self.printIndent ()
            self.printCode ("return 0")
            self.printNewline ()

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

        self.printIndent ()
        self.printCode (f"def {ctorLabel} (")
        # parameters
        if len(node.params) != 0:
            node.params[0].accept (self)
        for i in range(1, len(node.params)):
            self.printCode (", ")
            node.params[i].accept (self)
        self.printCode ("):")   
        self.printNewline ()

        self.indentation += 1

        # create class instance 
        self.printComment ("Creating Class Instance")
        # +1 because all classes start with a dispatch table 
        self.printIndent ()
        self.printCode (f"this = [0] * {len(node.parentClass.fields)+1}")
        self.printNewline ()

        # add dispatch table to instance
        self.printComment ("Add Dispatch Table")
        self.printIndent ()
        self.printCode (f"this[0] = {node.parentClass.dtableScopeName}")
        self.printNewline ()

        # ** maybe initialize entries? or that might be inefficient

        self.printComment ("Body")
        node.body.accept (self)

        # return constructed class instance
        self.printComment ("Return the constructed instance")
        self.printIndent ()
        self.printCode ("return this")
        self.printNewline ()

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

        self.indentation += 1

        self.printComment (f"Instances:")
        self.indentation += 1
        for instance in node.instantiations:
            node.instantiations[instance].accept (self)

        self.indentation -= 1
        self.indentation -= 1

        self.printComment (f"End Function Template - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

    def visitClassTemplateDeclarationNode (self, node):
        self.printDivider ()
        self.printComment (f"Class Template - {node.scopeName}")

        self.indentation += 1

        self.printComment (f"Instances:")
        self.indentation += 1
        for instance in node.instantiations:
            node.instantiations[instance].accept (self)

        self.indentation -= 1
        self.indentation -= 1

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

        self.printIndent ()
        self.printCode ("if (")
        # condition
        node.cond.accept (self)
        self.printCode ("):")
        self.printNewline ()

        # print the body 
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
            # self.printCode (f"__elif__{ifIndex}x{elifIndex}:")
            elifIndex += 1

            # create new scope level 
            self.scopeNames += [f"__elif__{ifIndex}x{elifIndex}"]

            self.printIndent ()
            self.printCode ("elif (")
            # condition
            elifNode.cond.accept (self)
            self.printCode ("):")
            self.printNewline ()

            # print the body 
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
            self.printIndent ()
            self.printCode (f"else:")
            self.printNewline ()

            # create new scope level 
            self.scopeNames += [elseLabel]

            self.indentation += 1
            node.elseStmt.body.accept (self)
            self.indentation -= 1

            # jump to endif not necessary since else is always at the end 

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

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
        self.printIndent ()
        node.init.accept (self)
        self.printNewline ()

        self.printIndent ()
        self.printCode ("while (")
        # condition
        node.cond.accept (self)
        self.printCode ("):")
        self.printNewline ()

        # body
        self.indentation += 1
        node.body.accept (self)

        # update
        self.printIndent ()
        node.update.accept (self)
        self.printNewline ()

        self.indentation -= 1

        # ** continue statements might be problematic, 
        # we may need to inject the update to before continue
        # but that still might not work because variable shadowing? maybe

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

        self.printIndent ()
        self.printCode ("while (")
        # condition
        node.cond.accept (self)
        self.printCode ("):")
        self.printNewline ()

        # print the body 
        self.indentation += 1
        self.printComment ("Body")
        node.body.accept (self)
        self.indentation -= 1

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
            self.printIndent ()
            node.expr.accept (self)
            self.printNewline ()

    def visitReturnStatementNode (self, node):
        self.printIndent ()
        self.printCode ("return")
        # if there is a value provided 
        if node.expr != None:
            self.printCode (' ')
            node.expr.accept (self)
        self.printNewline ()

    def visitContinueStatementNode (self, node):
        self.printComment (f"Continue in {self.parentLoops[-1].startLabel}")
        # goes to the start of the loop (aka the condition)
        self.printIndent ()
        self.printCode (f"continue")
        self.printNewline ()

    def visitBreakStatementNode (self, node):
        self.printComment (f"Break out of {self.parentLoops[-1].startLabel}")
        # goes to the end of the loop
        self.printIndent ()
        self.printCode (f"break")
        self.printNewline ()

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

        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")

        # simple assign 
        if node.overloadedFunctionCall == None:

            if isinstance(node.lhs, VariableDeclarationNode):
                node.lhs.accept (self)
                lhsStr = f"{node.lhs.scopeName}"

            elif isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
                node.lhs.accept (self)
                lhsStr = f"{node.lhs.decl.scopeName}"

            elif isinstance(node.lhs, SubscriptExpressionNode):
                node.lhs.lhs.accept (self)
                self.printCode ("[")
                node.lhs.offset.accept (self)
                self.printCode ("]")
                lhsStr = f"__pointer[__offset]"

            elif isinstance (node.lhs, MemberAccessorExpressionNode):
                # arr.size = arr[field__size] = 10
                node.lhs.lhs.accept (self)
                self.printCode (f"[{node.lhs.decl.scopeName}]")
                
            # =
            if node.op.type == "ASSIGN":
                op = "="
            # +=
            elif node.op.type == "ASSIGN_ADD":
                op = "+="
            # -=
            elif node.op.type == "ASSIGN_SUB":
                op = "-="
            # *=
            elif node.op.type == "ASSIGN_MUL":
                op = "*="
            # /=
            elif node.op.type == "ASSIGN_DIV":
                op = "/="
            # %=
            elif node.op.type == "ASSIGN_MOD":
                op = "%="


            self.printCode (f" {op} ")
            node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")
        

    def visitLogicalOrExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")

        node.lhs.accept (self)
        self.printCode (" or ")
        node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitLogicalAndExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        node.lhs.accept (self)
        self.printCode (" and ")
        node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitEqualityExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        node.lhs.accept (self)
        self.printCode (f" {node.op.lexeme} ")
        node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitInequalityExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        node.lhs.accept (self)
        self.printCode (f" {node.op.lexeme} ")
        node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitAdditiveExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # simple additive 
        if node.overloadedFunctionCall == None:
            node.lhs.accept (self)
            self.printCode (f" {node.op.lexeme} ")
            node.rhs.accept (self)
        # overloaded function call 
        else:
            self.printCode (f"{node.overloadedFunctionCall.decl.scopeName} (")
            node.lhs.accept (self)
            self.printCode (", ")
            node.rhs.accept (self)
            self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitMultiplicativeExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # simple additive 
        if node.overloadedFunctionCall == None:
            node.lhs.accept (self)
            if node.op.lexeme == '*':
                self.printCode (f" * ")
            if node.op.lexeme == '/':
                # integer division
                if node.lhs.type.type == Type.INT:
                    self.printCode (f" // ")
                else:
                    self.printCode (f" / ")
            if node.op.lexeme == '%':
                self.printCode (f" % ")
            node.rhs.accept (self)
        # overloaded function call 
        else:
            self.printCode (f"{node.overloadedFunctionCall.decl.scopeName} (")
            node.lhs.accept (self)
            self.printCode (", ")
            node.rhs.accept (self)
            self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")
            
    #  ++ | -- | + | - | ! | ~
    def visitUnaryLeftExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        if node.op.lexeme == "++":
            node.rhs.accept (self)
            self.printCode (" += 1")
        elif node.op.lexeme == "--":
            node.rhs.accept (self)
            self.printCode (" -= 1")
        elif node.op.lexeme == "+":
            node.rhs.accept (self)
        elif node.op.lexeme == "-":
            self.printCode ("-")
            node.rhs.accept (self)
        elif node.op.lexeme == "!":
            self.printCode ("not ")
            node.rhs.accept (self)
        elif node.op.lexeme == "~":
            self.printCode ("~")
            node.rhs.accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitPostIncrementExpressionNode(self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printComment ("Post-Increment")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"ASSIGN __res {node.lhs.decl.scopeName}")
            self.printCode (f"ADD {node.lhs.decl.scopeName} {node.lhs.decl.scopeName} 1")
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
            # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {node.lhs.decl.scopeName}")
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

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitPostDecrementExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printComment ("Post-Decrement")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"ASSIGN __res {node.lhs.decl.scopeName}")
            self.printCode (f"SUBTRACT {node.lhs.decl.scopeName} {node.lhs.decl.scopeName} 1")
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
            # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {node.lhs.decl.scopeName}")
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

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitSubscriptExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # simple subscript  
        if node.overloadedFunctionCall == None:
            node.lhs.accept (self)
            self.printCode ("[")
            node.offset.accept (self)
            self.printCode ("]")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"PUSH __offset")
            self.printCode (f"PUSH __pointer")
            self.printCode (f"CALL {node.overloadedFunctionCall.decl.scopeName}")
            self.printCode (f"RESPONSE __res")
            self.printCode (f"PUSH __res")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitFunctionCallExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"{node.decl.scopeName} (")

        # visit and print each argument comma separated
        if len(node.args) != 0:
            node.args[0].accept (self)
        for i in range(1, len(node.args)):
            self.printCode (", ")
            node.args[i].accept (self)

        # end parameter list
        self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitMemberAccessorExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # static calls 
        # lhs is not an identifier 
        if node.isstatic:
            # enum 
            self.printComment (f"Enum Member Accessor - {node.lhs.id}.{node.rhs.id}")
            self.indentation += 1
            self.printCode (f"PUSH {node.decl.scopeName}")
            self.indentation -= 1
            return 

        # obj[field_index]
        node.lhs.accept (self)

        if node.decl.scopeName == "":
            x = sum([1 if '\n' in s else 0 for s in self.code])
            print (f"[code-gen] [member-accessor] Error: no scope name for '{node.decl.id}' on line {node.lineNumber}")
            print (f"   this could have happened due to a cyclic reference/composition with template classes")
            print (f"   cyclic references are not yet supported")
            exit (1)
        self.printCode (f"[{node.decl.scopeName}]")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitFieldAccessorExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printComment ("Field Accessor")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        # construct field index var 
        self.printCode (f"PUSH {node.decl.scopeName}")
        self.indentation -= 1

        self.printCode ("POP __child")
        self.printCode ("POP __parent")
        self.printCode ("PUSH __parent[__child]")

        self.indentation -= 1

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitMethodAccessorExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # if node.decl.isVirtual:
        #     self.printComment (f"Virtual Method Call - {node.decl.signatureNoScope} -> {node.decl.type}")
        # else:
        #     self.printComment (f"Method Call - {node.decl.signature} -> {node.decl.type}")

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
            self.printCode (f"ASSIGN __dtable __obj[0]")
            self.printCode (f"CALL __dtable[{i}]")

        # otherwise, call function normally
        else:
            self.printCode (f"{node.decl.scopeName}")

        
        self.printCode (f" (")
        # lhs is object parameter
        node.lhs.accept (self)
        # add rest of params after object param
        for i in range(len(node.args)):
            self.printCode (", ")
            node.args[i].accept (self)
        self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitThisExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"this")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitIdentifierExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"{node.decl.scopeName}")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitArrayAllocatorExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # this is probably not ideal and will likely cause problems
        self.printCode ("[None] * ")
        node.dimensions[0].accept (self)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitConstructorCallExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # self.printComment (f"Constructor Call - {node.decl.signature} -> {node.decl.parentClass.type}")

        self.printCode (f"{node.decl.scopeName} (")
        if len(node.args) != 0:
            node.args[0].accept (self)
        for i in range(1, len(node.args)):
            self.printCode (", ")
            node.args[i].accept (self)
        self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")
    
    def visitSizeofExpressionNode(self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printComment ("Sizeof Operator")
        self.indentation += 1

        # calc rhs
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        self.printComment ("Calculate array size")
        self.printCode ("POP __array")
        self.printCode ("SIZEOF __size __array")
        self.printCode ("PUSH __size")

        self.indentation -= 1

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")
    
    def visitFreeExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        # nothing to do, python has its own garbage collector ;)
        # for now, i am just calling the builtin free function which will do nothing
        self.printCode ("free (")
        node.rhs.accept (self)
        self.printCode (")")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitIntLiteralExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"{node.value}")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitFloatLiteralExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"{node.value}")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitCharLiteralExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (f"'{(node.value)}'")

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitStringLiteralExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printCode (node.value)

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")

    def visitListConstructorExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            

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

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")
        

    def visitNullExpressionNode (self, node):
        # wrap expression in parentheses 
        # if it should have parentheses
        if node.hasParentheses:
            self.printCode ("(")
            
        self.printComment ("Null Literal")
        self.indentation += 1
        self.printCode ("ASSIGN __null 0")
        self.printCode ("PUSH __null")
        self.indentation -= 1

        # close parentheses if we were supposed to have parens
        if node.hasParentheses:
            self.printCode (")")


# ========================================================================