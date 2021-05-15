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

# ========================================================================

# determine what file to read from
file = sys.stdin
if (len(sys.argv) == 2):
    file = open(sys.argv[1])

statements = "".join(file.readlines())

# tokenize the input 
tokens = lexer.tokenize(statements)

# parse the syntax 
parser = Parser(tokens, True)
ast = parser.parse()

# Semantic Analysis Phase 1
symbolTableVisitor = SymbolTableVisitor ()
# add built-in functions/variables 
inputFunc = FunctionNode (TypeSpecifierNode (Type.STRING, "", None), "input", None, [], None)
printFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "print", None, [], None)
printlnFunc = FunctionNode (TypeSpecifierNode (Type.VOID, "", None), "println", None, [], None)
symbolTableVisitor.table.insert (inputFunc)
symbolTableVisitor.table.insert (printFunc)
symbolTableVisitor.table.insert (printlnFunc)

# Check AST
# checks for 
# - undeclared vars 
# - redeclared vars 
# - matching operand types 
ast.accept (symbolTableVisitor)
# ensure it was successful 
# if (not symbolTableVisitor.wasSuccessful):
#     exit (1)

# Reaches Here if the code is valid
print ("Valid!")

# get a string representation of the ast 
visitor = PrintVisitor ()
visitor.visitProgramNode (ast)
output = "".join(visitor.outputstrings)

print (output)
