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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\2\7\2g\n\2\f\2")
        buf.write("\16\2j\13\2\3\2\6\2m\n\2\r\2\16\2n\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\5\4w\n\4\3\4\3\4\6\4{\n\4\r\4\16\4|\3\4\7\4\u0080")
        buf.write("\n\4\f\4\16\4\u0083\13\4\3\4\5\4\u0086\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\7\5\u008d\n\5\f\5\16\5\u0090\13\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\5\6\u0097\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00ab\n\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u00b1\n\b\3\b\3\b\3\b\3\b\5\b\u00b7")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d0\n")
        buf.write("\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\6\f\u00db\n\f")
        buf.write("\r\f\16\f\u00dc\3\f\3\f\5\f\u00e1\n\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00eb\n\17\f\17\16\17\u00ee")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\5\23\u00fd\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u0114\n\27\3\27\5")
        buf.write("\27\u0117\n\27\3\27\3\27\3\30\3\30\3\30\7\30\u011e\n\30")
        buf.write("\f\30\16\30\u0121\13\30\3\31\3\31\3\31\3\31\5\31\u0127")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0132\n\32\3\32\3\32\5\32\u0136\n\32\3\32\3\32\5\32\u013a")
        buf.write("\n\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\7\37\u014b\n\37\f\37\16\37\u014e")
        buf.write("\13\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\5$\u0168\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\5(\u0181\n(\3(\5(\u0184\n(\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\5*\u018f\n*\3*\5*\u0192\n*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\2\2")
        buf.write("\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\n\3\2<>\3\2?@\3\2\22")
        buf.write("\23\3\29;\3\2\33\34\3\2\35\36\4\2\33\33 !\3\2#\'\2\u0194")
        buf.write("\2b\3\2\2\2\4s\3\2\2\2\6v\3\2\2\2\b\u0087\3\2\2\2\n\u0096")
        buf.write("\3\2\2\2\f\u0098\3\2\2\2\16\u00a3\3\2\2\2\20\u00ba\3\2")
        buf.write("\2\2\22\u00bc\3\2\2\2\24\u00d3\3\2\2\2\26\u00e0\3\2\2")
        buf.write("\2\30\u00e2\3\2\2\2\32\u00e4\3\2\2\2\34\u00e6\3\2\2\2")
        buf.write("\36\u00f1\3\2\2\2 \u00f6\3\2\2\2\"\u00f8\3\2\2\2$\u00fc")
        buf.write("\3\2\2\2&\u00fe\3\2\2\2(\u010b\3\2\2\2*\u010d\3\2\2\2")
        buf.write(",\u010f\3\2\2\2.\u011a\3\2\2\2\60\u0126\3\2\2\2\62\u0128")
        buf.write("\3\2\2\2\64\u013d\3\2\2\2\66\u013f\3\2\2\28\u0141\3\2")
        buf.write("\2\2:\u0143\3\2\2\2<\u0146\3\2\2\2>\u0151\3\2\2\2@\u015a")
        buf.write("\3\2\2\2B\u015c\3\2\2\2D\u0163\3\2\2\2F\u0167\3\2\2\2")
        buf.write("H\u0169\3\2\2\2J\u0170\3\2\2\2L\u0177\3\2\2\2N\u0179\3")
        buf.write("\2\2\2P\u0185\3\2\2\2R\u0187\3\2\2\2T\u0193\3\2\2\2V\u0198")
        buf.write("\3\2\2\2X\u019a\3\2\2\2Z\u019c\3\2\2\2\\\u019e\3\2\2\2")
        buf.write("^\u01a0\3\2\2\2`\u01a2\3\2\2\2bc\5\4\3\2cd\7\3\2\2dh\5")
        buf.write("\6\4\2eg\5&\24\2fe\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2")
        buf.write("\2il\3\2\2\2jh\3\2\2\2km\5V,\2lk\3\2\2\2mn\3\2\2\2nl\3")
        buf.write("\2\2\2no\3\2\2\2op\3\2\2\2pq\7\4\2\2qr\7\2\2\3r\3\3\2")
        buf.write("\2\2st\5\\/\2t\5\3\2\2\2uw\5\b\5\2vu\3\2\2\2vw\3\2\2\2")
        buf.write("wx\3\2\2\2xz\5\f\7\2y{\5\16\b\2zy\3\2\2\2{|\3\2\2\2|z")
        buf.write("\3\2\2\2|}\3\2\2\2}\u0081\3\2\2\2~\u0080\5\22\n\2\177")
        buf.write("~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0084\u0086\5\36\20\2\u0085\u0084\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\7\3\2\2\2\u0087\u0088\7\5\2\2\u0088\u0089")
        buf.write("\7\3\2\2\u0089\u008e\5\n\6\2\u008a\u008b\7\6\2\2\u008b")
        buf.write("\u008d\5\n\6\2\u008c\u008a\3\2\2\2\u008d\u0090\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\4\2\2\u0092\t")
        buf.write("\3\2\2\2\u0093\u0097\7\67\2\2\u0094\u0097\78\2\2\u0095")
        buf.write("\u0097\5\\/\2\u0096\u0093\3\2\2\2\u0096\u0094\3\2\2\2")
        buf.write("\u0096\u0095\3\2\2\2\u0097\13\3\2\2\2\u0098\u0099\7\7")
        buf.write("\2\2\u0099\u009a\7\3\2\2\u009a\u009b\7\b\2\2\u009b\u009c")
        buf.write("\7\t\2\2\u009c\u009d\5\"\22\2\u009d\u009e\7\6\2\2\u009e")
        buf.write("\u009f\7\n\2\2\u009f\u00a0\7\t\2\2\u00a0\u00a1\5$\23\2")
        buf.write("\u00a1\u00a2\7\4\2\2\u00a2\r\3\2\2\2\u00a3\u00a4\7\13")
        buf.write("\2\2\u00a4\u00a5\7\3\2\2\u00a5\u00a6\7\f\2\2\u00a6\u00a7")
        buf.write("\7\t\2\2\u00a7\u00aa\5\20\t\2\u00a8\u00a9\7\6\2\2\u00a9")
        buf.write("\u00ab\5\b\5\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00b0\3\2\2\2\u00ac\u00ad\7\6\2\2\u00ad\u00ae\7")
        buf.write("\b\2\2\u00ae\u00af\7\t\2\2\u00af\u00b1\5\"\22\2\u00b0")
        buf.write("\u00ac\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b6\3\2\2\2")
        buf.write("\u00b2\u00b3\7\6\2\2\u00b3\u00b4\7\n\2\2\u00b4\u00b5\7")
        buf.write("\t\2\2\u00b5\u00b7\5$\23\2\u00b6\u00b2\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\7\4\2\2\u00b9")
        buf.write("\17\3\2\2\2\u00ba\u00bb\5\\/\2\u00bb\21\3\2\2\2\u00bc")
        buf.write("\u00bd\7\r\2\2\u00bd\u00be\7\3\2\2\u00be\u00bf\7\f\2\2")
        buf.write("\u00bf\u00c0\7\t\2\2\u00c0\u00c1\5\24\13\2\u00c1\u00c2")
        buf.write("\7\6\2\2\u00c2\u00c3\7\16\2\2\u00c3\u00c4\7\t\2\2\u00c4")
        buf.write("\u00c5\5\26\f\2\u00c5\u00c6\7\6\2\2\u00c6\u00c7\7\17\2")
        buf.write("\2\u00c7\u00c8\7\t\2\2\u00c8\u00c9\5\30\r\2\u00c9\u00ca")
        buf.write("\7\6\2\2\u00ca\u00cb\7\20\2\2\u00cb\u00cc\7\t\2\2\u00cc")
        buf.write("\u00cf\5\32\16\2\u00cd\u00ce\7\6\2\2\u00ce\u00d0\5\34")
        buf.write("\17\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\u00d2\7\4\2\2\u00d2\23\3\2\2\2\u00d3\u00d4")
        buf.write("\5\\/\2\u00d4\25\3\2\2\2\u00d5\u00e1\5\\/\2\u00d6\u00d7")
        buf.write("\7\3\2\2\u00d7\u00da\5\\/\2\u00d8\u00d9\7\6\2\2\u00d9")
        buf.write("\u00db\5\\/\2\u00da\u00d8\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3")
        buf.write("\2\2\2\u00de\u00df\7\4\2\2\u00df\u00e1\3\2\2\2\u00e0\u00d5")
        buf.write("\3\2\2\2\u00e0\u00d6\3\2\2\2\u00e1\27\3\2\2\2\u00e2\u00e3")
        buf.write("\t\2\2\2\u00e3\31\3\2\2\2\u00e4\u00e5\t\3\2\2\u00e5\33")
        buf.write("\3\2\2\2\u00e6\u00e7\7\3\2\2\u00e7\u00ec\5\\/\2\u00e8")
        buf.write("\u00e9\7\6\2\2\u00e9\u00eb\5\\/\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3")
        buf.write("\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0")
        buf.write("\7\4\2\2\u00f0\35\3\2\2\2\u00f1\u00f2\7\21\2\2\u00f2\u00f3")
        buf.write("\7\3\2\2\u00f3\u00f4\5 \21\2\u00f4\u00f5\7\4\2\2\u00f5")
        buf.write("\37\3\2\2\2\u00f6\u00f7\t\4\2\2\u00f7!\3\2\2\2\u00f8\u00f9")
        buf.write("\5^\60\2\u00f9#\3\2\2\2\u00fa\u00fd\5^\60\2\u00fb\u00fd")
        buf.write("\7\24\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("%\3\2\2\2\u00fe\u00ff\7\25\2\2\u00ff\u0100\7\3\2\2\u0100")
        buf.write("\u0101\7\f\2\2\u0101\u0102\7\t\2\2\u0102\u0103\5(\25\2")
        buf.write("\u0103\u0104\7\6\2\2\u0104\u0105\7\26\2\2\u0105\u0106")
        buf.write("\7\t\2\2\u0106\u0107\5*\26\2\u0107\u0108\7\6\2\2\u0108")
        buf.write("\u0109\5,\27\2\u0109\u010a\7\4\2\2\u010a\'\3\2\2\2\u010b")
        buf.write("\u010c\5\\/\2\u010c)\3\2\2\2\u010d\u010e\t\5\2\2\u010e")
        buf.write("+\3\2\2\2\u010f\u0116\7\3\2\2\u0110\u0113\5.\30\2\u0111")
        buf.write("\u0112\7\27\2\2\u0112\u0114\5N(\2\u0113\u0111\3\2\2\2")
        buf.write("\u0113\u0114\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0117\5")
        buf.write("N(\2\u0116\u0110\3\2\2\2\u0116\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u0119\7\4\2\2\u0119-\3\2\2\2\u011a\u011f")
        buf.write("\5\60\31\2\u011b\u011c\7\27\2\2\u011c\u011e\5\60\31\2")
        buf.write("\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u011f\u0120\3\2\2\2\u0120/\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0127\5\62\32\2\u0123\u0127\5> \2\u0124")
        buf.write("\u0127\5B\"\2\u0125\u0127\5F$\2\u0126\u0122\3\2\2\2\u0126")
        buf.write("\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127\61\3\2\2\2\u0128\u0129\7\30\2\2\u0129\u012a\7\31")
        buf.write("\2\2\u012a\u012b\5\64\33\2\u012b\u012c\7\6\2\2\u012c\u012d")
        buf.write("\5\66\34\2\u012d\u012e\7\6\2\2\u012e\u0131\58\35\2\u012f")
        buf.write("\u0130\7\6\2\2\u0130\u0132\5:\36\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0134\7")
        buf.write("\6\2\2\u0134\u0136\5<\37\2\u0135\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0138\7\6\2\2\u0138")
        buf.write("\u013a\5L\'\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013b\u013c\7\32\2\2\u013c\63\3\2")
        buf.write("\2\2\u013d\u013e\t\6\2\2\u013e\65\3\2\2\2\u013f\u0140")
        buf.write("\t\7\2\2\u0140\67\3\2\2\2\u0141\u0142\5\\/\2\u01429\3")
        buf.write("\2\2\2\u0143\u0144\7\37\2\2\u0144\u0145\5\\/\2\u0145;")
        buf.write("\3\2\2\2\u0146\u0147\7\3\2\2\u0147\u014c\5`\61\2\u0148")
        buf.write("\u0149\7\6\2\2\u0149\u014b\5`\61\2\u014a\u0148\3\2\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150")
        buf.write("\7\4\2\2\u0150=\3\2\2\2\u0151\u0152\7\r\2\2\u0152\u0153")
        buf.write("\7\31\2\2\u0153\u0154\5@!\2\u0154\u0155\7\6\2\2\u0155")
        buf.write("\u0156\5\34\17\2\u0156\u0157\7\6\2\2\u0157\u0158\5\24")
        buf.write("\13\2\u0158\u0159\7\32\2\2\u0159?\3\2\2\2\u015a\u015b")
        buf.write("\t\b\2\2\u015bA\3\2\2\2\u015c\u015d\7\"\2\2\u015d\u015e")
        buf.write("\7\31\2\2\u015e\u015f\5D#\2\u015f\u0160\7\6\2\2\u0160")
        buf.write("\u0161\5\\/\2\u0161\u0162\7\32\2\2\u0162C\3\2\2\2\u0163")
        buf.write("\u0164\t\t\2\2\u0164E\3\2\2\2\u0165\u0168\5H%\2\u0166")
        buf.write("\u0168\5J&\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("G\3\2\2\2\u0169\u016a\7(\2\2\u016a\u016b\7\31\2\2\u016b")
        buf.write("\u016c\5L\'\2\u016c\u016d\7\6\2\2\u016d\u016e\5\n\6\2")
        buf.write("\u016e\u016f\7\32\2\2\u016fI\3\2\2\2\u0170\u0171\7)\2")
        buf.write("\2\u0171\u0172\7\31\2\2\u0172\u0173\5L\'\2\u0173\u0174")
        buf.write("\7\6\2\2\u0174\u0175\5\n\6\2\u0175\u0176\7\32\2\2\u0176")
        buf.write("K\3\2\2\2\u0177\u0178\5\\/\2\u0178M\3\2\2\2\u0179\u017a")
        buf.write("\7*\2\2\u017a\u017b\5P)\2\u017b\u017c\7+\2\2\u017c\u017d")
        buf.write("\7\3\2\2\u017d\u017e\5.\30\2\u017e\u0180\7\4\2\2\u017f")
        buf.write("\u0181\5R*\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0183\3\2\2\2\u0182\u0184\5T+\2\u0183\u0182\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184O\3\2\2\2\u0185\u0186\7,\2\2\u0186")
        buf.write("Q\3\2\2\2\u0187\u0188\7-\2\2\u0188\u0189\5P)\2\u0189\u018a")
        buf.write("\7+\2\2\u018a\u018b\7\3\2\2\u018b\u018c\5.\30\2\u018c")
        buf.write("\u018e\7\4\2\2\u018d\u018f\5R*\2\u018e\u018d\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u0192\5T+\2\u0191")
        buf.write("\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192S\3\2\2\2\u0193")
        buf.write("\u0194\7.\2\2\u0194\u0195\7\3\2\2\u0195\u0196\5.\30\2")
        buf.write("\u0196\u0197\7\4\2\2\u0197U\3\2\2\2\u0198\u0199\5\\/\2")
        buf.write("\u0199W\3\2\2\2\u019a\u019b\7\61\2\2\u019bY\3\2\2\2\u019c")
        buf.write("\u019d\7\60\2\2\u019d[\3\2\2\2\u019e\u019f\7/\2\2\u019f")
        buf.write("]\3\2\2\2\u01a0\u01a1\7\62\2\2\u01a1_\3\2\2\2\u01a2\u01a3")
        buf.write("\7\60\2\2\u01a3a\3\2\2\2\37hnv|\u0081\u0085\u008e\u0096")
        buf.write("\u00aa\u00b0\u00b6\u00cf\u00dc\u00e0\u00ec\u00fc\u0113")
        buf.write("\u0116\u011f\u0126\u0131\u0135\u0139\u014c\u0167\u0180")
        buf.write("\u0183\u018e\u0191")
        return buf.getvalue()


class dgdlParser ( Parser ):

    grammarFileName = "dgdl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'roles'", "','", "'participants'", 
                     "'min'", "':'", "'max'", "'player'", "'id'", "'store'", 
                     "'owner'", "'structure'", "'visibility'", "'backtracking'", 
                     "'on'", "'off'", "'undefined'", "'rule'", "'scope'", 
                     "'&'", "'move'", "'('", "')'", "'add'", "'delete'", 
                     "'next'", "'future'", "'$'", "'remove'", "'empty'", 
                     "'status'", "'active'", "'inactive'", "'complete'", 
                     "'incomplete'", "'terminate'", "'assign'", "'unassign'", 
                     "'if'", "'then'", "'{requirements}'", "'elseif '", 
                     "'else'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'listener'", "'speaker'", "'initial'", "'turnwise'", 
                     "'movewise'", "'set'", "'queue'", "'stack'", "'public'", 
                     "'private'" ]

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
                      "<INVALID>", "Identifier", "LowerChar", "UpperChar", 
                      "Number", "WS", "MOVEACTION", "MOVETIME", "ONOFF", 
                      "LISTENER", "SPEAKER", "INITIAL", "TURNWISE", "MOVEWISE", 
                      "SET", "QUEUE", "STACK", "PUBLIC", "PRIVATE", "STRINGLITERAL", 
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
    RULE_condelseif = 40
    RULE_condelse = 41
    RULE_interaction = 42
    RULE_upperChar = 43
    RULE_lowerChar = 44
    RULE_identifier = 45
    RULE_number = 46
    RULE_contentVar = 47

    ruleNames =  [ "game", "gameID", "composition", "roleList", "role", 
                   "participants", "player", "playerID", "store", "storeID", 
                   "storeOwner", "storeStructure", "storeVisibility", "storeContent", 
                   "backtrack", "onoff", "minplayers", "maxplayers", "rules", 
                   "ruleID", "scopeType", "ruleBody", "effects", "effect", 
                   "move", "moveaction", "movetime", "moveID", "addressee", 
                   "content", "storeOp", "storeaction", "statusUpdate", 
                   "status", "roleAssignment", "assignment", "unassignment", 
                   "user", "conditional", "requirements", "condelseif", 
                   "condelse", "interaction", "upperChar", "lowerChar", 
                   "identifier", "number", "contentVar" ]

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
    Identifier=45
    LowerChar=46
    UpperChar=47
    Number=48
    WS=49
    MOVEACTION=50
    MOVETIME=51
    ONOFF=52
    LISTENER=53
    SPEAKER=54
    INITIAL=55
    TURNWISE=56
    MOVEWISE=57
    SET=58
    QUEUE=59
    STACK=60
    PUBLIC=61
    PRIVATE=62
    STRINGLITERAL=63
    COMMENT=64
    LINE_COMMENT=65

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
            self.state = 96
            self.gameID()
            self.state = 97
            self.match(dgdlParser.T__0)
            self.state = 98
            self.composition()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__18:
                self.state = 99
                self.rules()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.interaction()
                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.Identifier):
                    break

            self.state = 110
            self.match(dgdlParser.T__1)
            self.state = 111
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
            self.state = 113
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
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__2:
                self.state = 115
                self.roleList()


            self.state = 118
            self.participants()
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.player()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.T__8):
                    break

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__10:
                self.state = 124
                self.store()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__14:
                self.state = 130
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
            self.state = 133
            self.match(dgdlParser.T__2)
            self.state = 134
            self.match(dgdlParser.T__0)
            self.state = 135
            self.role()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__3:
                self.state = 136
                self.match(dgdlParser.T__3)
                self.state = 137
                self.role()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(dgdlParser.T__1)
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.LISTENER]:
                self.state = 145
                self.match(dgdlParser.LISTENER)
                pass
            elif token in [dgdlParser.SPEAKER]:
                self.state = 146
                self.match(dgdlParser.SPEAKER)
                pass
            elif token in [dgdlParser.Identifier]:
                self.state = 147
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
            self.state = 150
            self.match(dgdlParser.T__4)
            self.state = 151
            self.match(dgdlParser.T__0)
            self.state = 152
            self.match(dgdlParser.T__5)
            self.state = 153
            self.match(dgdlParser.T__6)
            self.state = 154
            self.minplayers()
            self.state = 155
            self.match(dgdlParser.T__3)
            self.state = 156
            self.match(dgdlParser.T__7)
            self.state = 157
            self.match(dgdlParser.T__6)
            self.state = 158
            self.maxplayers()
            self.state = 159
            self.match(dgdlParser.T__1)
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
            self.state = 161
            self.match(dgdlParser.T__8)
            self.state = 162
            self.match(dgdlParser.T__0)
            self.state = 163
            self.match(dgdlParser.T__9)
            self.state = 164
            self.match(dgdlParser.T__6)
            self.state = 165
            self.playerID()
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 166
                self.match(dgdlParser.T__3)
                self.state = 167
                self.roleList()


            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(dgdlParser.T__3)
                self.state = 171
                self.match(dgdlParser.T__5)
                self.state = 172
                self.match(dgdlParser.T__6)
                self.state = 173
                self.minplayers()


            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__3:
                self.state = 176
                self.match(dgdlParser.T__3)
                self.state = 177
                self.match(dgdlParser.T__7)
                self.state = 178
                self.match(dgdlParser.T__6)
                self.state = 179
                self.maxplayers()


            self.state = 182
            self.match(dgdlParser.T__1)
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
            self.state = 184
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
            self.state = 186
            self.match(dgdlParser.T__10)
            self.state = 187
            self.match(dgdlParser.T__0)
            self.state = 188
            self.match(dgdlParser.T__9)
            self.state = 189
            self.match(dgdlParser.T__6)
            self.state = 190
            self.storeID()
            self.state = 191
            self.match(dgdlParser.T__3)
            self.state = 192
            self.match(dgdlParser.T__11)
            self.state = 193
            self.match(dgdlParser.T__6)
            self.state = 194
            self.storeOwner()
            self.state = 195
            self.match(dgdlParser.T__3)
            self.state = 196
            self.match(dgdlParser.T__12)
            self.state = 197
            self.match(dgdlParser.T__6)
            self.state = 198
            self.storeStructure()
            self.state = 199
            self.match(dgdlParser.T__3)
            self.state = 200
            self.match(dgdlParser.T__13)
            self.state = 201
            self.match(dgdlParser.T__6)
            self.state = 202
            self.storeVisibility()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__3:
                self.state = 203
                self.match(dgdlParser.T__3)
                self.state = 204
                self.storeContent()


            self.state = 207
            self.match(dgdlParser.T__1)
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
            self.state = 209
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
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Identifier]:
                self.state = 211
                self.identifier()
                pass
            elif token in [dgdlParser.T__0]:
                self.state = 212
                self.match(dgdlParser.T__0)
                self.state = 213
                self.identifier()
                self.state = 216 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 214
                    self.match(dgdlParser.T__3)
                    self.state = 215
                    self.identifier()
                    self.state = 218 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==dgdlParser.T__3):
                        break

                self.state = 220
                self.match(dgdlParser.T__1)
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
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.SET) | (1 << dgdlParser.QUEUE) | (1 << dgdlParser.STACK))) != 0)):
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
            self.state = 226
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dgdlParser.IdentifierContext,i)


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
            self.state = 228
            self.match(dgdlParser.T__0)
            self.state = 229
            self.identifier()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__3:
                self.state = 230
                self.match(dgdlParser.T__3)
                self.state = 231
                self.identifier()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self.match(dgdlParser.T__1)
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
            self.state = 239
            self.match(dgdlParser.T__14)
            self.state = 240
            self.match(dgdlParser.T__0)
            self.state = 241
            self.onoff()
            self.state = 242
            self.match(dgdlParser.T__1)
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
            self.state = 244
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__15 or _la==dgdlParser.T__16):
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
            self.state = 246
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Number]:
                self.state = 248
                self.number()
                pass
            elif token in [dgdlParser.T__17]:
                self.state = 249
                self.match(dgdlParser.T__17)
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
            self.state = 252
            self.match(dgdlParser.T__18)
            self.state = 253
            self.match(dgdlParser.T__0)
            self.state = 254
            self.match(dgdlParser.T__9)
            self.state = 255
            self.match(dgdlParser.T__6)
            self.state = 256
            self.ruleID()
            self.state = 257
            self.match(dgdlParser.T__3)
            self.state = 258
            self.match(dgdlParser.T__19)
            self.state = 259
            self.match(dgdlParser.T__6)
            self.state = 260
            self.scopeType()
            self.state = 261
            self.match(dgdlParser.T__3)
            self.state = 262
            self.ruleBody()
            self.state = 263
            self.match(dgdlParser.T__1)
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
            self.state = 265
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
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.INITIAL) | (1 << dgdlParser.TURNWISE) | (1 << dgdlParser.MOVEWISE))) != 0)):
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
            self.state = 269
            self.match(dgdlParser.T__0)
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__10, dgdlParser.T__21, dgdlParser.T__31, dgdlParser.T__37, dgdlParser.T__38]:
                self.state = 270
                self.effects()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==dgdlParser.T__20:
                    self.state = 271
                    self.match(dgdlParser.T__20)
                    self.state = 272
                    self.conditional()


                pass
            elif token in [dgdlParser.T__39]:
                self.state = 275
                self.conditional()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 278
            self.match(dgdlParser.T__1)
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.effect()
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 281
                    self.match(dgdlParser.T__20)
                    self.state = 282
                    self.effect() 
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__21]:
                self.state = 288
                self.move()
                pass
            elif token in [dgdlParser.T__10]:
                self.state = 289
                self.storeOp()
                pass
            elif token in [dgdlParser.T__31]:
                self.state = 290
                self.statusUpdate()
                pass
            elif token in [dgdlParser.T__37, dgdlParser.T__38]:
                self.state = 291
                self.roleAssignment()
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
            self.state = 294
            self.match(dgdlParser.T__21)
            self.state = 295
            self.match(dgdlParser.T__22)
            self.state = 296
            self.moveaction()
            self.state = 297
            self.match(dgdlParser.T__3)
            self.state = 298
            self.movetime()
            self.state = 299
            self.match(dgdlParser.T__3)
            self.state = 300
            self.moveID()
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 301
                self.match(dgdlParser.T__3)
                self.state = 302
                self.addressee()


            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 305
                self.match(dgdlParser.T__3)
                self.state = 306
                self.content()


            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__3:
                self.state = 309
                self.match(dgdlParser.T__3)
                self.state = 310
                self.user()


            self.state = 313
            self.match(dgdlParser.T__23)
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
            self.state = 315
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__24 or _la==dgdlParser.T__25):
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
            self.state = 317
            _la = self._input.LA(1)
            if not(_la==dgdlParser.T__26 or _la==dgdlParser.T__27):
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
            self.state = 319
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
            self.state = 321
            self.match(dgdlParser.T__28)
            self.state = 322
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
            self.state = 324
            self.match(dgdlParser.T__0)
            self.state = 325
            self.contentVar()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__3:
                self.state = 326
                self.match(dgdlParser.T__3)
                self.state = 327
                self.contentVar()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
            self.match(dgdlParser.T__1)
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
            self.state = 335
            self.match(dgdlParser.T__10)
            self.state = 336
            self.match(dgdlParser.T__22)
            self.state = 337
            self.storeaction()
            self.state = 338
            self.match(dgdlParser.T__3)
            self.state = 339
            self.storeContent()
            self.state = 340
            self.match(dgdlParser.T__3)
            self.state = 341
            self.storeID()
            self.state = 342
            self.match(dgdlParser.T__23)
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
            self.state = 344
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__24) | (1 << dgdlParser.T__29) | (1 << dgdlParser.T__30))) != 0)):
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
            self.state = 346
            self.match(dgdlParser.T__31)
            self.state = 347
            self.match(dgdlParser.T__22)
            self.state = 348
            self.status()
            self.state = 349
            self.match(dgdlParser.T__3)
            self.state = 350
            self.identifier()
            self.state = 351
            self.match(dgdlParser.T__23)
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
            self.state = 353
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dgdlParser.T__32) | (1 << dgdlParser.T__33) | (1 << dgdlParser.T__34) | (1 << dgdlParser.T__35) | (1 << dgdlParser.T__36))) != 0)):
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
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.T__37]:
                self.state = 355
                self.assignment()
                pass
            elif token in [dgdlParser.T__38]:
                self.state = 356
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
            self.state = 359
            self.match(dgdlParser.T__37)
            self.state = 360
            self.match(dgdlParser.T__22)
            self.state = 361
            self.user()
            self.state = 362
            self.match(dgdlParser.T__3)
            self.state = 363
            self.role()
            self.state = 364
            self.match(dgdlParser.T__23)
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
            self.state = 366
            self.match(dgdlParser.T__38)
            self.state = 367
            self.match(dgdlParser.T__22)
            self.state = 368
            self.user()
            self.state = 369
            self.match(dgdlParser.T__3)
            self.state = 370
            self.role()
            self.state = 371
            self.match(dgdlParser.T__23)
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
            self.state = 373
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
            self.state = 375
            self.match(dgdlParser.T__39)
            self.state = 376
            self.requirements()
            self.state = 377
            self.match(dgdlParser.T__40)
            self.state = 378
            self.match(dgdlParser.T__0)
            self.state = 379
            self.effects()
            self.state = 380
            self.match(dgdlParser.T__1)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__42:
                self.state = 381
                self.condelseif()


            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__43:
                self.state = 384
                self.condelse()


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(dgdlParser.T__41)
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
        self.enterRule(localctx, 80, self.RULE_condelseif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(dgdlParser.T__42)
            self.state = 390
            self.requirements()
            self.state = 391
            self.match(dgdlParser.T__40)
            self.state = 392
            self.match(dgdlParser.T__0)
            self.state = 393
            self.effects()
            self.state = 394
            self.match(dgdlParser.T__1)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__42:
                self.state = 395
                self.condelseif()


            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 398
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
        self.enterRule(localctx, 82, self.RULE_condelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(dgdlParser.T__43)
            self.state = 402
            self.match(dgdlParser.T__0)
            self.state = 403
            self.effects()
            self.state = 404
            self.match(dgdlParser.T__1)
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

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


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
        self.enterRule(localctx, 84, self.RULE_interaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.identifier()
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
        self.enterRule(localctx, 86, self.RULE_upperChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
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
        self.enterRule(localctx, 88, self.RULE_lowerChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        self.enterRule(localctx, 90, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        self.enterRule(localctx, 92, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self.enterRule(localctx, 94, self.RULE_contentVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(dgdlParser.LowerChar)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





