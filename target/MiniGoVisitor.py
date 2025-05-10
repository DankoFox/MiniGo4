# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declList.
    def visitDeclList(self, ctx:MiniGoParser.DeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDeclList.
    def visitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDecl.
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDeclList.
    def visitMethodDeclList(self, ctx:MiniGoParser.MethodDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramList.
    def visitParamList(self, ctx:MiniGoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idList.
    def visitIdList(self, ctx:MiniGoParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnType.
    def visitReturnType(self, ctx:MiniGoParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprList.
    def visitExprList(self, ctx:MiniGoParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#integer_literal.
    def visitInteger_literal(self, ctx:MiniGoParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#bool_literal.
    def visitBool_literal(self, ctx:MiniGoParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayContent.
    def visitArrayContent(self, ctx:MiniGoParser.ArrayContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayContentList.
    def visitArrayContentList(self, ctx:MiniGoParser.ArrayContentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal_shorthand.
    def visitArray_literal_shorthand(self, ctx:MiniGoParser.Array_literal_shorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldInitList.
    def visitFieldInitList(self, ctx:MiniGoParser.FieldInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldInit.
    def visitFieldInit(self, ctx:MiniGoParser.FieldInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionCall.
    def visitFunctionCall(self, ctx:MiniGoParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCall.
    def visitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argList.
    def visitArgList(self, ctx:MiniGoParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MiniGoParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseChain.
    def visitElseChain(self, ctx:MiniGoParser.ElseChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCStyle.
    def visitForCStyle(self, ctx:MiniGoParser.ForCStyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignExpr.
    def visitAssignExpr(self, ctx:MiniGoParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRange.
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList.
    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_.
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitiveType.
    def visitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)



del MiniGoParser