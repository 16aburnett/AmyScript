# Amy Script Compiler - x86 backend 
# By Amy Burnett
# April 11 2021
# ========================================================================

import os 
from sys import exit

if __name__ == "codegen_x86":
    from amyAST import *
    from visitor import ASTVisitor
    from symbolTable import SymbolTable
else:
    from .amyAST import *
    from .visitor import ASTVisitor
    from .symbolTable import SymbolTable

# ========================================================================

DIVIDER_LENGTH = 75 
TAB_LENGTH = 3

LIB_FILENAME = os.path.dirname(__file__) + "/AmyScriptBuiltinLib_x86.asm"

# ========================================================================

class CodeGenVisitor_x86 (ASTVisitor):

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
        self.indent = "        "

    # === HELPER FUNCTIONS ===============================================

    def printSpaces (self, level):
        if not self.shouldComment:
            return 
            
        while level > 0:
            for i in range(TAB_LENGTH):
                self.code += [" "]
            level -= 1

    def printLabel (self, line):
        self.code += [f"{line}\n"]

    def printCode (self, line):
        self.printSpaces (self.indentation)
        self.code += [self.indent, f"{line}\n"]

    def printComment (self, comment):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        self.code += [self.indent, "; ", comment, "\n"]

    def printHeader (self, header):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - len (header) - 8
        divider = ["; ### "]
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
        divider = ["; "]
        for i in range(dividerLength):
            divider += ["="]
        divider += ["\n"]
        self.code += ["".join(divider)]

    def printSubDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = [";"]
        for i in range(dividerLength):
            divider += ["-"]
        divider += ["\n"]
        self.code += ["".join(divider)]

    def printNewline (self):
        if not self.shouldComment:
            return 
        self.code += ["\n"]

    def enterScope (self, name):
        self.scopeNames += [f"__{name}"]

    def exitScope (self):
        self.scopeNames.pop ()

    # === VISITOR FUNCTIONS ==============================================

    def visitProgramNode (self, node):

        self.printHeader ("x86-64 generated from AmyScript Compiler")
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

        # predetermine string literal labels 
        # this needs to be done before processing the code
        # so that we know the label of the string to lookup
        # * this really should go in a pre-codegen step
        # * can be optimized to include only unique labels
        for i in range(len(node.stringLiterals)):
            node.stringLiterals[i].label = f".str{i}"

        self.printLabel ("_start:")
        self.printLabel ("main:")

        # FUNCTION HEADER
        self.printComment ("Main Header:")

        # setup stack 
        self.printCode ("push rbp")
        self.printCode ("mov rbp, rsp")
        neededSpace = len(node.localVariables) * 8 # each var is 8-bytes
        space = neededSpace if neededSpace % 16 == 0 else neededSpace + 8 # 16 byte aligned
        self.printCode (f"sub rsp, {space}")

        # process local variables 
        self.printComment ("Local Variables - Each variable is currently 64-bit (sorry not sorry)")
        for i in range(len(node.localVariables)):
            offset = i*8+8
            self.printComment (f"{node.localVariables[i].id} [rbp - {offset}]")
            # save the address for future lookups 
            node.localVariables[i].stackOffset = offset 

        self.printNewline ()

        self.printComment ("Body")

        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

        self.printDivider ()
        self.printHeader ("END OF CODE")
        self.printDivider ()
        self.printNewline ()

        # exit program
        self.printCode ("push 0")
        self.printCode ("call exit__int")

        # data section
        self.printDivider ()
        self.printHeader ("DATA SECTION")
        self.printDivider ()
        self.printNewline ()
        self.printCode ("section .data")
    
        # print all of the strings
        for i in range(len(node.stringLiterals)):

            # This routine splits the string to separate chars
            # because '\n' isn't automatically interpreted as a newline
            # so this finds escaped chars and replaces it with its ascii value
            # * this can be changed to compress adjacent chars into a string
            # like the following examples
            # Current:  db 'H', 'e', 'l', 'l', 'o', 10, 0
            # Expected: db "Hello", 10, 0

            # print (node.stringLiterals[i].value)
            import ast
            asciiString = (ast.literal_eval(node.stringLiterals[i].value))
            # print (asciiString)

            line = [f"{node.stringLiterals[i].label}: db "]

            if len(asciiString) > 0:
                # if it is an escape character - '\n'
                if len(repr(asciiString[0])) > 3:  
                    line += [f"{ord(asciiString[0])}"]  
                    # print (ord(asciiString[0]))
                # normal character
                else:
                    line += [f"'{asciiString[0]}'"]
            for j in range(1, len(asciiString)):
                # print (repr(asciiString[j])) 
                # if it is an escape character - '\n'
                if len(repr(asciiString[j])) > 3:  
                    line += [f", {ord(asciiString[j])}"]  
                    # print (ord(asciiString[j]))
                # normal character
                else:
                    line += [f", '{asciiString[j]}'"]
            # string needs to end in null \0
            line += [", 0"]

            self.printLabel ("".join(line))

    def visitTypeSpecifierNode (self, node):
        pass

    def visitParameterNode (self, node):
        node.type.accept (self)
        node.scopeName = "".join (self.scopeNames) + "__" + node.id

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        self.printComment (f"Variable Declaration - {node.id}")
        node.type.accept (self)

        self.indentation += 1

        # variable names are modified by its scope 
        scopeName = "".join (self.scopeNames) + "__" + node.id

        # declare the variable with default value 
        self.printCode (f"mov rax, qword [rbp - {node.stackOffset}]  ; {scopeName}")
        self.lhs = node.id
        node.scopeName = scopeName

        self.indentation -= 1

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

        # setup labels 
        node.label = f".{node.scopeName}"
        node.endLabel = f".__end__{node.scopeName}"

        self.printDivider ()
        self.printComment (f"Function Declaration - {node.signature} -> {node.type}")
        # add jump to skip over function 
        self.printComment ("Skip over function declaration")
        self.printCode (f"jmp {node.endLabel}")

        # place function jump-point label 
        self.printLabel (f"{node.label}:")

        self.indentation += 1
 
        # FUNCTION HEADER
        self.printComment ("Function Header:")
        self.indentation += 1

        # setup stack
        self.printComment ("Setup stack frame")
        self.indentation += 1
        self.printCode ("push rbp")
        self.printCode ("mov rbp, rsp")
        self.indentation -= 1

        # load parameters 
        self.printComment ("Parameters")
        self.indentation += 1
        for i in range(len(node.params)):
            node.params[i].accept (self)
            # +16 because retaddr (8-bytes) and prev_rbp (8-bytes)
            offset = i*8+16
            self.printComment (f"Param: {node.params[i].id} [rbp + {offset}]")
            # * parameter offsets are made negative since they are accessed opposite to localVars
            # could be weird, might want to flip localVars to be negative instead
            node.params[i].stackOffset = -offset 
        self.indentation -= 1

        # local variables 
        self.printComment ("Local Variables - Each variable is currently 64-bit (sorry not sorry)")
        self.indentation += 1
        for i in range(len(node.localVariables)):
            offset = i*8+8
            self.printComment (f"{node.localVariables[i].id} [rbp - {offset}]")
            # save the address for future lookups 
            node.localVariables[i].stackOffset = offset 
        self.indentation -= 1

        self.indentation -= 1
        self.printNewline ()

        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # extra return statement for if return is not provided 
        self.printCode ("ret ; ensure function returns")

        self.indentation -= 1

        self.printLabel (f"{node.endLabel}:")

        self.printComment (f"End Function Declaration - {node.signature} -> {node.type}")
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

        self.indentation += 1

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
        self.printComment ("Creating Dispatch Table")
        node.dtableScopeName = "__dtable__" + "".join (self.scopeNames)
        self.indentation += 1
        self.printCode (f"MALLOC {node.dtableScopeName} {len(node.virtualMethods)}")
        # populate dispatch table
        self.printComment ("Populate Dispatch Table")
        for i in range(len(node.functionPointerList)):
            self.printCode (f"ASSIGN {node.dtableScopeName}[{i}] {node.functionPointerList[i].scopeName}")
        self.indentation -= 1

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

        # add jump to skip over class dec  
        self.indentation -= 1
        self.printComment ("skip over class methods")
        self.printCode (f"JUMP __endclass__{node.scopeName}")
        self.indentation += 1

        for ctor in node.constructors:
            ctor.parentClass = node
            ctor.accept (self)

        for method in node.methods:
            method.parentClass = node
            method.accept (self)

        self.indentation -= 1

        self.printCode (f"__endclass__{node.scopeName}:")

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
        self.printCode (f"ASSIGN {node.scopeName} {node.index}")

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

        # add jump to skip over function 
        self.printCode (f"JUMP {endLabel}")

        # place function jump-point label 
        self.printCode (methodLabel + ":")

        self.indentation += 1

        # inherited methods
        if node.isInherited:
            self.printComment (f"Jump to {node.inheritedMethod.parentClass.id}'s version")
            self.printCode (f"JUMP {node.inheritedMethod.scopeName}")
        else:

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
                node.params[i-1].accept (self)
                # keep the same parameter name 
                self.printCode (f"STACKGET {node.params[i-1].scopeName} {i}")
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

        # add jump to skip over function 
        self.printCode (f"JUMP {endLabel}")

        # place function jump-point label 
        self.printCode (ctorLabel + ":")

        self.indentation += 1

        # create class instance 
        self.printComment ("Creating Class Instance")
        self.indentation += 1
        # +1 because all classes start with a dispatch table 
        self.printCode (f"MALLOC __this {len(node.parentClass.fields)+1}")

        # add dispatch table to instance
        self.printComment ("Add Dispatch Table")
        self.printCode (f"ASSIGN __this[0] {node.parentClass.dtableScopeName}")

        # ** maybe initialize entries? or that might be inefficient
        self.indentation -= 1

        # load parameters 
        self.printComment ("Parameters")
        self.indentation += 1
        for i in range(len(node.params)):
            self.printComment (f"Param: {node.params[i].id}")
            node.params[i].accept (self)
            # keep the same parameter name 
            self.printCode (f"STACKGET {node.params[i].scopeName} {i}")
        self.indentation -= 1        

        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # return constructed class instance
        self.printCode ("RETURN __this")

        self.indentation -= 1

        self.printCode (f"{endLabel}:")

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

        # start with . because they are local to 
        # the function that they are contained in
        # * might be able to use this in more cases
        elseLabel = f".__else__{ifIndex}"
        endLabel = f".__endif__{ifIndex}"

        # create new scope level 
        self.scopeNames += [f"__if__{ifIndex}"]

        self.indentation += 1

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("pop rdx ; __cond")

        # jump if false - negation of original condition
        self.printCode ("cmp rdx, 0 ; ensure condition is true")
        # jump to next elif if there is one 
        if (len(node.elifs) > 0):
            firstElif = f".__elif__{ifIndex}x{elifIndex}"
            self.printCode (f"je {firstElif} ; jump to first elif")
        # no elifs but has an else
        elif node.elseStmt != None:
            self.printCode (f"je {elseLabel} ; jump to else")
        # no elif or else, jump to end of if-chain
        else:
            self.printCode (f"je {endLabel} ; jump to end")
        self.indentation -= 1

        # print the body of if 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add jump to end of if 
        # skips over elifs and else
        self.printCode (f"jmp {endLabel} ; jump to end of condition chain")

        # exit if scope
        self.scopeNames.pop ()

        # print elifs 
        for i in range(len(node.elifs)):
            elifNode = node.elifs[i]

            self.printSubDivider ()
            self.printComment ("Elif-Statement")
            self.printLabel (f".__elif__{ifIndex}x{elifIndex}:")
            elifIndex += 1

            # create new scope level 
            self.scopeNames += [f"__elif__{ifIndex}x{elifIndex}"]

            self.indentation += 1

            self.printComment ("Condition")
            # condition is an expression 
            # that gets evaluated and the result 
            # should be stored on the stack 
            elifNode.cond.accept (self)

            # get condition result from stack
            self.printCode ("pop rdx ; __cond")

            # jump if false - negation of original condition
            self.printCode ("cmp rdx, 0 ; ensure condition is true")
            # jump to next elif if there is one 
            if (i+1 < len(node.elifs)):
                nextElif = f".__elif__{ifIndex}x{elifIndex}"
                self.printCode (f"je {nextElif}")
            # no more elifs but has an else
            elif node.elseStmt != None:
                self.printCode (f"je {elseLabel}")
            # no more elif nor else, jump to end of if-chain
            # skips over body 
            else:
                self.printCode (f"je {endLabel}")

            # Body
            self.printComment ("Body")
            elifNode.body.accept (self)

            # add jump to end of if 
            self.printCode (f"jmp {endLabel}")

            self.indentation -= 1

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

        # print else 
        if node.elseStmt != None:
            self.printSubDivider ()
            self.printComment ("Else-Statement")
            self.printLabel (f"{elseLabel}:")

            # create new scope level 
            self.scopeNames += [elseLabel]

            node.elseStmt.body.accept (self)

            # jump to endif not necessary since else is always at the end 

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

        # end of if 
        self.printComment ("End of if")
        self.printLabel (f"{endLabel}:")

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
        self.indentation += 1
        node.init.accept (self)
        self.indentation -= 1

        # skip over update
        self.printCode (f"jmp .{condLabel}")

        self.printLabel (f".{forLabel}:")

        self.indentation += 1

        # perform update
        self.printComment ("Update")
        self.indentation += 1
        node.update.accept (self)
        self.indentation -= 1

        self.printLabel (f".{condLabel}:")

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("pop rax ; __cond")
        # jump if false - negation of original condition
        self.printCode ("cmp rax, 0 ; __cond")
        if (node.elseStmt != None):
            self.printCode (f"je .{elseLabel}")
        else:
            self.printCode (f"je .{endLabel}")
        self.indentation -= 1

        # print the body 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add repeating jump
        self.printComment ("Repeat")
        self.printLabel (f"jmp .{forLabel}")

        # add else statement if it exists
        if (node.elseStmt != None):
            self.printSubDivider ()
            self.printComment ("For-Else-Statement")
            self.printLabel (f".{elseLabel}:")

            # create new scope level 
            self.scopeNames += [elseLabel]

            node.elseStmt.body.accept (self)

            # exit scope
            self.scopeNames.pop ()

            self.printSubDivider ()

        # end of for 
        self.printComment ("End of For")
        self.printLabel (f".{endLabel}:")

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.indentation -= 1

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

        self.printLabel (f".{whileLabel}:")

        self.indentation += 1

        self.printComment ("Condition")
        self.indentation += 1
        # condition is an expression 
        # that gets evaluated and the result 
        # should be stored on the stack 
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("pop rax ; __cond")

        # jump if false - negation of original condition
        self.printCode ("cmp rax, 0 ; __cond")
        self.printCode (f"je .{endLabel}")

        self.indentation -= 1

        # print the body 
        self.printComment ("Body")
        self.indentation += 1
        node.body.accept (self)
        self.indentation -= 1

        # add repeating jump
        self.printCode (f"jmp .{whileLabel}")

        # end of while 
        self.printComment ("End of While")
        self.printLabel (f".{endLabel}:")

        # end of loop context 
        # remove from current loop context
        self.parentLoops.pop ()

        self.indentation -= 1

        self.printSubDivider ()

        # exit scope 
        self.scopeNames.pop ()

    def visitExpressionStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)
            # don't need stack value from statement
            # in some cases, this extra value on the stack can break things
            self.printComment ("Statement results can be ignored")
            self.printCode ("pop rdx")

    def visitReturnStatementNode (self, node):
        self.printComment ("Return")

        self.indentation += 1
        # if there is a value provided 
        if node.expr != None:
            node.expr.accept (self)
            # get return value 
            self.printCode ("pop rax")
            # restore rbp
            self.printComment ("Clean up stack and return")
            self.printCode ("mov rsp, rbp ; remove local vars + unpopped pushes")
            self.printCode ("pop rbp")
            self.printCode ("ret")
        # no value provided 
        else:
            self.printCode ("mov rax, 0")
            # restore rbp
            self.printComment ("Clean up stack and return")
            self.printCode ("mov rsp, rbp ; remove local vars + unpopped pushes")
            self.printCode ("pop rbp")
            self.printCode ("ret")

        self.indentation -= 1

    def visitContinueStatementNode (self, node):
        self.printComment (f"Continue in {self.parentLoops[-1].startLabel}")
        # goes to the start of the loop (aka the condition)
        self.printCode (f"jmp .{self.parentLoops[-1].startLabel}")

    def visitBreakStatementNode (self, node):
        self.printComment (f"Break out of {self.parentLoops[-1].startLabel}")
        # goes to the end of the loop
        self.printCode (f"jmp .{self.parentLoops[-1].breakLabel}")

    def visitCodeBlockNode (self, node):
        self.printSubDivider ()
        self.printComment ("Code Block")
        self.indentation += 1

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

        self.indentation -= 1
        self.printSubDivider ()

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitAssignExpressionNode (self, node):
        self.printComment (f"Assignment - '{node.op.lexeme}'")

        self.indentation += 1

        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        if isinstance(node.lhs, VariableDeclarationNode):
            self.printComment ("LHS")
            self.indentation += 1
            node.lhs.accept (self)
            self.indentation -= 1
            self.printCode (f"pop rdx ; __rhs")
            lhsStr = f"qword [rbp - {node.lhs.stackOffset}]"

        elif isinstance(node.lhs, IdentifierExpressionNode):
            self.printCode (f"pop rdx ; __rhs")
            lhsStr = f"qword [rbp - {node.lhs.decl.stackOffset}]"
        elif isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"pop rdx ; __rhs")
            lhsStr = f"{node.lhs.decl.scopeName}"
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

            self.printCode ("pop rdx ; __offset")
            self.printCode ("pop rax ; __pointer")

            self.indentation -= 1
            self.indentation -= 1

            self.printCode (f"pop rdx ; __rhs")
            lhsStr = f"__pointer[__offset]"

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
            # # construct field index var 
            # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
            self.printCode (f"PUSH {node.lhs.decl.scopeName}")
            self.indentation -= 1

            self.printCode ("POP __child")
            self.printCode ("POP __parent")

            self.printCode (f"POP __rhs")
            
            lhsStr = f"__parent[__child]"

            self.indentation -= 1
            self.indentation -= 1

        # =
        if node.op.type == "ASSIGN":
            self.printCode (f"mov {lhsStr}, rdx")
            self.printCode ("push rdx")
        # +=
        elif node.op.type == "ASSIGN_ADD":
            self.printCode (f"ADD {lhsStr} {lhsStr} __rhs")
            self.printCode (f"PUSH {lhsStr}")
        # -=
        elif node.op.type == "ASSIGN_SUB":
            self.printCode (f"SUBTRACT {lhsStr} {lhsStr} __rhs")
            self.printCode (f"PUSH {lhsStr}")
        # *=
        elif node.op.type == "ASSIGN_MUL":
            self.printCode (f"MULTIPLY {lhsStr} {lhsStr} __rhs")
            self.printCode (f"PUSH {lhsStr}")
        # /=
        elif node.op.type == "ASSIGN_DIV":
            self.printCode (f"DIVIDE {lhsStr} {lhsStr} __rhs")
            self.printCode (f"PUSH {lhsStr}")
        # %=
        elif node.op.type == "ASSIGN_MOD":
            self.printCode (f"MOD {lhsStr} {lhsStr} __rhs")
            self.printCode (f"PUSH {lhsStr}")
        
        self.indentation -= 1

    def visitLogicalOrExpressionNode (self, node):
        self.printComment ("OR")

        self.indentation += 1

        # calc lhs 
        self.printComment ("Eval LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        # generate unique labels
        # this is done after eval LHS so the jumpIndexes increase top-down
        short_circuit_state_label = f".OR_SHORT_CIRCUIT{self.jumpIndex}"
        false_label = f".OR_FALSE{self.jumpIndex}"
        end_label = f".OR_END{self.jumpIndex}"
        self.jumpIndex += 1

        # short-circuit if true 
        self.printComment ("Check if we need to short-circuit")
        self.indentation += 1
        self.printCode ("pop rax ; __lhs")
        self.printCode ("test rax, rax")
        self.printCode (f"jne {short_circuit_state_label}")
        self.indentation -= 1

        # calc rhs 
        self.printComment ("Eval RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        # short-circuit if false 
        self.printComment ("Check rhs")
        self.indentation += 1
        self.printCode ("pop rax ; __rhs")
        self.printCode ("test rax, rax")
        self.printCode (f"je {false_label} ; skip true state if false (rax == 0)")
        self.indentation -= 1

        # short cicuit state
        self.printLabel (f"{short_circuit_state_label}:")
        self.printCode ("mov rax, 1 ; result = True")
        self.printCode (f"jmp {end_label} ; skip false state")

        # false state
        self.printComment ("False state")
        self.printLabel (f"{false_label}:")
        self.printCode ("mov rax, 0 ; result = False")

        # end state
        self.printLabel (f"{end_label}:")
        self.printCode ("movzx eax, al")
        self.printCode ("push rax ; result")

        self.indentation -= 1

    # *** might need to edit this for short circuit eval***
    def visitLogicalAndExpressionNode (self, node):
        self.printComment ("AND")

        self.indentation += 1

        # calc lhs 
        self.printComment ("Eval LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        # generate unique labels
        # this is done after eval LHS so the jumpIndexes increase top-down
        short_circuit_state_label = f".AND_SHORT_CIRCUIT{self.jumpIndex}"
        end_label = f".AND_END{self.jumpIndex}"
        self.jumpIndex += 1

        # short-circuit if false 
        self.printComment ("Check if we need to short-circuit")
        self.indentation += 1
        self.printCode ("pop rax ; __lhs")
        self.printCode ("test rax, rax")
        self.printCode (f"je {short_circuit_state_label}")
        self.indentation -= 1

        # calc rhs 
        self.printComment ("Eval RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        # short-circuit if false 
        self.printComment ("Check RHS")
        self.indentation += 1
        self.printCode ("pop rax ; __rhs")
        self.printCode ("test rax, rax")
        self.printCode (f"je {short_circuit_state_label}")
        self.indentation -= 1

        # success state
        self.printComment ("Success state")
        self.printCode ("mov rax, 1 ; result = True")
        self.printCode (f"jmp {end_label}")

        # short cicuit state
        self.printLabel (f"{short_circuit_state_label}:")
        self.printCode ("mov rax, 0 ; result = False")

        # end state
        self.printLabel (f"{end_label}:")
        self.printCode ("movzx eax, al")
        self.printCode ("push rax ; result")

        self.indentation -= 1

    def visitEqualityExpressionNode (self, node):
        if node.op.lexeme == "==":
            self.printComment ("Equal")
        elif node.op.lexeme == "!=":
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
        self.printCode ("pop rdx ; rhs")
        self.printCode ("pop rax ; lhs")

        if node.op.lexeme == "==":
            self.printCode ("cmp rax, rdx")
            self.printCode ("sete al")
            self.printCode ("movzx eax, al")
        elif node.op.lexeme == "!=":
            self.printCode ("cmp rax, rdx")
            self.printCode ("setne al")
            self.printCode ("movzx eax, al")

        # push result to the stack
        self.printCode ("push rax")

        self.indentation -= 1

    def visitInequalityExpressionNode (self, node):
        if node.op.lexeme == "<":
            self.printComment ("Less Than")
        elif node.op.lexeme == "<=":
            self.printComment ("Less Than or Equal to")
        elif node.op.lexeme == ">":
            self.printComment ("Greater Than")
        elif node.op.lexeme == ">=":
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
        self.printCode ("pop rdx ; rhs")
        self.printCode ("pop rax ; lhs")

        if node.op.lexeme == "<":
            self.printCode ("cmp rax, rdx")
            self.printCode ("setl al")
            self.printCode ("movzx eax, al")
        elif node.op.lexeme == "<=":
            self.printCode ("cmp rax, rdx")
            self.printCode ("setle al")
            self.printCode ("movzx eax, al")
        elif node.op.lexeme == ">":
            self.printCode ("cmp rax, rdx")
            self.printCode ("setg al")
            self.printCode ("movzx eax, al")
        elif node.op.lexeme == ">=":
            self.printCode ("cmp rax, rdx")
            self.printCode ("setge al")
            self.printCode ("movzx eax, al")

        # push result to the stack
        self.printCode ("push rax")

        self.indentation -= 1

    def visitAdditiveExpressionNode (self, node):
        # addition 
        if node.op.lexeme == "+":
            self.printComment ("Addition")
        # subtraction 
        elif node.op.lexeme == "-":
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
        self.printCode ("pop rdx")
        self.printCode ("pop rax")
        
        # simple additive 
        if node.overloadedFunctionCall == None:
            # addition
            if node.op.lexeme == "+":
                self.printCode ("add rax, rdx")
            # subtraction 
            elif node.op.lexeme == "-":
                self.printCode ("sub rax, rdx")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"push rdx")
            self.printCode (f"push rax")
            self.printCode (f"call {node.overloadedFunctionCall.decl.scopeName}")

        # push result to the stack
        self.printCode ("push rax")

        self.indentation -= 1

    def visitMultiplicativeExpressionNode (self, node):
        # Multiplication 
        if node.op.lexeme == "*":
            self.printComment ("Multiplication")
        # division 
        elif node.op.lexeme == "/":
            self.printComment ("Division")
        # Mod
        elif node.op.lexeme == "%":
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
        self.printCode ("pop rdx")
        self.printCode ("pop rax")
    
        # simple multiplicative  
        if node.overloadedFunctionCall == None:
            # Multiplication 
            if node.op.lexeme == "*":
                self.printCode ("imul rax, rdx")
            # division 
            elif node.op.lexeme == "/":
                self.printCode ("mov esi, edx")
                self.printCode ("mov edx, 0")
                self.printCode ("cdq")
                self.printCode ("idiv esi")
                # rax now contains quotient
                # rdx contains remainder
            # Mod
            elif node.op.lexeme == "%":
                self.printCode ("mov esi, edx")
                self.printCode ("mov edx, 0")
                self.printCode ("cdq")
                self.printCode ("idiv esi")
                # rax now contains quotient
                # rdx contains remainder
                # we want rax to have rdx
                self.printCode ("mov rax, rdx")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"push rdx")
            self.printCode (f"push rax")
            self.printCode (f"call {node.overloadedFunctionCall.decl.scopeName}")
        

        # push result to the stack
        self.printCode ("push rax")

        self.indentation -= 1
            
    #  ++ | -- | + | - | ! | ~
    # **INCR and DECR do not save the value
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

        self.indentation += 1

        # calc rhs 
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1
        # get rhs off the stack 
        self.printCode ("pop rdx")
    
        if node.op.lexeme == "++":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"add qword [rbp - {node.rhs.decl.stackOffset}], 1")
                self.printCode (f"mov rax, qword [rbp - {node.rhs.decl.stackOffset}]")
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
                # fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"PUSH {node.rhs.decl.scopeName}")
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
        elif node.op.lexeme == "--":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"sub qword [rbp - {node.rhs.decl.stackOffset}], 1")
                self.printCode (f"mov rax, qword [rbp - {node.rhs.decl.stackOffset}]")
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
                # fieldIndex = f"__field__{node.rhs.lhs.type.id}__{node.rhs.rhs.id}"
                self.printCode (f"PUSH {node.rhs.decl.scopeName}")
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
        elif node.op.lexeme == "+":
            self.printComment ("val = 0 + val")
            self.printCode ("mov rax, 0")
            self.printCode ("add rax, rdx")
        elif node.op.lexeme == "-":
            self.printComment ("val = 0 - val")
            self.printCode ("mov rax, 0")
            self.printCode ("sub rax, rdx")
        elif node.op.lexeme == "!":
            self.printCode ("cmp rdx, 0")
            self.printCode ("sete al")
            self.printCode ("movzx eax, al")
        elif node.op.lexeme == "~":
            self.printCode ("not rdx")
            self.printCode ("mov rax, rdx")

        # push result to the stack
        self.printCode ("push rax")

        self.indentation -= 1

    def visitPostIncrementExpressionNode(self, node):
        self.printComment ("Post-Increment")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"mov rax, qword [rbp - {node.lhs.decl.stackOffset}]")
            self.printCode (f"add qword [rbp - {node.lhs.decl.stackOffset}], 1")
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
        self.printCode ("push rax")

        self.indentation -= 1

    def visitPostDecrementExpressionNode (self, node):
        self.printComment ("Post-Decrement")

        self.indentation += 1

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"mov rax, qword [rbp - {node.lhs.decl.stackOffset}]")
            self.printCode (f"sub qword [rbp - {node.lhs.decl.stackOffset}], 1")
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
        self.printCode ("push rax")

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

        # simple subscript  
        if node.overloadedFunctionCall == None:
            self.printCode ("PUSH __pointer[__offset]")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"PUSH __offset")
            self.printCode (f"PUSH __pointer")
            self.printCode (f"CALL {node.overloadedFunctionCall.decl.scopeName}")
            self.printCode (f"RESPONSE __res")
            self.printCode (f"PUSH __res")

        self.indentation -= 1

    def visitFunctionCallExpressionNode (self, node):
        self.printComment (f"Function Call - {node.decl.signature} -> {node.decl.type}")

        self.indentation += 1

        self.printComment (f"Make space for {len(node.args)} arg(s)")
        self.printCode (f"sub rsp, {len(node.args)*8}")

        self.printComment ("Arguments")
        self.indentation += 1
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for i in range(len(node.args)):
            self.printComment (f"Eval arg{i}")
            self.indentation += 1
            node.args[i].accept (self)
            self.indentation -= 1
            
            # move arg result to proper place in stack
            self.printComment (f"Move arg{i}'s result to reverse order position on stack")
            self.printCode ("pop rax")
            offset = i * 8
            self.printCode (f"mov qword [rsp + {offset}], rax")
        
        self.indentation -= 1

        # call function
        self.printComment (f"Call {node.decl.signature}")
        if node.decl.scopeName == "":
            # x = sum([1 if '\n' in s else 0 for s in self.code])
            # print (f"[code-gen] Error: no scope name for {node.function.id} {[t.type.__str__() for t in node.args]} {node.lineNumber} {x}")
            # print (f"   this could have happened due to a template using a class that was defined after the template")
            # print (f"   temporary fix: move the class declaration to above the template class that uses it")
            # solution! extremely ad hoc 
            self.printCode (f"call ${node.decl.signature}")
            # exit (1)
        else:
            self.printCode (f"call {node.decl.label}")

        # remove arguments from stack
        self.printComment ("Remove args")
        self.printCode (f"add rsp, {len(node.args)*8}")
        
        # put function's return val on the stack
        self.printCode ("push rax")

        self.indentation -= 1

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

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        if node.decl.scopeName == "":
            x = sum([1 if '\n' in s else 0 for s in self.code])
            print (f"[code-gen] [member-accessor] Error: no scope name for '{node.decl.id}' on line {node.lineNumber}")
            print (f"   this could have happened due to a cyclic reference/composition with template classes")
            print (f"   cyclic references are not yet supported")
            exit (1)
        self.printCode (f"PUSH {node.decl.scopeName}")
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
        self.printCode (f"PUSH {node.decl.scopeName}")
        self.indentation -= 1

        self.printCode ("POP __child")
        self.printCode ("POP __parent")
        self.printCode ("PUSH __parent[__child]")

        self.indentation -= 1

    def visitMethodAccessorExpressionNode (self, node):
        if node.decl.isVirtual:
            self.printComment (f"Virtual Method Call - {node.decl.signatureNoScope} -> {node.decl.type}")
        else:
            self.printComment (f"Method Call - {node.decl.signature} -> {node.decl.type}")

        self.indentation += 1

        self.printComment ("LHS")
        self.indentation += 1
        node.lhs.accept (self)
        self.indentation -= 1

        self.printComment ("RHS")
        self.indentation += 1
        # construct field index var 
        # methodName = f"__method__{node.lhs.type.id}__{node.rhs.id}"
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
            self.printCode (f"CALL {node.decl.scopeName}")

        # remove parent object instance
        self.printCode (f"POP __void")

        # remove arguments from stack
        self.printComment ("Remove args")
        for i in range(0, len(node.args)):
            self.printCode (f"POP __void")
                
        # put function's return val on the stack
        self.printCode ("RESPONSE __retval")
        self.printCode ("PUSH __retval")

        self.indentation -= 1

    def visitThisExpressionNode (self, node):
        self.printComment (f"This keyword")
        self.indentation += 1
        # push [rbp - 8] ; this 
        self.printCode (f"PUSH __this")
        self.indentation -= 1

    def visitIdentifierExpressionNode (self, node):
        self.printComment (f"Identifier - {node.id}")
        self.indentation += 1
        self.printCode (f"push qword [rbp - {node.decl.stackOffset}]")
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
        self.printComment (f"Constructor Call - {node.decl.signature} -> {node.decl.parentClass.type}")

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
        self.printCode (f"CALL {node.decl.scopeName}")

        # remove arguments from stack
        self.printComment ("Remove args")
        for i in range(0, len(node.args)):
            self.printCode (f"POP __void")
        
        # put function's return val on the stack
        self.printCode ("RESPONSE __retval")
        self.printCode ("PUSH __retval")

        self.indentation -= 1
    
    def visitSizeofExpressionNode(self, node):
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
    
    def visitFreeExpressionNode (self, node):
        self.printComment ("Free Operator")
        self.indentation += 1

        # calc rhs
        self.printComment ("RHS")
        self.indentation += 1
        node.rhs.accept (self)
        self.indentation -= 1

        self.printComment ("Free array")
        self.printCode ("POP __array")
        self.printCode ("FREE __array")
        # put the array back on the stack 
        # this will get popped off the stack for the case:
        #    free(arr);
        # but the value can still be used 
        #    freedBAsWell = free(a) == b;
        self.printCode ("PUSH __array")

        self.indentation -= 1

    def visitIntLiteralExpressionNode (self, node):
        self.printComment ("Int Literal")
        self.indentation += 1
        self.printCode (f"push {node.value}")
        self.indentation -= 1

    def visitFloatLiteralExpressionNode (self, node):
        self.printComment ("Float Literal")
        self.indentation += 1
        self.printCode (f"PUSH {node.value}")
        self.indentation -= 1

    def visitCharLiteralExpressionNode (self, node):
        self.printComment ("Char Literal")
        self.indentation += 1
        # normal character:
        if node.value[0] != '\\':
            self.printCode (f"push '{(node.value)}'")
        # escaped character
        else:
            # convert to ascii value 
            import ast
            asciiValue = ord(ast.literal_eval(str("".join(["\"", node.value, "\""]))))
            self.printCode (f"push {asciiValue} ; {node.value}")
        self.indentation -= 1

    def visitStringLiteralExpressionNode (self, node):
        self.printComment ("String Literal")
        self.indentation += 1

        self.printComment (node.value)
        self.printCode (f"mov rax, {node.label}")
        self.printCode ("push rax")

        # # create string on heap as char[]
        # node.value = (node.value.replace(f'\n', f'\\n').replace ('\t', '\\t')).replace ("\r", "\\r").replace ("\b", "\\b")
        # # node.value = node.value.replace ("\\n", "\n").replace ("\\t", "\t").replace ("\\r", "\r").replace ("\\b", "\b")
        # chars = [node.value[i] for i in range(1, len(node.value)-1)]
        # for i in range(len(chars)-1):
        #     if i >= len(chars)-1:
        #         break
        #     if chars[i] == "\\" and \
        #         (chars[i+1] == 'n'  \
        #         or chars[i+1] == 't'\
        #         or chars[i+1] == 'r'\
        #         or chars[i+1] == 'b'):
        #         chars[i] = "\\" + chars[i+1]
        #         del chars[i+1]
        # node.value = chars
        # backSlashes = 0
        # # for c in node.value:
        # #     if c == '\\':
        # #         backSlashes += 1
        # self.printCode (f"MALLOC __str {len(node.value)-backSlashes}")
        # for i in range(len(node.value)-backSlashes):
        #     self.printCode (f"ASSIGN __str[{i}] '{(node.value[i])}'")
        # self.printCode ("PUSH __str")
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
        

    def visitNullExpressionNode (self, node):
        self.printComment ("Null Literal")
        self.indentation += 1
        self.printCode ("ASSIGN __null 0")
        self.printCode ("PUSH __null")
        self.indentation -= 1


# ========================================================================