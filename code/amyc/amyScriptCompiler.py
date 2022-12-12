# Amy Script Compiler
# By Amy Burnett
# November 19 2021
# ========================================================================

import sys 
from sys import exit
from enum import Enum
import argparse 

if __name__ == "__main__":
    import preprocessor
    from tokenizer import tokenize
    from amyAST import *
    from parser import Parser
    from visitor import *
    from semanticAnalyzer import *
    from codeGen import CodeGenVisitor
    from codegen_x86 import CodeGenVisitor_x86
    from codegen_python import CodeGenVisitor_python
    from codegen_cpp import CodeGenVisitor_cpp
else:
    from .tokenizer import tokenize
    from .amyAST import *
    from .parser import Parser
    from .visitor import *
    from .semanticAnalyzer import *
    from .codeGen import CodeGenVisitor
    from .codegen_x86 import CodeGenVisitor_x86
    from .codegen_python import CodeGenVisitor_python
    from .codegen_cpp import CodeGenVisitor_cpp


# ========================================================================

TARGET_AMYASM = "amyasm"
TARGET_X86    = "x86"
TARGET_PYTHON = "python"
TARGET_CPP    = "cpp"

BUILTIN_PREFIX = "__builtin__"

class AmyScriptCompiler:

    def __init__(self, mainFilename, otherFilenames, destFilename="a.amy.assembly", debug=False, emitAST=False, emitPreprocessed=False, preprocess=False, target=TARGET_AMYASM):
        self.mainFilename = mainFilename
        self.otherFilenames = otherFilenames
        self.destFilename = destFilename
        self.files = {}
        self.debug = False
        self.ast = ""

        self.emitAST = emitAST
        self.emitPreprocessed = emitPreprocessed
        self.onlyPreprocess = preprocess

        self.astFilename = mainFilename + ".ast"
        self.debugLines = []

        self.target = target

    #---------------------------------------------------------------------

    def compile (self):

        #=== PREPROCESSING =======================================================

        # send through preprocessor
        pp = preprocessor.AmyScriptPreprocessor(mainFilename, otherFilenames, emitPreprocessed=self.emitPreprocessed)
        preprocessedCode = pp.process ()
        self.debugLines = pp.outputLines
        self.files = pp.files 

        lines = preprocessedCode.split ("\n")

        # exit if only preprocessing
        if self.onlyPreprocess:
            return

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
        inputFunc.scopeName = BUILTIN_PREFIX+"input"
        inputFunc.label = inputFunc.scopeName
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
        printFunc.scopeName = BUILTIN_PREFIX+"print__char__1"
        printFunc.label = printFunc.scopeName
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
        printIntFunc.scopeName = BUILTIN_PREFIX+"print__int"
        printIntFunc.label = printIntFunc.scopeName
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
        printFloatFunc.scopeName = BUILTIN_PREFIX+"print__float"
        printFloatFunc.label = printFloatFunc.scopeName
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
        printCharFunc.scopeName = BUILTIN_PREFIX+"print__char"
        printCharFunc.label = printCharFunc.scopeName
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
        printEnumFunc.scopeName = BUILTIN_PREFIX+"print__Enum"
        printEnumFunc.label = printEnumFunc.scopeName
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
        printlnFunc.scopeName = BUILTIN_PREFIX+"println__char__1"
        printlnFunc.label = printlnFunc.scopeName
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
        printIntFunc.scopeName = BUILTIN_PREFIX+"println__int"
        printIntFunc.label = printIntFunc.scopeName
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
        printFloatFunc.scopeName = BUILTIN_PREFIX+"println__float"
        printFloatFunc.label = printFloatFunc.scopeName
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
        printCharFunc.scopeName = BUILTIN_PREFIX+"println__char"
        printCharFunc.label = printCharFunc.scopeName
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
        printEnumFunc.scopeName = BUILTIN_PREFIX+"println__Enum"
        printEnumFunc.label = printEnumFunc.scopeName
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
        printCharFunc.scopeName = BUILTIN_PREFIX+"println"
        printCharFunc.label = printCharFunc.scopeName
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
        # for x86 this directly calls the system exit
        exitFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "exit", None, [], None)
        exitFunc.scopeName = BUILTIN_PREFIX+"exit"
        exitFunc.label = exitFunc.scopeName
        # create signature for node
        exitFunc.signature = "exit()"
        symbolTableVisitor.table.insert (exitFunc, exitFunc.id, Kind.FUNC)

       #  void exit (int exit_status);
        # for x86 this directly calls the system exit
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "exit_status", None)
        exitFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "void", None), "exit", None, [param0], None)
        exitFunc.scopeName = BUILTIN_PREFIX+"exit__int"
        exitFunc.label = exitFunc.scopeName
        # create signature for node
        exitFunc.signature = "exit(int)"
        symbolTableVisitor.table.insert (exitFunc, exitFunc.id, Kind.FUNC)

        #  float float ();
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.FLOAT, "float", None, []), "float", None, [], None)
        builtinFunction.scopeName = BUILTIN_PREFIX+"float"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"intToFloat__int"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"stringToFloat__char__1"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"int"
        builtinFunction.label = builtinFunction.scopeName
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

        #  char char ();
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.CHAR, "char", None, []), "char", None, [], None)
        builtinFunction.scopeName = BUILTIN_PREFIX+"char"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"floatToInt__float"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"stringToInt__char__1"
        builtinFunction.label = builtinFunction.scopeName
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

        #  int charToInt (char);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        builtinFunction = FunctionNode (TypeSpecifierNode (Type.INT, "int", None), "charToInt", None, [param0], None)
        builtinFunction.scopeName = BUILTIN_PREFIX+"charToInt__char"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"string__int"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"string__float"
        builtinFunction.label = builtinFunction.scopeName
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
        builtinFunction.scopeName = BUILTIN_PREFIX+"null"
        builtinFunction.label = builtinFunction.scopeName
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
        # class Object
        # {
        #   public virtual char[] toString ()
        #   {
        #       return "<Object>";
        #   }
        # }
        objClass = ClassDeclarationNode (TypeSpecifierNode (Type.USERTYPE, "Object", None), "Object", None, None, [], [], [], [], [])
        objClass.scopeName = BUILTIN_PREFIX+"__main__Object"
        symbolTableVisitor.table.insert (objClass, "Object", Kind.TYPE)

        # create default object type 
        enumClass = ClassDeclarationNode (TypeSpecifierNode (Type.USERTYPE, "Enum", None), "Enum", None, None, ["Object"], [], [], [], [])
        enumClass.scopeName = BUILTIN_PREFIX+"__main__Enum"
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
            print ("Passes Semantic Analysis")

        # get a string representation of the ast 
        visitor = PrintVisitor ()
        visitor.visitProgramNode (ast)
        astOutput = "".join(visitor.outputstrings)

        # save ast 
        self.ast = astOutput

        if self.emitAST:
            print (f"Writing AST to \"{self.astFilename}\"")
            file = open(self.astFilename, "w")
            file.write (astOutput)

        #=== CODE GENERATION =====================================================

        if target == TARGET_AMYASM:
            codeGenVisitor = CodeGenVisitor (lines)
        elif target == TARGET_X86:
            codeGenVisitor = CodeGenVisitor_x86 (lines)
        elif target == TARGET_PYTHON:
            codeGenVisitor = CodeGenVisitor_python (lines)
        elif target == TARGET_CPP:
            codeGenVisitor = CodeGenVisitor_cpp (lines)

        # generate code
        ast.accept (codeGenVisitor)

        #=== OUTPUT ==============================================================

        destCode = "".join(codeGenVisitor.code)

        # output generated/compiled code to separate file
        print (f"Writing compiled code to \"{self.destFilename}\"")
        file = open(self.destFilename, "w")
        file.write (destCode)

        return destCode

        #=== END =================================================================


