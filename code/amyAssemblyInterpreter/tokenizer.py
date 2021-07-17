# The Amy Programming Language
# By Amy Burnett
# November 5 2020
##########################################################################

from typing import NamedTuple
import re
import sys

##########################################################################

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

token_specification = [
# Comments 
    ('COMMENT',  r'//.*\n?'),      # single line comment 
# literals 
    ('FLOAT',    r'\d*\.\d+'), 
    ('INT',      r'\d+(\.\d*)?'), 
    ('CHAR',     r'\'.\''),   
    ('STRING',   r'"[^"\\]*(\\.[^"\\]*)*"'),   
# Keywords 
# Identifier
    ('ID',       r'[A-Za-z_][A-Za-z_0-9]*'),    # Identifiers
# Operators
# Punctuators 
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('COMMA',    r'\,'),
# Whitespace 
    ('NEWLINE',  r'\n'),           # Line endings
    ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
# Everything else - non accepted 
    ('ERROR',    r'.'),          
]

def tokenize(code):
    tokens = [] 
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'INT':
            value = int(value)
        elif kind == 'FLOAT':
            value = float(value)
        elif kind == 'COMMENT':
            line_num += 1
            continue 
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'ERROR':
            pass
        tokens +=  [Token(kind, value, line_num, column)]
    return tokens 


statements = "".join(sys.stdin.readlines())

for token in tokenize(statements):
    print(token)