# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================


# ========================================================================

class Node:
    def __init__(self, token):
        self.token = token
        self.children = []

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.currentToken = 0
        self.doDebug = False
        self.level = 0

    # <start> -> { <code> }
    def parse(self):
        # tree = self.code ()
        while self.currentToken < len(self.tokens):
            self.code ()
        print ("Valid!")

    def match(self, function, expectedToken):
        if (self.tokens[self.currentToken].type == expectedToken):
            self.currentToken += 1
        else:
            self.error(function, expectedToken)

# ========================================================================
# debug 

    def error(self, function, expectedToken):
        print(f"Error in {function} on line {self.tokens[self.currentToken].line}:{self.tokens[self.currentToken].column}")
        print(f"   expected {expectedToken} but got {self.tokens[self.currentToken]}")
        exit(1)

    def enter (self, name):
        if (not self.doDebug): 
            return
        self.printSpaces(self.level)
        self.level += 1
        if self.currentToken < len(self.tokens):
            print (f"+-{name}: Enter, \tToken == {self.tokens[self.currentToken]}")
        else:
            print (f"+-{name}: Enter, \tToken == None")

    def leave (self, name):
        if (not self.doDebug): 
            return
        self.level -= 1
        self.printSpaces(self.level)
        if self.currentToken < len(self.tokens):
            print (f"+-{name}: Leave, \tToken == {self.tokens[self.currentToken]}")
        else:
            print (f"+-{name}: Leave, \tToken == None")
        
    def printSpaces (self, level):
        while (level > 0):
            level -= 1
            print("| ",end="")

