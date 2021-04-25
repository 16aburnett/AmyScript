# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

import sys 

import lexer
from parser import Parser
from visitor import *

# ========================================================================

# determine what file to read from
file = sys.stdin
if (len(sys.argv) == 2):
    file = open(sys.argv[1])

statements = "".join(file.readlines())

# tokenize the input 
tokens = lexer.tokenize(statements)

# parse the syntax 
parser = Parser(tokens, False)
ast = parser.parse()

visitor = PrintVisitor ()
visitor.visitProgramNode (ast)

output = "".join(visitor.outputstrings)

print (output)
