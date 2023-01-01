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
        self.indentation_stack = []
        # we have multiple code stacks so that we can build
        # function definitions and later push
        # them to the global stack for cpp
        # AmyScript allows functions within functions
        # but CPP does not so this allows us to
        # place function definitions in the correct order
        # i.e. nested functions need to be defined before parent functions
        self.global_code_stack = []
        # by default we add the global code stack
        # so that we can push to the global stack before main function
        self.code_stacks = [self.global_code_stack]
        # for compatability code references our global code
        self.code = self.global_code_stack
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

    def createCodeStack (self):
        self.code_stacks.append ([])
        # new code stacks have their own indentation
        # this is so separate functions arent weirdly indented
        self.indentation_stack.append (self.indentation)
        self.indentation = 0
    
    def popAndAddCodeStack (self):
        self.global_code_stack += self.code_stacks.pop ()
        # restore indentation
        self.indentation = self.indentation_stack.pop ()

    def printIndent (self):
        self.printSpaces (self.indentation)

    def printSpaces (self, level):
        while level > 0:
            for i in range(TAB_LENGTH):
                self.code_stacks[-1] += [" "]
            level -= 1

    def printCode (self, line, end="\n", shouldIndent=True):
        if shouldIndent: self.printSpaces (self.indentation)
        self.code_stacks[-1] += [f"{line}{end}"]

    def printComment (self, comment):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        self.code_stacks[-1] += ["// ", comment, "\n"]

    def printHeader (self, header):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - len (header) - 8
        divider = ["//### "]
        divider += [header, " "]
        for i in range(dividerLength):
            divider += ["#"]
        self.code_stacks[-1] += ["".join(divider)]
        self.printNewline ()

    def printDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//="]
        for i in range(dividerLength):
            divider += ["="]
        self.code_stacks[-1] += ["".join(divider)]
        self.printNewline ()

    def printSubDivider (self):
        if not self.shouldComment:
            return 
            
        self.printSpaces (self.indentation)
        dividerLength = DIVIDER_LENGTH - (self.indentation * TAB_LENGTH) - 3
        divider = ["//-"]
        for i in range(dividerLength):
            divider += ["-"]
        self.code_stacks[-1] += ["".join(divider)]
        self.printNewline ()

    def printNewline (self):
        self.code_stacks[-1] += ["\n"]

    def enterScope (self, name):
        self.scopeNames += [f"__{name}"]

    def exitScope (self):
        self.scopeNames.pop ()

    def printFunctionHeader (self):
        self.printComment ("Function Header")
        # expression result stack stores values from expressions 
        self.printComment ("This stack is used to store results of expressions")
        self.printCode ("std::vector<long> stack;")

        self.printComment ("Declare general purpose variables")
        self.printComment ("These are longs and can store anything up to 8 bytes via casting")
        self.printCode ("long __stackval = 0;")
        self.printCode ("long __pointer = 0;")
        self.printCode ("long __offset = 0;")
        self.printCode ("long __parent = 0;")
        self.printCode ("long __child = 0;")
        self.printCode ("long __obj = 0;")
        self.printCode ("long __lhs = 0;")
        self.printCode ("long __rhs = 0;")
        self.printCode ("long __res = 0;")

    # returns the equivalent cpp type for the AmyScript type
    def amyTypeToCPPType (self, type:TypeSpecifierNode):
        type_str = "long"
        # INT -> long
        if type.type == Type.INT:
            type_str = "long"
        # FLOAT -> double
        elif type.type == Type.FLOAT:
            type_str = "double"
        # CHAR -> char
        elif type.type == Type.CHAR:
            type_str = "char"
        # objects - > <user-type-name>*
        #   ex: Point* p;
        elif type.type == Type.USERTYPE:
            type_str = f"{type.decl.scopeName}*"
        # void
        elif type.type == Type.VOID:
            type_str = f"void"
        else:
            type_str = "<unknown-type>*"
        
        # handle arrays/pointers
        for _ in range(type.arrayDimensions):
            type_str += '*'
        return type_str

    # converts long to the given type using a given variable
    def stackToVar (self, type:TypeSpecifierNode, varname):
        type_str = "long"
        array_suffix = ""
        # handle arrays/pointers
        for _ in range(type.arrayDimensions):
            array_suffix += '*'
        # INT -> long
        if type.type == Type.INT:
            type_str = f"*reinterpret_cast<long*{array_suffix}>(&{varname})"
        # FLOAT -> double
        elif type.type == Type.FLOAT:
            type_str = f"*reinterpret_cast<double*{array_suffix}>(&{varname})"
        # CHAR -> char
        elif type.type == Type.CHAR:
            # non array
            if array_suffix == "":
                type_str = f"static_cast<char>(static_cast<unsigned char>({varname}))"
            # array
            else:
                type_str = f"*reinterpret_cast<char*{array_suffix}>(&{varname})"
        # objects - > <user-type-name>*
        #   ex: Point* p;
        elif type.type == Type.USERTYPE:
            type_str = f"reinterpret_cast<{type.decl.scopeName}*{array_suffix}>({varname})"
        else:
            type_str = f"<unknown-conversion>*{array_suffix}"
        
        return type_str
    
    # converts given varname to a long so that it can be stored on the stack
    def varToStack (self, type:TypeSpecifierNode, varname):
        type_str = "long"
        # arrays | objects
        if type.type == Type.USERTYPE or type.arrayDimensions > 0:
            # we can simply convert pointers to long
            # objects and arrays are both pointers
            type_str = f"reinterpret_cast<long>({varname})"
        # INT -> long
        elif type.type == Type.INT:
            type_str = f"*reinterpret_cast<long*>(&{varname})"
        # FLOAT -> double
        elif type.type == Type.FLOAT:
            type_str = f"*reinterpret_cast<long*>(&{varname})"
        # CHAR -> char
        elif type.type == Type.CHAR:
            type_str = f"static_cast<long>(static_cast<unsigned char>({varname}))"
        else:
            type_str = f"<unknown-conversion>*"
        
        return type_str

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
            self.code_stacks[-1] += [line]

        # Build main code stack
        self.createCodeStack ()

        self.printDivider ()
        self.printHeader ("Main function")
        self.printDivider ()
        self.printNewline ()

        self.printCode ("int main () {")
        self.indentation += 1

        self.printDivider ()
        self.printHeader ("SETUP EXPRESSION RESULT STACK")
        self.printDivider ()
        self.printNewline ()
        
        self.printFunctionHeader ()

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

        self.indentation -= 1
        self.printCode ("}")

        self.printDivider ()
        self.printHeader ("END OF MAIN")
        self.printDivider ()
        self.printNewline ()

        # push main function to the global stack
        self.popAndAddCodeStack ()

    def visitTypeSpecifierNode (self, node):
        pass

    def visitParameterNode (self, node):
        node.type.accept (self)
        node.scopeName = "".join (self.scopeNames) + "__" + node.id

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        self.printComment ("Variable declaration")
        node.type.accept (self)

        # variable names are modified by its scope 
        scopeName = "".join (self.scopeNames) + "__" + node.id

        self.printCode (f"{self.amyTypeToCPPType(node.type)} {scopeName};")
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
        for i in range(len(self.code_stacks[-1])):
            if f"${node.signature}" in self.code_stacks[-1][i]:
                self.code_stacks[-1][i] = self.code_stacks[-1][i].replace(f"${node.signature}", node.scopeName)

        # create new scope level 
        self.scopeNames += [f"__{node.id}"]

        self.printComment (f"Function Declaration - {node.signature} -> {node.type}")
        self.printComment ("*see this func def before this parent function")
        self.printNewline ()

        # create a new code stack to build this function's definition
        # we will add this before the main function
        self.createCodeStack ()

        self.printDivider ()
        self.printComment (f"Function Declaration - {node.signature} -> {node.type}")

        # parameters
        params = []
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (f"{self.amyTypeToCPPType(node.params[i].type)} {node.params[i].scopeName}")
        self.printCode (f"{self.amyTypeToCPPType(node.type)} {node.scopeName} ({', '.join(params)})")

        self.printCode ("{")
        self.indentation += 1

        self.printFunctionHeader ()

        self.printComment ("Body")
        node.body.accept (self)

        self.indentation -= 1
        self.printCode ("};")

        self.printComment (f"End Function Declaration - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

        self.popAndAddCodeStack ()

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

        if node.pDecl != None:
            self.printComment (f"Class Declaration - {node.scopeName} inherits {node.pDecl.scopeName}")
        else: 
            self.printComment (f"Class Declaration - {node.scopeName}")
        self.printComment ("*see this class def before this parent function")
        self.printNewline ()

        # first add a forward decl for any insider functions
        self.createCodeStack ()
        self.printComment ("Add forward decl for any inner functions and methods")
        self.printCode (f"class {node.scopeName};")
        self.popAndAddCodeStack ()

        # create a new code stack to build this class's definition
        # we will add this before the main function
        self.createCodeStack ()

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
        self.printCode (f"void* {node.dtableScopeName}[{len(node.functionPointerList)}];")

        # class header
        self.printCode (f"class {node.scopeName} : public {node.pDecl.scopeName}")
        self.printCode ("{")
        self.indentation += 1
        self.printCode ("public:")

        # create scope names for fields 
        for field in node.fields:
            # variable names are modified by its scope 
            fieldScopeName = "__field__" + "".join (self.scopeNames) + "____" + field.id
            field.scopeName = fieldScopeName
            # if this field was inherited by a parent class
            # then we need to use the original scopeName
            # *this may fail if the original scope name wasn't made yet
            if field.isInherited:
                field.scopeName = field.originalInheritedField.scopeName

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

        self.indentation -= 1
        self.printCode ("};")
        self.popAndAddCodeStack ()

        # we need to add the methods outside of the class
        for method in node.methods:
            method.parentClass = node
            method.accept (self)

        # this is printed in where the class was originally defined (probably main)
        self.printComment ("Populate Dispatch Table")
        # populate dispatch table
        for i in range(len(node.functionPointerList)):
            self.printCode (f"{node.dtableScopeName}[{i}] = (void*){node.functionPointerList[i].scopeName};")

        self.createCodeStack ()

        self.printComment (f"End Class Declaration - {node.scopeName}")
        self.printDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

        self.popAndAddCodeStack ()

    def visitFieldDeclarationNode (self, node):
        self.printSubDivider ()
        self.printComment (f"Field - {node.type} {node.signature}")
        if node.isInherited:
            self.printComment (f"Inherited from {node.parentClass.pDecl.id}")
            self.printComment (f"{node.originalInheritedField.scopeName}")
        else:
            # fieldIndexVarname = f"__field__{node.id}__{field.id}"
            self.printComment (f"{node.scopeName} = {node.index}")
            self.printCode (f"{self.amyTypeToCPPType(node.type)} {node.scopeName};")

        self.printSubDivider ()

    def visitMethodDeclarationNode (self, node):
        self.createCodeStack ()

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
        params_with_types = ['']
        params = ['']
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (node.params[i].scopeName)
            params_with_types.append (f"{self.amyTypeToCPPType(node.params[i].type)} {node.params[i].scopeName}")
        self.printCode (f"{self.amyTypeToCPPType(node.type)} {methodLabel} ({self.amyTypeToCPPType(node.parentClass.type)} __this{', '.join(params_with_types)})")
        self.printCode ("{")
        self.indentation += 1
        self.printFunctionHeader ()

        # inherited methods
        if node.isInherited:
            self.printComment (f"Jump to {node.inheritedMethod.parentClass.id}'s version")
            # function returns void
            if node.type.type == Type.VOID and node.type.arrayDimensions == 0:
                self.printCode (f"{node.inheritedMethod.scopeName} (__this{', '.join(params)});")
            # function returns a value
            else:
                self.printCode (f"{self.amyTypeToCPPType(node.type)} __inheritedres = {node.inheritedMethod.scopeName} (__this{', '.join(params)});")
                self.printCode (f"return __inheritedres;")
        else:
            self.printComment ("Body")
            node.body.accept (self)

            # extra return statement for if return is not provided 
            # self.printCode ("return 0")

        self.indentation -= 1
        self.printCode ("}")
        self.printComment (f"End Method Declaration - {methodLabel}")
        self.printSubDivider ()
        self.printNewline ()

        # remove scope level 
        self.scopeNames.pop ()

        self.popAndAddCodeStack ()

    def visitConstructorDeclarationNode (self, node):

        # create new scope level 
        self.scopeNames += [f"__{node.parentClass.id}"]

        self.printSubDivider ()
        self.printComment (f"Constructor Declaration - {node.signature} -> {node.parentClass.type}")

        endLabel = f"__end{node.scopeName}"
        ctorLabel = f"{node.scopeName}"

        # AD HOC CENTRAL!!
        # fill in prereferences with scopename 
        for i in range(len(self.code_stacks[-1])):
            if f"${node.signature}" in self.code_stacks[-1][i]:
                self.code_stacks[-1][i] = self.code_stacks[-1][i].replace(f"${node.signature}", node.scopeName)

        # parameters
        params = []
        for i in range(len(node.params)):
            node.params[i].accept (self)
            params.append (f"{self.amyTypeToCPPType(node.params[i].type)} {node.params[i].scopeName}")

        # ctor header
        self.printCode (f"{node.parentClass.scopeName} ({', '.join(params)})")
        self.printCode ("{")
        self.indentation += 1
        self.printFunctionHeader ()

        # create class instance 
        self.printComment ("Add dispatch table to instance")
        self.printCode (f"dtable = {node.parentClass.dtableScopeName};")
        self.printCode (f"{node.parentClass.scopeName}* __this = this;")

        # ** maybe initialize entries? or that might be inefficient
        
        # *** are we supposed to support inherited ctors?
        self.printComment ("Body")
        node.body.accept (self)

        # return constructed class instance
        # self.printComment ("Return the constructed instance")
        # self.printCode ("return this")

        self.indentation -= 1
        self.printCode ("}")
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
        self.printCode (f"long __if__{ifIndex}__cond = stack.back ();")
        self.printCode ("stack.pop_back ();")
        for i in range(len(node.elifs)):
            self.printComment (f"Condition for elif #{i}")
            node.elifs[i].cond.accept (self)
            self.printCode (f"long __elif__{ifIndex}x{elifIndex}__cond = stack.back ();")
            self.printCode ("stack.pop_back ();")
            elifIndex += 1
        elifIndex = 0

        self.printComment ("get condition from stack")
        self.printCode (f"if (__if__{ifIndex}__cond)")

        # print the body of if 
        self.printCode ("{")
        self.indentation += 1
        self.printComment ("Body")
        node.body.accept (self)
        self.indentation -= 1
        self.printCode ("}")

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
            # self.printCode ("__cond = stack.back ();")
            # self.printCode ("stack.pop_back ();")

            self.printCode (f"else if (__elif__{ifIndex}x{elifIndex}__cond)")
            elifIndex += 1

            # Body
            self.printCode ("{")
            self.indentation += 1
            self.printComment ("Body")
            elifNode.body.accept (self)
            self.indentation -= 1
            self.printCode ("}")

            self.printSubDivider ()

            # exit scope
            self.scopeNames.pop ()

        # print else 
        if node.elseStmt != None:
            self.printSubDivider ()
            self.printComment ("Else-Statement")

            # create new scope level 
            self.scopeNames += [elseLabel]

            self.printCode ("else")

            self.printCode ("{")
            self.indentation += 1
            node.elseStmt.body.accept (self)
            self.indentation -= 1
            self.printCode ("}")

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
        self.printCode ("while (1)")

        self.printCode ("{")
        self.indentation += 1

        self.printComment ("Condition")
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("long __cond = stack.back ();")
        self.printCode ("stack.pop_back ();")
        # jump if false - negation of original condition
        self.printComment ("break out of loop if condition is false")
        self.printCode ("if (__cond == 0) break;")

        # print the body 
        self.printComment ("Body")
        node.body.accept (self)

        # perform update
        self.printComment ("Update")
        node.update.accept (self)

        self.indentation -= 1
        self.printCode ("}")

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
        self.printCode ("while (1)")

        self.printCode ("{")
        self.indentation += 1

        self.printComment ("Condition")
        node.cond.accept (self)
        # get condition result from stack
        self.printCode ("long __cond = stack.back ();")
        self.printCode ("stack.pop_back ();")
        # jump if false - negation of original condition
        self.printComment ("break out of loop if condition is false")
        self.printCode ("if (__cond == 0) break;")

        # print the body 
        self.printComment ("Body")
        node.body.accept (self)

        self.indentation -= 1
        self.printCode ("}")

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
            self.printCode ("stack.pop_back ();")
            self.printComment ("End Statement")
            self.printNewline ()

    def visitReturnStatementNode (self, node):
        self.printComment ("Return")
        # if there is a value provided 
        if node.expr != None:
            node.expr.accept (self)
            # get return value 
            self.printCode ("__res = stack.back ();")
            self.printCode ("stack.pop_back ();")

            # cast res
            # INT
            if node.expr.type.type == Type.INT and node.expr.type.arrayDimensions == 0:
                res_str = f"*reinterpret_cast<long*>(&__res)"
            # FLOAT
            elif node.expr.type.type == Type.FLOAT and node.expr.type.arrayDimensions == 0:
                res_str = f"*reinterpret_cast<double*>(&__res)"
            # CHAR
            elif node.expr.type.type == Type.CHAR and node.expr.type.arrayDimensions == 0:
                res_str = f"static_cast<char>(static_cast<unsigned char>(__res))"
            # ARRAY or OBJECT
            else:
                res_str = f"reinterpret_cast<void*>(__res)"
                
            self.printCode (f"return {res_str};")
        # no value provided 
        else:
            self.printCode ("return;")

    def visitContinueStatementNode (self, node):
        self.printComment (f"Continue in {self.parentLoops[-1].startLabel}")
        # for loops need to inject the update
        # bc they were converted to while loops
        if isinstance (self.parentLoops[-1], ForStatementNode):
            self.parentLoops[-1].update.accept (self)
        # goes to the start of the loop (aka the condition)
        self.printCode (f"continue;")

    def visitBreakStatementNode (self, node):
        self.printComment (f"Break out of {self.parentLoops[-1].startLabel}")
        # goes to the end of the loop
        self.printCode (f"break;")

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
                self.printCode (f"__rhs = stack.back ();")
                self.printCode (f"stack.pop_back ();")
                lhsStr = f"{node.lhs.scopeName}"

            elif isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
                self.printCode (f"__rhs = stack.back ();")
                self.printCode (f"stack.pop_back ();")
                lhsStr = f"{node.lhs.decl.scopeName}"

            elif isinstance(node.lhs, SubscriptExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.lhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.lhs.offset.accept (self)

                self.printCode (f"__offset = stack.back ();")
                self.printCode ("stack.pop_back ();")
                self.printCode (f"__pointer = stack.back ();")
                self.printCode ("stack.pop_back ();")

                self.printCode (f"__rhs = stack.back ();")
                self.printCode (f"stack.pop_back ();")
                lhsStr = f"({self.stackToVar(node.lhs.lhs.type,'__pointer')})[__offset]"

            elif isinstance (node.lhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.lhs.lhs.accept (self)

                self.printComment ("RHS")
                # # construct field index var 
                # fieldIndex = f"__field__{node.lhs.lhs.type.id}__{node.lhs.rhs.id}"
                # self.printCode (f"stack.push_back({node.lhs.decl.scopeName})")

                # self.printCode (f"__child = stack.back ();")
                # self.printCode ("stack.pop_back ();")
                self.printCode (f"__parent = stack.back ();")
                self.printCode ("stack.pop_back ();")

                self.printCode (f"__rhs = stack.back ();")
                self.printCode (f"stack.pop_back ();")
                
                lhsStr = f"({self.stackToVar(node.lhs.lhs.type, '__parent')})->{node.lhs.decl.scopeName}"
                
            # =
            if node.op.type == "ASSIGN":
                self.printCode (f"{lhsStr} = {self.stackToVar(node.type,'__rhs')};")
            # +=
            elif node.op.type == "ASSIGN_ADD":
                self.printCode (f"{lhsStr} = {lhsStr} + {self.stackToVar(node.type,'__rhs')};")
            # -=
            elif node.op.type == "ASSIGN_SUB":
                self.printCode (f"{lhsStr} = {lhsStr} - {self.stackToVar(node.type,'__rhs')};")
            # *=
            elif node.op.type == "ASSIGN_MUL":
                self.printCode (f"{lhsStr} = {lhsStr} * {self.stackToVar(node.type,'__rhs')};")
            # /=
            elif node.op.type == "ASSIGN_DIV":
                self.printCode (f"{lhsStr} = {lhsStr} / {self.stackToVar(node.type,'__rhs')};")
            # %=
            elif node.op.type == "ASSIGN_MOD":
                self.printCode (f"{lhsStr} = {lhsStr} % {self.stackToVar(node.type,'__rhs')};")

            self.printComment ("Result of assignment")
            self.printCode (f"stack.push_back ({self.varToStack(node.type, lhsStr)});")
        

    def visitLogicalOrExpressionNode (self, node):
        self.printComment ("OR")
        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__res = __lhs or __rhs")
        # push result to the stack
        self.printCode ("stack.push_back (__res)")

    def visitLogicalAndExpressionNode (self, node):
        self.printComment ("AND")
        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__res = __lhs and __rhs")
        # push result to the stack
        self.printCode ("stack.push_back (__res)")

    def visitEqualityExpressionNode (self, node):
        if node.op.lexeme == "==":
            self.printComment ("Equal")
        elif node.op.lexeme == "!=":
            self.printComment ("Not Equal")

        self.printCode ("{")
        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        
        if node.op.lexeme == "==":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} == {self.stackToVar(node.rhs.type,'__rhs')};")
        elif node.op.lexeme == "!=":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} != {self.stackToVar(node.rhs.type,'__rhs')};")

        # push result to the stack
        self.printCode (f"stack.push_back ({self.varToStack (node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

    def visitInequalityExpressionNode (self, node):
        if node.op.lexeme == "<":
            self.printComment ("Less Than")
        elif node.op.lexeme == "<=":
            self.printComment ("Less Than or Equal to")
        elif node.op.lexeme == ">":
            self.printComment ("Greater Than")
        elif node.op.lexeme == ">=":
            self.printComment ("Greater Than or Equal to")

        self.printCode ("{")
        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")

        if node.op.lexeme == "<":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} < {self.stackToVar(node.rhs.type,'__rhs')};")
        elif node.op.lexeme == "<=":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} <= {self.stackToVar(node.rhs.type,'__rhs')};")
        elif node.op.lexeme == ">":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} > {self.stackToVar(node.rhs.type,'__rhs')};")
        elif node.op.lexeme == ">=":
            self.printCode (f"{self.amyTypeToCPPType (node.type)} __res = {self.stackToVar(node.lhs.type,'__lhs')} >= {self.stackToVar(node.rhs.type,'__rhs')};")

        # push result to the stack
        self.printCode (f"stack.push_back ({self.varToStack (node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

    def visitAdditiveExpressionNode (self, node):
        # addition 
        if node.op.lexeme == "+":
            self.printComment ("Addition")
        # subtraction 
        elif node.op.lexeme == "-":
            self.printComment ("Subtraction")

        self.printCode ("{")
        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")

        # cast lhs
        # INT
        if node.lhs.type.type == Type.INT and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"*reinterpret_cast<long*>(&__lhs)"
        # FLOAT
        elif node.lhs.type.type == Type.FLOAT and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"*reinterpret_cast<double*>(&__lhs)"
        # CHAR
        elif node.lhs.type.type == Type.CHAR and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"static_cast<char>(static_cast<unsigned char>(__lhs))"
        # ARRAY
        # OBJECT
        else:
            lhs_str = f"reinterpret_cast<void*>(__lhs)"

        # cast rhs
        # INT
        if node.rhs.type.type == Type.INT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<long*>(&__rhs)"
        # FLOAT
        elif node.rhs.type.type == Type.FLOAT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<double*>(&__rhs)"
        # CHAR
        elif node.rhs.type.type == Type.CHAR and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"static_cast<char>(static_cast<unsigned char>(__rhs))"
        # ARRAY
        # OBJECT
        else:
            rhs_str = f"reinterpret_cast<void*>(__rhs)"
        
        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY
        # OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        # simple additive 
        if node.overloadedFunctionCall == None:
            # addition
            if node.op.lexeme == "+":
                self.printCode (f"{res_type_str} __res = {lhs_str} + {rhs_str};")
            # subtraction 
            elif node.op.lexeme == "-":
                self.printCode (f"{res_type_str} __res = {lhs_str} - {rhs_str};")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            self.printCode (f"{res_type_str} __res = {node.overloadedFunctionCall.decl.scopeName} ({lhs_str}, {rhs_str});")

        # push result to the stack
        self.printCode (f"stack.push_back ({res_str});")

        self.indentation -= 1
        self.printCode ("}")

    def visitMultiplicativeExpressionNode (self, node):
        if node.op.lexeme == "*":
            self.printComment ("Multiplication")
        elif node.op.lexeme == "/":
            self.printComment ("Division")
        elif node.op.lexeme == "%":
            self.printComment ("Modulus")

        self.printCode ("{")
        self.indentation += 1

        # calc lhs 
        self.printComment ("LHS")
        node.lhs.accept (self)
        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)

        # get rhs and lhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__lhs = stack.back ();")
        self.printCode ("stack.pop_back ();")

        # cast lhs
        # INT
        if node.lhs.type.type == Type.INT and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"*reinterpret_cast<long*>(&__lhs)"
        # FLOAT
        elif node.lhs.type.type == Type.FLOAT and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"*reinterpret_cast<double*>(&__lhs)"
        # CHAR
        elif node.lhs.type.type == Type.CHAR and node.lhs.type.arrayDimensions == 0:
            lhs_str = f"static_cast<char>(static_cast<unsigned char>(__lhs))"
        # ARRAY
        # OBJECT
        else:
            lhs_str = f"reinterpret_cast<void*>(__lhs)"

        # cast rhs
        # INT
        if node.rhs.type.type == Type.INT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<long*>(&__rhs)"
        # FLOAT
        elif node.rhs.type.type == Type.FLOAT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<double*>(&__rhs)"
        # CHAR
        elif node.rhs.type.type == Type.CHAR and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"static_cast<char>(static_cast<unsigned char>(__rhs))"
        # ARRAY
        # OBJECT
        else:
            rhs_str = f"reinterpret_cast<void*>(__rhs)"
        
        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
            is_int = True
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY
        # OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        # simple additive 
        if node.overloadedFunctionCall == None:
            if node.op.lexeme == "*":
                self.printCode (f"{res_type_str} __res = {lhs_str} * {rhs_str};")
            elif node.op.lexeme == "/":
                # cpp already handles integer division
                self.printCode (f"{res_type_str} __res = {lhs_str} / {rhs_str};")
            elif node.op.lexeme == "%":
                self.printCode (f"{res_type_str} __res = {lhs_str} % {rhs_str};")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            self.printCode (f"{res_type_str} __res = {node.overloadedFunctionCall.decl.scopeName} ({lhs_str}, {rhs_str});")

        # push result to the stack
        self.printCode (f"stack.push_back ({res_str});")

        self.indentation -= 1
        self.printCode ("}")
            
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

        self.printCode ("{")
        self.indentation += 1

        # calc rhs 
        self.printComment ("RHS")
        node.rhs.accept (self)
        # get rhs off the stack 
        self.printCode ("__rhs = stack.back ();")
        self.printCode ("stack.pop_back ();")
        # cast rhs
        # INT
        if node.rhs.type.type == Type.INT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<long*>(&__rhs)"
        # FLOAT
        elif node.rhs.type.type == Type.FLOAT and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"*reinterpret_cast<double*>(&__rhs)"
        # CHAR
        elif node.rhs.type.type == Type.CHAR and node.rhs.type.arrayDimensions == 0:
            rhs_str = f"static_cast<char>(static_cast<unsigned char>(__rhs))"
        # ARRAY or OBJECT
        else:
            rhs_str = f"reinterpret_cast<void*>(__rhs)"
        # ** i think this could be a potential bug because we pop rhs before visiting lhs and offset

        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
            is_int = True
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY or OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        if node.op.lexeme == "++":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                # we should not be visiting rhs
                self.printCode (f"{node.rhs.decl.scopeName} = {node.rhs.decl.scopeName} + 1;")
                self.printCode (f"__res = {node.rhs.decl.scopeName};")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.rhs.offset.accept (self)

                self.printCode ("__offset = stack.back ();")
                self.printCode ("stack.pop_back ();")
                self.printCode ("__pointer = stack.back ();")
                self.printCode ("stack.pop_back ();")

                self.printCode (f"__pointer[__offset] = __pointer[__offset] + 1;")
                self.printCode (f"__res = __pointer[__offset];")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("RHS")

                self.printCode ("__parent = stack.back ();")
                self.printCode ("stack.pop_back ();")
                parent = f"({self.stackToVar(node.rhs.lhs.type, '__parent')})"
                lhsStr = f"{parent}->{node.rhs.decl.scopeName}"

                self.printCode (f"{lhsStr} = {lhsStr} + 1;")
                self.printCode (f"__res = {lhsStr};")

            else:
                print ("yikes!")
                exit (1)
        elif node.op.lexeme == "--":
            if isinstance(node.rhs, VariableDeclarationNode) or isinstance(node.rhs, IdentifierExpressionNode) or isinstance(node.rhs, ThisExpressionNode):
                self.printCode (f"{node.rhs.decl.scopeName} = {node.rhs.decl.scopeName} - 1;")
                self.printCode (f"__res = {node.rhs.decl.scopeName};")
            elif isinstance(node.rhs, SubscriptExpressionNode):
                self.printComment ("RHS")
                self.printComment ("Subscript assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("OFFSET")
                node.rhs.offset.accept (self)

                self.printCode ("__offset = stack.back ();")
                self.printCode ("stack.pop_back ();")
                self.printCode ("__pointer = stack.back ();")
                self.printCode ("stack.pop_back ();")

                self.printCode (f"__pointer[__offset] = __pointer[__offset] - 1;")
                self.printCode (f"__res = __pointer[__offset];")
            elif isinstance (node.rhs, MemberAccessorExpressionNode):
                self.printComment ("LHS")
                self.printComment ("Member Accessor Assignment")

                self.printComment ("LHS")
                node.rhs.lhs.accept (self)

                self.printComment ("RHS")

                self.printCode ("__parent = stack.back ();")
                self.printCode ("stack.pop_back ();")
                parent = f"({self.stackToVar(node.rhs.lhs.type, '__parent')})"
                lhsStr = f"{parent}->{node.rhs.decl.scopeName}"

                self.printCode (f"{lhsStr} = {lhsStr} - 1;")
                self.printCode (f"__res = {lhsStr};")
            else:
                print ("yikes!")
                exit (1)
        elif node.op.lexeme == "+":
            self.printCode (f"{res_type_str} __res = {rhs_str};")
        elif node.op.lexeme == "-":
            self.printCode (f"{res_type_str} __res = -{rhs_str};")
        elif node.op.lexeme == "!":
            self.printCode (f"{res_type_str} __res = !{rhs_str};")
        elif node.op.lexeme == "~":
            self.printCode (f"{res_type_str} __res = ~{rhs_str};")

        # push result to the stack
        self.printCode (f"stack.push_back ({res_str});")

        self.indentation -= 1
        self.printCode ("}")

    def visitPostIncrementExpressionNode(self, node):
        self.printComment ("Post-Increment")

        self.printCode ("{")
        self.indentation += 1

        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
            is_int = True
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY
        # OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"{res_type_str} __res = {node.lhs.decl.scopeName};")
            self.printCode (f"{node.lhs.decl.scopeName} = {node.lhs.decl.scopeName} + 1;")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.printComment ("Subscript assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("OFFSET")
            node.lhs.offset.accept (self)

            self.printCode ("__offset = stack.back ();")
            self.printCode ("stack.pop_back ();")
            self.printCode ("__pointer = stack.back ();")
            self.printCode ("stack.pop_back ();")

            self.printCode (f"{res_type_str} __res = __pointer[__offset];")
            self.printCode (f"__pointer[__offset] = __pointer[__offset] + 1;")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.printComment ("Member Accessor Assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("RHS")

            self.printCode ("__parent = stack.back ();")
            self.printCode ("stack.pop_back ();")
            parent = f"({self.stackToVar(node.lhs.lhs.type, '__parent')})"
            lhsStr = f"{parent}->{node.lhs.decl.scopeName}"

            self.printCode (f"{res_type_str} __res = {lhsStr};")
            self.printCode (f"{lhsStr} = {lhsStr} + 1;")

        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode (f"stack.push_back ({res_str});")

        self.indentation -= 1
        self.printCode ("}")

    def visitPostDecrementExpressionNode (self, node):
        self.printComment ("Post-Decrement")

        self.printCode ("{")
        self.indentation += 1

        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
            is_int = True
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY
        # OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        if isinstance(node.lhs, VariableDeclarationNode) or isinstance(node.lhs, IdentifierExpressionNode) or isinstance(node.lhs, ThisExpressionNode):
            self.printCode (f"{res_type_str} __res = {node.lhs.decl.scopeName};")
            self.printCode (f"{node.lhs.decl.scopeName} = {node.lhs.decl.scopeName} - 1;")
        elif isinstance(node.lhs, SubscriptExpressionNode):
            self.printComment ("RHS")
            self.printComment ("Subscript assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("OFFSET")
            node.lhs.offset.accept (self)

            self.printCode ("__offset = stack.back ();")
            self.printCode ("stack.pop_back ();")
            self.printCode ("__pointer = stack.back ();")
            self.printCode ("stack.pop_back ();")

            self.printCode (f"{res_type_str} __res = __pointer[__offset];")
            self.printCode (f"__pointer[__offset] = __pointer[__offset] - 1;")
        elif isinstance (node.lhs, MemberAccessorExpressionNode):
            self.printComment ("LHS")
            self.printComment ("Member Accessor Assignment")

            self.printComment ("LHS")
            node.lhs.lhs.accept (self)

            self.printComment ("RHS")

            self.printCode ("__parent = stack.back ();")
            self.printCode ("stack.pop_back ();")
            parent = f"({self.stackToVar(node.lhs.lhs.type, '__parent')})"
            lhsStr = f"{parent}->{node.lhs.decl.scopeName}"

            self.printCode (f"{res_type_str} __res = {lhsStr};")
            self.printCode (f"{lhsStr} = {lhsStr} - 1;")
        else:
            print ("yikes!")
            exit (1)

        # push result to the stack
        self.printCode (f"stack.push_back ({res_str});")

        self.indentation -= 1
        self.printCode ("}")

    def visitSubscriptExpressionNode (self, node):
        self.printComment ("Subscript Expression")

        self.printCode ("{")
        self.indentation += 1

        self.printComment ("LHS")
        node.lhs.accept (self)
        self.printComment ("OFFSET")
        node.offset.accept (self)

        self.printCode ("__offset = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__pointer = stack.back ();")
        self.printCode ("stack.pop_back ();")

        converted_pointer = self.stackToVar(node.lhs.type,'__pointer')
        converted_offset  = self.stackToVar(node.offset.type, "__offset")

        # simple subscript  
        if node.overloadedFunctionCall == None:
            result = f"({converted_pointer})[{converted_offset}]"
            self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = {result};")
            self.printCode (f"stack.push_back ({self.varToStack(node.type, '__res')});")
        # overloaded function call 
        else:
            self.printComment (f"Using Overloaded Version - {node.overloadedFunctionCall.function.id}")
            # push args in reverse order
            self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = {node.overloadedFunctionCall.decl.scopeName} ({converted_pointer}, {converted_offset});")
            self.printCode (f"stack.push_back ({self.varToStack(node.type,'__res')});")

        self.indentation -= 1
        self.printCode ("}")

    def visitFunctionCallExpressionNode (self, node):
        self.printComment (f"Function Call - {node.decl.signature} -> {node.decl.type}")

        # add scope so we can declare arg variables
        self.printCode ("{")
        self.indentation += 1

        self.printComment ("Arguments")
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        args = []
        for i in range (len(node.args)-1, -1, -1):
            arg = node.args[i]
            # save argument 
            argName = f"__arg{i}"

            self.printCode (f"")
            self.printCode (f"__stackval = stack.back ();")
            self.printCode (f"stack.pop_back ();")
            self.printComment ("Reinterpret from general register")
            self.printCode (f"{self.amyTypeToCPPType (arg.type)} {argName} = {self.stackToVar (arg.type, '__stackval')};")
            args.insert (0, argName)

        # call function
        self.printComment (f"{node.function.id}")
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

        # cast res
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            res_type_str = f"long"
            res_str = f"*reinterpret_cast<long*>(&__res)"
            is_int = True
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            res_type_str = f"double"
            res_str = f"*reinterpret_cast<long*>(&__res)"
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            res_type_str = f"char"
            res_str = f"static_cast<long>(static_cast<unsigned char>(__res))"
        # ARRAY
        # OBJECT
        else:
            res_type_str = f"void*"
            res_str = f"reinterpret_cast<long>(__res)"

        res_type_str = self.amyTypeToCPPType (node.type)

        # function returns void
        if node.decl.type.type == Type.VOID and node.decl.type.arrayDimensions == 0:
            self.printCode (f"{funcname} ({', '.join(args)});")
            # no return
            # but we'll still return something
            self.printComment ("push dummy value - funcall returns void")
            self.printCode (f"stack.push_back (0);")
        # function returns a value
        else:
            self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = {funcname} ({', '.join(args)});")
            # put function's return val on the stack
            self.printCode (f"stack.push_back ({self.varToStack(node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

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

        self.printComment (f"Member Accessor obj.{node.rhs.id}")

        self.printCode ("{")
        self.indentation += 1

        self.printComment ("LHS")
        node.lhs.accept (self)

        self.printComment ("RHS")
        if node.decl.scopeName == "":
            # x = sum([1 if '\n' in s else 0 for s in self.code])
            print (f"[code-gen] [member-accessor] Error: no scope name for '{node.decl.id}' on line {node.lineNumber}")
            print (f"   this could have happened due to a cyclic reference/composition with template classes")
            print (f"   cyclic references are not yet supported")
            exit (1)
        # self.printCode (f"stack.push_back ({node.decl.scopeName})")

        # self.printCode ("__child = stack.back ();")
        # self.printCode ("stack.pop_back ();")
        self.printCode ("__parent = stack.back ();")
        self.printCode ("stack.pop_back ();")
        # lhsStr = f"({self.stackToVar(node.lhs.lhs.type, '__parent')})->{node.lhs.decl.scopeName}"
        self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = ({self.stackToVar(node.lhs.type, '__parent')})->{node.decl.scopeName};")
        self.printCode (f"stack.push_back ({self.varToStack(node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

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

        # add scope so we can declare arg variables
        self.printCode ("{")
        self.indentation += 1

        self.printComment ("Arguments")
        # calc arguments first
        # an argument could be another function call
        # to avoid conflicts with variables, 
        # we will have a separate loop to pop the values
        for arg in node.args:
            arg.accept (self)

        args = ['']
        arg_types = ['']
        for i in range (len(node.args)-1, -1, -1):
            arg = node.args[i]
            # save argument 
            argName = f"__arg{i}"

            self.printCode (f"__stackval = stack.back ();")
            self.printCode (f"stack.pop_back ();")
            self.printComment ("Reinterpret from general register")

            self.printCode (f"{self.amyTypeToCPPType (arg.type)} {argName} = {self.stackToVar (arg.type, '__stackval')};")
            args.append (argName)
            arg_types.append (self.amyTypeToCPPType(arg.type))
        
        # parent object should be on the stack
        # *happens after args incase args uses __obj
        # in another method call
        self.printCode ("__obj = stack.back ();")
        self.printCode ("stack.pop_back ();")
        obj = self.stackToVar(node.decl.parentClass.type, '__obj')

        # determine function_name
        function_name = ""
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
            # get proper dispatch function 
            # Ex: ((void(*)(A*))(a->dtable[0]))
            func_type = f"{node.decl.type}(*)({self.amyTypeToCPPType(node.decl.parentClass.type)}{', '.join(arg_types)})"
            function_name = f"(({func_type})({obj}->dtable[{i}]))"

        # otherwise, normal function call
        else:
            function_name = node.decl.scopeName 

        # call function
        # function returns void
        if node.decl.type.type == Type.VOID and node.decl.type.arrayDimensions == 0:
            self.printCode (f"{function_name} ({obj}{', '.join(args)});")
            self.printComment ("push dummy value - method rtype is void")
            self.printCode ("stack.push_back (0);")
        # function returns a value
        else:
            self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = {function_name} ({obj}{', '.join(args)});")
            self.printCode (f"stack.push_back ({self.varToStack(node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

    def visitThisExpressionNode (self, node):
        self.printCode (f"stack.push_back ({self.varToStack(node.type, '__this')});")

    def visitIdentifierExpressionNode (self, node):
        # INT
        if node.type.type == Type.INT and node.type.arrayDimensions == 0:
            self.printCode (f"stack.push_back (*reinterpret_cast<long*>(&{node.decl.scopeName}));")
        # FLOAT
        elif node.type.type == Type.FLOAT and node.type.arrayDimensions == 0:
            self.printCode (f"stack.push_back (*reinterpret_cast<long*>(&{node.decl.scopeName}));")
        # CHAR
        elif node.type.type == Type.CHAR and node.type.arrayDimensions == 0:
            self.printCode (f"stack.push_back (static_cast<long>(static_cast<unsigned char>({node.decl.scopeName})));")
        # ARRAY or OBJECT
        else:
            self.printCode (f"stack.push_back (reinterpret_cast<long>({node.decl.scopeName}));")

    def visitArrayAllocatorExpressionNode (self, node):
        self.printComment ("Array Allocator")
        self.printCode ("{")
        self.indentation += 1

        node.dimensions[0].accept (self)
        self.printCode (f"__stackval = stack.back ();")
        self.printCode ("stack.pop_back ();")
        # the -1 removes one pointer level and substitutes it for [__stackval] for the allocation
        self.printCode (f"{self.amyTypeToCPPType(node.type)} __res = new {self.amyTypeToCPPType(node.type)[:-1]}[__stackval];")
        self.printCode (f"stack.push_back ({self.varToStack(node.type, '__res')});")

        self.indentation -= 1
        self.printCode ("}")

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
            self.printCode (f"{argName} = stack.back ();")
            self.printCode ("stack.pop_back ();")
            args.insert (0, argName)

        # call function
        ctor_expr = self.varToStack(node.type, f"new {node.decl.parentClass.scopeName} ({', '.join(args)})")
        
        # put function's return val on the stack
        self.printCode (f"stack.push_back ({ctor_expr});")
    
    def visitSizeofExpressionNode(self, node):
        node.rhs.accept (self)
        self.printCode ("__arr = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode ("__res = len (__arr);")
        self.printCode ("stack.push_back (__res);")
    
    def visitFreeExpressionNode (self, node):
        node.rhs.accept (self)
        self.printCode ("__stackval = stack.back ();")
        self.printCode ("stack.pop_back ();")
        self.printCode (f"delete {self.stackToVar (node.rhs.type, '__stackval')};")
        self.printCode ("stack.push_back (0);")

    def visitIntLiteralExpressionNode (self, node):
        self.printComment ("Int Literal")
        self.printCode (f"stack.push_back ({node.value});")

    def visitFloatLiteralExpressionNode (self, node):
        self.printComment ("Float Literal")
        self.printCode (f"{{")
        self.indentation += 1
        self.printCode (f"double float_literal = {node.value};")
        self.printCode (f"stack.push_back (*reinterpret_cast<long*>(&float_literal));")
        self.indentation -= 1
        self.printCode (f"}}")

    def visitCharLiteralExpressionNode (self, node):
        self.printComment ("Char Literal")
        self.printCode (f"stack.push_back (static_cast<long>(static_cast<unsigned char>('{node.value}')));")

    def visitStringLiteralExpressionNode (self, node):
        self.printComment ("String Literal")
        self.printCode ("{")
        self.indentation += 1

        self.printCode (f"char str_literal[] = {node.value};")
        self.printComment ("convert to a heap string")
        # -2 for double quotes
        # +1 for null terminator
        str_len = len(node.value)-2+1
        self.printCode (f"char* str = new char[{str_len}];")
        self.printComment ("copy string to heap allocation")
        self.printCode (f"std::memcpy (str, &str_literal, {str_len});")        

        self.printCode (f"stack.push_back (reinterpret_cast<long> (str));")

        self.indentation -= 1
        self.printCode ("}")

    def visitListConstructorExpressionNode (self, node):
        self.printComment ("Array Constructor")

        self.printCode ("{")
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
            self.printCode (f"long {elemName} = stack.back ();")
            self.printCode ("stack.pop_back ();")

        self.printCode (f"{self.amyTypeToCPPType(node.type)} __list = new {self.amyTypeToCPPType(node.type)[:-1]}[{len(node.elems)}];")

        # add elements to list in correct order
        for i in range(len(node.elems)):
            self.printCode (f"__list[{i}] = {self.stackToVar(node.elems[i].type, f'__elem{i}')};")

        # push array onto stack
        self.printCode (f"stack.push_back ({self.varToStack(node.type,'__list')});")

        self.indentation -= 1
        self.printCode ("}")
        

    def visitNullExpressionNode (self, node):
            
        self.printComment ("Null Literal")
        self.printCode ("stack.push_back (None)")


# ========================================================================