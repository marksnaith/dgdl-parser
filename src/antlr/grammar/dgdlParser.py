# Generated from grammar/dgdl.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u0216\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2|\n\2\f\2\16\2\177\13\2\3")
        buf.write("\2\6\2\u0082\n\2\r\2\16\2\u0083\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\5\4\u008c\n\4\3\4\3\4\6\4\u0090\n\4\r\4\16\4\u0091")
        buf.write("\3\4\7\4\u0095\n\4\f\4\16\4\u0098\13\4\3\4\5\4\u009b\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\7\5\u00a2\n\5\f\5\16\5\u00a5\13")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\5\6\u00ac\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00c0\n\b\3\b\3\b\3\b\3\b\5\b\u00c6\n\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u00cc\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00e5\n\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\6\f\u00f0\n\f\r\f\16\f\u00f1\3\f\3\f\5\f\u00f6\n\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\5\17\u00ff\n\17\3\17")
        buf.write("\3\17\3\17\5\17\u0104\n\17\7\17\u0106\n\17\f\17\16\17")
        buf.write("\u0109\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\5\23\u0118\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\27\5\27\u012d\n\27\3\27\5\27\u0130")
        buf.write("\n\27\3\27\3\27\3\30\6\30\u0135\n\30\r\30\16\30\u0136")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u013d\n\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u014a\n\32")
        buf.write("\3\32\3\32\5\32\u014e\n\32\3\32\3\32\5\32\u0152\n\32\3")
        buf.write("\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u0163\n\37\f\37\16\37\u0166")
        buf.write("\13\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\5$\u0180\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\5(\u019a\n(\3(\5(\u019d\n(\3(\5(\u01a0")
        buf.write("\n(\3)\3)\3)\7)\u01a5\n)\f)\16)\u01a8\13)\3*\5*\u01ab")
        buf.write("\n*\3*\3*\3*\5*\u01b0\n*\3+\3+\3+\3+\3+\3+\3+\5+\u01b9")
        buf.write("\n+\3+\3+\5+\u01bd\n+\3+\3+\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01d3\n.\3.\3.\5.\u01d7")
        buf.write("\n.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01e6\n\61\3\61\5\61\u01e9\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01f9\n\63\3\63\3\63\3\63\3\63\5\63\u01ff\n")
        buf.write("\63\3\63\3\63\3\63\3\63\5\63\u0205\n\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write("9\2\2:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\r\3\2LN")
        buf.write("\3\2OP\3\2\25\26\3\2IK\3\2\34\35\3\2\36\37\4\2\34\34!")
        buf.write("\"\3\2$(\3\2-\60\4\2\25\25\63\64\5\2//\65\65II\2\u020b")
        buf.write("\2r\3\2\2\2\4\u0088\3\2\2\2\6\u008b\3\2\2\2\b\u009c\3")
        buf.write("\2\2\2\n\u00ab\3\2\2\2\f\u00ad\3\2\2\2\16\u00b8\3\2\2")
        buf.write("\2\20\u00cf\3\2\2\2\22\u00d1\3\2\2\2\24\u00e8\3\2\2\2")
        buf.write("\26\u00f5\3\2\2\2\30\u00f7\3\2\2\2\32\u00f9\3\2\2\2\34")
        buf.write("\u00fb\3\2\2\2\36\u010c\3\2\2\2 \u0111\3\2\2\2\"\u0113")
        buf.write("\3\2\2\2$\u0117\3\2\2\2&\u0119\3\2\2\2(\u0125\3\2\2\2")
        buf.write("*\u0127\3\2\2\2,\u0129\3\2\2\2.\u0134\3\2\2\2\60\u013c")
        buf.write("\3\2\2\2\62\u0140\3\2\2\2\64\u0155\3\2\2\2\66\u0157\3")
        buf.write("\2\2\28\u0159\3\2\2\2:\u015b\3\2\2\2<\u015e\3\2\2\2>\u0169")
        buf.write("\3\2\2\2@\u0172\3\2\2\2B\u0174\3\2\2\2D\u017b\3\2\2\2")
        buf.write("F\u017f\3\2\2\2H\u0181\3\2\2\2J\u0188\3\2\2\2L\u018f\3")
        buf.write("\2\2\2N\u0191\3\2\2\2P\u01a1\3\2\2\2R\u01aa\3\2\2\2T\u01b1")
        buf.write("\3\2\2\2V\u01c0\3\2\2\2X\u01c2\3\2\2\2Z\u01c9\3\2\2\2")
        buf.write("\\\u01da\3\2\2\2^\u01dc\3\2\2\2`\u01de\3\2\2\2b\u01ea")
        buf.write("\3\2\2\2d\u01ef\3\2\2\2f\u0209\3\2\2\2h\u020b\3\2\2\2")
        buf.write("j\u020d\3\2\2\2l\u020f\3\2\2\2n\u0211\3\2\2\2p\u0213\3")
        buf.write("\2\2\2rs\7\3\2\2st\7\4\2\2tu\7\5\2\2uv\7\6\2\2vw\5\4\3")
        buf.write("\2wx\7\7\2\2xy\7\b\2\2y}\5\6\4\2z|\5&\24\2{z\3\2\2\2|")
        buf.write("\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0081\3\2\2\2\177}\3")
        buf.write("\2\2\2\u0080\u0082\5d\63\2\u0081\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\7\t\2\2\u0086\u0087\7\2\2\3")
        buf.write("\u0087\3\3\2\2\2\u0088\u0089\5l\67\2\u0089\5\3\2\2\2\u008a")
        buf.write("\u008c\5\b\5\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008f\5\f\7\2\u008e\u0090\5")
        buf.write("\16\b\2\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0096\3\2\2\2")
        buf.write("\u0093\u0095\5\22\n\2\u0094\u0093\3\2\2\2\u0095\u0098")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\5\36\20")
        buf.write("\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\7\3\2")
        buf.write("\2\2\u009c\u009d\7\n\2\2\u009d\u009e\7\4\2\2\u009e\u00a3")
        buf.write("\5\n\6\2\u009f\u00a0\7\13\2\2\u00a0\u00a2\5\n\6\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\7\7\2\2\u00a7\t\3\2\2\2\u00a8\u00ac")
        buf.write("\7G\2\2\u00a9\u00ac\7H\2\2\u00aa\u00ac\5l\67\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\13\3\2\2\2\u00ad\u00ae\7\f\2\2\u00ae\u00af\7\4\2\2\u00af")
        buf.write("\u00b0\7\r\2\2\u00b0\u00b1\7\6\2\2\u00b1\u00b2\5\"\22")
        buf.write("\2\u00b2\u00b3\7\13\2\2\u00b3\u00b4\7\16\2\2\u00b4\u00b5")
        buf.write("\7\6\2\2\u00b5\u00b6\5$\23\2\u00b6\u00b7\7\7\2\2\u00b7")
        buf.write("\r\3\2\2\2\u00b8\u00b9\7\17\2\2\u00b9\u00ba\7\4\2\2\u00ba")
        buf.write("\u00bb\7\5\2\2\u00bb\u00bc\7\6\2\2\u00bc\u00bf\5\20\t")
        buf.write("\2\u00bd\u00be\7\13\2\2\u00be\u00c0\5\b\5\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c5\3\2\2\2\u00c1")
        buf.write("\u00c2\7\13\2\2\u00c2\u00c3\7\r\2\2\u00c3\u00c4\7\6\2")
        buf.write("\2\u00c4\u00c6\5\"\22\2\u00c5\u00c1\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00cb\3\2\2\2\u00c7\u00c8\7\13\2\2\u00c8")
        buf.write("\u00c9\7\16\2\2\u00c9\u00ca\7\6\2\2\u00ca\u00cc\5$\23")
        buf.write("\2\u00cb\u00c7\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00ce\7\7\2\2\u00ce\17\3\2\2\2\u00cf\u00d0")
        buf.write("\5l\67\2\u00d0\21\3\2\2\2\u00d1\u00d2\7\20\2\2\u00d2\u00d3")
        buf.write("\7\4\2\2\u00d3\u00d4\7\5\2\2\u00d4\u00d5\7\6\2\2\u00d5")
        buf.write("\u00d6\5\24\13\2\u00d6\u00d7\7\13\2\2\u00d7\u00d8\7\21")
        buf.write("\2\2\u00d8\u00d9\7\6\2\2\u00d9\u00da\5\26\f\2\u00da\u00db")
        buf.write("\7\13\2\2\u00db\u00dc\7\22\2\2\u00dc\u00dd\7\6\2\2\u00dd")
        buf.write("\u00de\5\30\r\2\u00de\u00df\7\13\2\2\u00df\u00e0\7\23")
        buf.write("\2\2\u00e0\u00e1\7\6\2\2\u00e1\u00e4\5\32\16\2\u00e2\u00e3")
        buf.write("\7\13\2\2\u00e3\u00e5\5\34\17\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7\7\2\2")
        buf.write("\u00e7\23\3\2\2\2\u00e8\u00e9\5l\67\2\u00e9\25\3\2\2\2")
        buf.write("\u00ea\u00f6\5l\67\2\u00eb\u00ec\7\b\2\2\u00ec\u00ef\5")
        buf.write("l\67\2\u00ed\u00ee\7\13\2\2\u00ee\u00f0\5l\67\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\7")
        buf.write("\t\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00ea\3\2\2\2\u00f5\u00eb")
        buf.write("\3\2\2\2\u00f6\27\3\2\2\2\u00f7\u00f8\t\2\2\2\u00f8\31")
        buf.write("\3\2\2\2\u00f9\u00fa\t\3\2\2\u00fa\33\3\2\2\2\u00fb\u00fe")
        buf.write("\7\b\2\2\u00fc\u00ff\5p9\2\u00fd\u00ff\7Q\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0107\3\2\2\2\u0100")
        buf.write("\u0103\7\13\2\2\u0101\u0104\5p9\2\u0102\u0104\7Q\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104\u0106\3\2\2\2")
        buf.write("\u0105\u0100\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3")
        buf.write("\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107")
        buf.write("\3\2\2\2\u010a\u010b\7\t\2\2\u010b\35\3\2\2\2\u010c\u010d")
        buf.write("\7\24\2\2\u010d\u010e\7\4\2\2\u010e\u010f\5 \21\2\u010f")
        buf.write("\u0110\7\7\2\2\u0110\37\3\2\2\2\u0111\u0112\t\4\2\2\u0112")
        buf.write("!\3\2\2\2\u0113\u0114\5n8\2\u0114#\3\2\2\2\u0115\u0118")
        buf.write("\5n8\2\u0116\u0118\7\27\2\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118%\3\2\2\2\u0119\u011a\7\30\2\2\u011a")
        buf.write("\u011b\7\4\2\2\u011b\u011c\7\5\2\2\u011c\u011d\7\6\2\2")
        buf.write("\u011d\u011e\5(\25\2\u011e\u011f\7\13\2\2\u011f\u0120")
        buf.write("\7\31\2\2\u0120\u0121\7\6\2\2\u0121\u0122\5*\26\2\u0122")
        buf.write("\u0123\7\7\2\2\u0123\u0124\5,\27\2\u0124\'\3\2\2\2\u0125")
        buf.write("\u0126\5l\67\2\u0126)\3\2\2\2\u0127\u0128\t\5\2\2\u0128")
        buf.write("+\3\2\2\2\u0129\u012f\7\b\2\2\u012a\u012c\5.\30\2\u012b")
        buf.write("\u012d\5N(\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u0130\3\2\2\2\u012e\u0130\5N(\2\u012f\u012a\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\7\t\2\2")
        buf.write("\u0132-\3\2\2\2\u0133\u0135\5\60\31\2\u0134\u0133\3\2")
        buf.write("\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137/\3\2\2\2\u0138\u013d\5\62\32\2\u0139\u013d")
        buf.write("\5> \2\u013a\u013d\5B\"\2\u013b\u013d\5F$\2\u013c\u0138")
        buf.write("\3\2\2\2\u013c\u0139\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7\32\2")
        buf.write("\2\u013f\61\3\2\2\2\u0140\u0141\7\33\2\2\u0141\u0142\7")
        buf.write("\4\2\2\u0142\u0143\5\64\33\2\u0143\u0144\7\13\2\2\u0144")
        buf.write("\u0145\5\66\34\2\u0145\u0146\7\13\2\2\u0146\u0149\58\35")
        buf.write("\2\u0147\u0148\7\13\2\2\u0148\u014a\5:\36\2\u0149\u0147")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\3\2\2\2\u014b")
        buf.write("\u014c\7\13\2\2\u014c\u014e\5<\37\2\u014d\u014b\3\2\2")
        buf.write("\2\u014d\u014e\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u0150")
        buf.write("\7\13\2\2\u0150\u0152\5L\'\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\7\7\2\2")
        buf.write("\u0154\63\3\2\2\2\u0155\u0156\t\6\2\2\u0156\65\3\2\2\2")
        buf.write("\u0157\u0158\t\7\2\2\u0158\67\3\2\2\2\u0159\u015a\5l\67")
        buf.write("\2\u015a9\3\2\2\2\u015b\u015c\7 \2\2\u015c\u015d\5l\67")
        buf.write("\2\u015d;\3\2\2\2\u015e\u015f\7\b\2\2\u015f\u0164\5p9")
        buf.write("\2\u0160\u0161\7\13\2\2\u0161\u0163\5p9\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0167\u0168\7\t\2\2\u0168=\3\2\2\2\u0169\u016a\7\20\2")
        buf.write("\2\u016a\u016b\7\4\2\2\u016b\u016c\5@!\2\u016c\u016d\7")
        buf.write("\13\2\2\u016d\u016e\5\34\17\2\u016e\u016f\7\13\2\2\u016f")
        buf.write("\u0170\5\24\13\2\u0170\u0171\7\7\2\2\u0171?\3\2\2\2\u0172")
        buf.write("\u0173\t\b\2\2\u0173A\3\2\2\2\u0174\u0175\7#\2\2\u0175")
        buf.write("\u0176\7\4\2\2\u0176\u0177\5D#\2\u0177\u0178\7\13\2\2")
        buf.write("\u0178\u0179\5l\67\2\u0179\u017a\7\7\2\2\u017aC\3\2\2")
        buf.write("\2\u017b\u017c\t\t\2\2\u017cE\3\2\2\2\u017d\u0180\5H%")
        buf.write("\2\u017e\u0180\5J&\2\u017f\u017d\3\2\2\2\u017f\u017e\3")
        buf.write("\2\2\2\u0180G\3\2\2\2\u0181\u0182\7)\2\2\u0182\u0183\7")
        buf.write("\4\2\2\u0183\u0184\5L\'\2\u0184\u0185\7\13\2\2\u0185\u0186")
        buf.write("\5\n\6\2\u0186\u0187\7\7\2\2\u0187I\3\2\2\2\u0188\u0189")
        buf.write("\7*\2\2\u0189\u018a\7\4\2\2\u018a\u018b\5L\'\2\u018b\u018c")
        buf.write("\7\13\2\2\u018c\u018d\5\n\6\2\u018d\u018e\7\7\2\2\u018e")
        buf.write("K\3\2\2\2\u018f\u0190\5l\67\2\u0190M\3\2\2\2\u0191\u0192")
        buf.write("\7+\2\2\u0192\u0193\7\4\2\2\u0193\u0194\5P)\2\u0194\u0195")
        buf.write("\7\7\2\2\u0195\u0196\7\b\2\2\u0196\u0197\5.\30\2\u0197")
        buf.write("\u0199\7\t\2\2\u0198\u019a\5`\61\2\u0199\u0198\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2\u019b\u019d\5")
        buf.write("b\62\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f")
        buf.write("\3\2\2\2\u019e\u01a0\7\32\2\2\u019f\u019e\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0O\3\2\2\2\u01a1\u01a6\5R*\2\u01a2")
        buf.write("\u01a3\7D\2\2\u01a3\u01a5\5R*\2\u01a4\u01a2\3\2\2\2\u01a5")
        buf.write("\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7Q\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ab\7E\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01af\3")
        buf.write("\2\2\2\u01ac\u01b0\5T+\2\u01ad\u01b0\5X-\2\u01ae\u01b0")
        buf.write("\5Z.\2\u01af\u01ac\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0S\3\2\2\2\u01b1\u01b2\7,\2\2\u01b2\u01b3")
        buf.write("\7\4\2\2\u01b3\u01b4\5V,\2\u01b4\u01b5\7\13\2\2\u01b5")
        buf.write("\u01b8\58\35\2\u01b6\u01b7\7\13\2\2\u01b7\u01b9\5<\37")
        buf.write("\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01bb\7\13\2\2\u01bb\u01bd\5L\'\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\7\7\2\2\u01bfU\3\2\2\2\u01c0\u01c1\t\n\2")
        buf.write("\2\u01c1W\3\2\2\2\u01c2\u01c3\7\61\2\2\u01c3\u01c4\7\4")
        buf.write("\2\2\u01c4\u01c5\5\20\t\2\u01c5\u01c6\7\13\2\2\u01c6\u01c7")
        buf.write("\5\n\6\2\u01c7\u01c8\7\7\2\2\u01c8Y\3\2\2\2\u01c9\u01ca")
        buf.write("\7\62\2\2\u01ca\u01cb\7\4\2\2\u01cb\u01cc\5\\/\2\u01cc")
        buf.write("\u01cd\7\13\2\2\u01cd\u01ce\5\34\17\2\u01ce\u01cf\7\13")
        buf.write("\2\2\u01cf\u01d2\5\24\13\2\u01d0\u01d1\7\13\2\2\u01d1")
        buf.write("\u01d3\5L\'\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01d6\3\2\2\2\u01d4\u01d5\7\13\2\2\u01d5\u01d7")
        buf.write("\5^\60\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01d9\7\7\2\2\u01d9[\3\2\2\2\u01da")
        buf.write("\u01db\t\13\2\2\u01db]\3\2\2\2\u01dc\u01dd\t\f\2\2\u01dd")
        buf.write("_\3\2\2\2\u01de\u01df\7\66\2\2\u01df\u01e0\5P)\2\u01e0")
        buf.write("\u01e1\7\67\2\2\u01e1\u01e2\7\b\2\2\u01e2\u01e3\5.\30")
        buf.write("\2\u01e3\u01e5\7\t\2\2\u01e4\u01e6\5`\61\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7")
        buf.write("\u01e9\5b\62\2\u01e8\u01e7\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9a\3\2\2\2\u01ea\u01eb\78\2\2\u01eb\u01ec\7\b\2\2")
        buf.write("\u01ec\u01ed\5.\30\2\u01ed\u01ee\7\t\2\2\u01eec\3\2\2")
        buf.write("\2\u01ef\u01f0\79\2\2\u01f0\u01f1\7\4\2\2\u01f1\u01f2")
        buf.write("\7\5\2\2\u01f2\u01f3\7\6\2\2\u01f3\u01f8\58\35\2\u01f4")
        buf.write("\u01f5\7\13\2\2\u01f5\u01f6\7:\2\2\u01f6\u01f7\7\6\2\2")
        buf.write("\u01f7\u01f9\5L\'\2\u01f8\u01f4\3\2\2\2\u01f8\u01f9\3")
        buf.write("\2\2\2\u01f9\u01fe\3\2\2\2\u01fa\u01fb\7\13\2\2\u01fb")
        buf.write("\u01fc\7;\2\2\u01fc\u01fd\7\6\2\2\u01fd\u01ff\5<\37\2")
        buf.write("\u01fe\u01fa\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0204\3")
        buf.write("\2\2\2\u0200\u0201\7\13\2\2\u0201\u0202\7<\2\2\u0202\u0203")
        buf.write("\7\6\2\2\u0203\u0205\5f\64\2\u0204\u0200\3\2\2\2\u0204")
        buf.write("\u0205\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\7\7\2\2")
        buf.write("\u0207\u0208\5,\27\2\u0208e\3\2\2\2\u0209\u020a\7Q\2\2")
        buf.write("\u020ag\3\2\2\2\u020b\u020c\7?\2\2\u020ci\3\2\2\2\u020d")
        buf.write("\u020e\7>\2\2\u020ek\3\2\2\2\u020f\u0210\7=\2\2\u0210")
        buf.write("m\3\2\2\2\u0211\u0212\7@\2\2\u0212o\3\2\2\2\u0213\u0214")
        buf.write("\7>\2\2\u0214q\3\2\2\2,}\u0083\u008b\u0091\u0096\u009a")
        buf.write("\u00a3\u00ab\u00bf\u00c5\u00cb\u00e4\u00f1\u00f5\u00fe")
        buf.write("\u0103\u0107\u0117\u012c\u012f\u0136\u013c\u0149\u014d")
        buf.write("\u0151\u0164\u017f\u0199\u019c\u019f\u01a6\u01aa\u01af")
        buf.write("\u01b8\u01bc\u01d2\u01d6\u01e5\u01e8\u01f8\u01fe\u0204")
        return buf.getvalue()


class dgdlParser ( Parser ):

    grammarFileName = "dgdl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'game'", "'('", "'id'", "':'", "')'", 
                     "'{'", "'}'", "'roles'", "','", "'participants'", "'min'", 
                     "'max'", "'player'", "'store'", "'owner'", "'structure'", 
                     "'visibility'", "'backtracking'", "'on'", "'off'", 
                     "'undefined'", "'rule'", "'scope'", "';'", "'move'", 
                     "'add'", "'delete'", "'next'", "'future'", "'$'", "'remove'", 
                     "'empty'", "'status'", "'active'", "'inactive'", "'complete'", 
                     "'incomplete'", "'terminate'", "'assign'", "'unassign'", 
                     "'if'", "'event'", "'last'", "'!last'", "'past'", "'!past'", 
                     "'inrole'", "'inspect'", "'in'", "'top'", "'current'", 
                     "'elseif '", "'then'", "'else'", "'interaction'", "'addressee'", 
                     "'content'", "'opener'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'&&'", "'!'", "<INVALID>", "'listener'", 
                     "'speaker'", "'initial'", "'turnwise'", "'movewise'", 
                     "'set'", "'queue'", "'stack'", "'public'", "'private'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "LowerChar", "UpperChar", "Number", "WS", "MOVEACTION", 
                      "MOVETIME", "AMPAND", "NEG", "ONOFF", "LISTENER", 
                      "SPEAKER", "INITIAL", "TURNWISE", "MOVEWISE", "SET", 
                      "QUEUE", "STACK", "PUBLIC", "PRIVATE", "STRINGLITERAL", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_game = 0
    RULE_gameID = 1
    RULE_composition = 2
    RULE_roleList = 3
    RULE_role = 4
    RULE_participants = 5
    RULE_player = 6
    RULE_playerID = 7
    RULE_store = 8
    RULE_storeID = 9
    RULE_storeOwner = 10
    RULE_storeStructure = 11
    RULE_storeVisibility = 12
    RULE_storeContent = 13
    RULE_backtrack = 14
    RULE_onoff = 15
    RULE_minplayers = 16
    RULE_maxplayers = 17
    RULE_rules = 18
    RULE_ruleID = 19
    RULE_scopeType = 20
    RULE_ruleBody = 21
    RULE_effects = 22
    RULE_effect = 23
    RULE_move = 24
    RULE_moveaction = 25
    RULE_movetime = 26
    RULE_moveID = 27
    RULE_addressee = 28
    RULE_content = 29
    RULE_storeOp = 30
    RULE_storeaction = 31
    RULE_statusUpdate = 32
    RULE_status = 33
    RULE_roleAssignment = 34
    RULE_assignment = 35
    RULE_unassignment = 36
    RULE_user = 37
    RULE_conditional = 38
    RULE_requirements = 39
    RULE_condition = 40
    RULE_event = 41
    RULE_eventpos = 42
    RULE_roleInspection = 43
    RULE_storeInspection = 44
    RULE_storepos = 45
    RULE_storetime = 46
    RULE_condelseif = 47
    RULE_condelse = 48
    RULE_interaction = 49
    RULE_opener = 50
    RULE_upperChar = 51
    RULE_lowerChar = 52
    RULE_identifier = 53
    RULE_number = 54
    RULE_contentVar = 55

    ruleNames =  [ "game", "gameID", "composition", "roleList", "role", 
                   "participants", "player", "playerID", "store", "storeID", 
                   "storeOwner", "storeStructure", "storeVisibility", "storeContent", 
                   "backtrack", "onoff", "minplayers", "maxplayers", "rules", 
                   "ruleID", "scopeType", "ruleBody", "effects", "effect", 
                   "move", "moveaction", "movetime", "moveID", "addressee", 
                   "content", "storeOp", "storeaction", "statusUpdate", 
                   "status", "roleAssignment", "assignment", "unassignment", 
                   "user", "conditional", "requirements", "condition", "event", 
                   "eventpos", "roleInspection", "storeInspection", "storepos", 
                   "storetime", "condelseif", "condelse", "interaction", 
                   "opener", "upperChar", "lowerChar", "identifier", "number", 
                   "contentVar" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    Identifier=59
    LowerChar=60
    UpperChar=61
    Number=62
    WS=63
    MOVEACTION=64
    MOVETIME=65
    AMPAND=66
    NEG=67
    ONOFF=68
    LISTENER=69
    SPEAKER=70
    INITIAL=71
    TURNWISE=72
    MOVEWISE=73
    SET=74
    QUEUE=75
    STACK=76
    PUBLIC=77
    PRIVATE=78
    STRINGLITERAL=79
    COMMENT=80
    LINE_COMMENT=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gameID(self):
            return self.getTypedRuleContext(dgdlParser.GameIDContext,0)


        def composition(self):
            return self.getTypedRuleContext(dgdlParser.CompositionContext,0)


        def EOF(self):
            return self.getToken(dgdlParser.EOF, 0)

        def rules(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.RulesContext)
            else:
                return self.getTypedRuleContext(dgdlParser.RulesContext,i)


        def interaction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.InteractionContext)
            else:
                return self.getTypedRuleContext(dgdlParser.InteractionContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame" ):
                listener.enterGame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame" ):
                listener.exitGame(self)




    def game(self):

        localctx = dgdlParser.GameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_game)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(dgdlParser.T__0)
            self.state = 113
            self.match(dgdlParser.T__1)
            self.state = 114
            self.match(dgdlParser.T__2)
            self.state = 115
            self.match(dgdlParser.T__3)
            self.state = 116
            self.gameID()
            self.state = 117
            self.match(dgdlParser.T__4)
            self.state = 118
            self.match(dgdlParser.T__5)
            self.state = 119
            self.composition()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__21:
                self.state = 120
                self.rules()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.interaction()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.T__54):
                    break

            self.state = 131
            self.match(dgdlParser.T__6)
            self.state = 132
            self.match(dgdlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_gameID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameID" ):
                listener.enterGameID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameID" ):
                listener.exitGameID(self)




    def gameID(self):

        localctx = dgdlParser.GameIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gameID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def participants(self):
            return self.getTypedRuleContext(dgdlParser.ParticipantsContext,0)


        def roleList(self):
            return self.getTypedRuleContext(dgdlParser.RoleListContext,0)


        def player(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.PlayerContext)
            else:
                return self.getTypedRuleContext(dgdlParser.PlayerContext,i)


        def store(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.StoreContext)
            else:
                return self.getTypedRuleContext(dgdlParser.StoreContext,i)


        def backtrack(self):
            return self.getTypedRuleContext(dgdlParser.BacktrackContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_composition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposition" ):
                listener.enterComposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposition" ):
                listener.exitComposition(self)




    def composition(self):

        localctx = dgdlParser.CompositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_composition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__7:
                self.state = 136
                self.roleList()


            self.state = 139
            self.participants()
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.player()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.T__12):
                    break

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__13:
                self.state = 145
                self.store()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__17:
                self.state = 151
                self.backtrack()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def role(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.RoleContext)
            else:
                return self.getTypedRuleContext(dgdlParser.RoleContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_roleList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleList" ):
                listener.enterRoleList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleList" ):
                listener.exitRoleList(self)




    def roleList(self):

        localctx = dgdlParser.RoleListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_roleList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(dgdlParser.T__7)
            self.state = 155
            self.match(dgdlParser.T__1)
            self.state = 156
            self.role()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__8:
                self.state = 157
                self.match(dgdlParser.T__8)
                self.state = 158
                self.role()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LISTENER(self):
            return self.getToken(dgdlParser.LISTENER, 0)

        def SPEAKER(self):
            return self.getToken(dgdlParser.SPEAKER, 0)

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_role

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole" ):
                listener.enterRole(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole" ):
                listener.exitRole(self)




    def role(self):

        localctx = dgdlParser.RoleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_role)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.LISTENER]:
                self.state = 166
                self.match(dgdlParser.LISTENER)
                pass
            elif token in [dgdlParser.SPEAKER]:
                self.state = 167
                self.match(dgdlParser.SPEAKER)
                pass
            elif token in [dgdlParser.Identifier]:
                self.state = 168
                self.identifier()
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


    class ParticipantsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def minplayers(self):
            return self.getTypedRuleContext(dgdlParser.MinplayersContext,0)


        def maxplayers(self):
            return self.getTypedRuleContext(dgdlParser.MaxplayersContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_participants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParticipants" ):
                listener.enterParticipants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParticipants" ):
                listener.exitParticipants(self)




    def participants(self):

        localctx = dgdlParser.ParticipantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_participants)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(dgdlParser.T__9)
            self.state = 172
            self.match(dgdlParser.T__1)
            self.state = 173
            self.match(dgdlParser.T__10)
            self.state = 174
            self.match(dgdlParser.T__3)
            self.state = 175
            self.minplayers()
            self.state = 176
            self.match(dgdlParser.T__8)
            self.state = 177
            self.match(dgdlParser.T__11)
            self.state = 178
            self.match(dgdlParser.T__3)
            self.state = 179
            self.maxplayers()
            self.state = 180
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playerID(self):
            return self.getTypedRuleContext(dgdlParser.PlayerIDContext,0)


        def roleList(self):
            return self.getTypedRuleContext(dgdlParser.RoleListContext,0)


        def minplayers(self):
            return self.getTypedRuleContext(dgdlParser.MinplayersContext,0)


        def maxplayers(self):
            return self.getTypedRuleContext(dgdlParser.MaxplayersContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)




    def player(self):

        localctx = dgdlParser.PlayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_player)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(dgdlParser.T__12)
            self.state = 183
            self.match(dgdlParser.T__1)
            self.state = 184
            self.match(dgdlParser.T__2)
            self.state = 185
            self.match(dgdlParser.T__3)
            self.state = 186
            self.playerID()
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 187
                self.match(dgdlParser.T__8)
                self.state = 188
                self.roleList()


            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(dgdlParser.T__8)
                self.state = 192
                self.match(dgdlParser.T__10)
                self.state = 193
                self.match(dgdlParser.T__3)
                self.state = 194
                self.minplayers()


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 197
                self.match(dgdlParser.T__8)
                self.state = 198
                self.match(dgdlParser.T__11)
                self.state = 199
                self.match(dgdlParser.T__3)
                self.state = 200
                self.maxplayers()


            self.state = 203
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_playerID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerID" ):
                listener.enterPlayerID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerID" ):
                listener.exitPlayerID(self)




    def playerID(self):

        localctx = dgdlParser.PlayerIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_playerID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storeID(self):
            return self.getTypedRuleContext(dgdlParser.StoreIDContext,0)


        def storeOwner(self):
            return self.getTypedRuleContext(dgdlParser.StoreOwnerContext,0)


        def storeStructure(self):
            return self.getTypedRuleContext(dgdlParser.StoreStructureContext,0)


        def storeVisibility(self):
            return self.getTypedRuleContext(dgdlParser.StoreVisibilityContext,0)


        def storeContent(self):
            return self.getTypedRuleContext(dgdlParser.StoreContentContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)




    def store(self):

        localctx = dgdlParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_store)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(dgdlParser.T__13)
            self.state = 208
            self.match(dgdlParser.T__1)
            self.state = 209
            self.match(dgdlParser.T__2)
            self.state = 210
            self.match(dgdlParser.T__3)
            self.state = 211
            self.storeID()
            self.state = 212
            self.match(dgdlParser.T__8)
            self.state = 213
            self.match(dgdlParser.T__14)
            self.state = 214
            self.match(dgdlParser.T__3)
            self.state = 215
            self.storeOwner()
            self.state = 216
            self.match(dgdlParser.T__8)
            self.state = 217
            self.match(dgdlParser.T__15)
            self.state = 218
            self.match(dgdlParser.T__3)
            self.state = 219
            self.storeStructure()
            self.state = 220
            self.match(dgdlParser.T__8)
            self.state = 221
            self.match(dgdlParser.T__16)
            self.state = 222
            self.match(dgdlParser.T__3)
            self.state = 223
            self.storeVisibility()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 224
                self.match(dgdlParser.T__8)
                self.state = 225
                self.storeContent()


            self.state = 228
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_storeID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreID" ):
                listener.enterStoreID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreID" ):
                listener.exitStoreID(self)




    def storeID(self):

        localctx = dgdlParser.StoreIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_storeID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreOwnerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dgdlParser.IdentifierContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_storeOwner

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreOwner" ):
                listener.enterStoreOwner(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreOwner" ):
                listener.exitStoreOwner(self)




    def storeOwner(self):

        localctx = dgdlParser.StoreOwnerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_storeOwner)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Identifier]:
                self.state = 232
                self.identifier()
                pass
            elif token in [dgdlParser.T__5]:
                self.state = 233
                self.match(dgdlParser.T__5)
                self.state = 234
                self.identifier()
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 235
                    self.match(dgdlParser.T__8)
                    self.state = 236
                    self.identifier()
                    self.state = 239 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==dgdlParser.T__8):
                        break

                self.state = 241
                self.match(dgdlParser.T__6)
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


    class StoreStructureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(dgdlParser.SET, 0)

        def QUEUE(self):
            return self.getToken(dgdlParser.QUEUE, 0)

        def STACK(self):
            return self.getToken(dgdlParser.STACK, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_storeStructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreStructure" ):
                listener.enterStoreStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreStructure" ):
                listener.exitStoreStructure(self)




    def storeStructure(self):

        localctx = dgdlParser.StoreStructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_storeStructure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not(((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (dgdlParser.SET - 74)) | (1 << (dgdlParser.QUEUE - 74)) | (1 << (dgdlParser.STACK - 74)))) != 0)):
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


    class StoreVisibilityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(dgdlParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(dgdlParser.PRIVATE, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_storeVisibility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreVisibility" ):
                listener.enterStoreVisibility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreVisibility" ):
                listener.exitStoreVisibility(self)




    def storeVisibility(self):

        localctx = dgdlParser.StoreVisibilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_storeVisibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not(_la==dgdlParser.PUBLIC or _la==dgdlParser.PRIVATE):
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


    class StoreContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def contentVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.ContentVarContext)
            else:
                return self.getTypedRuleContext(dgdlParser.ContentVarContext,i)


        def STRINGLITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(dgdlParser.STRINGLITERAL)
            else:
                return self.getToken(dgdlParser.STRINGLITERAL, i)

        def getRuleIndex(self):
            return dgdlParser.RULE_storeContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreContent" ):
                listener.enterStoreContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreContent" ):
                listener.exitStoreContent(self)




    def storeContent(self):

        localctx = dgdlParser.StoreContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_storeContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(dgdlParser.T__5)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.LowerChar]:
                self.state = 250
                self.contentVar()
                pass
            elif token in [dgdlParser.STRINGLITERAL]:
                self.state = 251
                self.match(dgdlParser.STRINGLITERAL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__8:
                self.state = 254
                self.match(dgdlParser.T__8)
                self.state = 257
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [dgdlParser.LowerChar]:
                    self.state = 255
                    self.contentVar()
                    pass
                elif token in [dgdlParser.STRINGLITERAL]:
                    self.state = 256
                    self.match(dgdlParser.STRINGLITERAL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.match(dgdlParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BacktrackContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def onoff(self):
            return self.getTypedRuleContext(dgdlParser.OnoffContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_backtrack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBacktrack" ):
                listener.enterBacktrack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBacktrack" ):
                listener.exitBacktrack(self)




    def backtrack(self):

        localctx = dgdlParser.BacktrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_backtrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(dgdlParser.T__17)
            self.state = 267
            self.match(dgdlParser.T__1)
            self.state = 268
            self.onoff()
            self.state = 269
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnoffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_onoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnoff" ):
                listener.enterOnoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnoff" ):
                listener.exitOnoff(self)




    def onoff(self):

        localctx = dgdlParser.OnoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_onoff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__18 or _la==dgdlParser.T__19):
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


    class MinplayersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(dgdlParser.NumberContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_minplayers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinplayers" ):
                listener.enterMinplayers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinplayers" ):
                listener.exitMinplayers(self)




    def minplayers(self):

        localctx = dgdlParser.MinplayersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_minplayers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxplayersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(dgdlParser.NumberContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_maxplayers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxplayers" ):
                listener.enterMaxplayers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxplayers" ):
                listener.exitMaxplayers(self)




    def maxplayers(self):

        localctx = dgdlParser.MaxplayersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_maxplayers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Number]:
                self.state = 275
                self.number()
                pass
            elif token in [dgdlParser.T__20]:
                self.state = 276
                self.match(dgdlParser.T__20)
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


    class RulesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleID(self):
            return self.getTypedRuleContext(dgdlParser.RuleIDContext,0)


        def scopeType(self):
            return self.getTypedRuleContext(dgdlParser.ScopeTypeContext,0)


        def ruleBody(self):
            return self.getTypedRuleContext(dgdlParser.RuleBodyContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRules" ):
                listener.enterRules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRules" ):
                listener.exitRules(self)




    def rules(self):

        localctx = dgdlParser.RulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_rules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(dgdlParser.T__21)
            self.state = 280
            self.match(dgdlParser.T__1)
            self.state = 281
            self.match(dgdlParser.T__2)
            self.state = 282
            self.match(dgdlParser.T__3)
            self.state = 283
            self.ruleID()
            self.state = 284
            self.match(dgdlParser.T__8)
            self.state = 285
            self.match(dgdlParser.T__22)
            self.state = 286
            self.match(dgdlParser.T__3)
            self.state = 287
            self.scopeType()
            self.state = 288
            self.match(dgdlParser.T__4)
            self.state = 289
            self.ruleBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_ruleID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleID" ):
                listener.enterRuleID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleID" ):
                listener.exitRuleID(self)




    def ruleID(self):

        localctx = dgdlParser.RuleIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ruleID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INITIAL(self):
            return self.getToken(dgdlParser.INITIAL, 0)

        def TURNWISE(self):
            return self.getToken(dgdlParser.TURNWISE, 0)

        def MOVEWISE(self):
            return self.getToken(dgdlParser.MOVEWISE, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_scopeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopeType" ):
                listener.enterScopeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopeType" ):
                listener.exitScopeType(self)




    def scopeType(self):

        localctx = dgdlParser.ScopeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_scopeType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            _la = self._input.LA(1)
            if not(((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & ((1 << (dgdlParser.INITIAL - 71)) | (1 << (dgdlParser.TURNWISE - 71)) | (1 << (dgdlParser.MOVEWISE - 71)))) != 0)):
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


    class RuleBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effects(self):
            return self.getTypedRuleContext(dgdlParser.EffectsContext,0)


        def conditional(self):
            return self.getTypedRuleContext(dgdlParser.ConditionalContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_ruleBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleBody" ):
                listener.enterRuleBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleBody" ):
                listener.exitRuleBody(self)




    def ruleBody(self):

        localctx = dgdlParser.RuleBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ruleBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(dgdlParser.T__5)
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__13, dgdlParser.T__24, dgdlParser.T__32, dgdlParser.T__38, dgdlParser.T__39]:
                self.state = 296
                self.effects()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==dgdlParser.T__40:
                    self.state = 297
                    self.conditional()


                pass
            elif token in [dgdlParser.T__40]:
                self.state = 300
                self.conditional()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 303
            self.match(dgdlParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.EffectContext)
            else:
                return self.getTypedRuleContext(dgdlParser.EffectContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_effects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffects" ):
                listener.enterEffects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffects" ):
                listener.exitEffects(self)




    def effects(self):

        localctx = dgdlParser.EffectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_effects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 305
                self.effect()
                self.state = 308 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__13) | (1 << dgdlParser.T__24) | (1 << dgdlParser.T__32) | (1 << dgdlParser.T__38) | (1 << dgdlParser.T__39))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def move(self):
            return self.getTypedRuleContext(dgdlParser.MoveContext,0)


        def storeOp(self):
            return self.getTypedRuleContext(dgdlParser.StoreOpContext,0)


        def statusUpdate(self):
            return self.getTypedRuleContext(dgdlParser.StatusUpdateContext,0)


        def roleAssignment(self):
            return self.getTypedRuleContext(dgdlParser.RoleAssignmentContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect" ):
                listener.enterEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect" ):
                listener.exitEffect(self)




    def effect(self):

        localctx = dgdlParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_effect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__24]:
                self.state = 310
                self.move()
                pass
            elif token in [dgdlParser.T__13]:
                self.state = 311
                self.storeOp()
                pass
            elif token in [dgdlParser.T__32]:
                self.state = 312
                self.statusUpdate()
                pass
            elif token in [dgdlParser.T__38, dgdlParser.T__39]:
                self.state = 313
                self.roleAssignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 316
            self.match(dgdlParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveaction(self):
            return self.getTypedRuleContext(dgdlParser.MoveactionContext,0)


        def movetime(self):
            return self.getTypedRuleContext(dgdlParser.MovetimeContext,0)


        def moveID(self):
            return self.getTypedRuleContext(dgdlParser.MoveIDContext,0)


        def addressee(self):
            return self.getTypedRuleContext(dgdlParser.AddresseeContext,0)


        def content(self):
            return self.getTypedRuleContext(dgdlParser.ContentContext,0)


        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)




    def move(self):

        localctx = dgdlParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_move)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(dgdlParser.T__24)
            self.state = 319
            self.match(dgdlParser.T__1)
            self.state = 320
            self.moveaction()
            self.state = 321
            self.match(dgdlParser.T__8)
            self.state = 322
            self.movetime()
            self.state = 323
            self.match(dgdlParser.T__8)
            self.state = 324
            self.moveID()
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 325
                self.match(dgdlParser.T__8)
                self.state = 326
                self.addressee()


            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 329
                self.match(dgdlParser.T__8)
                self.state = 330
                self.content()


            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 333
                self.match(dgdlParser.T__8)
                self.state = 334
                self.user()


            self.state = 337
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveactionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_moveaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveaction" ):
                listener.enterMoveaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveaction" ):
                listener.exitMoveaction(self)




    def moveaction(self):

        localctx = dgdlParser.MoveactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_moveaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__25 or _la==dgdlParser.T__26):
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


    class MovetimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_movetime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMovetime" ):
                listener.enterMovetime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMovetime" ):
                listener.exitMovetime(self)




    def movetime(self):

        localctx = dgdlParser.MovetimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_movetime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__27 or _la==dgdlParser.T__28):
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


    class MoveIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_moveID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveID" ):
                listener.enterMoveID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveID" ):
                listener.exitMoveID(self)




    def moveID(self):

        localctx = dgdlParser.MoveIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_moveID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddresseeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_addressee

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressee" ):
                listener.enterAddressee(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressee" ):
                listener.exitAddressee(self)




    def addressee(self):

        localctx = dgdlParser.AddresseeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_addressee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(dgdlParser.T__29)
            self.state = 346
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def contentVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.ContentVarContext)
            else:
                return self.getTypedRuleContext(dgdlParser.ContentVarContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = dgdlParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(dgdlParser.T__5)
            self.state = 349
            self.contentVar()
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__8:
                self.state = 350
                self.match(dgdlParser.T__8)
                self.state = 351
                self.contentVar()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
            self.match(dgdlParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storeaction(self):
            return self.getTypedRuleContext(dgdlParser.StoreactionContext,0)


        def storeContent(self):
            return self.getTypedRuleContext(dgdlParser.StoreContentContext,0)


        def storeID(self):
            return self.getTypedRuleContext(dgdlParser.StoreIDContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_storeOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreOp" ):
                listener.enterStoreOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreOp" ):
                listener.exitStoreOp(self)




    def storeOp(self):

        localctx = dgdlParser.StoreOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_storeOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(dgdlParser.T__13)
            self.state = 360
            self.match(dgdlParser.T__1)
            self.state = 361
            self.storeaction()
            self.state = 362
            self.match(dgdlParser.T__8)
            self.state = 363
            self.storeContent()
            self.state = 364
            self.match(dgdlParser.T__8)
            self.state = 365
            self.storeID()
            self.state = 366
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreactionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_storeaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreaction" ):
                listener.enterStoreaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreaction" ):
                listener.exitStoreaction(self)




    def storeaction(self):

        localctx = dgdlParser.StoreactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_storeaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__25) | (1 << dgdlParser.T__30) | (1 << dgdlParser.T__31))) != 0)):
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


    class StatusUpdateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def status(self):
            return self.getTypedRuleContext(dgdlParser.StatusContext,0)


        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_statusUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatusUpdate" ):
                listener.enterStatusUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatusUpdate" ):
                listener.exitStatusUpdate(self)




    def statusUpdate(self):

        localctx = dgdlParser.StatusUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statusUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(dgdlParser.T__32)
            self.state = 371
            self.match(dgdlParser.T__1)
            self.state = 372
            self.status()
            self.state = 373
            self.match(dgdlParser.T__8)
            self.state = 374
            self.identifier()
            self.state = 375
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_status

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatus" ):
                listener.enterStatus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatus" ):
                listener.exitStatus(self)




    def status(self):

        localctx = dgdlParser.StatusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_status)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__33) | (1 << dgdlParser.T__34) | (1 << dgdlParser.T__35) | (1 << dgdlParser.T__36) | (1 << dgdlParser.T__37))) != 0)):
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


    class RoleAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(dgdlParser.AssignmentContext,0)


        def unassignment(self):
            return self.getTypedRuleContext(dgdlParser.UnassignmentContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_roleAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleAssignment" ):
                listener.enterRoleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleAssignment" ):
                listener.exitRoleAssignment(self)




    def roleAssignment(self):

        localctx = dgdlParser.RoleAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_roleAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__38]:
                self.state = 379
                self.assignment()
                pass
            elif token in [dgdlParser.T__39]:
                self.state = 380
                self.unassignment()
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


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def role(self):
            return self.getTypedRuleContext(dgdlParser.RoleContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = dgdlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(dgdlParser.T__38)
            self.state = 384
            self.match(dgdlParser.T__1)
            self.state = 385
            self.user()
            self.state = 386
            self.match(dgdlParser.T__8)
            self.state = 387
            self.role()
            self.state = 388
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnassignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def role(self):
            return self.getTypedRuleContext(dgdlParser.RoleContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_unassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnassignment" ):
                listener.enterUnassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnassignment" ):
                listener.exitUnassignment(self)




    def unassignment(self):

        localctx = dgdlParser.UnassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(dgdlParser.T__39)
            self.state = 391
            self.match(dgdlParser.T__1)
            self.state = 392
            self.user()
            self.state = 393
            self.match(dgdlParser.T__8)
            self.state = 394
            self.role()
            self.state = 395
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UserContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_user

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUser" ):
                listener.enterUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUser" ):
                listener.exitUser(self)




    def user(self):

        localctx = dgdlParser.UserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_user)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirements(self):
            return self.getTypedRuleContext(dgdlParser.RequirementsContext,0)


        def effects(self):
            return self.getTypedRuleContext(dgdlParser.EffectsContext,0)


        def condelseif(self):
            return self.getTypedRuleContext(dgdlParser.CondelseifContext,0)


        def condelse(self):
            return self.getTypedRuleContext(dgdlParser.CondelseContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = dgdlParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(dgdlParser.T__40)
            self.state = 400
            self.match(dgdlParser.T__1)
            self.state = 401
            self.requirements()
            self.state = 402
            self.match(dgdlParser.T__4)
            self.state = 403
            self.match(dgdlParser.T__5)
            self.state = 404
            self.effects()
            self.state = 405
            self.match(dgdlParser.T__6)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__51:
                self.state = 406
                self.condelseif()


            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__53:
                self.state = 409
                self.condelse()


            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__23:
                self.state = 412
                self.match(dgdlParser.T__23)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.ConditionContext)
            else:
                return self.getTypedRuleContext(dgdlParser.ConditionContext,i)


        def AMPAND(self, i:int=None):
            if i is None:
                return self.getTokens(dgdlParser.AMPAND)
            else:
                return self.getToken(dgdlParser.AMPAND, i)

        def getRuleIndex(self):
            return dgdlParser.RULE_requirements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirements" ):
                listener.enterRequirements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirements" ):
                listener.exitRequirements(self)




    def requirements(self):

        localctx = dgdlParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.condition()
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.AMPAND:
                self.state = 416
                self.match(dgdlParser.AMPAND)
                self.state = 417
                self.condition()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def event(self):
            return self.getTypedRuleContext(dgdlParser.EventContext,0)


        def roleInspection(self):
            return self.getTypedRuleContext(dgdlParser.RoleInspectionContext,0)


        def storeInspection(self):
            return self.getTypedRuleContext(dgdlParser.StoreInspectionContext,0)


        def NEG(self):
            return self.getToken(dgdlParser.NEG, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = dgdlParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.NEG:
                self.state = 423
                self.match(dgdlParser.NEG)


            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__41]:
                self.state = 426
                self.event()
                pass
            elif token in [dgdlParser.T__46]:
                self.state = 427
                self.roleInspection()
                pass
            elif token in [dgdlParser.T__47]:
                self.state = 428
                self.storeInspection()
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


    class EventContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eventpos(self):
            return self.getTypedRuleContext(dgdlParser.EventposContext,0)


        def moveID(self):
            return self.getTypedRuleContext(dgdlParser.MoveIDContext,0)


        def content(self):
            return self.getTypedRuleContext(dgdlParser.ContentContext,0)


        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = dgdlParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(dgdlParser.T__41)
            self.state = 432
            self.match(dgdlParser.T__1)
            self.state = 433
            self.eventpos()
            self.state = 434
            self.match(dgdlParser.T__8)
            self.state = 435
            self.moveID()
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 436
                self.match(dgdlParser.T__8)
                self.state = 437
                self.content()


            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 440
                self.match(dgdlParser.T__8)
                self.state = 441
                self.user()


            self.state = 444
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventposContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_eventpos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventpos" ):
                listener.enterEventpos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventpos" ):
                listener.exitEventpos(self)




    def eventpos(self):

        localctx = dgdlParser.EventposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_eventpos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__42) | (1 << dgdlParser.T__43) | (1 << dgdlParser.T__44) | (1 << dgdlParser.T__45))) != 0)):
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


    class RoleInspectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playerID(self):
            return self.getTypedRuleContext(dgdlParser.PlayerIDContext,0)


        def role(self):
            return self.getTypedRuleContext(dgdlParser.RoleContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_roleInspection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleInspection" ):
                listener.enterRoleInspection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleInspection" ):
                listener.exitRoleInspection(self)




    def roleInspection(self):

        localctx = dgdlParser.RoleInspectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_roleInspection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(dgdlParser.T__46)
            self.state = 449
            self.match(dgdlParser.T__1)
            self.state = 450
            self.playerID()
            self.state = 451
            self.match(dgdlParser.T__8)
            self.state = 452
            self.role()
            self.state = 453
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreInspectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storepos(self):
            return self.getTypedRuleContext(dgdlParser.StoreposContext,0)


        def storeContent(self):
            return self.getTypedRuleContext(dgdlParser.StoreContentContext,0)


        def storeID(self):
            return self.getTypedRuleContext(dgdlParser.StoreIDContext,0)


        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def storetime(self):
            return self.getTypedRuleContext(dgdlParser.StoretimeContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_storeInspection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreInspection" ):
                listener.enterStoreInspection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreInspection" ):
                listener.exitStoreInspection(self)




    def storeInspection(self):

        localctx = dgdlParser.StoreInspectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_storeInspection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(dgdlParser.T__47)
            self.state = 456
            self.match(dgdlParser.T__1)
            self.state = 457
            self.storepos()
            self.state = 458
            self.match(dgdlParser.T__8)
            self.state = 459
            self.storeContent()
            self.state = 460
            self.match(dgdlParser.T__8)
            self.state = 461
            self.storeID()
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 462
                self.match(dgdlParser.T__8)
                self.state = 463
                self.user()


            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 466
                self.match(dgdlParser.T__8)
                self.state = 467
                self.storetime()


            self.state = 470
            self.match(dgdlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreposContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dgdlParser.RULE_storepos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStorepos" ):
                listener.enterStorepos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStorepos" ):
                listener.exitStorepos(self)




    def storepos(self):

        localctx = dgdlParser.StoreposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_storepos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__18) | (1 << dgdlParser.T__48) | (1 << dgdlParser.T__49))) != 0)):
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


    class StoretimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INITIAL(self):
            return self.getToken(dgdlParser.INITIAL, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_storetime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoretime" ):
                listener.enterStoretime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoretime" ):
                listener.exitStoretime(self)




    def storetime(self):

        localctx = dgdlParser.StoretimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_storetime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (dgdlParser.T__44 - 45)) | (1 << (dgdlParser.T__50 - 45)) | (1 << (dgdlParser.INITIAL - 45)))) != 0)):
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


    class CondelseifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirements(self):
            return self.getTypedRuleContext(dgdlParser.RequirementsContext,0)


        def effects(self):
            return self.getTypedRuleContext(dgdlParser.EffectsContext,0)


        def condelseif(self):
            return self.getTypedRuleContext(dgdlParser.CondelseifContext,0)


        def condelse(self):
            return self.getTypedRuleContext(dgdlParser.CondelseContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_condelseif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondelseif" ):
                listener.enterCondelseif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondelseif" ):
                listener.exitCondelseif(self)




    def condelseif(self):

        localctx = dgdlParser.CondelseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_condelseif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(dgdlParser.T__51)
            self.state = 477
            self.requirements()
            self.state = 478
            self.match(dgdlParser.T__52)
            self.state = 479
            self.match(dgdlParser.T__5)
            self.state = 480
            self.effects()
            self.state = 481
            self.match(dgdlParser.T__6)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__51:
                self.state = 482
                self.condelseif()


            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 485
                self.condelse()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondelseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effects(self):
            return self.getTypedRuleContext(dgdlParser.EffectsContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_condelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondelse" ):
                listener.enterCondelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondelse" ):
                listener.exitCondelse(self)




    def condelse(self):

        localctx = dgdlParser.CondelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_condelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(dgdlParser.T__53)
            self.state = 489
            self.match(dgdlParser.T__5)
            self.state = 490
            self.effects()
            self.state = 491
            self.match(dgdlParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InteractionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveID(self):
            return self.getTypedRuleContext(dgdlParser.MoveIDContext,0)


        def ruleBody(self):
            return self.getTypedRuleContext(dgdlParser.RuleBodyContext,0)


        def user(self):
            return self.getTypedRuleContext(dgdlParser.UserContext,0)


        def content(self):
            return self.getTypedRuleContext(dgdlParser.ContentContext,0)


        def opener(self):
            return self.getTypedRuleContext(dgdlParser.OpenerContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_interaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteraction" ):
                listener.enterInteraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteraction" ):
                listener.exitInteraction(self)




    def interaction(self):

        localctx = dgdlParser.InteractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_interaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(dgdlParser.T__54)
            self.state = 494
            self.match(dgdlParser.T__1)
            self.state = 495
            self.match(dgdlParser.T__2)
            self.state = 496
            self.match(dgdlParser.T__3)
            self.state = 497
            self.moveID()
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 498
                self.match(dgdlParser.T__8)
                self.state = 499
                self.match(dgdlParser.T__55)
                self.state = 500
                self.match(dgdlParser.T__3)
                self.state = 501
                self.user()


            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 504
                self.match(dgdlParser.T__8)
                self.state = 505
                self.match(dgdlParser.T__56)
                self.state = 506
                self.match(dgdlParser.T__3)
                self.state = 507
                self.content()


            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__8:
                self.state = 510
                self.match(dgdlParser.T__8)
                self.state = 511
                self.match(dgdlParser.T__57)
                self.state = 512
                self.match(dgdlParser.T__3)
                self.state = 513
                self.opener()


            self.state = 516
            self.match(dgdlParser.T__4)
            self.state = 517
            self.ruleBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(dgdlParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_opener

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpener" ):
                listener.enterOpener(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpener" ):
                listener.exitOpener(self)




    def opener(self):

        localctx = dgdlParser.OpenerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_opener)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(dgdlParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpperCharContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UpperChar(self):
            return self.getToken(dgdlParser.UpperChar, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_upperChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpperChar" ):
                listener.enterUpperChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpperChar" ):
                listener.exitUpperChar(self)




    def upperChar(self):

        localctx = dgdlParser.UpperCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_upperChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(dgdlParser.UpperChar)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LowerCharContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LowerChar(self):
            return self.getToken(dgdlParser.LowerChar, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_lowerChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowerChar" ):
                listener.enterLowerChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowerChar" ):
                listener.exitLowerChar(self)




    def lowerChar(self):

        localctx = dgdlParser.LowerCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_lowerChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(dgdlParser.LowerChar)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(dgdlParser.Identifier, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = dgdlParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(dgdlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(dgdlParser.Number, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = dgdlParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(dgdlParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LowerChar(self):
            return self.getToken(dgdlParser.LowerChar, 0)

        def getRuleIndex(self):
            return dgdlParser.RULE_contentVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentVar" ):
                listener.enterContentVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentVar" ):
                listener.exitContentVar(self)




    def contentVar(self):

        localctx = dgdlParser.ContentVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_contentVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(dgdlParser.LowerChar)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





