from typing import NamedTuple
import re

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
    ("IF",       r'if'),
    ("WHILE",    r'while'),
    ("FOR",      r'for'),
    ("RETURN",   r'return'),
# Identifier
    ('ID',       r'[A-Za-z_][A-Za-z_0-9]*'),    # Identifiers
# Operators
    ('PLUS',     r'\+'),
    ('MINUS',    r'\-'),
    ('MULT',     r'\*'),
    ('DIVIDE',   r'\/'),
    ('MOD',      r'\%'),
    ('EQUAL',    r'=='),
    ('NEQUAL',   r'!='),
    ('LT',       r'\<'),
    ('LTE',      r'\<='),
    ('GT',       r'\>'),
    ('GTE',      r'\>='),
    ('ASSIGN',   r'='),
# Punctuators 
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SEMI',     r';'),           # Statement terminator
# Whitespace 
    ('NEWLINE',  r'\n'),           # Line endings
    ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
# Everything else - non accepted 
    ('ERROR', r'.'),          
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
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
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

statements = '''
void main() 
{
    // this is a comment 
    if(name == "Amy")
    {
        print("hello beautiful");
    }
    return 0; 
}
//This is also a comment'''

for token in tokenize(statements):
    print(token)