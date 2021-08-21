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
    ('CHAR',     r'\'(\\n|\\t|\\r|\\b|\\f|.)\''),   
    # ('STRING',   r'"[^"\\]*(\\.[^"\\]*)*"'),   
    ('STRING',   r'"([^"]|\\")*"'),   
# Keywords - handled after identifiers are matched
    # ('IF',       r'if'),  
    # ('ELIF',     r'elif'),  
    # ('ELSE',     r'else'),   
    # ('FOR',      r'for'),  
    # ('WHILE',    r'while'),  
    # ('RETURN',   r'return'),  
    # ('BREAK',    r'break'),  
    # ('CONTINUE', r'continue'),  
    # ('FUNCTION', r'function'),  
    # ('CLASS',    r'class'),  
    # ('INHERITS', r'inherits'),  
    # ('PUBLIC',   r'public'),  
    # ('PRIVATE',  r'private'),  
    # ('FIELD',    r'field'),  
    # ('METHOD',   r'method'),  
    # ('CONSTRUCTOR',r'constructor'),  
    # ('NEW',      r'new'),  
    # ('FREE',      r'free'),  
    # ('THIS',     r'this'),  
    # ('SIZEOF',   r'sizeof'),  
    # ('NULL',     r'null'),  
# Built-in types - handled after identifiers are matched
    # ('INTTYPE',   r'int'),  
    # ('FLOATTYPE', r'float'),  
    # ('BOOLTYPE',  r'bool'),  
    # ('CHARTYPE',  r'char'),  
    # ('VOIDTYPE',  r'void'),  
# Identifier
    ('IDENTIFIER',r'[A-Za-z_][A-Za-z_0-9]*'),    # Identifiers
# Operators
    ('LTEMP',    r'\<\:'),
    ('RTEMP',    r'\:\>'),
    ('INCR',     r'\+\+'),
    ('DECR',     r'\-\-'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'\-'),
    ('TIMES',    r'\*'),
    ('DIVIDE',   r'\/'),
    ('MOD',      r'\%'),
    ('LTE',      r'\<\='),
    ('LT',       r'\<'),
    ('GTE',      r'\>\='),
    ('GT',       r'\>'),
    ('EQ',       r'\=\='),
    ('NE',       r'\!\='),
    ('ASSIGN',   r'\='),
    # ('ASSIGNPLUS',  r'\+\='),
    # ('ASSIGNMINUS', r'\-\='),
    # ('ASSIGNTIMES', r'\*\='),
    # ('ASSIGNDIVIDE',r'\/\='),
    # ('ASSIGNMOD',r'\%\='),
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
        elif kind == 'CHAR':
            value = value[1:-1]
        elif kind == 'COMMENT':
            line_start = mo.end()
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
        # match keywords 
        elif kind == 'IDENTIFIER':
            if (lexeme == "if"):
                kind = "IF"
            elif (lexeme == "elif"):
                kind = "ELIF"
            elif (lexeme == "else"):
                kind = "ELSE"
            elif (lexeme == "for"):
                kind = "FOR"
            elif (lexeme == "while"):
                kind = "WHILE"
            elif (lexeme == "return"):
                kind = "RETURN"
            elif (lexeme == "break"):
                kind = "BREAK"
            elif (lexeme == "continue"):
                kind = "CONTINUE"
            elif (lexeme == "function"):
                kind = "FUNCTION"
            elif (lexeme == "class"):
                kind = "CLASS"
            elif (lexeme == "inherits"):
                kind = "INHERITS"
            elif (lexeme == "public"):
                kind = "PUBLIC"
            elif (lexeme == "private"):
                kind = "PRIVATE"
            elif (lexeme == "field"):
                kind = "FIELD"
            elif (lexeme == "virtual"):
                kind = "VIRTUAL"
            elif (lexeme == "method"):
                kind = "METHOD"
            elif (lexeme == "constructor"):
                kind = "CONSTRUCTOR"
            elif (lexeme == "enum"):
                kind = "ENUM"
            elif (lexeme == "template"):
                kind = "TEMPLATE"
            elif (lexeme == "new"):
                kind = "NEW"
            elif (lexeme == "free"):
                kind = "FREE"
            elif (lexeme == "this"):
                kind = "THIS"
            elif (lexeme == "sizeof"):
                kind = "SIZEOF"
            elif (lexeme == "null"):
                kind = "NULL"
            elif (lexeme == "int"):
                kind = "INTTYPE"
            elif (lexeme == "float"):
                kind = "FLOATTYPE"
            elif (lexeme == "bool"):
                kind = "BOOLTYPE"
            elif (lexeme == "char"):
                kind = "CHARTYPE"
            elif (lexeme == "void"):
                kind = "VOIDTYPE"

        tokens +=  [Token(kind, lexeme, value, line_num, column)]
    # add end of file token
    tokens += [Token("END_OF_FILE", "EOF", 0, line_num, len(code) - line_start + 1)]
    return tokens 

# ========================================================================


