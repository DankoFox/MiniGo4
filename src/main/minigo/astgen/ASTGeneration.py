from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):

    ###############################################################################
    #                                                                             #
    #                    Variables, Constants and Function                        #
    #                                                                             #
    ###############################################################################
    def visitProgram(self, ctx: MiniGoParser.ProgramContext): # OK
        return Program(self.visit(ctx.declList()))

    def visitDeclList(self, ctx: MiniGoParser.DeclListContext): # OK
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.declList())

    def visitDecl(self, ctx: MiniGoParser.DeclContext): # OK
        return self.visit(ctx.getChild(0))

    def visitVardecl(self, ctx: MiniGoParser.VardeclContext): # OK
        var_name = ctx.ID().getText()
        var_type = self.visit(ctx.type_()) if ctx.type_() else None
        init_value = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(var_name, var_type, init_value)

    def visitConstdecl(self, ctx: MiniGoParser.ConstdeclContext): # OK
        const_name = ctx.ID().getText()
        const_type = None;
        init_value = self.visit(ctx.expr())
        return ConstDecl(const_name,const_type,init_value)

    def visitFuncdecl(self, ctx: MiniGoParser.FuncdeclContext): # OK
        func_name = ctx.ID().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        return_type = self.visit(ctx.returnType()) if ctx.returnType() else VoidType()
        body = self.visit(ctx.block())

        if ctx.receiver():
            receiver_name, receiver_type = self.visit(ctx.receiver())
            return MethodDecl(receiver_name, receiver_type, FuncDecl(func_name, params, return_type, body))

        return FuncDecl(func_name, params, return_type, body)

    def visitReceiver(self, ctx: MiniGoParser.ReceiverContext): # OK
        receiver_name = ctx.ID(0).getText()
        receiver_type = Id(ctx.ID(1).getText())

        return receiver_name, receiver_type

    def visitStructdecl(self, ctx: MiniGoParser.StructdeclContext): # OK
        struct_name = ctx.ID().getText()
        fields = self.visit(ctx.fieldDeclList()) if ctx.fieldDeclList() else []
        methods =  [] # NOT REALLY EXIST BUT OK

        return StructType(struct_name, fields, methods)

    def visitInterfacedecl(self, ctx: MiniGoParser.InterfacedeclContext): # OK
        interface_name = ctx.ID().getText()
        methods = self.visit(ctx.methodDeclList()) if ctx.methodDeclList() else []
        return InterfaceType(interface_name, methods)

    def visitFieldDeclList(self, ctx: MiniGoParser.FieldDeclListContext): # OK
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.fieldDecl())]
        else:
            return [self.visit(ctx.fieldDecl())] + self.visit(ctx.fieldDeclList())

    def visitFieldDecl(self, ctx: MiniGoParser.FieldDeclContext): # OK
        field_name = ctx.ID().getText()
        field_type = self.visit(ctx.type_())
        return (field_name, field_type)

    def visitMethodDeclList(self, ctx: MiniGoParser.MethodDeclListContext): # OK
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.methodDecl())]
        else:
            return [self.visit(ctx.methodDecl())] + self.visit(ctx.methodDeclList())

    def visitMethodDecl(self, ctx: MiniGoParser.MethodDeclContext): # OK
        method_name = ctx.ID().getText()
        param_decls = self.visit(ctx.paramList()) if ctx.paramList() else []
        param_types = [param.parType for param in param_decls]

        return_type = self.visit(ctx.returnType()) if ctx.returnType() else VoidType()
        return Prototype(method_name, param_types, return_type)

    def visitParamList(self, ctx: MiniGoParser.ParamListContext): # OK
        if ctx.getChildCount() == 1:
            return self.visitParam(ctx.param())
        else:
            return self.visitParam(ctx.param()) + self.visitParamList(ctx.paramList())

    def visitParam(self, ctx: MiniGoParser.ParamContext): # OK
        param_type = self.visit(ctx.type_())

        if ctx.idList():
            ids = self.visit(ctx.idList())
            return [ParamDecl(id_, param_type) for id_ in ids]  
        else:
            id_name = ctx.ID().getText()
            return [ParamDecl(id_name, param_type)]

    def visitIdList(self, ctx: MiniGoParser.IdListContext): # OK
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.idList())

    def visitReturnType(self, ctx: MiniGoParser.ReturnTypeContext): # OK
        return self.visit(ctx.type_())

    ###############################################################################
    #                                                                             #
    #                                  TYPE                                       #
    #                                                                             #
    ###############################################################################

    def visitType_(self, ctx: MiniGoParser.Type_Context): # OK
        return self.visit(ctx.getChild(0))

    def visitPrimitiveType(self, ctx: MiniGoParser.PrimitiveTypeContext): # OK
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()

    def visitArrayType(self, ctx: MiniGoParser.ArrayTypeContext):
        if ctx is None:
            return None  # Safety check
        
        # Get dimension size (integer literal or identifier)
        if ctx.integer_literal():
            dim = self.visit(ctx.integer_literal())  # This returns IntLiteral
        elif ctx.ID():
            dim = Id(ctx.ID().getText())
        else:
            raise Exception("Unexpected array dimension type")

        # Recursively process the inner type
        inner_type = self.visit(ctx.type_())

        # Merge dimensions: If the inner type is already an ArrayType, extend its dimensions
        if isinstance(inner_type, ArrayType):
            return ArrayType([dim] + inner_type.dimens, inner_type.eleType)
        else:
            return ArrayType([dim], inner_type)

    def visitStructType(self, ctx: MiniGoParser.StructTypeContext): # OK
        return Id(ctx.ID().getText())

    def visitInterfaceType(self, ctx: MiniGoParser.InterfaceTypeContext): # OK
        return Id(ctx.ID().getText())

    ###############################################################################
    #                                                                             #
    #                                 EXPRESSION                                  #
    #                                                                             #
    ###############################################################################

    def visitExpr(self, ctx: MiniGoParser.ExprContext): # OK
        return self.visit(ctx.expr1())

    def visitExpr1(self, ctx: MiniGoParser.Expr1Context): # OK
        if ctx.OR():
            op = ctx.OR().getText()
            return BinaryOp(op, self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        return self.visit(ctx.expr2())

    def visitExpr2(self, ctx: MiniGoParser.Expr2Context): # OK
        if ctx.AND():
            op = ctx.AND().getText()
            return BinaryOp(op, self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    def visitExpr3(self, ctx: MiniGoParser.Expr3Context): # OK
        op = None
        if ctx.EQUALS(): op = ctx.EQUALS().getText()
        elif ctx.NOT_EQUALS(): op = ctx.NOT_EQUALS().getText()
        elif ctx.LESS_THAN(): op = ctx.LESS_THAN().getText()
        elif ctx.LESS_THAN_EQ(): op = ctx.LESS_THAN_EQ().getText()
        elif ctx.GREATER_THAN(): op = ctx.GREATER_THAN().getText()
        elif ctx.GREATER_THAN_EQ(): op = ctx.GREATER_THAN_EQ().getText()

        if op:
            return BinaryOp(op, self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())

    def visitExpr4(self, ctx: MiniGoParser.Expr4Context): # OK
        op = None
        if ctx.ADD(): op = ctx.ADD().getText()
        elif ctx.SUB(): op = ctx.SUB().getText()

        if op:
            return BinaryOp(op, self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    def visitExpr5(self, ctx: MiniGoParser.Expr5Context): # OK
        op = None
        if ctx.MUL(): op = ctx.MUL().getText()
        elif ctx.DIV(): op = ctx.DIV().getText()
        elif ctx.MOD(): op = ctx.MOD().getText()

        if op:
            return BinaryOp(op, self.visit(ctx.expr5()), self.visit(ctx.expr6()))
        return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: MiniGoParser.Expr6Context): # OK
        op = None
        if ctx.NOT(): op = ctx.NOT().getText()
        elif ctx.SUB(): op = ctx.SUB().getText()

        if op:
            return UnaryOp(op, self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    def visitExpr7(self, ctx: MiniGoParser.Expr7Context):
        if ctx.LBRACKET():  # Array Access - OK
            #return ArrayCell(self.visit(ctx.expr7()), [self.visit(ctx.expr())])
            base = self.visit(ctx.expr7())  # Get the base array
            indices = [self.visit(ctx.expr())]  # Collect indices
            while isinstance(base, ArrayCell):  # Flatten nested ArrayCell
                indices = base.idx + indices  # Append previous indices
                base = base.arr  # Get the base array reference
            return ArrayCell(base, indices)
            
        elif ctx.DOT() and ctx.LPAREN():  # Method Call - OK
            return MethCall(self.visit(ctx.expr7()), ctx.ID().getText(), self.visit(ctx.argList()) if ctx.argList() else [])
        elif ctx.DOT():  # Struct Field Access - OK
            return FieldAccess(self.visit(ctx.expr7()), ctx.ID().getText())
        elif ctx.ID() and ctx.LPAREN():  # Function Call - FIXED: Only call FuncCall if there's an ID before LPAREN
            return FuncCall(ctx.ID().getText(), self.visit(ctx.argList()) if ctx.argList() else [])
        elif ctx.LPAREN() and ctx.expr():  # Parenthesized Expression - FIXED
            return self.visit(ctx.expr())
        elif ctx.ID():  # Identifier - OK
            return Id(ctx.ID().getText())
        elif ctx.literals():  # Literals (int, string, etc.) - OK
            return self.visit(ctx.literals())


    def visitExprList(self, ctx: MiniGoParser.ExprListContext): # OK
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprList())
        return [self.visit(ctx.expr())]

    ###############################################################################
    #                                                                             #
    #                                 LITERALS                                    #
    #                                                                             #
    ###############################################################################

    def visitLiterals(self, ctx: MiniGoParser.LiteralsContext): # OK
        if ctx.integer_literal():
            return self.visit(ctx.integer_literal())
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.bool_literal():
            return self.visit(ctx.bool_literal())
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.NIL():
            return NilLiteral()

    def visitInteger_literal(self, ctx: MiniGoParser.Integer_literalContext): # OK
        return IntLiteral(int(ctx.getText(),0))

    def visitBool_literal(self, ctx: MiniGoParser.Bool_literalContext): # OK
        return BooleanLiteral(ctx.getText() == "true")

    ######### ARRAY LITERAL - NOT SURE #########

    def visitArray_literal(self, ctx: MiniGoParser.Array_literalContext):
        array_type = self.visit(ctx.arrayType())
        dimens = array_type.dimens
        eleType = array_type.eleType
        value = self.visit(ctx.arrayContentList()) if ctx.arrayContentList() else []
        return ArrayLiteral(dimens, eleType, value)

    def visitArrayContentList(self, ctx: MiniGoParser.ArrayContentListContext):
        if ctx.COMMA():
            return [self.visit(ctx.arrayContent())] + self.visit(ctx.arrayContentList())
        return [self.visit(ctx.arrayContent())]

    def visitArrayContent(self, ctx: MiniGoParser.ArrayContentContext):
        if ctx.integer_literal():
            return self.visit(ctx.integer_literal())
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.bool_literal():
            return self.visit(ctx.bool_literal())
        elif ctx.array_literal_shorthand():
            return self.visit(ctx.array_literal_shorthand())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.NIL():
            return NilLiteral()

    def visitArray_literal_shorthand(self, ctx: MiniGoParser.Array_literal_shorthandContext):
        return self.visit(ctx.arrayContentList()) if ctx.arrayContentList() else []

    ######### STRUCT LITERAL #########

    def visitStruct_literal(self, ctx: MiniGoParser.Struct_literalContext):
        struct_name = ctx.ID().getText()
        elements = self.visit(ctx.fieldInitList()) if ctx.fieldInitList() else []
        return StructLiteral(struct_name, elements)

    def visitFieldInitList(self, ctx: MiniGoParser.FieldInitListContext):
        if ctx.COMMA():
            return [self.visit(ctx.fieldInit())] + self.visit(ctx.fieldInitList())
        return [self.visit(ctx.fieldInit())]

    def visitFieldInit(self, ctx: MiniGoParser.FieldInitContext):
        field_name = ctx.ID().getText()
        expr_value = self.visit(ctx.expr())
        return (field_name, expr_value)  # Return as tuple

    ######### Function & Method Calls #########

    def visitFunctionCall(self, ctx: MiniGoParser.FunctionCallContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.argList()) if ctx.argList() else [])

    def visitMethodCall(self, ctx: MiniGoParser.MethodCallContext):
        return MethCall(self.visit(ctx.expr()), ctx.ID().getText(), self.visit(ctx.argList()) if ctx.argList() else [])

    def visitArgList(self, ctx: MiniGoParser.ArgListContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.argList())
        return [self.visit(ctx.expr())]

    ###############################################################################
    #                                                                             #
    #                               STATEMENTS                                    #
    #                                                                             #
    ###############################################################################

    def visitStatement(self, ctx):
        if ctx.vardecl(): # DONE
            return self.visit(ctx.vardecl())
        elif ctx.constdecl(): # DONE
            return self.visit(ctx.constdecl())
        elif ctx.assignmentStatement(): # DONE
            return self.visit(ctx.assignmentStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.breakStatement(): # DONE
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement(): # DONE
            return self.visit(ctx.continueStatement())
        elif ctx.callStatement(): # DONE
            return self.visit(ctx.callStatement())
        elif ctx.returnStatement(): # DONE
            return self.visit(ctx.returnStatement())
        elif ctx.block(): # DONE
            return self.visit(ctx.block())
        elif ctx.expr(): # DONE
            return self.visit(ctx.expr())
        else:
            return None

    def visitBreakStatement(self, ctx):
        return Break()

    def visitContinueStatement(self, ctx):
        return Continue()

    def visitReturnStatement(self, ctx):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)

    def visitBlock(self, ctx):
        statements = self.visit(ctx.statementList()) if ctx.statementList() else []
        return Block(statements)

    def visitStatementList(self, ctx):
        if ctx.statementList():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementList())
        return [self.visit(ctx.statement())]

    def visitCallStatement(self, ctx):
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.methodCall():
            return self.visit(ctx.methodCall())

    def visitAssignmentStatement(self, ctx):
        lhs = self.visit(ctx.expr7())  # LHS (variable, array cell, or field access)
        rhs = self.visit(ctx.expr())    # RHS (expression to assign)
        op = ctx.assignmentOperator().getText()

        if op == ":=":
            return Assign(lhs, rhs)
        else:
            # Convert compound assignment (+=, -=, etc.) into explicit binary operations
            bin_op = op[0]  # Extract the first character of +=, -=, etc.
            new_rhs = BinaryOp(bin_op, lhs, rhs)
            return Assign(lhs, new_rhs)

    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.block())
        else_stmt = self.visit(ctx.elseChain()) if ctx.elseChain() else None
        return If(cond, then_stmt, else_stmt)

    def visitElseChain(self, ctx):
        if ctx.IF():
            else_stmt = self.visit(ctx.elseChain()) if ctx.elseChain() else None
            return If(self.visit(ctx.expr()), self.visit(ctx.block()), else_stmt)
        else:
            return self.visit(ctx.block())

    def visitForStatement(self, ctx):
        loop_body = self.visit(ctx.block())  # Retrieve the loop body at the forStatement level
        
        if ctx.forCondition():
            cond = self.visit(ctx.forCondition())
            return ForBasic(cond, loop_body)

        elif ctx.forCStyle():
            init, cond, upda = self.visit(ctx.forCStyle())
            return ForStep(init, cond, upda, loop_body)

        elif ctx.forRange():
            idx, value, arr = self.visit(ctx.forRange())
            return ForEach(idx, value, arr, loop_body)

    def visitForCondition(self, ctx):
        return self.visit(ctx.expr())  # Just return the condition

    def visitForCStyle(self, ctx):
        init = self.visit(ctx.init())  # Visit either VarInit or AssignInit
        cond = self.visit(ctx.expr())
        upda = self.visit(ctx.update())

        return init, cond, upda  # Return all three parts without the loop body

    def visitInit(self, ctx):
        if ctx.assignExpr():
            return self.visit(ctx.assignExpr())

        return VarDecl(ctx.ID().getText(), self.visit(ctx.type_()) if ctx.type_() else None, self.visit(ctx.expr()))

    def visitUpdate(self, ctx):
        return self.visit(ctx.assignExpr())

    def visitAssignExpr(self, ctx):
        lhs = self.visit(ctx.expr7())  # LHS (variable, array cell, or field access)
        rhs = self.visit(ctx.expr())    # RHS (expression to assign)
        op = ctx.assignmentOperator().getText()

        if op == ":=":
            return Assign(lhs, rhs)
        else:
            # Convert compound assignment (+=, -=, etc.) into explicit binary operations
            bin_op = op[0]  # Extract the first character of +=, -=, etc.
            new_rhs = BinaryOp(bin_op, lhs, rhs)
            return Assign(lhs, new_rhs)

    def visitForRange(self, ctx):
        idx = Id(ctx.ID(0).getText()) if ctx.ID(0) else Id("_")
        value = Id(ctx.ID(1).getText())
        arr = self.visit(ctx.expr())

        return idx, value, arr  # Return only necessary information
