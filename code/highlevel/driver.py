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

# tokenize the input 
print ("Tokenizing...")
tokens = lexer.tokenize(statements)

# parse the syntax 
print ("Parsing...")
parser = Parser(tokens, False)
ast = parser.parse()

# Semantic Analysis Phase 1
print ("Analyzing Semantics...")
symbolTableVisitor = SymbolTableVisitor (lines)
# add built-in functions/variables 
inputFunc = FunctionNode (TypeSpecifierNode (Type.STRING, "", None), "input", None, [], None)
printFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "print", None, [], None)
printIntFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "printInt", None, [], None)
printlnFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "println", None, [], None)
symbolTableVisitor.table.insert (inputFunc)
symbolTableVisitor.table.insert (printFunc)
symbolTableVisitor.table.insert (printIntFunc)
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

# CODE GENERATION
codeGenVisitor = CodeGenVisitor (lines, srcFilename, libFilename)
# generate code
ast.accept (codeGenVisitor)

# output generated/compiled code to separate file
file = open(destFilename, "w")
file.write ("".join(codeGenVisitor.code))

print ("Code written to file", destFilename)