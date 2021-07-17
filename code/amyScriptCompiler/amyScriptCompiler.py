# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

import sys 

if __name__ == "__main__":
    from tokenizer import tokenize
    from parser import Parser
    from ast import *
    from visitor import *
    from semanticAnalyzer import SymbolTableVisitor
    from codeGen import CodeGenVisitor
else:
    from .tokenizer import tokenize
    from .parser import Parser
    from .ast import *
    from .visitor import *
    from .semanticAnalyzer import SymbolTableVisitor
    from .codeGen import CodeGenVisitor


# ========================================================================

class AmyScriptCompiler:

    def __init__(self):
        self.debug = False
        self.ast = ""

    #---------------------------------------------------------------------

    def compile (self, code):

        lines = code.split ("\n")

        statements = code

        #=== TOKENIZATION ========================================================

        if (self.debug):
            print ("Tokenizing...")
        tokens = tokenize(statements)

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
        symbolTableVisitor.table.insert (inputFunc)

        #  void print (char[] str);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
        param0.type.arrayDimensions += 1
        printFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "print", None, [param0], None)
        printFunc.scopeName = "print"
        symbolTableVisitor.table.insert (printFunc)

        #  void printInt (int intToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "intToPrint", None)
        printIntFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printInt", None, [param0], None)
        printIntFunc.scopeName = "printInt"
        symbolTableVisitor.table.insert (printIntFunc)

        #  void printFloat (float floatToPrint);
        param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
        printFloatFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printFloat", None, [param0], None)
        printFloatFunc.scopeName = "printFloat"
        symbolTableVisitor.table.insert (printFloatFunc)

        #  void printChar (char c);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
        printCharFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printChar", None, [param0], None)
        printCharFunc.scopeName = "printChar"
        symbolTableVisitor.table.insert (printCharFunc)

        #  void println (char[] str);
        param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
        param0.type.arrayDimensions += 1
        printlnFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "println", None, [param0], None)
        printlnFunc.scopeName = "println"
        symbolTableVisitor.table.insert (printlnFunc)

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

    # if len(sys.argv) < 2:
    #     print("Please provide a file_name")
    #     exit()

    # determine what file to read from
    file = sys.stdin
    srcFilename = ""
    astFilename = "output.amy.ast"
    destFilename = "output.amy.assembly"
    if (len(sys.argv) == 2):
        srcFilename = sys.argv[1]
        file = open(srcFilename)
        astFilename = srcFilename + ".ast"
        destFilename = srcFilename + ".assembly"
        
    srcCode = file.readlines ()

    compiler = AmyScriptCompiler ()
    destCode = compiler.compile ("".join(srcCode))

    # output generated/compiled code to separate file
    print (f"Writing compiled code to {destFilename}")
    file = open(destFilename, "w")
    file.write (destCode)