# ========================================================================
# syntax productions 

    # Generic syntax start state 
    # <code> -> <function>
    #        -> <statement>
    #        -> <codeblock>
    #        -> <forloop>
    #        -> <whileloop>
    #        -> <conditional>
    def code (self):
        self.enter ("code")

        # <code> -> <function>
        if (self.tokens[self.currentToken].type == 'FUNCTION'):
            self.function ()
        # <code> -> <codeblock>
        elif (self.tokens[self.currentToken].type == "LBRACE"):
            self.codeblock ()
        # <code> -> <forloop>
        elif (self.tokens[self.currentToken].type == "FOR"):
            self.forloop ()
        # <code> -> <whileloop>
        elif (self.tokens[self.currentToken].type == "WHILE"):
            self.whileloop ()
        # <code> -> <condition>
        elif (self.tokens[self.currentToken].type == "IF"):
            self.conditional ()
        # <code> -> <statement> 
        else:
            self.statement ()

        self.leave ("code")

    # ====================================================================
    # function declaration
    # <function> -> FUNCTION IDENTIFIER <paramlist> <codeblock>
    
    def function (self):
        self.enter ("function")

        self.match ("function", "FUNCTION")
        self.match ("function", "IDENTIFIER")
        self.paramlist()
        self.codeblock()

        self.leave ("function")

    # ====================================================================
    # parameter list for a function declaration
    # <paramlist> -> '(' [ IDENTIFIER [ , IDENTIFIER ] ] ')'

    def paramlist (self): 
        self.enter ("paramlist")

        self.match ("paramlist", "LPAREN")

        lookahead = self.tokens[self.currentToken]
        if lookahead.type == "IDENTIFIER":
            self.match ("paramlist", "IDENTIFIER")

            while self.tokens[self.currentToken].type == "COMMA":
                self.match ("paramlist", "COMMA")
                self.match ("paramlist", "IDENTIFIER")

        self.match ("paramlist", "RPAREN")

        self.leave ("paramlist")

    # ====================================================================
    # codeblock 
    # <codeblock> -> '{' <code> '}'

    def codeblock (self):
        self.enter ("codeblock")

        self.match ("codeblock", "LBRACE")
        self.code ()
        self.match ("codeblock", "RBRACE")

        self.leave ("codeblock")

    # ====================================================================
    # for loop 
    # <forloop> -> for ( <expr> ; <expr> ; <expr> ) <codeblock>

    def forloop (self):
        self.enter ("forloop")

        self.match ("forloop", "FOR")
        self.match ("forloop", "LPAREN")
        self.expression ()
        self.match ("forloop", "SEMI")
        self.expression ()
        self.match ("forloop", "SEMI")
        self.expression ()
        self.match ("forloop", "RPAREN")
        self.codeblock ()

        self.leave ("forloop")

    # ====================================================================
    # while loop 
    # <whileloop> -> while ( <expr> ) <codeblock>

    def whileloop (self):
        self.enter ("forloop")

        self.match ("forloop", "FOR")
        self.match ("forloop", "LPAREN")
        self.expression ()
        self.match ("forloop", "RPAREN")
        self.codeblock ()

        self.leave ("forloop")

    # ====================================================================
    # if statement 
    # <conditional> -> if ( <expr> ) <codeblock>

    def conditional (self):
        self.enter ("conditional")

        self.match ("conditional", "IF")
        self.match ("conditional", "LPAREN")
        self.expression ()
        self.match ("conditional", "RPAREN")
        self.codeblock ()

        self.leave ("conditional")

    # ====================================================================
    # statement
    # <statement> -> <expression> ; 
    #             -> return <expression> ;

    def statement (self):
        self.enter ("statement")

        if self.tokens[self.currentToken].type == "RETURN":
            self.match ("statement", "RETURN")
        self.expression ()
        # could give error message here saying
        # "hey fricker, you missed a semi"
        self.match ("statement", "SEMI")

        self.leave ("statement")

    # ====================================================================
    # expression
    # <expression> -> <tuple>

    def expression (self):
        self.enter ("expression")

        self.tuple ()

        self.leave ("expression")

    # ====================================================================
    # tuple 
    # <tuple> -> <assignexpr> { , <assignexpr> }

    def tuple (self):
        self.enter ("tuple")

        self.assignexpr ()
        while (self.tokens[self.currentToken].type == "COMMA"):
            self.match ("tuple", "COMMA")
            self.assignexpr () 

        self.leave ("tuple")

    # ====================================================================
    # assignment expressions 
    # <assignexpr> -> <logicalOR> [ = <logicalOR> ]
    # this does not work like C++ assignment expressions (a = b = 10) because that
    # requires right recursion which im not sure how to handle yet 
    # with recursive descent and prediction
    # HOWEVER! you can use parentheses to enforce it (a = (b = 10))
    # which should have the same effect

    def assignexpr (self):
        self.enter ("assignexpr")

        self.logicalOR ()
        if self.tokens[self.currentToken].type == "ASSIGN":
            self.match ("assignexpr", "ASSIGN")
            self.logicalOR ()

        self.leave ("assignexpr")

    # ====================================================================
    # logical OR 
    # <logicalOR> -> <logicalAND> { || <logicalAND> }

    def logicalOR (self):
        self.enter ("logicalOR")

        self.logicalAND ()
        while self.tokens[self.currentToken].type == "LOR":
            self.match ("logicalOR", "LOR")
            self.logicalAND ()

        self.leave ("logicalOR")

    # ====================================================================
    # logical AND
    # <logicalAND> -> <equalop> { && <equalop> }

    def logicalAND (self):
        self.enter ("logicalAND")

        self.equalop ()
        while self.tokens[self.currentToken].type == "LAND":
            self.match ("logicalOR", "LAND")
            self.equalop ()

        self.leave ("logicalAND")

    # ====================================================================
    # equal operator
    # <equalop> -> <inequalop> -> { ( == | != ) <inequalop> }

    def equalop (self):
        self.enter ("equalop")

        self.inequalop ()
        while self.tokens[self.currentToken].type == "EQ" \
            or self.tokens[self.currentToken].type == "NE": 
            if self.tokens[self.currentToken].type == "EQ":
                self.match ("equalop", "EQ")
            else:
                self.match ("equalop", "NE")
            self.inequalop ()

        self.leave ("equalop")

    # ====================================================================
    # inequal operator
    # <inequalop> -> <addsub> -> { (  ) <addsub> }

    def inequalop (self):
        self.enter ("inequalop")

        self.addsub ()
        while self.tokens[self.currentToken].type == "LT"   \
            or self.tokens[self.currentToken].type == "LTE" \
            or self.tokens[self.currentToken].type == "GT"  \
            or self.tokens[self.currentToken].type == "GTE":
            self.match ("inequalop", self.tokens[self.currentToken].type)
            self.addsub ()

        self.leave ("inequalop")

    # ====================================================================
    # addition and subtraction 
    # <addsub> -> <term> { ( + | - ) <term> }

    def addsub (self):
        self.enter ("addsub")

        self.term ()
        while  self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS":
            self.match ("addsub", self.tokens[self.currentToken].type)
            self.term ()

        self.leave ("addsub")

    # ====================================================================
    # multiplication / division / remainder (mod)
    # <term> -> <unaryleft> { ( * | / | % ) <unaryleft> }

    def term (self):
        self.enter ("term")

        self.unaryleft ()
        while self.tokens[self.currentToken].type == "TIMES"   \
            or self.tokens[self.currentToken].type == "DIVIDE" \
            or self.tokens[self.currentToken].type == "MOD":
            self.match ("term", self.tokens[self.currentToken].type)
            self.unaryleft ()

        self.leave ("term")

    # ====================================================================
    # unary left operators
    # <unaryleft> -> [ ( ++ | -- | + | - | ! | ~ ) ] <unaryright>

    def unaryleft (self):
        self.enter ("unaryleft")

        if     self.tokens[self.currentToken].type == "INCR"  \
            or self.tokens[self.currentToken].type == "DECR"  \
            or self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS" \
            or self.tokens[self.currentToken].type == "LNOT"  \
            or self.tokens[self.currentToken].type == "BNOT":
            self.match ("unaryleft", self.tokens[self.currentToken].type)
        self.unaryright ()

        self.leave ("unaryleft")

    # ====================================================================
    # unary right operators / funcall / subscript / member accessor 
    # <unaryright> -> <factor> [ ( ++ | -- ) ]
    #              -> <factor> [ '(' <expr> ')' ]
    #              -> <factor> [ '[' <expr> ']' ]
    #              -> <factor> [ . <member> ]

    def unaryright (self):
        self.enter ("unaryright")

        self.factor ()
        # <unaryright> -> <factor> [ ++ ]
        if self.tokens[self.currentToken].type == "INCR":
            self.match ("unaryright", "INCR")
        # <unaryright> -> <factor> [ -- ]
        elif self.tokens[self.currentToken].type == "DECR":
            self.match ("unaryright", "DECR")
        # <unaryright> -> <factor> [ '(' <expr> ')' ]
        elif self.tokens[self.currentToken].type == "LPAREN":
            self.match ("unaryright", "LPAREN")
            self.expression ()
            self.match ("unaryright", "RPAREN")
        # <unaryright> -> <factor> [ '[' <expr> ']' ]
        elif self.tokens[self.currentToken].type == "LBRACKET":
            self.match ("unaryright", "LBRACKET")
            self.expression ()
            self.match ("unaryright", "RBRACKET")
        # <unaryright> -> <factor> [ . <member> ]
        elif self.tokens[self.currentToken].type == "DOT":
            self.match ("unaryright", "DOT")
            self.member ()

        self.leave ("unaryright")

    # ====================================================================
    # member accessor
    # <member> -> IDENTIFIER [ '(' <expr> ')' ]
    def member (self):
        self.enter ("member")

        self.match ("member", "IDENTIFIER")
        if (self.tokens[self.currentToken].type == "LPAREN"):
            self.match ("member", "LPAREN")
            self.expression ()
            self.match ("member", "RPAREN")

        self.leave ("member")

    # ====================================================================
    # parentheses / indentifiers / literals 
    # <factor> -> '(' <expr> ')'
    #          -> INDENTIFIER
    #          -> <literal>

    def factor (self):
        self.enter ("factor")

        if self.tokens[self.currentToken].type == "LPAREN":
            self.match ("factor", "LPAREN")
            self.expression ()
            self.match ("factor", "RPAREN")
        elif self.tokens[self.currentToken].type == "IDENTIFIER":
            self.match ("factor", "IDENTIFIER")
        else:
            self.literal ()

        self.leave ("factor")

    # ====================================================================
    # literals
    # <literal> -> INT
    #           -> FLOAT
    #           -> CHAR
    #           -> STRING

    def literal (self):
        self.enter ("literal")

        if self.tokens[self.currentToken].type == "INT":
            self.match ("literal", "INT")
        elif self.tokens[self.currentToken].type == "FLOAT":
            self.match ("literal", "FLOAT")
        elif self.tokens[self.currentToken].type == "CHAR":
            self.match ("literal", "CHAR")
        elif self.tokens[self.currentToken].type == "STRING":
            self.match ("literal", "STRING")

        self.leave ("literal")

# ========================================================================
