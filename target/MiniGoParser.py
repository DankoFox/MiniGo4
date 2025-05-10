# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u025d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u0086\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008d\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u00a1\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\5\7\u00ab\n\7\3\7\3\7\3\7\5\7\u00b0\n\7\3\7\3\7\5")
        buf.write("\7\u00b4\n\7\3\7\3\7\5\7\u00b8\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00d3\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00dd\n\r\3\16\3\16\3\16")
        buf.write("\5\16\u00e2\n\16\3\16\3\16\5\16\u00e6\n\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00ef\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00f6\n\20\3\21\3\21\3\21\3\21\5\21\u00fc")
        buf.write("\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u0108\n\24\f\24\16\24\u010b\13\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\7\25\u0113\n\25\f\25\16\25\u0116\13\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u012d\n\26\f\26\16\26\u0130\13\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u013b\n\27\f\27\16\27\u013e")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\7\30\u014c\n\30\f\30\16\30\u014f\13\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u0156\n\31\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u015c\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u0165\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0171\n\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0177\n\32\f\32\16\32\u017a\13\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0181\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u018a\n\34\3\35\3\35\3\36\3\36\3\37\3\37\3")
        buf.write("\37\5\37\u0193\n\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 ")
        buf.write("\u019e\n \3!\3!\3!\3!\3!\5!\u01a5\n!\3\"\3\"\5\"\u01a9")
        buf.write("\n\"\3\"\3\"\3#\3#\3#\5#\u01b0\n#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\5$\u01b9\n$\3%\3%\3%\3%\3&\3&\3&\5&\u01c2\n&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\5\'\u01cb\n\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\5(\u01d4\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5")
        buf.write(")\u01e3\n)\3*\3*\3*\3*\3*\3+\3+\3,\3,\3,\3,\5,\u01f0\n")
        buf.write(",\3-\3-\3-\3-\3-\5-\u01f7\n-\3-\3-\5-\u01fb\n-\3.\3.\3")
        buf.write(".\3.\5.\u0201\n.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\5\61\u0210\n\61\3\61\3\61\3\61\5")
        buf.write("\61\u0215\n\61\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u0229\n\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\5")
        buf.write("\67\u0233\n\67\3\67\3\67\38\38\58\u0239\n8\38\38\39\3")
        buf.write("9\39\39\59\u0241\n9\3:\3:\3:\3:\5:\u0247\n:\3;\3;\3;\3")
        buf.write(";\5;\u024d\n;\3<\3<\3=\3=\3=\5=\u0254\n=\3=\3=\3=\3>\3")
        buf.write(">\3?\3?\3?\2\b&(*,.\62@\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|\2\6\3\2:=\3\2\27\30\3\2).\3\2\16\21\2\u0276")
        buf.write("\2~\3\2\2\2\4\u0085\3\2\2\2\6\u008c\3\2\2\2\b\u00a0\3")
        buf.write("\2\2\2\n\u00a2\3\2\2\2\f\u00a8\3\2\2\2\16\u00b9\3\2\2")
        buf.write("\2\20\u00be\3\2\2\2\22\u00c6\3\2\2\2\24\u00d2\3\2\2\2")
        buf.write("\26\u00d4\3\2\2\2\30\u00dc\3\2\2\2\32\u00de\3\2\2\2\34")
        buf.write("\u00ee\3\2\2\2\36\u00f5\3\2\2\2 \u00fb\3\2\2\2\"\u00fd")
        buf.write("\3\2\2\2$\u00ff\3\2\2\2&\u0101\3\2\2\2(\u010c\3\2\2\2")
        buf.write("*\u0117\3\2\2\2,\u0131\3\2\2\2.\u013f\3\2\2\2\60\u0155")
        buf.write("\3\2\2\2\62\u0164\3\2\2\2\64\u0180\3\2\2\2\66\u0189\3")
        buf.write("\2\2\28\u018b\3\2\2\2:\u018d\3\2\2\2<\u018f\3\2\2\2>\u019d")
        buf.write("\3\2\2\2@\u01a4\3\2\2\2B\u01a6\3\2\2\2D\u01ac\3\2\2\2")
        buf.write("F\u01b8\3\2\2\2H\u01ba\3\2\2\2J\u01be\3\2\2\2L\u01c5\3")
        buf.write("\2\2\2N\u01d3\3\2\2\2P\u01e2\3\2\2\2R\u01e4\3\2\2\2T\u01e9")
        buf.write("\3\2\2\2V\u01eb\3\2\2\2X\u01fa\3\2\2\2Z\u01fc\3\2\2\2")
        buf.write("\\\u0204\3\2\2\2^\u0206\3\2\2\2`\u0214\3\2\2\2b\u0216")
        buf.write("\3\2\2\2d\u0218\3\2\2\2f\u0228\3\2\2\2h\u022a\3\2\2\2")
        buf.write("j\u022d\3\2\2\2l\u0232\3\2\2\2n\u0236\3\2\2\2p\u023c\3")
        buf.write("\2\2\2r\u0246\3\2\2\2t\u024c\3\2\2\2v\u024e\3\2\2\2x\u0250")
        buf.write("\3\2\2\2z\u0258\3\2\2\2|\u025a\3\2\2\2~\177\5\4\3\2\177")
        buf.write("\u0080\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\5\6\4\2\u0082")
        buf.write("\u0083\5\4\3\2\u0083\u0086\3\2\2\2\u0084\u0086\5\6\4\2")
        buf.write("\u0085\u0081\3\2\2\2\u0085\u0084\3\2\2\2\u0086\5\3\2\2")
        buf.write("\2\u0087\u008d\5\b\5\2\u0088\u008d\5\n\6\2\u0089\u008d")
        buf.write("\5\f\7\2\u008a\u008d\5\20\t\2\u008b\u008d\5\22\n\2\u008c")
        buf.write("\u0087\3\2\2\2\u008c\u0088\3\2\2\2\u008c\u0089\3\2\2\2")
        buf.write("\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\7\3\2\2")
        buf.write("\2\u008e\u008f\7\23\2\2\u008f\u0090\7?\2\2\u0090\u0091")
        buf.write("\5t;\2\u0091\u0092\7(\2\2\u0092\u0093\5$\23\2\u0093\u0094")
        buf.write("\7\66\2\2\u0094\u00a1\3\2\2\2\u0095\u0096\7\23\2\2\u0096")
        buf.write("\u0097\7?\2\2\u0097\u0098\5t;\2\u0098\u0099\7\66\2\2\u0099")
        buf.write("\u00a1\3\2\2\2\u009a\u009b\7\23\2\2\u009b\u009c\7?\2\2")
        buf.write("\u009c\u009d\7(\2\2\u009d\u009e\5$\23\2\u009e\u009f\7")
        buf.write("\66\2\2\u009f\u00a1\3\2\2\2\u00a0\u008e\3\2\2\2\u00a0")
        buf.write("\u0095\3\2\2\2\u00a0\u009a\3\2\2\2\u00a1\t\3\2\2\2\u00a2")
        buf.write("\u00a3\7\22\2\2\u00a3\u00a4\7?\2\2\u00a4\u00a5\7(\2\2")
        buf.write("\u00a5\u00a6\5$\23\2\u00a6\u00a7\7\66\2\2\u00a7\13\3\2")
        buf.write("\2\2\u00a8\u00aa\7\n\2\2\u00a9\u00ab\5\16\b\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ad\7?\2\2\u00ad\u00af\7/\2\2\u00ae\u00b0\5\34\17\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b3\7\60\2\2\u00b2\u00b4\5\"\22\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b7\5p9\2\u00b6\u00b8\7\66\2\2\u00b7\u00b6\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\r\3\2\2\2\u00b9\u00ba")
        buf.write("\7/\2\2\u00ba\u00bb\7?\2\2\u00bb\u00bc\7?\2\2\u00bc\u00bd")
        buf.write("\7\60\2\2\u00bd\17\3\2\2\2\u00be\u00bf\7\13\2\2\u00bf")
        buf.write("\u00c0\7?\2\2\u00c0\u00c1\7\f\2\2\u00c1\u00c2\7\61\2\2")
        buf.write("\u00c2\u00c3\5\24\13\2\u00c3\u00c4\7\62\2\2\u00c4\u00c5")
        buf.write("\7\66\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\7\13\2\2\u00c7")
        buf.write("\u00c8\7?\2\2\u00c8\u00c9\7\r\2\2\u00c9\u00ca\7\61\2\2")
        buf.write("\u00ca\u00cb\5\30\r\2\u00cb\u00cc\7\62\2\2\u00cc\u00cd")
        buf.write("\7\66\2\2\u00cd\23\3\2\2\2\u00ce\u00cf\5\26\f\2\u00cf")
        buf.write("\u00d0\5\24\13\2\u00d0\u00d3\3\2\2\2\u00d1\u00d3\5\26")
        buf.write("\f\2\u00d2\u00ce\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\25")
        buf.write("\3\2\2\2\u00d4\u00d5\7?\2\2\u00d5\u00d6\5t;\2\u00d6\u00d7")
        buf.write("\7\66\2\2\u00d7\27\3\2\2\2\u00d8\u00d9\5\32\16\2\u00d9")
        buf.write("\u00da\5\30\r\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5\32\16")
        buf.write("\2\u00dc\u00d8\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\31\3")
        buf.write("\2\2\2\u00de\u00df\7?\2\2\u00df\u00e1\7/\2\2\u00e0\u00e2")
        buf.write("\5\34\17\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e5\7\60\2\2\u00e4\u00e6\5\"\22")
        buf.write("\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7\u00e8\7\66\2\2\u00e8\33\3\2\2\2\u00e9\u00ea")
        buf.write("\5\36\20\2\u00ea\u00eb\7\65\2\2\u00eb\u00ec\5\34\17\2")
        buf.write("\u00ec\u00ef\3\2\2\2\u00ed\u00ef\5\36\20\2\u00ee\u00e9")
        buf.write("\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\35\3\2\2\2\u00f0\u00f1")
        buf.write("\7?\2\2\u00f1\u00f6\5t;\2\u00f2\u00f3\5 \21\2\u00f3\u00f4")
        buf.write("\5t;\2\u00f4\u00f6\3\2\2\2\u00f5\u00f0\3\2\2\2\u00f5\u00f2")
        buf.write("\3\2\2\2\u00f6\37\3\2\2\2\u00f7\u00f8\7?\2\2\u00f8\u00f9")
        buf.write("\7\65\2\2\u00f9\u00fc\5 \21\2\u00fa\u00fc\7?\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc!\3\2\2\2\u00fd")
        buf.write("\u00fe\5t;\2\u00fe#\3\2\2\2\u00ff\u0100\5&\24\2\u0100")
        buf.write("%\3\2\2\2\u0101\u0102\b\24\1\2\u0102\u0103\5(\25\2\u0103")
        buf.write("\u0109\3\2\2\2\u0104\u0105\f\4\2\2\u0105\u0106\7&\2\2")
        buf.write("\u0106\u0108\5(\25\2\u0107\u0104\3\2\2\2\u0108\u010b\3")
        buf.write("\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\'")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\b\25\1\2\u010d")
        buf.write("\u010e\5*\26\2\u010e\u0114\3\2\2\2\u010f\u0110\f\4\2\2")
        buf.write("\u0110\u0111\7%\2\2\u0111\u0113\5*\26\2\u0112\u010f\3")
        buf.write("\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115)\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118")
        buf.write("\b\26\1\2\u0118\u0119\5,\27\2\u0119\u012e\3\2\2\2\u011a")
        buf.write("\u011b\f\t\2\2\u011b\u011c\7\37\2\2\u011c\u012d\5,\27")
        buf.write("\2\u011d\u011e\f\b\2\2\u011e\u011f\7 \2\2\u011f\u012d")
        buf.write("\5,\27\2\u0120\u0121\f\7\2\2\u0121\u0122\7!\2\2\u0122")
        buf.write("\u012d\5,\27\2\u0123\u0124\f\6\2\2\u0124\u0125\7\"\2\2")
        buf.write("\u0125\u012d\5,\27\2\u0126\u0127\f\5\2\2\u0127\u0128\7")
        buf.write("#\2\2\u0128\u012d\5,\27\2\u0129\u012a\f\4\2\2\u012a\u012b")
        buf.write("\7$\2\2\u012b\u012d\5,\27\2\u012c\u011a\3\2\2\2\u012c")
        buf.write("\u011d\3\2\2\2\u012c\u0120\3\2\2\2\u012c\u0123\3\2\2\2")
        buf.write("\u012c\u0126\3\2\2\2\u012c\u0129\3\2\2\2\u012d\u0130\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f+")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\b\27\1\2\u0132")
        buf.write("\u0133\5.\30\2\u0133\u013c\3\2\2\2\u0134\u0135\f\5\2\2")
        buf.write("\u0135\u0136\7\32\2\2\u0136\u013b\5.\30\2\u0137\u0138")
        buf.write("\f\4\2\2\u0138\u0139\7\33\2\2\u0139\u013b\5.\30\2\u013a")
        buf.write("\u0134\3\2\2\2\u013a\u0137\3\2\2\2\u013b\u013e\3\2\2\2")
        buf.write("\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d-\3\2\2")
        buf.write("\2\u013e\u013c\3\2\2\2\u013f\u0140\b\30\1\2\u0140\u0141")
        buf.write("\5\60\31\2\u0141\u014d\3\2\2\2\u0142\u0143\f\6\2\2\u0143")
        buf.write("\u0144\7\34\2\2\u0144\u014c\5\60\31\2\u0145\u0146\f\5")
        buf.write("\2\2\u0146\u0147\7\35\2\2\u0147\u014c\5\60\31\2\u0148")
        buf.write("\u0149\f\4\2\2\u0149\u014a\7\36\2\2\u014a\u014c\5\60\31")
        buf.write("\2\u014b\u0142\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0148")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e/\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0151\7\'\2\2\u0151\u0156\5\60\31\2\u0152\u0153\7\33")
        buf.write("\2\2\u0153\u0156\5\60\31\2\u0154\u0156\5\62\32\2\u0155")
        buf.write("\u0150\3\2\2\2\u0155\u0152\3\2\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156\61\3\2\2\2\u0157\u0158\b\32\1\2\u0158\u0159\7?")
        buf.write("\2\2\u0159\u015b\7/\2\2\u015a\u015c\5N(\2\u015b\u015a")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u0165\7\60\2\2\u015e\u0165\7?\2\2\u015f\u0165\5\66\34")
        buf.write("\2\u0160\u0161\7/\2\2\u0161\u0162\5$\23\2\u0162\u0163")
        buf.write("\7\60\2\2\u0163\u0165\3\2\2\2\u0164\u0157\3\2\2\2\u0164")
        buf.write("\u015e\3\2\2\2\u0164\u015f\3\2\2\2\u0164\u0160\3\2\2\2")
        buf.write("\u0165\u0178\3\2\2\2\u0166\u0167\f\t\2\2\u0167\u0168\7")
        buf.write("\63\2\2\u0168\u0169\5$\23\2\u0169\u016a\7\64\2\2\u016a")
        buf.write("\u0177\3\2\2\2\u016b\u016c\f\b\2\2\u016c\u016d\78\2\2")
        buf.write("\u016d\u016e\7?\2\2\u016e\u0170\7/\2\2\u016f\u0171\5N")
        buf.write("(\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0177\7\60\2\2\u0173\u0174\f\7\2\2\u0174")
        buf.write("\u0175\78\2\2\u0175\u0177\7?\2\2\u0176\u0166\3\2\2\2\u0176")
        buf.write("\u016b\3\2\2\2\u0176\u0173\3\2\2\2\u0177\u017a\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\63\3\2")
        buf.write("\2\2\u017a\u0178\3\2\2\2\u017b\u017c\5$\23\2\u017c\u017d")
        buf.write("\7\65\2\2\u017d\u017e\5\64\33\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u0181\5$\23\2\u0180\u017b\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181\65\3\2\2\2\u0182\u018a\58\35\2\u0183\u018a\7>\2")
        buf.write("\2\u0184\u018a\7@\2\2\u0185\u018a\5:\36\2\u0186\u018a")
        buf.write("\5<\37\2\u0187\u018a\5D#\2\u0188\u018a\7\31\2\2\u0189")
        buf.write("\u0182\3\2\2\2\u0189\u0183\3\2\2\2\u0189\u0184\3\2\2\2")
        buf.write("\u0189\u0185\3\2\2\2\u0189\u0186\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u0189\u0188\3\2\2\2\u018a\67\3\2\2\2\u018b\u018c")
        buf.write("\t\2\2\2\u018c9\3\2\2\2\u018d\u018e\t\3\2\2\u018e;\3\2")
        buf.write("\2\2\u018f\u0190\5x=\2\u0190\u0192\7\61\2\2\u0191\u0193")
        buf.write("\5@!\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194\u0195\7\62\2\2\u0195=\3\2\2\2\u0196\u019e")
        buf.write("\58\35\2\u0197\u019e\7>\2\2\u0198\u019e\7@\2\2\u0199\u019e")
        buf.write("\5:\36\2\u019a\u019e\5B\"\2\u019b\u019e\5D#\2\u019c\u019e")
        buf.write("\7\31\2\2\u019d\u0196\3\2\2\2\u019d\u0197\3\2\2\2\u019d")
        buf.write("\u0198\3\2\2\2\u019d\u0199\3\2\2\2\u019d\u019a\3\2\2\2")
        buf.write("\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e?\3\2\2")
        buf.write("\2\u019f\u01a0\5> \2\u01a0\u01a1\7\65\2\2\u01a1\u01a2")
        buf.write("\5@!\2\u01a2\u01a5\3\2\2\2\u01a3\u01a5\5> \2\u01a4\u019f")
        buf.write("\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5A\3\2\2\2\u01a6\u01a8")
        buf.write("\7\61\2\2\u01a7\u01a9\5@!\2\u01a8\u01a7\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7\62\2")
        buf.write("\2\u01abC\3\2\2\2\u01ac\u01ad\7?\2\2\u01ad\u01af\7\61")
        buf.write("\2\2\u01ae\u01b0\5F$\2\u01af\u01ae\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\7\62\2\2\u01b2")
        buf.write("E\3\2\2\2\u01b3\u01b4\5H%\2\u01b4\u01b5\7\65\2\2\u01b5")
        buf.write("\u01b6\5F$\2\u01b6\u01b9\3\2\2\2\u01b7\u01b9\5H%\2\u01b8")
        buf.write("\u01b3\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9G\3\2\2\2\u01ba")
        buf.write("\u01bb\7?\2\2\u01bb\u01bc\7\67\2\2\u01bc\u01bd\5$\23\2")
        buf.write("\u01bdI\3\2\2\2\u01be\u01bf\7?\2\2\u01bf\u01c1\7/\2\2")
        buf.write("\u01c0\u01c2\5N(\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2")
        buf.write("\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\7\60\2\2\u01c4K\3")
        buf.write("\2\2\2\u01c5\u01c6\5$\23\2\u01c6\u01c7\78\2\2\u01c7\u01c8")
        buf.write("\7?\2\2\u01c8\u01ca\7/\2\2\u01c9\u01cb\5N(\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01cd\7\60\2\2\u01cdM\3\2\2\2\u01ce\u01cf\5$\23\2\u01cf")
        buf.write("\u01d0\7\65\2\2\u01d0\u01d1\5N(\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d4\5$\23\2\u01d3\u01ce\3\2\2\2\u01d3\u01d2\3")
        buf.write("\2\2\2\u01d4O\3\2\2\2\u01d5\u01e3\5\b\5\2\u01d6\u01e3")
        buf.write("\5\n\6\2\u01d7\u01e3\5R*\2\u01d8\u01e3\5V,\2\u01d9\u01e3")
        buf.write("\5Z.\2\u01da\u01e3\5h\65\2\u01db\u01e3\5j\66\2\u01dc\u01e3")
        buf.write("\5l\67\2\u01dd\u01e3\5n8\2\u01de\u01e3\5p9\2\u01df\u01e0")
        buf.write("\5$\23\2\u01e0\u01e1\7\66\2\2\u01e1\u01e3\3\2\2\2\u01e2")
        buf.write("\u01d5\3\2\2\2\u01e2\u01d6\3\2\2\2\u01e2\u01d7\3\2\2\2")
        buf.write("\u01e2\u01d8\3\2\2\2\u01e2\u01d9\3\2\2\2\u01e2\u01da\3")
        buf.write("\2\2\2\u01e2\u01db\3\2\2\2\u01e2\u01dc\3\2\2\2\u01e2\u01dd")
        buf.write("\3\2\2\2\u01e2\u01de\3\2\2\2\u01e2\u01df\3\2\2\2\u01e3")
        buf.write("Q\3\2\2\2\u01e4\u01e5\5\62\32\2\u01e5\u01e6\5T+\2\u01e6")
        buf.write("\u01e7\5$\23\2\u01e7\u01e8\7\66\2\2\u01e8S\3\2\2\2\u01e9")
        buf.write("\u01ea\t\4\2\2\u01eaU\3\2\2\2\u01eb\u01ec\7\6\2\2\u01ec")
        buf.write("\u01ed\5$\23\2\u01ed\u01ef\5p9\2\u01ee\u01f0\5X-\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0W\3\2\2\2\u01f1")
        buf.write("\u01f2\7\7\2\2\u01f2\u01f3\7\6\2\2\u01f3\u01f4\5$\23\2")
        buf.write("\u01f4\u01f6\5p9\2\u01f5\u01f7\5X-\2\u01f6\u01f5\3\2\2")
        buf.write("\2\u01f6\u01f7\3\2\2\2\u01f7\u01fb\3\2\2\2\u01f8\u01f9")
        buf.write("\7\7\2\2\u01f9\u01fb\5p9\2\u01fa\u01f1\3\2\2\2\u01fa\u01f8")
        buf.write("\3\2\2\2\u01fbY\3\2\2\2\u01fc\u0200\7\b\2\2\u01fd\u0201")
        buf.write("\5\\/\2\u01fe\u0201\5^\60\2\u01ff\u0201\5f\64\2\u0200")
        buf.write("\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202\u0203\5p9\2\u0203[\3\2\2\2")
        buf.write("\u0204\u0205\5$\23\2\u0205]\3\2\2\2\u0206\u0207\5`\61")
        buf.write("\2\u0207\u0208\7\66\2\2\u0208\u0209\5$\23\2\u0209\u020a")
        buf.write("\7\66\2\2\u020a\u020b\5b\62\2\u020b_\3\2\2\2\u020c\u020d")
        buf.write("\7\23\2\2\u020d\u020f\7?\2\2\u020e\u0210\5t;\2\u020f\u020e")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0212\7(\2\2\u0212\u0215\5$\23\2\u0213\u0215\5d\63\2")
        buf.write("\u0214\u020c\3\2\2\2\u0214\u0213\3\2\2\2\u0215a\3\2\2")
        buf.write("\2\u0216\u0217\5d\63\2\u0217c\3\2\2\2\u0218\u0219\5\62")
        buf.write("\32\2\u0219\u021a\5T+\2\u021a\u021b\5$\23\2\u021be\3\2")
        buf.write("\2\2\u021c\u021d\7?\2\2\u021d\u021e\7\65\2\2\u021e\u021f")
        buf.write("\7?\2\2\u021f\u0220\7.\2\2\u0220\u0221\7\26\2\2\u0221")
        buf.write("\u0229\5$\23\2\u0222\u0223\7\3\2\2\u0223\u0224\7\65\2")
        buf.write("\2\u0224\u0225\7?\2\2\u0225\u0226\7.\2\2\u0226\u0227\7")
        buf.write("\26\2\2\u0227\u0229\5$\23\2\u0228\u021c\3\2\2\2\u0228")
        buf.write("\u0222\3\2\2\2\u0229g\3\2\2\2\u022a\u022b\7\25\2\2\u022b")
        buf.write("\u022c\7\66\2\2\u022ci\3\2\2\2\u022d\u022e\7\24\2\2\u022e")
        buf.write("\u022f\7\66\2\2\u022fk\3\2\2\2\u0230\u0233\5J&\2\u0231")
        buf.write("\u0233\5L\'\2\u0232\u0230\3\2\2\2\u0232\u0231\3\2\2\2")
        buf.write("\u0233\u0234\3\2\2\2\u0234\u0235\7\66\2\2\u0235m\3\2\2")
        buf.write("\2\u0236\u0238\7\t\2\2\u0237\u0239\5$\23\2\u0238\u0237")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u023b\7\66\2\2\u023bo\3\2\2\2\u023c\u023d\7\61\2\2\u023d")
        buf.write("\u023e\5r:\2\u023e\u0240\7\62\2\2\u023f\u0241\7\66\2\2")
        buf.write("\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241q\3\2\2")
        buf.write("\2\u0242\u0243\5P)\2\u0243\u0244\5r:\2\u0244\u0247\3\2")
        buf.write("\2\2\u0245\u0247\5P)\2\u0246\u0242\3\2\2\2\u0246\u0245")
        buf.write("\3\2\2\2\u0247s\3\2\2\2\u0248\u024d\5v<\2\u0249\u024d")
        buf.write("\5x=\2\u024a\u024d\5z>\2\u024b\u024d\5|?\2\u024c\u0248")
        buf.write("\3\2\2\2\u024c\u0249\3\2\2\2\u024c\u024a\3\2\2\2\u024c")
        buf.write("\u024b\3\2\2\2\u024du\3\2\2\2\u024e\u024f\t\5\2\2\u024f")
        buf.write("w\3\2\2\2\u0250\u0253\7\63\2\2\u0251\u0254\58\35\2\u0252")
        buf.write("\u0254\7?\2\2\u0253\u0251\3\2\2\2\u0253\u0252\3\2\2\2")
        buf.write("\u0254\u0255\3\2\2\2\u0255\u0256\7\64\2\2\u0256\u0257")
        buf.write("\5t;\2\u0257y\3\2\2\2\u0258\u0259\7?\2\2\u0259{\3\2\2")
        buf.write("\2\u025a\u025b\7?\2\2\u025b}\3\2\2\2\67\u0085\u008c\u00a0")
        buf.write("\u00aa\u00af\u00b3\u00b7\u00d2\u00dc\u00e1\u00e5\u00ee")
        buf.write("\u00f5\u00fb\u0109\u0114\u012c\u012e\u013a\u013c\u014b")
        buf.write("\u014d\u0155\u015b\u0164\u0170\u0176\u0178\u0180\u0189")
        buf.write("\u0192\u019d\u01a4\u01a8\u01af\u01b8\u01c1\u01ca\u01d3")
        buf.write("\u01e2\u01ef\u01f6\u01fa\u0200\u020f\u0214\u0228\u0232")
        buf.write("\u0238\u0240\u0246\u024c\u0253")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "<INVALID>", "<INVALID>", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'true'", "'false'", "'nil'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "':='", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "':'", "'.'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "TRUE", 
                      "FALSE", "NIL", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQUALS", "NOT_EQUALS", "LESS_THAN", "LESS_THAN_EQ", 
                      "GREATER_THAN", "GREATER_THAN_EQ", "AND", "OR", "NOT", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DECLARE_ASSIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "COMMA", "SEMICOLON", "COLON", "DOT", "SEMICOLON_NEWLINE", 
                      "DEC_INT_LITERAL", "OCT_INT_LITERAL", "HEX_INT_LITERAL", 
                      "BIN_INT_LITERAL", "FLOAT_LITERAL", "ID", "STRING_LITERAL", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "NL", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declList = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_constdecl = 4
    RULE_funcdecl = 5
    RULE_receiver = 6
    RULE_structdecl = 7
    RULE_interfacedecl = 8
    RULE_fieldDeclList = 9
    RULE_fieldDecl = 10
    RULE_methodDeclList = 11
    RULE_methodDecl = 12
    RULE_paramList = 13
    RULE_param = 14
    RULE_idList = 15
    RULE_returnType = 16
    RULE_expr = 17
    RULE_expr1 = 18
    RULE_expr2 = 19
    RULE_expr3 = 20
    RULE_expr4 = 21
    RULE_expr5 = 22
    RULE_expr6 = 23
    RULE_expr7 = 24
    RULE_exprList = 25
    RULE_literals = 26
    RULE_integer_literal = 27
    RULE_bool_literal = 28
    RULE_array_literal = 29
    RULE_arrayContent = 30
    RULE_arrayContentList = 31
    RULE_array_literal_shorthand = 32
    RULE_struct_literal = 33
    RULE_fieldInitList = 34
    RULE_fieldInit = 35
    RULE_functionCall = 36
    RULE_methodCall = 37
    RULE_argList = 38
    RULE_statement = 39
    RULE_assignmentStatement = 40
    RULE_assignmentOperator = 41
    RULE_ifStatement = 42
    RULE_elseChain = 43
    RULE_forStatement = 44
    RULE_forCondition = 45
    RULE_forCStyle = 46
    RULE_init = 47
    RULE_update = 48
    RULE_assignExpr = 49
    RULE_forRange = 50
    RULE_breakStatement = 51
    RULE_continueStatement = 52
    RULE_callStatement = 53
    RULE_returnStatement = 54
    RULE_block = 55
    RULE_statementList = 56
    RULE_type_ = 57
    RULE_primitiveType = 58
    RULE_arrayType = 59
    RULE_structType = 60
    RULE_interfaceType = 61

    ruleNames =  [ "program", "declList", "decl", "vardecl", "constdecl", 
                   "funcdecl", "receiver", "structdecl", "interfacedecl", 
                   "fieldDeclList", "fieldDecl", "methodDeclList", "methodDecl", 
                   "paramList", "param", "idList", "returnType", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "exprList", "literals", "integer_literal", "bool_literal", 
                   "array_literal", "arrayContent", "arrayContentList", 
                   "array_literal_shorthand", "struct_literal", "fieldInitList", 
                   "fieldInit", "functionCall", "methodCall", "argList", 
                   "statement", "assignmentStatement", "assignmentOperator", 
                   "ifStatement", "elseChain", "forStatement", "forCondition", 
                   "forCStyle", "init", "update", "assignExpr", "forRange", 
                   "breakStatement", "continueStatement", "callStatement", 
                   "returnStatement", "block", "statementList", "type_", 
                   "primitiveType", "arrayType", "structType", "interfaceType" ]

    EOF = Token.EOF
    T__0=1
    LINE_COMMENT=2
    BLOCK_COMMENT=3
    IF=4
    ELSE=5
    FOR=6
    RETURN=7
    FUNC=8
    TYPE=9
    STRUCT=10
    INTERFACE=11
    STRING=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    CONST=16
    VAR=17
    CONTINUE=18
    BREAK=19
    RANGE=20
    TRUE=21
    FALSE=22
    NIL=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    EQUALS=29
    NOT_EQUALS=30
    LESS_THAN=31
    LESS_THAN_EQ=32
    GREATER_THAN=33
    GREATER_THAN_EQ=34
    AND=35
    OR=36
    NOT=37
    ASSIGN=38
    ADD_ASSIGN=39
    SUB_ASSIGN=40
    MUL_ASSIGN=41
    DIV_ASSIGN=42
    MOD_ASSIGN=43
    DECLARE_ASSIGN=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    LBRACKET=49
    RBRACKET=50
    COMMA=51
    SEMICOLON=52
    COLON=53
    DOT=54
    SEMICOLON_NEWLINE=55
    DEC_INT_LITERAL=56
    OCT_INT_LITERAL=57
    HEX_INT_LITERAL=58
    BIN_INT_LITERAL=59
    FLOAT_LITERAL=60
    ID=61
    STRING_LITERAL=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    NL=65
    WS=66
    ERROR_CHAR=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.declList()
            self.state = 125
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclList" ):
                return visitor.visitDeclList(self)
            else:
                return visitor.visitChildren(self)




    def declList(self):

        localctx = MiniGoParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declList)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.decl()
                self.state = 128
                self.declList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.funcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.interfacedecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(MiniGoParser.VAR)
                self.state = 141
                self.match(MiniGoParser.ID)
                self.state = 142
                self.type_()
                self.state = 143
                self.match(MiniGoParser.ASSIGN)
                self.state = 144
                self.expr()
                self.state = 145
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(MiniGoParser.VAR)
                self.state = 148
                self.match(MiniGoParser.ID)
                self.state = 149
                self.type_()
                self.state = 150
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(MiniGoParser.VAR)
                self.state = 153
                self.match(MiniGoParser.ID)
                self.state = 154
                self.match(MiniGoParser.ASSIGN)
                self.state = 155
                self.expr()
                self.state = 156
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniGoParser.CONST)
            self.state = 161
            self.match(MiniGoParser.ID)
            self.state = 162
            self.match(MiniGoParser.ASSIGN)
            self.state = 163
            self.expr()
            self.state = 164
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def returnType(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnTypeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.FUNC)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 167
                self.receiver()


            self.state = 170
            self.match(MiniGoParser.ID)
            self.state = 171
            self.match(MiniGoParser.LPAREN)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 172
                self.paramList()


            self.state = 175
            self.match(MiniGoParser.RPAREN)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 176
                self.returnType()


            self.state = 179
            self.block()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 180
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.LPAREN)
            self.state = 184
            self.match(MiniGoParser.ID)
            self.state = 185
            self.match(MiniGoParser.ID)
            self.state = 186
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.TYPE)
            self.state = 189
            self.match(MiniGoParser.ID)
            self.state = 190
            self.match(MiniGoParser.STRUCT)
            self.state = 191
            self.match(MiniGoParser.LBRACE)
            self.state = 192
            self.fieldDeclList()
            self.state = 193
            self.match(MiniGoParser.RBRACE)
            self.state = 194
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def methodDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interfacedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.TYPE)
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 198
            self.match(MiniGoParser.INTERFACE)
            self.state = 199
            self.match(MiniGoParser.LBRACE)
            self.state = 200
            self.methodDeclList()
            self.state = 201
            self.match(MiniGoParser.RBRACE)
            self.state = 202
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclContext,0)


        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclList" ):
                return visitor.visitFieldDeclList(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclList(self):

        localctx = MiniGoParser.FieldDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fieldDeclList)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.fieldDecl()
                self.state = 205
                self.fieldDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.fieldDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = MiniGoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MiniGoParser.ID)
            self.state = 211
            self.type_()
            self.state = 212
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def methodDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclList" ):
                return visitor.visitMethodDeclList(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclList(self):

        localctx = MiniGoParser.MethodDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methodDeclList)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.methodDecl()
                self.state = 215
                self.methodDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def returnType(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.ID)
            self.state = 221
            self.match(MiniGoParser.LPAREN)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 222
                self.paramList()


            self.state = 225
            self.match(MiniGoParser.RPAREN)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 226
                self.returnType()


            self.state = 229
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.param()
                self.state = 232
                self.match(MiniGoParser.COMMA)
                self.state = 233
                self.paramList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def idList(self):
            return self.getTypedRuleContext(MiniGoParser.IdListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(MiniGoParser.ID)
                self.state = 239
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.idList()
                self.state = 241
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def idList(self):
            return self.getTypedRuleContext(MiniGoParser.IdListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = MiniGoParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idList)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(MiniGoParser.ID)
                self.state = 246
                self.match(MiniGoParser.COMMA)
                self.state = 247
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = MiniGoParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    self.match(MiniGoParser.OR)
                    self.state = 260
                    self.expr2(0) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    self.match(MiniGoParser.AND)
                    self.state = 271
                    self.expr3(0) 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def EQUALS(self):
            return self.getToken(MiniGoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MiniGoParser.NOT_EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_THAN_EQ(self):
            return self.getToken(MiniGoParser.LESS_THAN_EQ, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_THAN_EQ(self):
            return self.getToken(MiniGoParser.GREATER_THAN_EQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 298
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 280
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 281
                        self.match(MiniGoParser.EQUALS)
                        self.state = 282
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 283
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 284
                        self.match(MiniGoParser.NOT_EQUALS)
                        self.state = 285
                        self.expr4(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 286
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 287
                        self.match(MiniGoParser.LESS_THAN)
                        self.state = 288
                        self.expr4(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 289
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 290
                        self.match(MiniGoParser.LESS_THAN_EQ)
                        self.state = 291
                        self.expr4(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 292
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 293
                        self.match(MiniGoParser.GREATER_THAN)
                        self.state = 294
                        self.expr4(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 295
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 296
                        self.match(MiniGoParser.GREATER_THAN_EQ)
                        self.state = 297
                        self.expr4(0)
                        pass

             
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 312
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 306
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 307
                        self.match(MiniGoParser.ADD)
                        self.state = 308
                        self.expr5(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 309
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 310
                        self.match(MiniGoParser.SUB)
                        self.state = 311
                        self.expr5(0)
                        pass

             
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 329
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 320
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 321
                        self.match(MiniGoParser.MUL)
                        self.state = 322
                        self.expr6()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 323
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 324
                        self.match(MiniGoParser.DIV)
                        self.state = 325
                        self.expr6()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 326
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 327
                        self.match(MiniGoParser.MOD)
                        self.state = 328
                        self.expr6()
                        pass

             
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr6)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MiniGoParser.NOT)
                self.state = 335
                self.expr6()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(MiniGoParser.SUB)
                self.state = 337
                self.expr6()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.DEC_INT_LITERAL, MiniGoParser.OCT_INT_LITERAL, MiniGoParser.HEX_INT_LITERAL, MiniGoParser.BIN_INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.ID, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 342
                self.match(MiniGoParser.ID)
                self.state = 343
                self.match(MiniGoParser.LPAREN)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                    self.state = 344
                    self.argList()


                self.state = 347
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 348
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.state = 349
                self.literals()
                pass

            elif la_ == 4:
                self.state = 350
                self.match(MiniGoParser.LPAREN)
                self.state = 351
                self.expr()
                self.state = 352
                self.match(MiniGoParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 372
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 356
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 357
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 358
                        self.expr()
                        self.state = 359
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 361
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 362
                        self.match(MiniGoParser.DOT)
                        self.state = 363
                        self.match(MiniGoParser.ID)
                        self.state = 364
                        self.match(MiniGoParser.LPAREN)
                        self.state = 366
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                            self.state = 365
                            self.argList()


                        self.state = 368
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                        self.state = 369
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 370
                        self.match(MiniGoParser.DOT)
                        self.state = 371
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def exprList(self):
            return self.getTypedRuleContext(MiniGoParser.ExprListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MiniGoParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprList)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.expr()
                self.state = 378
                self.match(MiniGoParser.COMMA)
                self.state = 379
                self.exprList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Integer_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literals)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_INT_LITERAL, MiniGoParser.OCT_INT_LITERAL, MiniGoParser.HEX_INT_LITERAL, MiniGoParser.BIN_INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.integer_literal()
                pass
            elif token in [MiniGoParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass
            elif token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.bool_literal()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.struct_literal()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 390
                self.match(MiniGoParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integer_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_INT_LITERAL(self):
            return self.getToken(MiniGoParser.DEC_INT_LITERAL, 0)

        def OCT_INT_LITERAL(self):
            return self.getToken(MiniGoParser.OCT_INT_LITERAL, 0)

        def HEX_INT_LITERAL(self):
            return self.getToken(MiniGoParser.HEX_INT_LITERAL, 0)

        def BIN_INT_LITERAL(self):
            return self.getToken(MiniGoParser.BIN_INT_LITERAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_integer_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_literal" ):
                return visitor.visitInteger_literal(self)
            else:
                return visitor.visitChildren(self)




    def integer_literal(self):

        localctx = MiniGoParser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_integer_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_literal" ):
                return visitor.visitBool_literal(self)
            else:
                return visitor.visitChildren(self)




    def bool_literal(self):

        localctx = MiniGoParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def arrayContentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContentListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.arrayType()
            self.state = 398
            self.match(MiniGoParser.LBRACE)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 399
                self.arrayContentList()


            self.state = 402
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Integer_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_literalContext,0)


        def array_literal_shorthand(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_shorthandContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayContent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayContent" ):
                return visitor.visitArrayContent(self)
            else:
                return visitor.visitChildren(self)




    def arrayContent(self):

        localctx = MiniGoParser.ArrayContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayContent)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_INT_LITERAL, MiniGoParser.OCT_INT_LITERAL, MiniGoParser.HEX_INT_LITERAL, MiniGoParser.BIN_INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.integer_literal()
                pass
            elif token in [MiniGoParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass
            elif token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.bool_literal()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.array_literal_shorthand()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 409
                self.struct_literal()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 410
                self.match(MiniGoParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayContent(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContentContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayContentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContentListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayContentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayContentList" ):
                return visitor.visitArrayContentList(self)
            else:
                return visitor.visitChildren(self)




    def arrayContentList(self):

        localctx = MiniGoParser.ArrayContentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arrayContentList)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.arrayContent()
                self.state = 414
                self.match(MiniGoParser.COMMA)
                self.state = 415
                self.arrayContentList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.arrayContent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_shorthandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def arrayContentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContentListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_shorthand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_shorthand" ):
                return visitor.visitArray_literal_shorthand(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_shorthand(self):

        localctx = MiniGoParser.Array_literal_shorthandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_literal_shorthand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.LBRACE)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 421
                self.arrayContentList()


            self.state = 424
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def fieldInitList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.match(MiniGoParser.LBRACE)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 428
                self.fieldInitList()


            self.state = 431
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldInit(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def fieldInitList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInitList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldInitList" ):
                return visitor.visitFieldInitList(self)
            else:
                return visitor.visitChildren(self)




    def fieldInitList(self):

        localctx = MiniGoParser.FieldInitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_fieldInitList)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.fieldInit()
                self.state = 434
                self.match(MiniGoParser.COMMA)
                self.state = 435
                self.fieldInitList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.fieldInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldInit" ):
                return visitor.visitFieldInit(self)
            else:
                return visitor.visitChildren(self)




    def fieldInit(self):

        localctx = MiniGoParser.FieldInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_fieldInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(MiniGoParser.ID)
            self.state = 441
            self.match(MiniGoParser.COLON)
            self.state = 442
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MiniGoParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.ID)
            self.state = 445
            self.match(MiniGoParser.LPAREN)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 446
                self.argList()


            self.state = 449
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expr()
            self.state = 452
            self.match(MiniGoParser.DOT)
            self.state = 453
            self.match(MiniGoParser.ID)
            self.state = 454
            self.match(MiniGoParser.LPAREN)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 455
                self.argList()


            self.state = 458
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = MiniGoParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_argList)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.expr()
                self.state = 461
                self.match(MiniGoParser.COMMA)
                self.state = 462
                self.argList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 473
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 474
                self.callStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 475
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 476
                self.block()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 477
                self.expr()
                self.state = 478
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MiniGoParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr7(0)
            self.state = 483
            self.assignmentOperator()
            self.state = 484
            self.expr()
            self.state = 485
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.DECLARE_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseChain(self):
            return self.getTypedRuleContext(MiniGoParser.ElseChainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(MiniGoParser.IF)
            self.state = 490
            self.expr()
            self.state = 491
            self.block()
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 492
                self.elseChain()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseChain(self):
            return self.getTypedRuleContext(MiniGoParser.ElseChainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseChain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseChain" ):
                return visitor.visitElseChain(self)
            else:
                return visitor.visitChildren(self)




    def elseChain(self):

        localctx = MiniGoParser.ElseChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elseChain)
        self._la = 0 # Token type
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(MiniGoParser.ELSE)
                self.state = 496
                self.match(MiniGoParser.IF)
                self.state = 497
                self.expr()
                self.state = 498
                self.block()
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 499
                    self.elseChain()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.match(MiniGoParser.ELSE)
                self.state = 503
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def forCStyle(self):
            return self.getTypedRuleContext(MiniGoParser.ForCStyleContext,0)


        def forRange(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.FOR)
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 507
                self.forCondition()
                pass

            elif la_ == 2:
                self.state = 508
                self.forCStyle()
                pass

            elif la_ == 3:
                self.state = 509
                self.forRange()
                pass


            self.state = 512
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForCStyleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCStyle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCStyle" ):
                return visitor.visitForCStyle(self)
            else:
                return visitor.visitChildren(self)




    def forCStyle(self):

        localctx = MiniGoParser.ForCStyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forCStyle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.init()
            self.state = 517
            self.match(MiniGoParser.SEMICOLON)
            self.state = 518
            self.expr()
            self.state = 519
            self.match(MiniGoParser.SEMICOLON)
            self.state = 520
            self.update()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def assignExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AssignExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.match(MiniGoParser.VAR)
                self.state = 523
                self.match(MiniGoParser.ID)
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 524
                    self.type_()


                self.state = 527
                self.match(MiniGoParser.ASSIGN)
                self.state = 528
                self.expr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.DEC_INT_LITERAL, MiniGoParser.OCT_INT_LITERAL, MiniGoParser.HEX_INT_LITERAL, MiniGoParser.BIN_INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.ID, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.assignExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AssignExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.assignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)




    def assignExpr(self):

        localctx = MiniGoParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assignExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.expr7(0)
            self.state = 535
            self.assignmentOperator()
            self.state = 536
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forRange)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.match(MiniGoParser.ID)
                self.state = 539
                self.match(MiniGoParser.COMMA)
                self.state = 540
                self.match(MiniGoParser.ID)
                self.state = 541
                self.match(MiniGoParser.DECLARE_ASSIGN)
                self.state = 542
                self.match(MiniGoParser.RANGE)
                self.state = 543
                self.expr()
                pass
            elif token in [MiniGoParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.match(MiniGoParser.T__0)
                self.state = 545
                self.match(MiniGoParser.COMMA)
                self.state = 546
                self.match(MiniGoParser.ID)
                self.state = 547
                self.match(MiniGoParser.DECLARE_ASSIGN)
                self.state = 548
                self.match(MiniGoParser.RANGE)
                self.state = 549
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(MiniGoParser.BREAK)
            self.state = 553
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.CONTINUE)
            self.state = 556
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 558
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 559
                self.methodCall()
                pass


            self.state = 562
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.RETURN)
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.DEC_INT_LITERAL) | (1 << MiniGoParser.OCT_INT_LITERAL) | (1 << MiniGoParser.HEX_INT_LITERAL) | (1 << MiniGoParser.BIN_INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 565
                self.expr()


            self.state = 568
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(MiniGoParser.LBRACE)
            self.state = 571
            self.statementList()
            self.state = 572
            self.match(MiniGoParser.RBRACE)
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 573
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_statementList)
        try:
            self.state = 580
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.statement()
                self.state = 577
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_type_)
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.primitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 584
                self.structType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 585
                self.interfaceType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = MiniGoParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def integer_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Integer_literalContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(MiniGoParser.LBRACKET)
            self.state = 593
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_INT_LITERAL, MiniGoParser.OCT_INT_LITERAL, MiniGoParser.HEX_INT_LITERAL, MiniGoParser.BIN_INT_LITERAL]:
                self.state = 591
                self.integer_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 592
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 595
            self.match(MiniGoParser.RBRACKET)
            self.state = 596
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr1_sempred
        self._predicates[19] = self.expr2_sempred
        self._predicates[20] = self.expr3_sempred
        self._predicates[21] = self.expr4_sempred
        self._predicates[22] = self.expr5_sempred
        self._predicates[24] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         




