import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_000(self):
        input = """
func foo() int {return foo1();}
var a = foo() + foo1();
func main() {
    putInt(a)
    a := foo()
    putInt(a)
}
func foo1() int {return 1;}
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_001(self):
        input = """
func foo(a int, c int) {
    var b = a + c;
    putInt(b)
}
func main() {
    foo(2, 3)
}
func foo1() int {return 1;}
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_002(self):
        input = """
func main() {
    var a = 1 + 2.0;
    var b = 1.0 > 2.0;
    var c = "vo" + "tien";
    var d = "a" < "b";

    putFloatLn(a)
    putBoolLn(b)
    putStringLn(c)
    putBoolLn(d)
}
"""
        expect = "3.0\nfalse\nvotien\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
        
    def test_003(self):
        input = """
func main() {
    putIntLn(1)
    putFloatLn(1.0)
    putStringLn("TIEN")
    putLn()
}
        """
        expect = "1\n1.0\nTIEN\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    def test_004(self):
        input = """
var a = 1;
func main() {
    b := a + 1;
    putInt(a)
    putInt(b)
}
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    def test_005(self):
        input = """
    func main() {
        var f = true;
        var g boolean;

        putBoolLn(f)
        putBool(g)
    }
        """
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
#     def test_006(self):
#         input = """
# func main() {
#     a := getInt()
#     putInt(a)
# }
#         """
#         expect = "50"
#         self.assertTrue(TestCodeGen.test(input, expect, 506))
        
    def test_007(self):
        input = """
        var a float = 3;
        func main() {
            putFloatLn(a)
            var a float = 4;
            putFloatLn(a)
            a := 2
            putFloat(a)
        }
        """
        expect = "3.0\n4.0\n2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_gllobal_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,513))