# ========================================================================

if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description="Tests argparse")

    argparser.add_argument(dest="sourceFiles", nargs="+", help="source files to compile (first file should be the main file)")
    argparser.add_argument("-o", "--outputFilename", dest="outputFilename", help="name of the outputted compiled file")
    argparser.add_argument("--emitPreprocessed", dest="emitPreprocessed", action="store_true", help="output the preprocessed code")
    argparser.add_argument("--emitAST", dest="emitAST", action="store_true", help="output the ast")
    argparser.add_argument("--preprocess", dest="preprocess", action="store_true", help="only run preprocessor")
    argparser.add_argument("--target", nargs=1, dest="target", help="specifies the target language to compile to [default amyasm] (amyasm | x86 | python | cpp)")

    args = argparser.parse_args()

    mainFilename = args.sourceFiles[0]
    otherFilenames = args.sourceFiles[1:]
    destFilename = "a.amy.assembly"
    if args.outputFilename:
        destFilename = args.outputFilename

    # ensure valid target
    if args.target == None or args.target[0] == "amyasm": # Default 
        target=TARGET_AMYASM
    elif args.target[0] == "x86":  # Intel x86
        target=TARGET_X86
    elif args.target[0] == "python": # transpile to python
        target=TARGET_PYTHON
    elif args.target[0] == "cpp": # transpile to python
        target=TARGET_CPP
    else: # Invalid/unknown target
        print (f"Unknown target {args.target}")
        exit (1)

    # output compilation info 
    print ("target      :", target)
    print ("destFilename:", destFilename)

    # compile code 
    compiler = AmyScriptCompiler (
        mainFilename, 
        otherFilenames, 
        destFilename=destFilename,
        emitAST=args.emitAST, 
        emitPreprocessed=args.emitPreprocessed, 
        preprocess=args.preprocess,
        target=target
    )
    destCode = compiler.compile ()



