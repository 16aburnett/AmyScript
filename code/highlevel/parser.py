# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================


# ========================================================================

class Node:
    def __init__(self, name, token=None):
        self.name = name
        self.token = token
        self.children = []

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.currentToken = 0
        self.doDebug = False
        self.level = 0

    # <start> -> <code> { <code> }
    def parse(self):
        tree = Node("source")
        while self.currentToken < len(self.tokens):
            tree.children += [self.codeunit ()]
        print ("Valid!")
        return tree

    def match(self, function, expectedToken, additional=""):
        if (self.tokens[self.currentToken].type == expectedToken):
            self.currentToken += 1
        else:
            self.error(function, expectedToken, additional)

# ========================================================================
# debug 

    def error(self, function, expectedToken, additional=""):
        print(f"Error in {function} on line {self.tokens[self.currentToken].line}:{self.tokens[self.currentToken].column}")
        print(f"   expected {expectedToken} but got {self.tokens[self.currentToken].type}")
        if additional != "":
            print(f"   -> {additional}")
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
    # <codeunit> -> <function>
    #        -> <statement>
    #        -> <codeblock>
    #        -> <forloop>
    #        -> <whileloop>
    #        -> <conditional>
    def codeunit (self):
        self.enter ("codeunit")

        tree = Node("codeunit")

        # <codeunit> -> <function>
        if (self.tokens[self.currentToken].type == 'FUNCTION'):
            tree.children += [self.function ()]
        # <codeunit> -> <codeblock>
        elif (self.tokens[self.currentToken].type == "LBRACE"):
            tree.children += [self.codeblock ()]
        # <codeunit> -> <forloop>
        elif (self.tokens[self.currentToken].type == "FOR"):
            tree.children += [self.forloop ()]
        # <codeunit> -> <whileloop>
        elif (self.tokens[self.currentToken].type == "WHILE"):
            tree.children += [self.whileloop ()]
        # <codeunit> -> <condition>
        elif (self.tokens[self.currentToken].type == "IF"):
            tree.children += [self.conditional ()]
        # <codeunit> -> <statement> 
        else:
            tree.children += [self.statement ()]

        self.leave ("codeunit")

        return tree

    # ====================================================================
    # function declaration
    # <function> -> FUNCTION IDENTIFIER <paramlist> <codeblock>
    
    def function (self):
        self.enter ("function")

        tree = Node("function")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("function", "FUNCTION")
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("function", "IDENTIFIER")
        tree.children += [self.paramlist()]
        tree.children += [self.codeblock()]

        self.leave ("function")

        return tree

    # ====================================================================
    # parameter list for a function declaration
    # <paramlist> -> '(' [ IDENTIFIER [ , IDENTIFIER ] ] ')'

    def paramlist (self): 
        self.enter ("paramlist")

        tree = Node("paramlist")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("paramlist", "LPAREN")

        if self.tokens[self.currentToken].type == "IDENTIFIER":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("paramlist", "IDENTIFIER")

            while self.tokens[self.currentToken].type == "COMMA":
                tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
                self.match ("paramlist", "COMMA")
                tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
                self.match ("paramlist", "IDENTIFIER")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("paramlist", "RPAREN")

        self.leave ("paramlist")

        return tree

    # ====================================================================
    # codeblock 
    # <codeblock> -> '{' { <code> } '}'

    def codeblock (self):
        self.enter ("codeblock")

        tree = Node("codeblock")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("codeblock", "LBRACE")
        while self.tokens[self.currentToken].type != "RBRACE":
            tree.children += [self.codeunit ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("codeblock", "RBRACE")

        self.leave ("codeblock")

        return tree

    # ====================================================================
    # for loop 
    # <forloop> -> for ( <expr> ; <expr> ; <expr> ) <codeblock>

    def forloop (self):
        self.enter ("forloop")

        tree = Node("forloop")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "FOR")
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "LPAREN")
        tree.children += [self.expression ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "SEMI")
        tree.children += [self.expression ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "SEMI")
        tree.children += [self.expression ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "RPAREN")
        tree.children += [self.codeblock ()]

        self.leave ("forloop")

        return tree

    # ====================================================================
    # while loop 
    # <whileloop> -> while ( <expr> ) <codeblock>

    def whileloop (self):
        self.enter ("forloop")

        tree = Node("whileloop")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "FOR")
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "LPAREN")
        tree.children += [self.expression ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("forloop", "RPAREN")
        tree.children += [self.codeblock ()]

        self.leave ("forloop")

        return tree

    # ====================================================================
    # if statement 
    # <conditional> -> if ( <expr> ) <codeblock>

    def conditional (self):
        self.enter ("conditional")

        tree = Node("conditional")

        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("conditional", "IF")
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("conditional", "LPAREN")
        tree.children += [self.expression ()]
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("conditional", "RPAREN")
        tree.children += [self.codeblock ()]

        self.leave ("conditional")

        return tree

    # ====================================================================
    # statement
    # <statement> -> <expression> ; 
    #             -> return <expression> ;

    def statement (self):
        self.enter ("statement")

        tree = Node("statement")

        if self.tokens[self.currentToken].type == "RETURN":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("statement", "RETURN")
        tree.children += [self.expression ()]
        # could give error message here saying
        # "hey fricker, you missed a semi"
        tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
        self.match ("statement", "SEMI", "You should add a semicolon")

        self.leave ("statement")

        return tree

    # ====================================================================
    # expression
    # <expression> -> <tuple>

    def expression (self):
        self.enter ("expression")

        tree = Node("expression")
        
        tree.children += [self.tuple ()]

        self.leave ("expression")

        return tree

    # ====================================================================
    # tuple 
    # <tuple> -> <assignexpr> { , <assignexpr> }

    def tuple (self):
        self.enter ("tuple")

        tree = Node("tuple")

        tree.children += [self.assignexpr ()]
        while (self.tokens[self.currentToken].type == "COMMA"):
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("tuple", "COMMA")
            tree.children += [self.assignexpr ()]

        self.leave ("tuple")

        return tree

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

        tree = Node("assignexpr")

        tree.children += [self.logicalOR ()]
        if self.tokens[self.currentToken].type == "ASSIGN":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("assignexpr", "ASSIGN")
            tree.children += [self.logicalOR ()]

        self.leave ("assignexpr")

        return tree

    # ====================================================================
    # logical OR 
    # <logicalOR> -> <logicalAND> { || <logicalAND> }

    def logicalOR (self):
        self.enter ("logicalOR")

        tree = Node("logicalOR")

        tree.children += [self.logicalAND ()]
        while self.tokens[self.currentToken].type == "LOR":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("logicalOR", "LOR")
            tree.children += [self.logicalAND ()]

        self.leave ("logicalOR")

        return tree

    # ====================================================================
    # logical AND
    # <logicalAND> -> <equalop> { && <equalop> }

    def logicalAND (self):
        self.enter ("logicalAND")

        tree = Node("logicalAND")

        tree.children += [self.equalop ()]
        while self.tokens[self.currentToken].type == "LAND":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("logicalOR", "LAND")
            tree.children += [self.equalop ()]

        self.leave ("logicalAND")

        return tree

    # ====================================================================
    # equal operator
    # <equalop> -> <inequalop> -> { ( == | != ) <inequalop> }

    def equalop (self):
        self.enter ("equalop")

        tree = Node("equalop")

        tree.children += [self.inequalop ()]
        while self.tokens[self.currentToken].type == "EQ" \
            or self.tokens[self.currentToken].type == "NE": 
            if self.tokens[self.currentToken].type == "EQ":
                tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
                self.match ("equalop", "EQ")
            else:
                tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
                self.match ("equalop", "NE")
            tree.children += [self.inequalop ()]

        self.leave ("equalop")

        return tree

    # ====================================================================
    # inequal operator
    # <inequalop> -> <addsub> -> { (  ) <addsub> }

    def inequalop (self):
        self.enter ("inequalop")

        tree = Node("inequalop")

        tree.children += [self.addsub ()]
        while self.tokens[self.currentToken].type == "LT"   \
            or self.tokens[self.currentToken].type == "LTE" \
            or self.tokens[self.currentToken].type == "GT"  \
            or self.tokens[self.currentToken].type == "GTE":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("inequalop", self.tokens[self.currentToken].type)
            tree.children += [self.addsub ()]

        self.leave ("inequalop")

        return tree

    # ====================================================================
    # addition and subtraction 
    # <addsub> -> <term> { ( + | - ) <term> }

    def addsub (self):
        self.enter ("addsub")

        tree = Node("addsub")

        tree.children += [self.term ()]
        while  self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("addsub", self.tokens[self.currentToken].type)
            tree.children += [self.term ()]

        self.leave ("addsub")

        return tree

    # ====================================================================
    # multiplication / division / remainder (mod)
    # <term> -> <unaryleft> { ( * | / | % ) <unaryleft> }

    def term (self):
        self.enter ("term")

        tree = Node("term")

        tree.children += [self.unaryleft ()]
        while self.tokens[self.currentToken].type == "TIMES"   \
            or self.tokens[self.currentToken].type == "DIVIDE" \
            or self.tokens[self.currentToken].type == "MOD":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("term", self.tokens[self.currentToken].type)
            tree.children += [self.unaryleft ()]

        self.leave ("term")

        return tree

    # ====================================================================
    # unary left operators
    # <unaryleft> -> [ ( ++ | -- | + | - | ! | ~ ) ] <unaryright>

    def unaryleft (self):
        self.enter ("unaryleft")

        tree = Node("unaryleft")

        if     self.tokens[self.currentToken].type == "INCR"  \
            or self.tokens[self.currentToken].type == "DECR"  \
            or self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS" \
            or self.tokens[self.currentToken].type == "LNOT"  \
            or self.tokens[self.currentToken].type == "BNOT":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryleft", self.tokens[self.currentToken].type)
        tree.children += [self.unaryright ()]

        self.leave ("unaryleft")

        return tree

    # ====================================================================
    # unary right operators / funcall / subscript / member accessor 
    # <unaryright> -> <factor> [ ( ++ | -- ) ]
    #              -> <factor> [ '(' [ <expr> ] ')' ]
    #              -> <factor> [ '[' [ <expr> ] ']' ]
    #              -> <factor> [ . <member> ]

    def unaryright (self):
        self.enter ("unaryright")

        tree = Node("unaryright")
        
        tree.children += [self.factor ()]

        # <unaryright> -> <factor> [ ++ ]
        if self.tokens[self.currentToken].type == "INCR":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "INCR")
        # <unaryright> -> <factor> [ -- ]
        elif self.tokens[self.currentToken].type == "DECR":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "DECR")
        # <unaryright> -> <factor> [ '(' <expr> ')' ]
        elif self.tokens[self.currentToken].type == "LPAREN":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "LPAREN")
            if self.tokens[self.currentToken].type != "RPAREN":
                tree.children += [self.expression ()]
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "RPAREN")
        # <unaryright> -> <factor> [ '[' <expr> ']' ]
        elif self.tokens[self.currentToken].type == "LBRACKET":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "LBRACKET")
            if self.tokens[self.currentToken].type != "RBRACKET":
                tree.children += [self.expression ()]
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "RBRACKET")
        # <unaryright> -> <factor> [ . <member> ]
        elif self.tokens[self.currentToken].type == "DOT":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("unaryright", "DOT")
            tree.children += [self.member ()]

        self.leave ("unaryright")

        return tree

    # ====================================================================
    # member accessor
    # <member> -> IDENTIFIER [ '(' [ <expr> ] ')' ]
    def member (self):
        self.enter ("member")

        tree = Node("MEMBER")
        tree.children += [Node("IDENTIFIER", self.tokens[self.currentToken])]
        self.match ("member", "IDENTIFIER")
        if (self.tokens[self.currentToken].type == "LPAREN"):
            tree.children += [Node("LPAREN", self.tokens[self.currentToken])]
            self.match ("member", "LPAREN")
            if self.tokens[self.currentToken].type != "RPAREN":
                tree.children += [self.expression ()]
            tree.children += [Node("RPAREN", self.tokens[self.currentToken])]
            self.match ("member", "RPAREN")

        self.leave ("member")

        return tree

    # ====================================================================
    # parentheses / indentifiers / list / literals 
    # <factor> -> '(' [ <expr> ] ')'
    #          -> INDENTIFIER
    #          -> '[' [ <expr> ] ']'
    #          -> <literal>

    def factor (self):
        self.enter ("factor")

        tree = None

        # <factor> -> '(' [ <expr> ] ')'
        if self.tokens[self.currentToken].type == "LPAREN":
            tree = Node("PARENS")
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("factor", "LPAREN")
            if self.tokens[self.currentToken].type != "RPAREN":
                tree.children += [self.expression ()]
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("factor", "RPAREN")
        # <factor> -> INDENTIFIER
        elif self.tokens[self.currentToken].type == "IDENTIFIER":
            tree = Node("IDENTIFIER", self.tokens[self.currentToken])
            self.match ("factor", "IDENTIFIER")
        # <factor> -> '[' [ <expr> ] ']'
        elif self.tokens[self.currentToken].type == "LBRACKET":
            tree = Node("LIST")
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("factor", "LBRACKET")
            if self.tokens[self.currentToken].type != "RBRACKET":
                tree.children += [self.expression ()]
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("factor", "RBRACKET")
        else:
            tree = self.literal ()

        self.leave ("factor")

        return tree

    # ====================================================================
    # literals
    # <literal> -> INT
    #           -> FLOAT
    #           -> CHAR
    #           -> STRING

    def literal (self):
        self.enter ("literal")

        tree = Node("literal")

        if self.tokens[self.currentToken].type == "INT":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("literal", "INT")
        elif self.tokens[self.currentToken].type == "FLOAT":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("literal", "FLOAT")
        elif self.tokens[self.currentToken].type == "CHAR":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("literal", "CHAR")
        elif self.tokens[self.currentToken].type == "STRING":
            tree.children += [Node(self.tokens[self.currentToken].type, self.tokens[self.currentToken])]
            self.match ("literal", "STRING")
        # expected literal but didnt get one 
        else:
            self.error ("literal", "INT")

        self.leave ("literal")

        return tree

# ========================================================================
