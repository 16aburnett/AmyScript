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
        # <codeunit> -> <class>
        elif (self.tokens[self.currentToken].type == "CLASS"):
            node = self.classDeclaration ()
        # <codeunit> -> <statement>
        else:
            node = self.statement ()
        
        self.leave ("codeunit")

        return node

    # ====================================================================
    # function declaration
    # <function> -> FUNCTION <typeSpecifier> IDENTIFIER <paramlist> <codeblock>
    
    def function (self):
        self.enter ("function")

        self.match ("function", "FUNCTION")
        
        type = self.typeSpecifier ()

        id = self.tokens[self.currentToken].lexeme
        token = self.tokens[self.currentToken]
        self.match ("function", "IDENTIFIER")
        
        params = self.paramlist()

        body = self.codeblock()

        self.leave ("function")

        return FunctionNode (type, id, token, params, body)

    # ====================================================================
    # class declaration
    # <class> -> CLASS IDENTIFIER LBRACE { ( <fieldDeclaration> | <methodDeclaration> ) } RBRACE
    
    def classDeclaration (self):
        self.enter ("classDeclaration")

        self.match ("classDeclaration", "CLASS")

        id = self.tokens[self.currentToken].lexeme
        token = self.tokens[self.currentToken]
        self.match ("classDeclaration", "IDENTIFIER")
        
        self.match ("classDeclaration", "LBRACE")

        constructors = []
        fields = []
        methods = [] 
        while (self.tokens[self.currentToken].type == "PUBLIC"\
            or self.tokens[self.currentToken].type == "PRIVATE"\
            or self.tokens[self.currentToken].type == "FIELD"\
            or self.tokens[self.currentToken].type == "METHOD"\
            or self.tokens[self.currentToken].type == "CONSTRUCTOR"):
            if (self.tokens[self.currentToken].type == "PUBLIC"
                or self.tokens[self.currentToken].type == "PRIVATE"):
                if (self.tokens[self.currentToken+1].type == "FIELD"):
                    fields += [self.fieldDeclaration ()]
                elif (self.tokens[self.currentToken+1].type == "METHOD"):
                    methods += [self.methodDeclaration ()]
                else: 
                    self.error ("classDeclaration", "FIELD", "Expected a field or method in class body")
            else:
                if (self.tokens[self.currentToken].type == "FIELD"):
                    fields += [self.fieldDeclaration ()]
                elif (self.tokens[self.currentToken].type == "METHOD"):
                    methods += [self.methodDeclaration ()]
                elif (self.tokens[self.currentToken].type == "CONSTRUCTOR"):
                    constructors += [self.constructorDeclaration ()]
                else: 
                    self.error ("classDeclaration", "FIELD", "Expected a field or method in class body")
            
        self.match ("classDeclaration", "RBRACE")

        self.leave ("classDeclaration")

        return ClassDeclarationNode (id, token, constructors, fields, methods)

    # ====================================================================
    # field declaration
    # <fieldDeclaration> -> [ SECURITY ] FIELD <typeSpecifier> IDENTIFIER SEMI
    
    def fieldDeclaration (self):
        self.enter ("fieldDeclaration")

        # private by default 
        security = Security.PRIVATE
        if (self.tokens[self.currentToken].type == "PUBLIC"):
            security = Security.PUBLIC
            self.match ("methodDeclaration", "PUBLIC")
        elif (self.tokens[self.currentToken].type == "PRIVATE"):
            security = Security.PRIVATE
            self.match ("methodDeclaration", "PRIVATE")

        self.match ("fieldDeclaration", "FIELD")

        type = self.typeSpecifier ()

        id = self.tokens[self.currentToken].lexeme
        token = self.tokens[self.currentToken]
        self.match ("fieldDeclaration", "IDENTIFIER")

        self.match ("fieldDeclaration", "SEMI")

        self.leave ("fieldDeclaration")

        return FieldDeclarationNode (security, type, id, token)

    # ====================================================================
    # method declaration
    # <methodDeclaration> -> [ SECURITY ] METHOD <typeSpecifier> IDENTIFIER <paramlist> <codeblock>
    
    def methodDeclaration (self):
        self.enter ("methodDeclaration")

        # private by default 
        security = Security.PRIVATE
        if (self.tokens[self.currentToken].type == "PUBLIC"):
            security = Security.PUBLIC
            self.match ("methodDeclaration", "PUBLIC")
        elif (self.tokens[self.currentToken].type == "PRIVATE"):
            security = Security.PRIVATE
            self.match ("methodDeclaration", "PRIVATE")

        self.match ("fieldDeclaration", "METHOD")

        type = self.typeSpecifier ()

        id = self.tokens[self.currentToken].lexeme
        token = self.tokens[self.currentToken]
        self.match ("methodDeclaration", "IDENTIFIER")
        
        params = self.paramlist()

        body = self.codeblock()

        self.leave ("methodDeclaration")

        return MethodDeclarationNode (security, type, id, token, params, body)

    # ====================================================================
    # constructor declaration
    # <constructorDeclaration> -> CONSTRUCTOR <paramlist> <codeblock>
    
    def constructorDeclaration (self):
        self.enter ("constructorDeclaration")

        token = self.tokens[self.currentToken]
        self.match ("constructorDeclaration", "CONSTRUCTOR")
        
        params = self.paramlist()

        body = self.codeblock()

        self.leave ("constructorDeclaration")

        return ConstructorDeclarationNode (token, params, body)

    # ====================================================================
    # parameter list for a function declaration
    # <paramlist> -> '(' [ <typeSpecifier> IDENTIFIER [ , <typeSpecifier> IDENTIFIER ] ] ')'

    def paramlist (self): 
        self.enter ("paramlist")

        params = []

        self.match ("paramlist", "LPAREN")

        if self.tokens[self.currentToken].type != "RPAREN":

            type = self.typeSpecifier ()

            id = self.tokens[self.currentToken].lexeme
            token = self.tokens[self.currentToken]
            self.match ("paramlist", "IDENTIFIER")
            params += [ParameterNode (type, id, token)]

            while self.tokens[self.currentToken].type == "COMMA":
                self.match ("paramlist", "COMMA")

                type = self.typeSpecifier ()

                id = self.tokens[self.currentToken].lexeme
                token = self.tokens[self.currentToken]
                self.match ("paramlist", "IDENTIFIER")
                params += [ParameterNode (type, id, token)]

        self.match ("paramlist", "RPAREN")

        self.leave ("paramlist")

        return params

    # ====================================================================

    def isType (self):
        # <typeSpecifier> -> INTTYPE
        return self.tokens[self.currentToken].type == 'INTTYPE'   \
            or self.tokens[self.currentToken].type == 'FLOATTYPE' \
            or self.tokens[self.currentToken].type == 'CHARTYPE'  \
            or self.tokens[self.currentToken].type == 'BOOLTYPE'  \
            or self.tokens[self.currentToken].type == 'STRINGTYPE'\
            or self.tokens[self.currentToken].type == 'VOIDTYPE'

    # <typeSpecifier> -> INTTYPE { '[' ']' }
    #                  | FLOATTYPE { '[' ']' }
    #                  | CHARTYPE { '[' ']' }
    #                  | BOOLTYPE { '[' ']' }
    #                  | STRINGTYPE { '[' ']' }
    #                  | IDENTIFIER { '[' ']' }
    def typeSpecifier (self):
        self.enter ("typeSpecifier")

        # unknown by default 
        type = None
        temp = self.currentToken

        # <typeSpecifier> -> INTTYPE
        if (self.tokens[self.currentToken].type == 'INTTYPE'):
            self.match ("typeSpecifier", 'INTTYPE')
            type = TypeSpecifierNode (Type.INT, "int", self.tokens[self.currentToken])
        # <typeSpecifier> -> FLOATTYPE
        elif (self.tokens[self.currentToken].type == 'FLOATTYPE'):
            self.match ("typeSpecifier", 'FLOATTYPE')
            type = TypeSpecifierNode (Type.FLOAT, "float", self.tokens[self.currentToken])
        # <typeSpecifier> -> CHARTYPE
        elif (self.tokens[self.currentToken].type == 'CHARTYPE'):
            self.match ("typeSpecifier", 'CHARTYPE')
            type = TypeSpecifierNode (Type.CHAR, "char", self.tokens[self.currentToken])
        # <typeSpecifier> -> BOOLTYPE
        elif (self.tokens[self.currentToken].type == 'BOOLTYPE'):
            self.match ("typeSpecifier", 'BOOLTYPE')
            type = TypeSpecifierNode (Type.BOOL, "bool", self.tokens[self.currentToken])
        # <typeSpecifier> -> STRINGTYPE
        elif (self.tokens[self.currentToken].type == 'STRINGTYPE'):
            self.match ("typeSpecifier", 'STRINGTYPE')
            type = TypeSpecifierNode (Type.STRING, "string", self.tokens[self.currentToken])
        # <typeSpecifier> -> VOIDTYPE
        elif (self.tokens[self.currentToken].type == 'VOIDTYPE'):
            self.match ("typeSpecifier", 'VOIDTYPE')
            type = TypeSpecifierNode (Type.VOID, "void", self.tokens[self.currentToken])
        # <typeSpecifier> -> IDENTIFIER
        elif (self.tokens[self.currentToken].type == 'IDENTIFIER'):
            type = TypeSpecifierNode (Type.USERTYPE, self.tokens[self.currentToken].lexeme, self.tokens[self.currentToken])
            self.match ("typeSpecifier", 'IDENTIFIER')
        
        # match array 
        if type != None:
            while (self.tokens[self.currentToken].type == "LBRACKET"):
                self.match ("typeSpecifier", "LBRACKET")
                # possibly not a type spec
                if (self.tokens[self.currentToken].type != "RBRACKET"):
                    self.currentToken = temp
                    self.leave ("typeSpecifier")
                    return None
                self.match ("typeSpecifier", "RBRACKET")
                type.arrayDimensions += 1
        
        self.leave ("typeSpecifier")

        return type

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
    # **add for/else

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
    # <expressionStatement> -> [ <expression> ] SEMI

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
    # varDeclaration 
    # <varDeclaration> -> ( TYPE [ "[]" ] ID | ID [ "[]" ] ID | <logicalOR> )

    def varDeclaration (self):
        self.enter ("varDeclaration")

        lhs = None

        #     -> ID { '[' ']' } ID 
        #     -> <logicalOR> 
        if (self.isType () or self.tokens[self.currentToken].type == "IDENTIFIER"):

            varIndex = self.currentToken
            # match type
            type = self.typeSpecifier ()

            # assumption was wrong
            # -> <logicalOR> 
            if (type == None or self.tokens[self.currentToken].type != "IDENTIFIER"):
                # restore state
                self.currentToken = varIndex
                lhs = self.logicalOR ()
            else:
                id = self.tokens[self.currentToken].lexeme
                token = self.tokens[self.currentToken]
                self.match ("varDeclaration", "IDENTIFIER")
                lhs = VariableDeclarationNode (type, id, token)
        # assumption was wrong
        else:
            lhs = self.logicalOR ()

        self.leave ("varDeclaration")

        return lhs

    # ====================================================================
    # assignment expressions 
    # <assignexpr> -> { <varDeclaration> = } <varDeclaration>
    def assignexpr (self):
        self.enter ("assignexpr")

        root = None
        lastAssign = None

        # while lhs is var or var declaration
        while (self.tokens[self.currentToken].type == "IDENTIFIER" \
            or self.isType()):
            # save return state
            varIndex = self.currentToken
            lhs = self.varDeclaration ()

            # if there is an assign
            if (self.tokens[self.currentToken].type == "ASSIGN"):
                line = self.tokens[self.currentToken].line
                column = self.tokens[self.currentToken].column
                self.match ("assignexpr", "ASSIGN")
                rhs = AssignExpressionNode (lhs, "=", None, line, column)
                # if this is the first assignment expression
                if (root == None):
                    # make this the root 
                    root = rhs 
                    lastAssign = root 
                # not the first assignment statement
                else:
                    lastAssign.rhs = rhs 
                    lastAssign = rhs 
            # no ASSIGN
            # assumption was wrong
            else:
                # assumption was wrong, the var should be a logicalOR
                self.currentToken = varIndex
                break 

        # if there was at least one assign expr 
        if (root != None):
            lastAssign.rhs = self.varDeclaration ()
            self.leave ("assignexpr")
            return root 
        
        lhs = self.varDeclaration ()

        self.leave ("assignexpr")
        return lhs

    # ====================================================================
    # logical OR 
    # <logicalOR> -> <logicalAND> { || <logicalAND> }

    def logicalOR (self):
        self.enter ("logicalOR")

        lhs = self.logicalAND ()

        while self.tokens[self.currentToken].type == "LOR":
            
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("logicalOR", "LOR")
            rhs = self.logicalAND ()

            lhs = LogicalOrExpressionNode (lhs, rhs, line, column)

        self.leave ("logicalOR")

        return lhs

    # ====================================================================
    # logical AND
    # <logicalAND> -> <equalop> { && <equalop> }

    def logicalAND (self):
        self.enter ("logicalAND")

        lhs = self.equalop ()

        while self.tokens[self.currentToken].type == "LAND":

            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("logicalOR", "LAND")
            rhs = self.equalop ()

            lhs = LogicalAndExpressionNode (lhs, rhs, line, column)

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

            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            op = ""
            if self.tokens[self.currentToken].type == "EQ":
                op = "=="
                self.match ("equalop", "EQ")
            else:
                op = "!="
                self.match ("equalop", "NE")
            rhs = self.inequalop ()

            lhs = EqualityExpressionNode (lhs, op, rhs, line, column)

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

            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            op = self.tokens[self.currentToken].lexeme
            self.match ("inequalop", self.tokens[self.currentToken].type)
            rhs = self.addsub ()

            lhs = InequalityExpressionNode (lhs, op, rhs, line, column)

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

            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            op = self.tokens[self.currentToken].lexeme
            self.match ("addsub", self.tokens[self.currentToken].type)
            rhs = self.term ()

            lhs = AdditiveExpressionNode (lhs, op, rhs, line, column)

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

            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            op = self.tokens[self.currentToken].lexeme
            self.match ("term", self.tokens[self.currentToken].type)
            rhs = self.unaryleft ()

            lhs = MultiplicativeExpressionNode (lhs, op, rhs, line, column)

        self.leave ("term")

        return lhs 

    # ====================================================================
    # unary left operators
    # <unaryleft> -> [ ( ++ | -- | + | - | ! | ~ ) ] <unaryright>

    def unaryleft (self):
        self.enter ("unaryleft")

        op = None
        line = 0
        column = 0
        if     self.tokens[self.currentToken].type == "INCR"  \
            or self.tokens[self.currentToken].type == "DECR"  \
            or self.tokens[self.currentToken].type == "PLUS"  \
            or self.tokens[self.currentToken].type == "MINUS" \
            or self.tokens[self.currentToken].type == "LNOT"  \
            or self.tokens[self.currentToken].type == "BNOT":
            op = self.tokens[self.currentToken].lexeme
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("unaryleft", self.tokens[self.currentToken].type)

        rhs = self.unaryright ()

        self.leave ("unaryleft")

        if (op != None):
            return UnaryLeftExpressionNode (op, rhs, line, column)
        return rhs

    # ====================================================================
    # unary right operators 
    # <unaryright> -> <arrayAccess> [ ( ++ | -- ) ]

    def unaryright (self):
        self.enter ("unaryright")
        
        lhs = self.arrayAccess ()

        # <unaryright> -> <arrayAccess> [ ++ ]
        if self.tokens[self.currentToken].type == "INCR":
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("unaryright", "INCR")
            lhs = PostIncrementExpressionNode (lhs, line, column)
        # <unaryright> -> <arrayAccess> [ -- ]
        elif self.tokens[self.currentToken].type == "DECR":
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("unaryright", "DECR")
            lhs = PostDecrementExpressionNode (lhs, line, column)

        self.leave ("unaryright")

        return lhs

    # ====================================================================
    # array accessor and function call and member accessor
    # string.length
    # string.substring(0, 12).size()
    # string.data[10]
    # (matrixA * matrixB).transpose()
    # <arrayAccess> -> <factor> { ( '(' [ <assignExpression> { COMMA <assignExpression> } ] ')' | '[' [ <expression> ] ']' | DOT <factor> ) }
    def arrayAccess (self):
        self.enter ("arrayAccess")

        lhs = self.factor ()

        while (self.tokens[self.currentToken].type == "LPAREN" \
            or self.tokens[self.currentToken].type == "LBRACKET"\
            or self.tokens[self.currentToken].type == "DOT"):

            # function call 
            # <arrayAccess> -> <factor> { '(' [ <assignExpression> { COMMA <assignExpression> } ] ')' }
            if self.tokens[self.currentToken].type == "LPAREN":
                line = self.tokens[self.currentToken].line
                column = self.tokens[self.currentToken].column
                self.match ("arrayAccess", "LPAREN")
                args = []
                # optional arguments 
                if self.tokens[self.currentToken].type != "RPAREN":
                    args += [self.assignexpr ()]
                    # 0 or more additional arguments 
                    while self.tokens[self.currentToken].type == "COMMA":
                        self.match ("arrayAccess", "COMMA")
                        args += [self.assignexpr ()]
                self.match ("arrayAccess", "RPAREN")
                lhs = FunctionCallExpressionNode (lhs, args, line, column)
            # subscript operator 
            # <arrayAccess> -> <factor> { '[' <expr> ']' }
            elif self.tokens[self.currentToken].type == "LBRACKET":
                line = self.tokens[self.currentToken].line
                column = self.tokens[self.currentToken].column
                self.match ("arrayAccess", "LBRACKET")
                offset = self.expression ()
                self.match ("arrayAccess", "RBRACKET")
                lhs = SubscriptExpressionNode (lhs, offset, line, column)
            # member accessor
            # <arrayAccess> -> <factor> { DOT <factor> }
            elif (self.tokens[self.currentToken].type == "DOT"):
                line = self.tokens[self.currentToken].line
                column = self.tokens[self.currentToken].column
                self.match ("arrayAccess", "DOT")
                rhs = self.factor ()
                lhs = MemberAccessorExpressionNode (lhs, rhs, line, column)

        self.leave ("arrayAccess")

        return lhs

    # ====================================================================
    # parentheses / indentifiers / list / literals 
    # <factor> -> '(' [ <expr> ] ')'
    #          -> IDENTIFIER
    #          -> '[' [ [ <assignExpression> { COMMA <assignExpression> } ] ] ']'
    #          -> NEW ( TYPE | IDENTIFIER ) ( '[' <expr> ']' { '[' <expr> ']' } | '(' <args> ')' )
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
        # <factor> -> IDENTIFIER
        elif self.tokens[self.currentToken].type == "IDENTIFIER":
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            id = self.tokens[self.currentToken].lexeme
            token = self.tokens[self.currentToken]
            self.match ("factor", "IDENTIFIER")
            lhs = IdentifierExpressionNode (id, token, line, column)
        # list creator operator  
        # <factor> -> '[' [ [ <assignExpression> { COMMA <assignExpression> } ] ] ']'
        elif self.tokens[self.currentToken].type == "LBRACKET":
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
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
            lhs = ListConstructorExpressionNode (items, line, column)
        # <factor> -> NEW ( TYPE '[' <expr> ']' { '[' <expr> ']' } | IDENTIFIER ( '[' <expr> ']' { '[' <expr> ']' } | '(' <args> ')' ) ) 
        elif self.tokens[self.currentToken].type == "NEW":
            line = self.tokens[self.currentToken].line
            column = self.tokens[self.currentToken].column
            self.match ("factor", "NEW")
            # primitive type array allocator 
            if self.isType ():
                type = None
                # <typeSpecifier> -> INTTYPE
                if (self.tokens[self.currentToken].type == 'INTTYPE'):
                    type = TypeSpecifierNode (Type.INT, "int", self.tokens[self.currentToken])
                    self.match ("factor", 'INTTYPE')
                # <typeSpecifier> -> FLOATTYPE
                elif (self.tokens[self.currentToken].type == 'FLOATTYPE'):
                    type = TypeSpecifierNode (Type.FLOAT, "float", self.tokens[self.currentToken])
                    self.match ("factor", 'FLOATTYPE')
                # <typeSpecifier> -> CHARTYPE
                elif (self.tokens[self.currentToken].type == 'CHARTYPE'):
                    type = TypeSpecifierNode (Type.CHAR, "char", self.tokens[self.currentToken])
                    self.match ("factor", 'CHARTYPE')
                # <typeSpecifier> -> BOOLTYPE
                elif (self.tokens[self.currentToken].type == 'BOOLTYPE'):
                    type = TypeSpecifierNode (Type.BOOL, "bool", self.tokens[self.currentToken])
                    self.match ("factor", 'BOOLTYPE')
                # <typeSpecifier> -> STRINGTYPE
                elif (self.tokens[self.currentToken].type == 'STRINGTYPE'):
                    type = TypeSpecifierNode (Type.STRING, "string", self.tokens[self.currentToken])
                    self.match ("factor", 'STRINGTYPE')
                # <typeSpecifier> -> VOIDTYPE
                elif (self.tokens[self.currentToken].type == 'VOIDTYPE'):
                    type = TypeSpecifierNode (Type.VOID, "void", self.tokens[self.currentToken])
                    self.match ("factor", 'VOIDTYPE')
                else:
                    self.error ("factor", "INTTYPE")

                self.match ("factor", "LBRACKET")
                offsets = [self.expression ()]
                type.arrayDimensions += 1
                self.match ("factor", "RBRACKET")

                while (self.tokens[self.currentToken].type == "LBRACKET"):
                    self.match ("factor", "LBRACKET")
                    offsets += [self.expression ()]
                    type.arrayDimensions += 1
                    self.match ("factor", "RBRACKET")

                lhs = ArrayAllocatorExpressionNode (type, offsets, line, column)
            # usertype array alloc or constructor call 
            else:

                type = TypeSpecifierNode (Type.USERTYPE, self.tokens[self.currentToken].lexeme, self.tokens[self.currentToken])
                self.match ("factor", "IDENTIFIER")

                # usertype array
                if (self.tokens[self.currentToken].type == "LBRACKET"):
                    self.match ("factor", "LBRACKET")
                    offsets = [self.expression ()]
                    type.arrayDimensions += 1
                    self.match ("factor", "RBRACKET")

                    while (self.tokens[self.currentToken].type == "LBRACKET"):
                        self.match ("factor", "LBRACKET")
                        offsets += [self.expression ()]
                        type.arrayDimensions += 1
                        self.match ("factor", "RBRACKET")

                    lhs = ArrayAllocatorExpressionNode (type, offsets, line, column)
                # constructor call 
                elif (self.tokens[self.currentToken].type == "LPAREN"):
                    self.match ("factor", "LPAREN")
                    args = []
                    # optional arguments 
                    if self.tokens[self.currentToken].type != "RPAREN":
                        args += [self.assignexpr ()]
                        # 0 or more additional arguments 
                        while self.tokens[self.currentToken].type == "COMMA":
                            self.match ("factor", "COMMA")
                            args += [self.assignexpr ()]
                    self.match ("factor", "RPAREN")

                    lhs = ConstructorCallExpressionNode (type, args, line, column)

                else:
                    self.error ("factor", "LBRACKET", "Expecting an array allocator or class constructor call")

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
