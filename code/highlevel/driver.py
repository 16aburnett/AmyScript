# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

import sys 

import lexer
from parser import Parser
from ast import *
from visitor import *
from semanticAnalyzer import SymbolTableVisitor
from codeGen import CodeGenVisitor

# ========================================================================

# determine what file to read from
file = sys.stdin
srcFilename = ""
astFilename = "output.amy.ast"
destFilename = "output.amy.assembly"
libFilename = "AmyScriptLib.amy"
if (len(sys.argv) == 2):
    srcFilename = sys.argv[1]
    file = open(srcFilename)
    astFilename = srcFilename + ".ast"
    destFilename = srcFilename + ".assembly"

lines = file.readlines ()

statements = "".join(lines)

#=== TOKENIZATION ========================================================

print ("Tokenizing...")
tokens = lexer.tokenize(statements)

#=== PARSING =============================================================

print ("Parsing...")
parser = Parser(tokens, False)
ast = parser.parse()

#=== SEMANTIC ANALYSIS ===================================================

print ("Analyzing Semantics...")
symbolTableVisitor = SymbolTableVisitor (lines)

# Add built-in functions/variables 

#  char[] input ();
inputFunc = FunctionNode (TypeSpecifierNode (Type.CHAR, "char", None), "input", None, [], None)
inputFunc.type.arrayDimensions += 1
symbolTableVisitor.table.insert (inputFunc)

#  void print (char[] str);
param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
param0.type.arrayDimensions += 1
printFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "print", None, [param0], None)
symbolTableVisitor.table.insert (printFunc)

#  void printInt (int intToPrint);
param0 = ParameterNode(TypeSpecifierNode (Type.INT, "int", None), "intToPrint", None)
printIntFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printInt", None, [param0], None)
symbolTableVisitor.table.insert (printIntFunc)

#  void printFloat (float floatToPrint);
param0 = ParameterNode(TypeSpecifierNode (Type.FLOAT, "float", None), "val", None)
printFloatFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printFloat", None, [param0], None)
symbolTableVisitor.table.insert (printFloatFunc)

#  void printChar (char c);
param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "val", None)
printCharFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printChar", None, [param0], None)
symbolTableVisitor.table.insert (printCharFunc)

#  void println (char[] str);
param0 = ParameterNode(TypeSpecifierNode (Type.CHAR, "char", None), "str", None)
param0.type.arrayDimensions += 1
printlnFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "println", None, [param0], None)
symbolTableVisitor.table.insert (printlnFunc)

# sizeof function for arrays
sizeofFunc = FunctionNode (TypeSpecifierNode (Type.INT, "", None), "sizeof", None, [], None)
symbolTableVisitor.table.insert (sizeofFunc)

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
print ("Valid!")

# get a string representation of the ast 
visitor = PrintVisitor ()
visitor.visitProgramNode (ast)
astOutput = "".join(visitor.outputstrings)

file = open(astFilename, "w")
file.write (astOutput)

#=== CODE GENERATION =====================================================

codeGenVisitor = CodeGenVisitor (lines, srcFilename, libFilename)
# generate code
ast.accept (codeGenVisitor)

# output generated/compiled code to separate file
file = open(destFilename, "w")
file.write ("".join(codeGenVisitor.code))

print ("Code written to file", destFilename)


#=== END =================================================================