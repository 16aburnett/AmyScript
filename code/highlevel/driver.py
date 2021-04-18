# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

import sys 

import lexer
from parser import Parser

# ========================================================================

statements = "".join(sys.stdin.readlines())

# tokenize the input 
tokens = lexer.tokenize(statements)

# parse the syntax 
parser = Parser(tokens)
parser.doDebug = False
ast = parser.parse()

def treeprint(tree, spaces):
    for i in range(spaces):
        print("| ",end="")
    print(tree.name, end=" -> ") 
    for child in tree.children:
        print(child.name,end=" ")
    print("")
    for child in tree.children:
        treeprint(child, spaces+1)


treeprint(ast, 0)