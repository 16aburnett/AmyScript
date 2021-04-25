# Amy Script Compiler
# By Amy Burnett
# April 10 2021
# ========================================================================

from ast import *

# ========================================================================

class Node:
    def __init__(self, name, token=None):
        self.name = name
        self.token = token
        self.children = []

class Parser:

    def __init__(self, tokens, doDebug=False):
        self.tokens = tokens
        self.currentToken = 0
        self.doDebug = doDebug
        self.level = 0

    # <start> -> { <codeunit> }
    def parse(self):

        codeunits = [] 
        
        while self.currentToken < len(self.tokens) and self.tokens[self.currentToken].type != "END_OF_FILE":
            codeunits += [self.codeunit ()]
        
        return ProgramNode(codeunits)

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
    #            -> <class>
    #            -> <namespace>
    #            -> <statement>
    def codeunit (self):
        self.enter ("codeunit")

        node = None

        # <codeunit> -> <function>
        if (self.tokens[self.currentToken].type == 'FUNCTION'):
            node = self.function ()
        # <codeunit> -> <statement>
        else:
            node = self.statement ()
        
        self.leave ("codeunit")

        return node

    # ====================================================================
    # function declaration
    # <function> -> FUNCTION IDENTIFIER <paramlist> <codeblock>
    
    def function (self):
        self.enter ("function")

        self.match ("function", "FUNCTION")
        
        id = self.tokens[self.currentToken].lexeme
        self.match ("function", "IDENTIFIER")
        
        params = self.paramlist()

        body = self.codeblock()

        self.leave ("function")

        return FunctionNode (id, params, body)

    # ====================================================================
    # parameter list for a function declaration
    # <paramlist> -> '(' [ IDENTIFIER [ , IDENTIFIER ] ] ')'

    def paramlist (self): 
        self.enter ("paramlist")

        params = []

        self.match ("paramlist", "LPAREN")

        if self.tokens[self.currentToken].type == "IDENTIFIER":

            id = self.tokens[self.currentToken].lexeme
            self.match ("paramlist", "IDENTIFIER")
            params += [ParameterNode (id)]

            while self.tokens[self.currentToken].type == "COMMA":
                self.match ("paramlist", "COMMA")

                id = self.tokens[self.currentToken].lexeme
                self.match ("paramlist", "IDENTIFIER")
                params += [ParameterNode (id)]

        self.match ("paramlist", "RPAREN")

        self.leave ("paramlist")

        return params

    # ====================================================================
    # statement 
    # <statement> -> <codeblock>
    #             -> <forloop>
    #             -> <whileloop>
    #             -> <condition>
    #             -> <returnStatement>
    #             -> <continueStatement>
    #             -> <breakStatement>
    #             -> <expressionStatement>

    def statement (self):
        self.enter ("statement")

        node = None

        # <statement> -> <codeblock>
        if (self.tokens[self.currentToken].type == "LBRACE"):
            node = self.codeblock ()
        # <statement> -> <forloop>
        elif (self.tokens[self.currentToken].type == "FOR"):
            node = self.forloop ()
        # <statement> -> <whileloop>
        elif (self.tokens[self.currentToken].type == "WHILE"):
            node = self.whileloop ()
        # <statement> -> <condition>
        elif (self.tokens[self.currentToken].type == "IF"):
            node = self.conditional ()
        # <statement> -> <returnStatement>
        elif (self.tokens[self.currentToken].type == "RETURN"):
            node = self.returnStatement ()
        # <statement> -> <continueStatement>
        elif (self.tokens[self.currentToken].type == "CONTINUE"):
            node = self.continueStatement ()
        # <statement> -> <breakStatement>
        elif (self.tokens[self.currentToken].type == "BREAK"):
            node = self.breakStatement ()
        # <statement> -> <expressionStatement> 
        else:
            node = self.expressionStatement ()

        self.leave ("statement")

        return node

    # ====================================================================
    # codeblock 
    # <codeblock> -> '{' { <codeunit> } '}'

    def codeblock (self):
        self.enter ("codeblock")

        codeunits = []

        self.match ("codeblock", "LBRACE")
        
        while self.tokens[self.currentToken].type != "RBRACE":
            codeunits += [self.codeunit ()]
        
        self.match ("codeblock", "RBRACE")

        self.leave ("codeblock")

        return CodeBlockNode (codeunits)

    # ====================================================================
    # for loop 
    # <forloop> -> for ( <expr> ; <expr> ; <expr> ) <statement>

    def forloop (self):
        self.enter ("forloop")

        self.match ("forloop", "FOR")
        self.match ("forloop", "LPAREN")
        init = self.expression ()
        self.match ("forloop", "SEMI")
        cond = self.expression ()
        self.match ("forloop", "SEMI")
        update = self.expression ()
        self.match ("forloop", "RPAREN")
        body = self.statement ()

        self.leave ("forloop")

        return ForStatementNode (init, cond, update, body)

    # ====================================================================
    # while loop 
    # <whileloop> -> while ( <expr> ) <statement>

    def whileloop (self):
        self.enter ("whileloop")

        self.match ("whileloop", "WHILE")
        self.match ("whileloop", "LPAREN")
        cond = self.expression ()
        self.match ("whileloop", "RPAREN")
        body = self.statement ()

        self.leave ("whileloop")

        return WhileStatementNode (cond, body)

    # ====================================================================
    # if statement 
    # <conditional> -> if ( <expr> ) <statement> { <elif> } [ <else> ]

    def conditional (self):
        self.enter ("conditional")

        self.match ("conditional", "IF")
        
        self.match ("conditional", "LPAREN")

        cond = self.expression ()
        
        self.match ("conditional", "RPAREN")

        body = self.statement ()

        # match 0 or more elifs 
        elifs = []
        while (self.tokens[self.currentToken].type == "ELIF"):
            elifs += [self.elifStatement ()]
        
        # match 0 or 1 else
        elseStmt = None
        if (self.tokens[self.currentToken].type == "ELSE"):
            elseStmt = self.elseStatement ()

        self.leave ("conditional")

        return IfStatementNode (cond, body, elifs, elseStmt)

    # ====================================================================
    # elif statement 
    # <elifStatement> -> ELIF ( <expr> ) <statement>

    def elifStatement (self):
        self.enter ("elifStatement")

        self.match ("elifStatement", "ELIF")
        self.match ("elifStatement", "LPAREN")

        cond = self.expression ()

        self.match ("elifStatement", "RPAREN")

        body = self.statement ()

        self.leave ("elifStatement")

        return ElifStatementNode (cond, body)

    # ====================================================================
    # else statement 
    # <elseStatement> -> ELSE <statement>

    def elseStatement (self):
        self.enter ("elseStatement")

        self.match ("elseStatement", "ELSE")

        body = self.statement ()

        self.leave ("elseStatement")

        return ElseStatementNode (body)

    # ====================================================================
    # expressionStatement
    # <expressionStatement> -> [ <expression> ] ; 

    def expressionStatement (self):
        self.enter ("expressionStatement")

        # optionally an expression
        expr = None
        if (self.tokens[self.currentToken].type != "SEMI"):
            expr = self.expression ()

        # could give error message here saying
        # "hey fricker, you missed a semi"
        self.match ("expressionStatement", "SEMI", "You should add a semicolon")

        self.leave ("expressionStatement")

        return ExpressionStatementNode (expr)

    # ====================================================================
    # return statement
    # <returnStatement> -> RETURN [ <expression> ] ; 

    def returnStatement (self):
        self.enter ("returnStatement")

        self.match ("returnStatement", "RETURN")

        # optionally an expression
        expr = None
        if (self.tokens[self.currentToken].type != "SEMI"):
            expr = self.expression ()

        # could give error message here saying
        # "hey fricker, you missed a semi"
        self.match ("returnStatement", "SEMI", "You should add a semicolon")

        self.leave ("returnStatement")

        return ReturnStatementNode (expr)

    # ====================================================================
    # break statement
    # <breakStatement> -> BREAK; 

    def breakStatement (self):
        self.enter ("breakStatement")

        self.match ("breakStatement", "BREAK")

        # could give error message here saying
        # "hey fricker, you missed a semi"
        self.match ("breakStatement", "SEMI", "You should add a semicolon")

        self.leave ("breakStatement")

        return BreakStatementNode ()

    # ====================================================================
    # continue statement
    # <continueStatement> -> CONTINUE; 

    def continueStatement (self):
        self.enter ("continueStatement")

        self.match ("continueStatement", "CONTINUE")

        # could give error message here saying
        # "hey fricker, you missed a semi"
        self.match ("continueStatement", "SEMI", "You should add a semicolon")

        self.leave ("continueStatement")

        return ContinueStatementNode ()

    # ====================================================================
    # expression
    # <expression> -> <tuple>

    def expression (self):
        self.enter ("expression")
        
        node = self.tuple ()

        self.leave ("expression")

        return node

    # ====================================================================
    # tuple 
    # <tuple> -> <assignexpr> { , <assignexpr> }

    def tuple (self):
        self.enter ("tuple")

        lhs = self.assignexpr ()

        while (self.tokens[self.currentToken].type == "COMMA"):
            self.match ("tuple", "COMMA")
            rhs = self.assignexpr ()

            lhs = TupleExpressionNode (lhs, rhs)

        self.leave ("tuple")

        return lhs

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

        lhs = self.logicalOR ()

        if self.tokens[self.currentToken].type == "ASSIGN":
            self.match ("assignexpr", "ASSIGN")
            rhs = self.logicalOR ()

            lhs = AssignExpressionNode (lhs, "=", rhs)

        self.leave ("assignexpr")

        return lhs

    # ====================================================================
    # logical OR 
    # <logicalOR> -> <logicalAND> { || <logicalAND> }

    def logicalOR (self):
        self.enter ("logicalOR")

        lhs = self.logicalAND ()

        while self.tokens[self.currentToken].type == "LOR":
            self.match ("logicalOR", "LOR")
            rhs = self.logicalAND ()

            lhs = LogicalOrExpressionNode (lhs, rhs)

        self.leave ("logicalOR")

        return lhs

    # ====================================================================
    # logical AND
    # <logicalAND> -> <equalop> { && <equalop> }

    def logicalAND (self):
        self.enter ("logicalAND")

        lhs = self.equalop ()

        while self.tokens[self.currentToken].type == "LAND":
            self.match ("logicalOR", "LAND")
            rhs = self.equalop ()

            lhs = LogicalAndExpressionNode (lhs, rhs)

        self.leave ("logicalAND")

        return lhs

    # ====================================================================
    # equal operator
    # <equalop> -> <inequalop> -> { ( == | != ) <inequalop> }

    def equalop (self):
        self.enter ("equalop")

        lhs = self.inequalop ()

        while self.tokens[self.currentToken].type == "EQ" \
            or self.tokens[self.currentToken].type == "NE": 
            op = ""
            if self.tokens[self.currentToken].type == "EQ":
                op = "=="
                self.match ("equalop", "EQ")
            else:
                op = "!="
                self.match ("equalop", "NE")
            rhs = self.inequalop ()

            lhs = EqualityExpressionNode (lhs, op, rhs)

        self.leave ("equalop")

        return lhs

    # ====================================================================
    # inequal operator
    # <inequalop> -> <addsub> -> { (  ) <addsub> }

    def inequalop (self):
        self.enter ("inequalop")

        lhs = self.addsub ()

        while self.tokens[self.currentToken].type == "LT"   \
            or self.tokens[self.currentToken].type == "LTE" \
            or self.tokens[self.currentToken].type == "GT"  \
            or self.tokens[self.currentToken].type == "GTE":
            op = self.tokens[self.currentToken].lexeme
            self.match ("inequalop", self.tokens[self.currentToken].type)
            rhs = self.addsub ()

            lhs = InequalityExpressionNode (lhs, op, rhs)

        self.leave ("inequalop")

        return lhs

    # ====================================================================
    # addition and subtraction 
    # <addsub> -> <term> { ( + | - ) <term> }

    def addsub (self):
        self.enter ("addsub")

        lhs = self.term ()

        while  self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS":

            op = self.tokens[self.currentToken].lexeme
            self.match ("addsub", self.tokens[self.currentToken].type)
            rhs = self.term ()

            lhs = AdditiveExpressionNode (lhs, op, rhs)

        self.leave ("addsub")

        return lhs

    # ====================================================================
    # multiplication / division / remainder (mod)
    # <term> -> <unaryleft> { ( * | / | % ) <unaryleft> }

    def term (self):
        self.enter ("term")

        lhs = self.unaryleft ()

        while self.tokens[self.currentToken].type == "TIMES"   \
            or self.tokens[self.currentToken].type == "DIVIDE" \
            or self.tokens[self.currentToken].type == "MOD":

            op = self.tokens[self.currentToken].lexeme
            self.match ("term", self.tokens[self.currentToken].type)
            rhs = self.unaryleft ()

            lhs = MultiplicativeExpressionNode (lhs, op, rhs)

        self.leave ("term")

        return lhs 

    # ====================================================================
    # unary left operators
    # <unaryleft> -> [ ( ++ | -- | + | - | ! | ~ ) ] <unaryright>

    def unaryleft (self):
        self.enter ("unaryleft")

        op = None
        if     self.tokens[self.currentToken].type == "INCR"  \
            or self.tokens[self.currentToken].type == "DECR"  \
            or self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS" \
            or self.tokens[self.currentToken].type == "LNOT"  \
            or self.tokens[self.currentToken].type == "BNOT":
            op = self.tokens[self.currentToken].lexeme
            self.match ("unaryleft", self.tokens[self.currentToken].type)

        rhs = self.unaryright ()

        self.leave ("unaryleft")

        if (op != None):
            return UnaryLeftExpressionNode (op, rhs)
        return rhs

    # ====================================================================
    # unary right operators / funcall / subscript
    # <unaryright> -> <member> [ ( ++ | -- ) ]
    #              -> <member> [ '(' [ <assignExpression> { COMMA <assignExpression> } ] ')' ]
    #              -> <member> [ '[' [ <expression> ] ']' ]

    def unaryright (self):
        self.enter ("unaryright")
        
        lhs = self.member ()

        # <unaryright> -> <member> [ ++ ]
        if self.tokens[self.currentToken].type == "INCR":
            self.match ("unaryright", "INCR")
            lhs = PostIncrementExpressionNode (lhs)
        # <unaryright> -> <member> [ -- ]
        elif self.tokens[self.currentToken].type == "DECR":
            self.match ("unaryright", "DECR")
            lhs = PostDecrementExpressionNode (lhs)
        # function call 
        # <unaryright> -> <member> [ '(' [ <assignExpression> { COMMA <assignExpression> } ] ')' ]
        elif self.tokens[self.currentToken].type == "LPAREN":
            self.match ("unaryright", "LPAREN")
            args = []
            # optional arguments 
            if self.tokens[self.currentToken].type != "RPAREN":
                args += [self.assignexpr ()]
                # 0 or more additional arguments 
                while self.tokens[self.currentToken].type == "COMMA":
                    self.match ("unaryright", "COMMA")
                    args += [self.assignexpr ()]
            self.match ("unaryright", "RPAREN")
            lhs = FunctionCallExpressionNode (lhs, args)
        # subscript operator 
        # <unaryright> -> <member> [ '[' <expr> ']' ]
        elif self.tokens[self.currentToken].type == "LBRACKET":
            self.match ("unaryright", "LBRACKET")
            offset = self.expression ()
            self.match ("unaryright", "RBRACKET")
            lhs = SubscriptExpressionNode (lhs, offset)

        self.leave ("unaryright")

        return lhs

    # ====================================================================
    # member accessor
    # string.length
    # string.substring(0, 12).size()
    # string.data[10]
    # (matrixA * matrixB).transpose()
    # <member> -> <factor> { DOT <factor> }
    def member (self):
        self.enter ("member")

        lhs = self.factor ()

        while (self.tokens[self.currentToken].type == "DOT"):
            self.match ("member", "DOT")
            rhs = self.factor ()

            lhs = MemberAccessorExpressionNode (lhs, rhs)

        self.leave ("member")

        return lhs

    # ====================================================================
    # parentheses / indentifiers / list / literals 
    # <factor> -> '(' [ <expr> ] ')'
    #          -> INDENTIFIER
    #          -> '[' [ [ <assignExpression> { COMMA <assignExpression> } ] ] ']'
    #          -> <literal>

    def factor (self):
        self.enter ("factor")

        lhs = None 

        # <factor> -> '(' [ <expr> ] ')'
        if self.tokens[self.currentToken].type == "LPAREN":
            self.match ("factor", "LPAREN")
            if self.tokens[self.currentToken].type != "RPAREN":
                lhs = self.expression ()
            self.match ("factor", "RPAREN")
        # <factor> -> INDENTIFIER
        elif self.tokens[self.currentToken].type == "IDENTIFIER":
            id = self.tokens[self.currentToken].lexeme
            self.match ("factor", "IDENTIFIER")
            lhs = IdentifierExpressionNode (id)
        # list creator operator  
        # <factor> -> '[' [ [ <assignExpression> { COMMA <assignExpression> } ] ] ']'
        elif self.tokens[self.currentToken].type == "LBRACKET":
            self.match ("factor", "LBRACKET")
            items = []
            # optional items 
            if self.tokens[self.currentToken].type != "RPAREN":
                items += [self.assignexpr ()]
                # 0 or more additional items 
                while self.tokens[self.currentToken].type == "COMMA":
                    self.match ("factor", "COMMA")
                    items += [self.assignexpr ()]
            self.match ("factor", "RBRACKET")
            lhs = ListConstructorExpressionNode (items)
        else:
            lhs = self.literal ()

        self.leave ("factor")

        return lhs

    # ====================================================================
    # literals
    # <literal> -> INT
    #           -> FLOAT
    #           -> CHAR
    #           -> STRING

    def literal (self):
        self.enter ("literal")

        node = None

        if self.tokens[self.currentToken].type == "INT":
            value = self.tokens[self.currentToken].value
            self.match ("literal", "INT")
            node = IntLiteralExpressionNode (value)
        elif self.tokens[self.currentToken].type == "FLOAT":
            value = self.tokens[self.currentToken].value
            self.match ("literal", "FLOAT")
            node = FloatLiteralExpressionNode (value)
        elif self.tokens[self.currentToken].type == "CHAR":
            value = self.tokens[self.currentToken].value
            self.match ("literal", "CHAR")
            node = CharLiteralExpressionNode (value)
        elif self.tokens[self.currentToken].type == "STRING":
            value = self.tokens[self.currentToken].value
            self.match ("literal", "STRING")
            node = StringLiteralExpressionNode (value)
        # expected literal but didnt get one 
        else:
            self.error ("literal", "INT")

        self.leave ("literal")

        return node

# ========================================================================
