# Amy Script Compiler
# By Amy Burnett
# April 11 2021
# ========================================================================

if __name__ == "template":
    from ast import *
    from visitor import ASTVisitor
else:
    from .ast import *
    from .visitor import ASTVisitor

# ========================================================================
# Scans through a template instance and replaces template aliases with 
# their overridden new type 
# ** nested template functions with the same template parameter names will shadow 
# the parent template 
# ** if a template parameter has the same name as an existing type in a parent scope
# then that existing type is shadowed 

class TemplateVisitor (ASTVisitor):

    def __init__(self, templateParameterAliases, templateParameterOverrides):
        # zip alias and override type into a map
        self.templateParameters = {}
        # alias and overrides should be same size 
        # and aliases should be unique 
        for i in range(len(templateParameterAliases)):
            self.templateParameters[templateParameterAliases[i].type.id] = templateParameterOverrides[i]

    def visitProgramNode (self, node):
        for codeunit in node.codeunits:
            if codeunit != None:
                codeunit.accept (self)

    def visitTypeSpecifierNode (self, node):
        # print (f"[template] {node} ",end="")
        # visit templateParams
        # for case of 
        #   public field Node<:T:> header;
        # where T is the template param to overwrite 
        # and Node<:T:> is the type specifier we are currently at 
        for tparam in node.templateParams:
            tparam.accept (self)
        # is a template alias 
        if node.id in self.templateParameters:
            # assign type 
            id = node.id
            node.type =            self.templateParameters[id].type
            node.id =              self.templateParameters[id].id
            node.token =           self.templateParameters[id].token
            # replaced type should keep its array dimensions 
            # example: T[] (where T is replaced with int) should be int[]
            # example: T[] (where T is replaced with float[]) should be float[][]
            #   NOTE: the first [] refers to the T[] and the second comes from the float[] 
            node.arrayDimensions = self.templateParameters[id].arrayDimensions + node.arrayDimensions
            node.decl =            self.templateParameters[id].decl
            node.isGeneric =       self.templateParameters[id].isGeneric

            # # copy over template params 
            for tparam in self.templateParameters[id].templateParams:
                node.templateParams += [tparam.copy ()]
        # print (f"-> {node}")


    def visitParameterNode (self, node):
        node.type.accept (self)

    def visitCodeUnitNode (self, node):
        pass

    def visitVariableDeclarationNode (self, node):
        node.type.accept (self)

    def visitFunctionNode (self, node):
        node.type.accept (self)
        for p in node.params:
            p.type.accept (self)
        node.body.accept (self)

    def visitClassDeclarationNode(self, node):
        # eval fields first to add to scope 
        for field in node.fields:
            field.accept (self)

        for ctor in node.constructors:
            ctor.accept (self)
        
        for method in node.methods:
            method.accept (self)
        
        for method in node.virtualMethods:
            method.accept (self)

    def visitFieldDeclarationNode (self, node):
        node.type.accept (self)

    def visitMethodDeclarationNode (self, node):
        node.type.accept (self)

        for p in node.params:
            p.type.accept (self)

        node.body.accept (self)

    def visitConstructorDeclarationNode (self, node):
        for p in node.params:
            p.type.accept (self)

        node.body.accept (self)

    def visitEnumDeclarationNode (self, node):
        pass

    def visitFunctionTemplateNode (self, node):

        # shadow any overridden template parameters 
        # check for same template param alias
        shadowedAliases = {}
        for alias in self.templateParameters:
            for other in node.types:
                # overrides alias
                if alias == other.id:
                    # shadow alias 
                    shadowedAliases[alias] = self.templateParameters[alias]
        # remove shadowed aliases 
        for alias in shadowedAliases:
            self.templateParameters.pop (alias)

        # check function template without shadowed aliases 
        node.function.accept (self)

        # add shadowed aliases back 
        for shadowedAlias in shadowedAliases:
            self.templateParameters[shadowedAlias] = shadowedAliases[shadowedAlias]

    def visitClassTemplateDeclarationNode (self, node):
        pass
        # # shadow any overridden template parameters 
        # # check for same template param alias
        # shadowedAliases = {}
        # for alias in self.templateParameters:
        #     for other in node.types:
        #         # overrides alias
        #         if alias == other.id:
        #             # shadow alias 
        #             shadowedAliases[alias] = self.templateParameters[alias]
        # # remove shadowed aliases 
        # for alias in shadowedAliases:
        #     self.templateParameters.pop (alias)

        # # check function template without shadowed aliases 
        # node.function.accept (self)

        # # add shadowed aliases back 
        # for shadowedAlias in shadowedAliases:
        #     self.templateParameters[shadowedAlias] = shadowedAliases[shadowedAlias]

    def visitStatementNode (self, node):
        pass

    def visitIfStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)
        
        for e in node.elifs:
            e.accept (self)

        if node.elseStmt != None:
            node.elseStmt.accept (self)

    def visitElifStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)

    def visitElseStatementNode (self, node):
        node.body.accept (self)

    def visitForStatementNode (self, node):
        node.init.accept (self)
        node.cond.accept (self)
        node.update.accept (self)
        node.body.accept (self)

        if node.elseStmt:
            node.elseStmt.accept (self)

    def visitWhileStatementNode (self, node):
        node.cond.accept (self)
        node.body.accept (self)

    def visitExpressionStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)

    def visitReturnStatementNode (self, node):
        if node.expr != None:
            node.expr.accept (self)

    def visitContinueStatementNode (self, node):
        pass

    def visitBreakStatementNode (self, node):
        pass

    def visitCodeBlockNode (self, node):
        for unit in node.codeunits:
            unit.accept (self)

    def visitExpressionNode (self, node):
        pass

    def visitTupleExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitAssignExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

        node.type = node.lhs.type

    def visitLogicalOrExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

    def visitLogicalAndExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

    def visitEqualityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

    def visitInequalityExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        
        # results in true/false which is an int 
        node.type = TypeSpecifierNode (Type.INT, "int", None)

    def visitAdditiveExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        node.type = node.lhs.type

    def visitMultiplicativeExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)
        node.type = node.lhs.type

    def visitUnaryLeftExpressionNode (self, node):
        node.rhs.accept (self)
        node.type = node.rhs.type 

    def visitPostIncrementExpressionNode(self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

    def visitPostDecrementExpressionNode (self, node):
        node.lhs.accept (self)
        node.type = node.lhs.type

    def visitSubscriptExpressionNode (self, node):
        node.lhs.accept (self)

        # the type for this is lhs - 1 dimension
        node.type = node.lhs.type.copy()

        node.type.arrayDimensions = node.lhs.type.arrayDimensions - 1

        node.type.accept (self)
        node.offset.accept (self)

    def visitFunctionCallExpressionNode (self, node):
        # default construct template type 
        if isinstance(node.function, IdentifierExpressionNode) and node.function.id in self.templateParameters:
            # print (f"default constructor for template parameter '{node.function.id}'")

            templateParam = self.templateParameters[node.function.id]

            # ARRAY -> null
            if templateParam.arrayDimensions > 0:
                # print (f"array default constructor,     {templateParam}")
                node.function.id = "null"

            # OBJECT TYPE -> ctor for object
            elif templateParam.type == Type.USERTYPE:
                # print (f"object default constructor,    {templateParam}")
                # node = ConstructorCallExpressionNode (templateParam, templateParam.id, node.args, node.templateParams, node.lineNumber, node.columnNumber)
                node.function.id = f"{templateParam}::{templateParam.id}"

            # PRIMITIVE TYPE
            else:
                # print (f"primitive default constructor, {templateParam}")
                node.function.id = templateParam.id


        # eval arguments to get types 
        for arg in node.args:
            arg.accept (self)

        # template parameter in funcall could be a template alias 
        # example:
        # template <:T:>
        # function T sum (T a, T b)
        # {
        #   return add<:T:> (a, b);
        # }
        for targ in node.templateParams:
            targ.accept (self)

    # not evaluated at this stage 
    def visitMemberAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitFieldAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitMethodAccessorExpressionNode (self, node):
        node.lhs.accept (self)
        node.rhs.accept (self)

    def visitThisExpressionNode (self, node):
        node.type.accept (self)

    def visitIdentifierExpressionNode (self, node):
        pass

    def visitArrayAllocatorExpressionNode (self, node):
        node.type.accept (self)
        for d in node.dimensions:
            d.accept (self)

    def visitConstructorCallExpressionNode (self, node):
        node.type.accept (self)
        # eval arguments
        for arg in node.args:
            arg.accept (self)
    
    def visitSizeofExpressionNode(self, node):
        node.rhs.accept (self)
    
    def visitFreeExpressionNode (self, node):
        node.rhs.accept (self)

    def visitIntLiteralExpressionNode (self, node):
        pass

    def visitFloatLiteralExpressionNode (self, node):
        pass

    def visitCharLiteralExpressionNode (self, node):
        pass

    def visitStringLiteralExpressionNode (self, node):
        pass

    def visitListConstructorExpressionNode (self, node):
        for elem in node.elems:
            elem.accept (self)

    def visitNullExpressionNode (self, node):
        pass


# ========================================================================