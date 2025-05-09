# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01f7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\7\3\u009a\n\3\f\3\16\3\u009d\13\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\7\4\u00a6\n\4\f\4\16\4\u00a9\13\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\58\u0171\n8\38\3")
        buf.write("8\58\u0175\n8\39\39\39\79\u017a\n9\f9\169\u017d\139\5")
        buf.write("9\u017f\n9\3:\3:\3:\6:\u0184\n:\r:\16:\u0185\3;\3;\3;")
        buf.write("\6;\u018b\n;\r;\16;\u018c\3<\3<\3<\6<\u0192\n<\r<\16<")
        buf.write("\u0193\3=\3=\3>\3>\5>\u019a\n>\3>\6>\u019d\n>\r>\16>\u019e")
        buf.write("\3?\6?\u01a2\n?\r?\16?\u01a3\3?\3?\7?\u01a8\n?\f?\16?")
        buf.write("\u01ab\13?\3?\5?\u01ae\n?\3?\3?\6?\u01b2\n?\r?\16?\u01b3")
        buf.write("\3?\5?\u01b7\n?\5?\u01b9\n?\3@\3@\7@\u01bd\n@\f@\16@\u01c0")
        buf.write("\13@\3A\3A\5A\u01c4\nA\3B\3B\3B\3C\3C\7C\u01cb\nC\fC\16")
        buf.write("C\u01ce\13C\3C\3C\3D\3D\7D\u01d4\nD\fD\16D\u01d7\13D\3")
        buf.write("D\3D\3D\5D\u01dc\nD\3D\3D\3E\3E\3E\3F\3F\7F\u01e5\nF\f")
        buf.write("F\16F\u01e8\13F\3F\3F\3F\3G\3G\3H\6H\u01f0\nH\rH\16H\u01f1")
        buf.write("\3H\3H\3I\3I\3\u00a7\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}>\177?\u0081\2\u0083")
        buf.write("\2\u0085@\u0087A\u0089\2\u008bB\u008dC\u008fD\u0091E\3")
        buf.write("\2\23\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2QQqq\3\2\629\4")
        buf.write("\2ZZzz\5\2\62;CHch\4\2DDdd\3\2\62\63\4\2GGgg\4\2--//\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^\7\2$$^^ppt")
        buf.write("tvv\3\3\f\f\5\2\13\13\17\17\"\"\2\u020a\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2")
        buf.write("\2\5\u0095\3\2\2\2\7\u00a0\3\2\2\2\t\u00af\3\2\2\2\13")
        buf.write("\u00b2\3\2\2\2\r\u00b7\3\2\2\2\17\u00bb\3\2\2\2\21\u00c2")
        buf.write("\3\2\2\2\23\u00c7\3\2\2\2\25\u00cc\3\2\2\2\27\u00d3\3")
        buf.write("\2\2\2\31\u00dd\3\2\2\2\33\u00e4\3\2\2\2\35\u00e8\3\2")
        buf.write("\2\2\37\u00ee\3\2\2\2!\u00f6\3\2\2\2#\u00fc\3\2\2\2%\u0100")
        buf.write("\3\2\2\2\'\u0109\3\2\2\2)\u010f\3\2\2\2+\u0115\3\2\2\2")
        buf.write("-\u011a\3\2\2\2/\u0120\3\2\2\2\61\u0124\3\2\2\2\63\u0126")
        buf.write("\3\2\2\2\65\u0128\3\2\2\2\67\u012a\3\2\2\29\u012c\3\2")
        buf.write("\2\2;\u012e\3\2\2\2=\u0131\3\2\2\2?\u0134\3\2\2\2A\u0136")
        buf.write("\3\2\2\2C\u0139\3\2\2\2E\u013b\3\2\2\2G\u013e\3\2\2\2")
        buf.write("I\u0141\3\2\2\2K\u0144\3\2\2\2M\u0146\3\2\2\2O\u0148\3")
        buf.write("\2\2\2Q\u014b\3\2\2\2S\u014e\3\2\2\2U\u0151\3\2\2\2W\u0154")
        buf.write("\3\2\2\2Y\u0157\3\2\2\2[\u015a\3\2\2\2]\u015c\3\2\2\2")
        buf.write("_\u015e\3\2\2\2a\u0160\3\2\2\2c\u0162\3\2\2\2e\u0164\3")
        buf.write("\2\2\2g\u0166\3\2\2\2i\u0168\3\2\2\2k\u016a\3\2\2\2m\u016c")
        buf.write("\3\2\2\2o\u0174\3\2\2\2q\u017e\3\2\2\2s\u0180\3\2\2\2")
        buf.write("u\u0187\3\2\2\2w\u018e\3\2\2\2y\u0195\3\2\2\2{\u0197\3")
        buf.write("\2\2\2}\u01b8\3\2\2\2\177\u01ba\3\2\2\2\u0081\u01c3\3")
        buf.write("\2\2\2\u0083\u01c5\3\2\2\2\u0085\u01c8\3\2\2\2\u0087\u01d1")
        buf.write("\3\2\2\2\u0089\u01df\3\2\2\2\u008b\u01e2\3\2\2\2\u008d")
        buf.write("\u01ec\3\2\2\2\u008f\u01ef\3\2\2\2\u0091\u01f5\3\2\2\2")
        buf.write("\u0093\u0094\7a\2\2\u0094\4\3\2\2\2\u0095\u0096\7\61\2")
        buf.write("\2\u0096\u0097\7\61\2\2\u0097\u009b\3\2\2\2\u0098\u009a")
        buf.write("\n\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u009f\b\3\2\2\u009f\6\3\2\2")
        buf.write("\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a7")
        buf.write("\3\2\2\2\u00a3\u00a6\5\7\4\2\u00a4\u00a6\13\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00aa\3")
        buf.write("\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7,\2\2\u00ab\u00ac")
        buf.write("\7\61\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\b\4\2\2\u00ae")
        buf.write("\b\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7h\2\2\u00b1")
        buf.write("\n\3\2\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7n\2\2\u00b4")
        buf.write("\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\f\3\2\2\2\u00b7")
        buf.write("\u00b8\7h\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\16\3\2\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\u00be\7v\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7p\2\2\u00c1\20\3\2\2\2\u00c2\u00c3\7h\2\2\u00c3")
        buf.write("\u00c4\7w\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7e\2\2\u00c6")
        buf.write("\22\3\2\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7{\2\2\u00c9")
        buf.write("\u00ca\7r\2\2\u00ca\u00cb\7g\2\2\u00cb\24\3\2\2\2\u00cc")
        buf.write("\u00cd\7u\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7w\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\26\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7v\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("\u00d9\7h\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7e\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7u\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7k\2\2\u00e1")
        buf.write("\u00e2\7p\2\2\u00e2\u00e3\7i\2\2\u00e3\32\3\2\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7v\2\2\u00e7")
        buf.write("\34\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7q\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7v\2\2\u00ed")
        buf.write("\36\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7c\2\2\u00f4\u00f5\7p\2\2\u00f5 \3\2\2\2\u00f6")
        buf.write("\u00f7\7e\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7u\2\2\u00fa\u00fb\7v\2\2\u00fb\"\3\2\2\2\u00fc")
        buf.write("\u00fd\7x\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("$\3\2\2\2\u0100\u0101\7e\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7v\2\2\u0104\u0105\7k\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\u0107\7w\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("&\3\2\2\2\u0109\u010a\7d\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e\7m\2\2\u010e")
        buf.write("(\3\2\2\2\u010f\u0110\7t\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7i\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("*\3\2\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write("\u0118\7w\2\2\u0118\u0119\7g\2\2\u0119,\3\2\2\2\u011a")
        buf.write("\u011b\7h\2\2\u011b\u011c\7c\2\2\u011c\u011d\7n\2\2\u011d")
        buf.write("\u011e\7u\2\2\u011e\u011f\7g\2\2\u011f.\3\2\2\2\u0120")
        buf.write("\u0121\7p\2\2\u0121\u0122\7k\2\2\u0122\u0123\7n\2\2\u0123")
        buf.write("\60\3\2\2\2\u0124\u0125\7-\2\2\u0125\62\3\2\2\2\u0126")
        buf.write("\u0127\7/\2\2\u0127\64\3\2\2\2\u0128\u0129\7,\2\2\u0129")
        buf.write("\66\3\2\2\2\u012a\u012b\7\61\2\2\u012b8\3\2\2\2\u012c")
        buf.write("\u012d\7\'\2\2\u012d:\3\2\2\2\u012e\u012f\7?\2\2\u012f")
        buf.write("\u0130\7?\2\2\u0130<\3\2\2\2\u0131\u0132\7#\2\2\u0132")
        buf.write("\u0133\7?\2\2\u0133>\3\2\2\2\u0134\u0135\7>\2\2\u0135")
        buf.write("@\3\2\2\2\u0136\u0137\7>\2\2\u0137\u0138\7?\2\2\u0138")
        buf.write("B\3\2\2\2\u0139\u013a\7@\2\2\u013aD\3\2\2\2\u013b\u013c")
        buf.write("\7@\2\2\u013c\u013d\7?\2\2\u013dF\3\2\2\2\u013e\u013f")
        buf.write("\7(\2\2\u013f\u0140\7(\2\2\u0140H\3\2\2\2\u0141\u0142")
        buf.write("\7~\2\2\u0142\u0143\7~\2\2\u0143J\3\2\2\2\u0144\u0145")
        buf.write("\7#\2\2\u0145L\3\2\2\2\u0146\u0147\7?\2\2\u0147N\3\2\2")
        buf.write("\2\u0148\u0149\7-\2\2\u0149\u014a\7?\2\2\u014aP\3\2\2")
        buf.write("\2\u014b\u014c\7/\2\2\u014c\u014d\7?\2\2\u014dR\3\2\2")
        buf.write("\2\u014e\u014f\7,\2\2\u014f\u0150\7?\2\2\u0150T\3\2\2")
        buf.write("\2\u0151\u0152\7\61\2\2\u0152\u0153\7?\2\2\u0153V\3\2")
        buf.write("\2\2\u0154\u0155\7\'\2\2\u0155\u0156\7?\2\2\u0156X\3\2")
        buf.write("\2\2\u0157\u0158\7<\2\2\u0158\u0159\7?\2\2\u0159Z\3\2")
        buf.write("\2\2\u015a\u015b\7*\2\2\u015b\\\3\2\2\2\u015c\u015d\7")
        buf.write("+\2\2\u015d^\3\2\2\2\u015e\u015f\7}\2\2\u015f`\3\2\2\2")
        buf.write("\u0160\u0161\7\177\2\2\u0161b\3\2\2\2\u0162\u0163\7]\2")
        buf.write("\2\u0163d\3\2\2\2\u0164\u0165\7_\2\2\u0165f\3\2\2\2\u0166")
        buf.write("\u0167\7.\2\2\u0167h\3\2\2\2\u0168\u0169\7=\2\2\u0169")
        buf.write("j\3\2\2\2\u016a\u016b\7<\2\2\u016bl\3\2\2\2\u016c\u016d")
        buf.write("\7\60\2\2\u016dn\3\2\2\2\u016e\u0175\5i\65\2\u016f\u0171")
        buf.write("\7\17\2\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0173\7\f\2\2\u0173\u0175\b8\3\2")
        buf.write("\u0174\u016e\3\2\2\2\u0174\u0170\3\2\2\2\u0175p\3\2\2")
        buf.write("\2\u0176\u017f\7\62\2\2\u0177\u017b\t\3\2\2\u0178\u017a")
        buf.write("\t\4\2\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017f\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017e\u0176\3\2\2\2\u017e\u0177\3")
        buf.write("\2\2\2\u017fr\3\2\2\2\u0180\u0181\7\62\2\2\u0181\u0183")
        buf.write("\t\5\2\2\u0182\u0184\t\6\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186t\3\2\2\2\u0187\u0188\7\62\2\2\u0188\u018a\t\7\2")
        buf.write("\2\u0189\u018b\t\b\2\2\u018a\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("v\3\2\2\2\u018e\u018f\7\62\2\2\u018f\u0191\t\t\2\2\u0190")
        buf.write("\u0192\t\n\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194x\3\2\2")
        buf.write("\2\u0195\u0196\t\4\2\2\u0196z\3\2\2\2\u0197\u0199\t\13")
        buf.write("\2\2\u0198\u019a\t\f\2\2\u0199\u0198\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a\u019c\3\2\2\2\u019b\u019d\5y=\2\u019c\u019b")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f|\3\2\2\2\u01a0\u01a2\5y=\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a9\7")
        buf.write("\60\2\2\u01a6\u01a8\5y=\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\5{>\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b9\3\2\2\2")
        buf.write("\u01af\u01b1\7\60\2\2\u01b0\u01b2\5y=\2\u01b1\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b7\5{>\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8")
        buf.write("\u01a1\3\2\2\2\u01b8\u01af\3\2\2\2\u01b9~\3\2\2\2\u01ba")
        buf.write("\u01be\t\r\2\2\u01bb\u01bd\t\16\2\2\u01bc\u01bb\3\2\2")
        buf.write("\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u0080\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c4\n\17\2\2\u01c2\u01c4\5\u0083B\2\u01c3\u01c1\3\2")
        buf.write("\2\2\u01c3\u01c2\3\2\2\2\u01c4\u0082\3\2\2\2\u01c5\u01c6")
        buf.write("\7^\2\2\u01c6\u01c7\t\20\2\2\u01c7\u0084\3\2\2\2\u01c8")
        buf.write("\u01cc\7$\2\2\u01c9\u01cb\5\u0081A\2\u01ca\u01c9\3\2\2")
        buf.write("\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf")
        buf.write("\u01d0\7$\2\2\u01d0\u0086\3\2\2\2\u01d1\u01d5\7$\2\2\u01d2")
        buf.write("\u01d4\5\u0081A\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2")
        buf.write("\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01db")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7\17\2\2\u01d9")
        buf.write("\u01dc\7\f\2\2\u01da\u01dc\t\21\2\2\u01db\u01d8\3\2\2")
        buf.write("\2\u01db\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de")
        buf.write("\bD\4\2\u01de\u0088\3\2\2\2\u01df\u01e0\7^\2\2\u01e0\u01e1")
        buf.write("\n\20\2\2\u01e1\u008a\3\2\2\2\u01e2\u01e6\7$\2\2\u01e3")
        buf.write("\u01e5\5\u0081A\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2")
        buf.write("\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01ea\5\u0089E\2\u01ea")
        buf.write("\u01eb\bF\5\2\u01eb\u008c\3\2\2\2\u01ec\u01ed\7\f\2\2")
        buf.write("\u01ed\u008e\3\2\2\2\u01ee\u01f0\t\22\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\bH\2\2")
        buf.write("\u01f4\u0090\3\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u0092")
        buf.write("\3\2\2\2\34\2\u009b\u00a5\u00a7\u0170\u0174\u017b\u017e")
        buf.write("\u0185\u018c\u0193\u0199\u019e\u01a3\u01a9\u01ad\u01b3")
        buf.write("\u01b6\u01b8\u01be\u01c3\u01cc\u01d5\u01db\u01e6\u01f1")
        buf.write("\6\b\2\2\38\2\3D\3\3F\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LINE_COMMENT = 2
    BLOCK_COMMENT = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNC = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    TRUE = 21
    FALSE = 22
    NIL = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQUALS = 29
    NOT_EQUALS = 30
    LESS_THAN = 31
    LESS_THAN_EQ = 32
    GREATER_THAN = 33
    GREATER_THAN_EQ = 34
    AND = 35
    OR = 36
    NOT = 37
    ASSIGN = 38
    ADD_ASSIGN = 39
    SUB_ASSIGN = 40
    MUL_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    DECLARE_ASSIGN = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACKET = 49
    RBRACKET = 50
    COMMA = 51
    SEMICOLON = 52
    COLON = 53
    DOT = 54
    SEMICOLON_NEWLINE = 55
    DEC_INT_LITERAL = 56
    OCT_INT_LITERAL = 57
    HEX_INT_LITERAL = 58
    BIN_INT_LITERAL = 59
    FLOAT_LITERAL = 60
    ID = 61
    STRING_LITERAL = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    NL = 65
    WS = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'true'", 
            "'false'", "'nil'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'", "'.'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", "FOR", "RETURN", 
            "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
            "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "TRUE", 
            "FALSE", "NIL", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUALS", 
            "NOT_EQUALS", "LESS_THAN", "LESS_THAN_EQ", "GREATER_THAN", "GREATER_THAN_EQ", 
            "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DECLARE_ASSIGN", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", 
            "COLON", "DOT", "SEMICOLON_NEWLINE", "DEC_INT_LITERAL", "OCT_INT_LITERAL", 
            "HEX_INT_LITERAL", "BIN_INT_LITERAL", "FLOAT_LITERAL", "ID", 
            "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "NL", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", 
                  "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "EQUALS", "NOT_EQUALS", "LESS_THAN", 
                  "LESS_THAN_EQ", "GREATER_THAN", "GREATER_THAN_EQ", "AND", 
                  "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "DECLARE_ASSIGN", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "COMMA", "SEMICOLON", "COLON", "DOT", "SEMICOLON_NEWLINE", 
                  "DEC_INT_LITERAL", "OCT_INT_LITERAL", "HEX_INT_LITERAL", 
                  "BIN_INT_LITERAL", "DIGIT", "EXPONENT_PART", "FLOAT_LITERAL", 
                  "ID", "STR_CHAR", "ESC_SEQ", "STRING_LITERAL", "UNCLOSE_STRING", 
                  "ESC_ILLEGAL", "ILLEGAL_ESCAPE", "NL", "WS", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None 

    def emit(self):
        tk = self.type
        self.preType = tk;
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.SEMICOLON_NEWLINE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def SEMICOLON_NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    if self.preType in {
                        self.ID, 
            			self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
            			self.DEC_INT_LITERAL, self.OCT_INT_LITERAL,
            			self.HEX_INT_LITERAL, self.BIN_INT_LITERAL,
            			self.FLOAT_LITERAL, self.TRUE, self.FALSE,
            			self.STRING_LITERAL, 
                        self.RETURN, self.CONTINUE, self.BREAK,
                        self.RPAREN, self.RBRACKET, self.RBRACE
                    }:
                        self.type = self.SEMICOLON;
                        self.text = ';';
                    else:
                        self.skip();
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            		raise UncloseString(self.text[:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[:-1])
            	else:
            		raise UncloseString(self.text[:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[:])

     


