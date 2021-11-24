# Amy Script Compiler
# By Amy Burnett
# November 19 2021
# ========================================================================

import sys 
from sys import exit
from enum import Enum

if __name__ == "__main__":
    import preprocessor
    from tokenizer import tokenize
    from amyAST import *
    from parser import Parser
    from visitor import *
    from semanticAnalyzer import *
    from codeGen import CodeGenVisitor
else:
    from .tokenizer import tokenize
    from .amyAST import *
    from .parser import Parser
    from .visitor import *
    from .semanticAnalyzer import *
    from .codeGen import CodeGenVisitor


# ========================================================================

class AmyScriptCompiler:

    def __init__(self, mainFilename, otherFilenames, debug=False, emitAST=False):
        self.mainFilename = mainFilename
        self.otherFilenames = otherFilenames
        self.files = {}
        self.debug = False
        self.ast = ""
        self.emitAST = emitAST
        self.astFilename = mainFilename + ".ast"
        self.debugLines = []

    #---------------------------------------------------------------------

    def compile (self):

        #=== PREPROCESSING =======================================================

        # send through preprocessor
        pp = preprocessor.AmyScriptPreprocessor(mainFilename, otherFilenames)
        # pp.outputProcessed = True
        preprocessedCode = pp.process ()
        self.debugLines = pp.outputLines
        self.files = pp.files 

        lines = preprocessedCode.split ("\n")

        #=== TOKENIZATION ========================================================

        if (self.debug):
            print ("Tokenizing...")
        tokens = tokenize(preprocessedCode, self.mainFilename, self.debugLines)

        #=== PARSING =============================================================

        if (self.debug):
            print ("Parsing...")    
        parser = Parser(tokens, lines, False)
        ast = parser.parse()

        #=== SEMANTIC ANALYSIS ===================================================

        if (self.debug):
            print ("Analyzing Semantics...")
        symbolTableVisitor = SymbolTableVisitor (lines)

        # Add built-in functions/variables 

        #  char[] input ();
        inputFunc = FunctionNode (TypeSpecifierNode (Type.CHAR, "char", None), "input", None, [], None)
        inputFunc.scopeName = "input"
        inputFunc.type.arrayDimensions += 1
        # create signature for node
        signature = [f"{inputFunc.id}("]
        if len(inputFunc.params) > 0:
            signature += [inputFunc.params[0].type.__str__()]
        for i in range(1, len(inputFunc.params)):
            signature += [f", {inputFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        inputFunc.signature = signature
        symbolTableVisitor.table.insert (inputFunc, inputFunc.id, Kind.FUNC)

        #  void print (char[] str);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
        param0.type.arrayDimensions += 1
        printFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "print", None, [param0], None)
        printFunc.scopeName = "print__char__1"
        # create signature for node
        signature = [f"{printFunc.id}("]
        if len(printFunc.params) > 0:
            signature += [printFunc.params[0].type.__str__()]
        for i in range(1, len(printFunc.params)):
            signature += [f", {printFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printFunc.signature = signature
        symbolTableVisitor.table.insert (printFunc, printFunc.id, Kind.FUNC)

        #  void print (int intToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "intToPrint", None)
        printIntFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "print", None, [param0], None)
        printIntFunc.scopeName = "print__int"
        # create signature for node
        signature = [f"{printIntFunc.id}("]
        if len(printIntFunc.params) > 0:
            signature += [printIntFunc.params[0].type.__str__()]
        for i in range(1, len(printIntFunc.params)):
            signature += [f", {printIntFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printIntFunc.signature = signature
        symbolTableVisitor.table.insert (printIntFunc, printIntFunc.id, Kind.FUNC)

        #  void print (float floatToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
        printFloatFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "print", None, [param0], None)
        printFloatFunc.scopeName = "print__float"
        # create signature for node
        signature = [f"{printFloatFunc.id}("]
        if len(printFloatFunc.params) > 0:
            signature += [printFloatFunc.params[0].type.__str__()]
        for i in range(1, len(printFloatFunc.params)):
            signature += [f", {printFloatFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printFloatFunc.signature = signature
        symbolTableVisitor.table.insert (printFloatFunc, printFloatFunc.id, Kind.FUNC)

        #  void print (char c);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        printCharFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "print", None, [param0], None)
        printCharFunc.scopeName = "print__char"
        # create signature for node
        signature = [f"{printCharFunc.id}("]
        if len(printCharFunc.params) > 0:
            signature += [printCharFunc.params[0].type.__str__()]
        for i in range(1, len(printCharFunc.params)):
            signature += [f", {printCharFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printCharFunc.signature = signature
        symbolTableVisitor.table.insert (printCharFunc, printCharFunc.id, Kind.FUNC)

        #  void print (Enum e);
        param0 = ParameterNode(TypeSpecifierNode (Type.USERTYPE, "Enum", None), "e", None)
        printEnumFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "print", None, [param0], None)
        printEnumFunc.scopeName = "print__Enum"
        # create signature for node
        signature = [f"{printEnumFunc.id}("]
        if len(printEnumFunc.params) > 0:
            signature += [printEnumFunc.params[0].type.__str__()]
        for i in range(1, len(printEnumFunc.params)):
            signature += [f", {printEnumFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printEnumFunc.signature = signature
        symbolTableVisitor.table.insert (printEnumFunc, printEnumFunc.id, Kind.FUNC)

        #  void println (char[] str);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
        param0.type.arrayDimensions += 1
        printlnFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [param0], None)
        printlnFunc.scopeName = "println__char__1"
        # create signature for node
        signature = [f"{printlnFunc.id}("]
        if len(printlnFunc.params) > 0:
            signature += [printlnFunc.params[0].type.__str__()]
        for i in range(1, len(printlnFunc.params)):
            signature += [f", {printlnFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printlnFunc.signature = signature
        symbolTableVisitor.table.insert (printlnFunc, printlnFunc.id, Kind.FUNC)

        #  void println (int intToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "intToPrint", None)
        printIntFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [param0], None)
        printIntFunc.scopeName = "println__int"
        # create signature for node
        signature = [f"{printIntFunc.id}("]
        if len(printIntFunc.params) > 0:
            signature += [printIntFunc.params[0].type.__str__()]
        for i in range(1, len(printIntFunc.params)):
            signature += [f", {printIntFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printIntFunc.signature = signature
        symbolTableVisitor.table.insert (printIntFunc, printIntFunc.id, Kind.FUNC)

        #  void println (float floatToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
        printFloatFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [param0], None)
        printFloatFunc.scopeName = "println__float"
        # create signature for node
        signature = [f"{printFloatFunc.id}("]
        if len(printFloatFunc.params) > 0:
            signature += [printFloatFunc.params[0].type.__str__()]
        for i in range(1, len(printFloatFunc.params)):
            signature += [f", {printFloatFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printFloatFunc.signature = signature
        symbolTableVisitor.table.insert (printFloatFunc, printFloatFunc.id, Kind.FUNC)

        #  void println (char c);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        printCharFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [param0], None)
        printCharFunc.scopeName = "println__char"
        # create signature for node
        signature = [f"{printCharFunc.id}("]
        if len(printCharFunc.params) > 0:
            signature += [printCharFunc.params[0].type.__str__()]
        for i in range(1, len(printCharFunc.params)):
            signature += [f", {printCharFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printCharFunc.signature = signature
        symbolTableVisitor.table.insert (printCharFunc, printCharFunc.id, Kind.FUNC)

        #  void println (Enum e);
        param0 = ParameterNode(TypeSpecifierNode (Type.USERTYPE, "Enum", None), "e", None)
        printEnumFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [param0], None)
        printEnumFunc.scopeName = "println__Enum"
        # create signature for node
        signature = [f"{printEnumFunc.id}("]
        if len(printEnumFunc.params) > 0:
            signature += [printEnumFunc.params[0].type.__str__()]
        for i in range(1, len(printEnumFunc.params)):
            signature += [f", {printEnumFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printEnumFunc.signature = signature
        symbolTableVisitor.table.insert (printEnumFunc, printEnumFunc.id, Kind.FUNC)

        #  void println ();
        printCharFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "println", None, [], None)
        printCharFunc.scopeName = "println"
        # create signature for node
        signature = [f"{printCharFunc.id}("]
        if len(printCharFunc.params) > 0:
            signature += [printCharFunc.params[0].type.__str__()]
        for i in range(1, len(printCharFunc.params)):
            signature += [f", {printCharFunc.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        printCharFunc.signature = signature
        symbolTableVisitor.table.insert (printCharFunc, printCharFunc.id, Kind.FUNC)

        #  void exit ();
        exitFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "exit", None, [], None)
        exitFunc.scopeName = "exit"
        # create signature for node
        exitFunc.signature = "exit()"
        symbolTableVisitor.table.insert (exitFunc, exitFunc.id, Kind.FUNC)

        #  float float ();
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.FLOAT, "float", None, []), "float", None, [], None)
        builtinFunction.scopeName = "float"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  float intToFloat (int val);
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "val", None)
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.FLOAT, "float", None), "intToFloat", None, [param0], None)
        builtinFunction.scopeName = "intToFloat__int"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  float stringToFloat (char[]);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        param0.type.arrayDimensions = 1
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.FLOAT, "float", None), "stringToFloat", None, [param0], None)
        builtinFunction.scopeName = "stringToFloat__char__1"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  int int ();
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.INT, "int", None, []), "int", None, [], None)
        builtinFunction.scopeName = "int"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  int floatToInt (float);
        param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.INT, "int", None), "floatToInt", None, [param0], None)
        builtinFunction.scopeName = "floatToInt__float"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  int stringToInt (char[]);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        param0.type.arrayDimensions = 1
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.INT, "int", None), "stringToInt", None, [param0], None)
        builtinFunction.scopeName = "stringToInt__char__1"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  char[] string (int);
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "val", None)
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.CHAR, "char", None), "string", None, [param0], None)
        builtinFunction.type.arrayDimensions = 1
        builtinFunction.scopeName = "string__int"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  char[] string (float);
        param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.CHAR, "char", None), "string", None, [param0], None)
        builtinFunction.type.arrayDimensions = 1
        builtinFunction.scopeName = "string__float"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)

        #  null null ();
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.NULL, "null", None, []), "null", None, [], None)
        builtinFunction.scopeName = "null"
        # create signature for node
        signature = [f"{builtinFunction.id}("]
        if len(builtinFunction.params) > 0:
            signature += [builtinFunction.params[0].type.__str__()]
        for i in range(1, len(builtinFunction.params)):
            signature += [f", {builtinFunction.params[i].type.__str__()}"]
        signature += [")"]
        signature = "".join(signature)
        builtinFunction.signature = signature
        symbolTableVisitor.table.insert (builtinFunction, builtinFunction.id, Kind.FUNC)


        # LIBRARY OBJECTS

        # create default object type 
        objClass = ClassDeclarationNode (TypeSpecifierNode (Type.USERTYPE, "Object", None), "Object", None, None, [], [], [], [], [])
        objClass.scopeName = "__main__Object"
        symbolTableVisitor.table.insert (objClass, "Object", Kind.TYPE)

        # create default object type 
        enumClass = ClassDeclarationNode (TypeSpecifierNode (Type.USERTYPE, "Enum", None), "Enum", None, None, ["Object"], [], [], [], [])
        enumClass.scopeName = "__main__Enum"
        symbolTableVisitor.table.insert (enumClass, "Enum", Kind.TYPE)


        # Check AST
        # checks for 
        # - undeclared vars 
        # - redeclared vars 
        # - matching operand types 
        ast.accept (symbolTableVisitor)
        # ensure it was successful 
        if (not symbolTableVisitor.wasSuccessful):
            exit (1)

        # Reaches Here if the code is valid
        if (self.debug):
            print ("Valid!")

        # get a string representation of the ast 
        visitor = PrintVisitor ()
        visitor.visitProgramNode (ast)
        astOutput = "".join(visitor.outputstrings)

        # save ast 
        self.ast = astOutput

        # file = open(astFilename, "w")
        # file.write (astOutput)

        #=== CODE GENERATION =====================================================

        codeGenVisitor = CodeGenVisitor (lines)
        # generate code
        ast.accept (codeGenVisitor)

        #=== OUTPUT ==============================================================

        return "".join(codeGenVisitor.code)

        #=== END =================================================================


# ========================================================================

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<file-name> {<extra-filenames>}")
        exit()

    # get all filenames 
    # first file is main file 
    mainFilename = sys.argv[1]
    destFilename = mainFilename + ".assembly"
    # get rest of files if they are provided 
    otherFilenames = []
    for i in range(2, len(sys.argv)):
        otherFilenames += [sys.argv[i]]

    # compile code 
    compiler = AmyScriptCompiler (mainFilename, otherFilenames)
    destCode = compiler.compile ()

    # output generated/compiled code to separate file
    print (f"Writing compiled code to \"{destFilename}\"")
    file = open(destFilename, "w")
    file.write (destCode)


