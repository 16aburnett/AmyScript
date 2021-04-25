# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

from typing import NamedTuple
from enum import Enum, auto 
import re
import sys

# ========================================================================

class Token(NamedTuple):
    type: str
    lexeme: str
    value: str
    line: int
    column: int

# ========================================================================

token_specification = [
# Comments 
    ('COMMENT',  r'//.*\n?'),      # single line comment 
# literals 
    ('FLOAT',    r'\d*\.\d+'), 
    ('INT',      r'\d+(\.\d*)?'), 
    ('CHAR',     r'\'.\''),   
    ('STRING',   r'"[^"\\]*(\\.[^"\\]*)*"'),   
# Keywords 
    ('IF',       r'if'),  
    ('ELIF',     r'elif'),  
    ('ELSE',     r'else'),   
    ('FOR',      r'for'),  
    ('WHILE',    r'while'),  
    ('RETURN',   r'return'),  
    ('BREAK',    r'break'),  
    ('CONTINUE', r'continue'),  
    ('FUNCTION', r'function'),  
# Identifier
    ('IDENTIFIER',r'[A-Za-z_][A-Za-z_0-9]*'),    # Identifiers
# Operators
    ('INCR',     r'\+\+'),
    ('DECR',     r'\-\-'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'\-'),
    ('TIMES',    r'\*'),
    ('DIVIDE',   r'\/'),
    ('MOD',      r'\%'),
    ('LT',       r'\<'),
    ('LTE',      r'\<\='),
    ('GT',       r'\>'),
    ('GTE',      r'\>\='),
    ('EQ',       r'\=\='),
    ('NE',       r'\!\='),
    ('ASSIGN',   r'\='),
    # ('ASSIGNPLUS',  r'\+\='),
    # ('ASSIGNMINUS', r'\-\='),
    # ('ASSIGNTIMES', r'\*\='),
    # ('ASSIGNDIVIDE',r'\/\='),
    ('LOR',      r'\|\|'),
    ('LAND',     r'\&\&'),
    ('LNOT',     r'\!'),
    ('BNOT',     r'\~'),
    ('DOT',      r'\.'),
# Punctuators 
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('COMMA',    r'\,'),
    ('SEMI',     r'\;'),
# Whitespace 
    ('NEWLINE',  r'\n'),           # Line endings
    ('SKIP',     r'[ \t\r]+'),       # Skip over spaces and tabs
# Everything else - non accepted 
    ('ERROR',    r'.'),          
]

# ========================================================================

def tokenize(code):
    tokens = [] 
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        lexeme = value
        # + 1 bc 1-based indexes for columns 
        column = mo.start() - line_start + 1
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
        tokens +=  [Token(kind, lexeme, value, line_num, column)]
    # add end of file token
    tokens += [Token("END_OF_FILE", "EOF", 0, line_num, len(code) - line_start + 1)]
    return tokens 

# ========================================================================


