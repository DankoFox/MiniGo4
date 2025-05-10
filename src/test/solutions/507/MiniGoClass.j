.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a <class 'AST.FloatType'>

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a <class 'AST.FloatType'>
	invokestatic io/putFloatLn(<class 'AST.FloatType'>)V
.var 1 is a <class 'AST.FloatType'> from Label2 to Label3
	iconst_4
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(<class 'AST.FloatType'>)V
	iconst_2
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloat(<class 'AST.FloatType'>)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
	iconst_3
	i2f
	putstatic MiniGoClass/a <class 'AST.FloatType'>
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
