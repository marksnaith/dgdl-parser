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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\u0102\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\3\2\6\2@\n\2\r\2\16\2A\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\7\4N\n\4\f\4\16\4Q\13\4\3\4\6\4T\n")
        buf.write("\4\r\4\16\4U\3\4\3\4\3\5\3\5\3\6\5\6]\n\6\3\6\3\6\6\6")
        buf.write("a\n\6\r\6\16\6b\3\6\7\6f\n\6\f\6\16\6i\13\6\3\6\5\6l\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\7\7s\n\7\f\7\16\7v\13\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\5\b}\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u0097\n\n\3\n\3\n\3\n\3\n\5\n\u009d")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b6")
        buf.write("\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\6\16\u00c1")
        buf.write("\n\16\r\16\16\16\u00c2\3\16\3\16\5\16\u00c7\n\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00d1\n\21\f")
        buf.write("\21\16\21\u00d4\13\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\5\25\u00e3\n\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\2\2\37\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:\2\6")
        buf.write("\3\2$&\3\2\'(\3\2\22\23\3\2!#\2\u00f6\2<\3\2\2\2\4G\3")
        buf.write("\2\2\2\6I\3\2\2\2\bY\3\2\2\2\n\\\3\2\2\2\fm\3\2\2\2\16")
        buf.write("|\3\2\2\2\20~\3\2\2\2\22\u0089\3\2\2\2\24\u00a0\3\2\2")
        buf.write("\2\26\u00a2\3\2\2\2\30\u00b9\3\2\2\2\32\u00c6\3\2\2\2")
        buf.write("\34\u00c8\3\2\2\2\36\u00ca\3\2\2\2 \u00cc\3\2\2\2\"\u00d7")
        buf.write("\3\2\2\2$\u00dc\3\2\2\2&\u00de\3\2\2\2(\u00e2\3\2\2\2")
        buf.write("*\u00e4\3\2\2\2,\u00f1\3\2\2\2.\u00f3\3\2\2\2\60\u00f5")
        buf.write("\3\2\2\2\62\u00f7\3\2\2\2\64\u00f9\3\2\2\2\66\u00fb\3")
        buf.write("\2\2\28\u00fd\3\2\2\2:\u00ff\3\2\2\2<=\5\4\3\2=?\7\3\2")
        buf.write("\2>@\5\6\4\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B")
        buf.write("C\3\2\2\2CD\7\4\2\2DE\3\2\2\2EF\7\2\2\3F\3\3\2\2\2GH\5")
        buf.write("8\35\2H\5\3\2\2\2IJ\5\b\5\2JK\7\3\2\2KO\5\n\6\2LN\5*\26")
        buf.write("\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PS\3\2\2\2Q")
        buf.write("O\3\2\2\2RT\5\62\32\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV")
        buf.write("\3\2\2\2VW\3\2\2\2WX\7\4\2\2X\7\3\2\2\2YZ\58\35\2Z\t\3")
        buf.write("\2\2\2[]\5\f\7\2\\[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\5\20")
        buf.write("\t\2_a\5\22\n\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2")
        buf.write("\2cg\3\2\2\2df\5\26\f\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2")
        buf.write("gh\3\2\2\2hk\3\2\2\2ig\3\2\2\2jl\5\"\22\2kj\3\2\2\2kl")
        buf.write("\3\2\2\2l\13\3\2\2\2mn\7\5\2\2no\7\3\2\2ot\5\16\b\2pq")
        buf.write("\7\6\2\2qs\5\16\b\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3")
        buf.write("\2\2\2uw\3\2\2\2vt\3\2\2\2wx\7\4\2\2x\r\3\2\2\2y}\7\37")
        buf.write("\2\2z}\7 \2\2{}\58\35\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2")
        buf.write("}\17\3\2\2\2~\177\7\7\2\2\177\u0080\7\3\2\2\u0080\u0081")
        buf.write("\7\b\2\2\u0081\u0082\7\t\2\2\u0082\u0083\5&\24\2\u0083")
        buf.write("\u0084\7\6\2\2\u0084\u0085\7\n\2\2\u0085\u0086\7\t\2\2")
        buf.write("\u0086\u0087\5(\25\2\u0087\u0088\7\4\2\2\u0088\21\3\2")
        buf.write("\2\2\u0089\u008a\7\13\2\2\u008a\u008b\7\3\2\2\u008b\u008c")
        buf.write("\7\f\2\2\u008c\u008d\7\t\2\2\u008d\u0090\5\24\13\2\u008e")
        buf.write("\u008f\7\6\2\2\u008f\u0091\5\f\7\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0096\3\2\2\2\u0092\u0093\7")
        buf.write("\6\2\2\u0093\u0094\7\b\2\2\u0094\u0095\7\t\2\2\u0095\u0097")
        buf.write("\5&\24\2\u0096\u0092\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u009c\3\2\2\2\u0098\u0099\7\6\2\2\u0099\u009a\7\n\2\2")
        buf.write("\u009a\u009b\7\t\2\2\u009b\u009d\5(\25\2\u009c\u0098\3")
        buf.write("\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f")
        buf.write("\7\4\2\2\u009f\23\3\2\2\2\u00a0\u00a1\58\35\2\u00a1\25")
        buf.write("\3\2\2\2\u00a2\u00a3\7\r\2\2\u00a3\u00a4\7\3\2\2\u00a4")
        buf.write("\u00a5\7\f\2\2\u00a5\u00a6\7\t\2\2\u00a6\u00a7\5\30\r")
        buf.write("\2\u00a7\u00a8\7\6\2\2\u00a8\u00a9\7\16\2\2\u00a9\u00aa")
        buf.write("\7\t\2\2\u00aa\u00ab\5\32\16\2\u00ab\u00ac\7\6\2\2\u00ac")
        buf.write("\u00ad\7\17\2\2\u00ad\u00ae\7\t\2\2\u00ae\u00af\5\34\17")
        buf.write("\2\u00af\u00b0\7\6\2\2\u00b0\u00b1\7\20\2\2\u00b1\u00b2")
        buf.write("\7\t\2\2\u00b2\u00b5\5\36\20\2\u00b3\u00b4\7\6\2\2\u00b4")
        buf.write("\u00b6\5 \21\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7\4\2\2\u00b8\27\3\2")
        buf.write("\2\2\u00b9\u00ba\58\35\2\u00ba\31\3\2\2\2\u00bb\u00c7")
        buf.write("\58\35\2\u00bc\u00bd\7\3\2\2\u00bd\u00c0\58\35\2\u00be")
        buf.write("\u00bf\7\6\2\2\u00bf\u00c1\58\35\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3")
        buf.write("\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7\4\2\2\u00c5\u00c7")
        buf.write("\3\2\2\2\u00c6\u00bb\3\2\2\2\u00c6\u00bc\3\2\2\2\u00c7")
        buf.write("\33\3\2\2\2\u00c8\u00c9\t\2\2\2\u00c9\35\3\2\2\2\u00ca")
        buf.write("\u00cb\t\3\2\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\3\2\2\u00cd")
        buf.write("\u00d2\58\35\2\u00ce\u00cf\7\6\2\2\u00cf\u00d1\58\35\2")
        buf.write("\u00d0\u00ce\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d5\u00d6\7\4\2\2\u00d6!\3\2\2\2\u00d7\u00d8")
        buf.write("\7\21\2\2\u00d8\u00d9\7\3\2\2\u00d9\u00da\5$\23\2\u00da")
        buf.write("\u00db\7\4\2\2\u00db#\3\2\2\2\u00dc\u00dd\t\4\2\2\u00dd")
        buf.write("%\3\2\2\2\u00de\u00df\5:\36\2\u00df\'\3\2\2\2\u00e0\u00e3")
        buf.write("\5:\36\2\u00e1\u00e3\7\24\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3)\3\2\2\2\u00e4\u00e5\7\25\2\2\u00e5")
        buf.write("\u00e6\7\3\2\2\u00e6\u00e7\7\f\2\2\u00e7\u00e8\7\t\2\2")
        buf.write("\u00e8\u00e9\5,\27\2\u00e9\u00ea\7\6\2\2\u00ea\u00eb\7")
        buf.write("\26\2\2\u00eb\u00ec\7\t\2\2\u00ec\u00ed\5.\30\2\u00ed")
        buf.write("\u00ee\7\6\2\2\u00ee\u00ef\5\60\31\2\u00ef\u00f0\7\4\2")
        buf.write("\2\u00f0+\3\2\2\2\u00f1\u00f2\58\35\2\u00f2-\3\2\2\2\u00f3")
        buf.write("\u00f4\t\5\2\2\u00f4/\3\2\2\2\u00f5\u00f6\58\35\2\u00f6")
        buf.write("\61\3\2\2\2\u00f7\u00f8\58\35\2\u00f8\63\3\2\2\2\u00f9")
        buf.write("\u00fa\7\31\2\2\u00fa\65\3\2\2\2\u00fb\u00fc\7\30\2\2")
        buf.write("\u00fc\67\3\2\2\2\u00fd\u00fe\7\27\2\2\u00fe9\3\2\2\2")
        buf.write("\u00ff\u0100\7\32\2\2\u0100;\3\2\2\2\23AOU\\bgkt|\u0090")
        buf.write("\u0096\u009c\u00b5\u00c2\u00c6\u00d2\u00e2")
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'listener'", "'speaker'", "'initial'", "'turnwise'", 
                     "'movewise'", "'set'", "'queue'", "'stack'", "'public'", 
                     "'private'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Identifier", "LowerChar", "UpperChar", 
                      "Number", "WS", "MOVEACTION", "MOVETIME", "ONOFF", 
                      "LISTENER", "SPEAKER", "INITIAL", "TURNWISE", "MOVEWISE", 
                      "SET", "QUEUE", "STACK", "PUBLIC", "PRIVATE", "STRINGLITERAL", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_system = 0
    RULE_systemID = 1
    RULE_game = 2
    RULE_gameID = 3
    RULE_composition = 4
    RULE_roleList = 5
    RULE_role = 6
    RULE_participants = 7
    RULE_player = 8
    RULE_playerID = 9
    RULE_store = 10
    RULE_storeID = 11
    RULE_storeOwner = 12
    RULE_storeStructure = 13
    RULE_storeVisibility = 14
    RULE_storeContent = 15
    RULE_backtrack = 16
    RULE_onoff = 17
    RULE_minplayers = 18
    RULE_maxplayers = 19
    RULE_rules = 20
    RULE_ruleID = 21
    RULE_scopeType = 22
    RULE_ruleBody = 23
    RULE_interaction = 24
    RULE_upperChar = 25
    RULE_lowerChar = 26
    RULE_identifier = 27
    RULE_number = 28

    ruleNames =  [ "system", "systemID", "game", "gameID", "composition", 
                   "roleList", "role", "participants", "player", "playerID", 
                   "store", "storeID", "storeOwner", "storeStructure", "storeVisibility", 
                   "storeContent", "backtrack", "onoff", "minplayers", "maxplayers", 
                   "rules", "ruleID", "scopeType", "ruleBody", "interaction", 
                   "upperChar", "lowerChar", "identifier", "number" ]

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
    Identifier=21
    LowerChar=22
    UpperChar=23
    Number=24
    WS=25
    MOVEACTION=26
    MOVETIME=27
    ONOFF=28
    LISTENER=29
    SPEAKER=30
    INITIAL=31
    TURNWISE=32
    MOVEWISE=33
    SET=34
    QUEUE=35
    STACK=36
    PUBLIC=37
    PRIVATE=38
    STRINGLITERAL=39
    COMMENT=40
    LINE_COMMENT=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SystemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(dgdlParser.EOF, 0)

        def systemID(self):
            return self.getTypedRuleContext(dgdlParser.SystemIDContext,0)


        def game(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dgdlParser.GameContext)
            else:
                return self.getTypedRuleContext(dgdlParser.GameContext,i)


        def getRuleIndex(self):
            return dgdlParser.RULE_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem" ):
                listener.enterSystem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem" ):
                listener.exitSystem(self)




    def system(self):

        localctx = dgdlParser.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.systemID()
            self.state = 59
            self.match(dgdlParser.T__0)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.game()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.Identifier):
                    break

            self.state = 65
            self.match(dgdlParser.T__1)
            self.state = 67
            self.match(dgdlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dgdlParser.RULE_systemID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystemID" ):
                listener.enterSystemID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystemID" ):
                listener.exitSystemID(self)




    def systemID(self):

        localctx = dgdlParser.SystemIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_systemID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gameID(self):
            return self.getTypedRuleContext(dgdlParser.GameIDContext,0)


        def composition(self):
            return self.getTypedRuleContext(dgdlParser.CompositionContext,0)


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
        self.enterRule(localctx, 4, self.RULE_game)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.gameID()
            self.state = 72
            self.match(dgdlParser.T__0)
            self.state = 73
            self.composition()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__18:
                self.state = 74
                self.rules()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.interaction()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.Identifier):
                    break

            self.state = 85
            self.match(dgdlParser.T__1)
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
        self.enterRule(localctx, 6, self.RULE_gameID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 8, self.RULE_composition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__2:
                self.state = 89
                self.roleList()


            self.state = 92
            self.participants()
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.player()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.T__8):
                    break

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__10:
                self.state = 98
                self.store()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__14:
                self.state = 104
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
        self.enterRule(localctx, 10, self.RULE_roleList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(dgdlParser.T__2)
            self.state = 108
            self.match(dgdlParser.T__0)
            self.state = 109
            self.role()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__3:
                self.state = 110
                self.match(dgdlParser.T__3)
                self.state = 111
                self.role()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
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
        self.enterRule(localctx, 12, self.RULE_role)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.LISTENER]:
                self.state = 119
                self.match(dgdlParser.LISTENER)
                pass
            elif token in [dgdlParser.SPEAKER]:
                self.state = 120
                self.match(dgdlParser.SPEAKER)
                pass
            elif token in [dgdlParser.Identifier]:
                self.state = 121
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
        self.enterRule(localctx, 14, self.RULE_participants)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(dgdlParser.T__4)
            self.state = 125
            self.match(dgdlParser.T__0)
            self.state = 126
            self.match(dgdlParser.T__5)
            self.state = 127
            self.match(dgdlParser.T__6)
            self.state = 128
            self.minplayers()
            self.state = 129
            self.match(dgdlParser.T__3)
            self.state = 130
            self.match(dgdlParser.T__7)
            self.state = 131
            self.match(dgdlParser.T__6)
            self.state = 132
            self.maxplayers()
            self.state = 133
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
        self.enterRule(localctx, 16, self.RULE_player)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(dgdlParser.T__8)
            self.state = 136
            self.match(dgdlParser.T__0)
            self.state = 137
            self.match(dgdlParser.T__9)
            self.state = 138
            self.match(dgdlParser.T__6)
            self.state = 139
            self.playerID()
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 140
                self.match(dgdlParser.T__3)
                self.state = 141
                self.roleList()


            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(dgdlParser.T__3)
                self.state = 145
                self.match(dgdlParser.T__5)
                self.state = 146
                self.match(dgdlParser.T__6)
                self.state = 147
                self.minplayers()


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__3:
                self.state = 150
                self.match(dgdlParser.T__3)
                self.state = 151
                self.match(dgdlParser.T__7)
                self.state = 152
                self.match(dgdlParser.T__6)
                self.state = 153
                self.maxplayers()


            self.state = 156
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
        self.enterRule(localctx, 18, self.RULE_playerID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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
        self.enterRule(localctx, 20, self.RULE_store)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(dgdlParser.T__10)
            self.state = 161
            self.match(dgdlParser.T__0)
            self.state = 162
            self.match(dgdlParser.T__9)
            self.state = 163
            self.match(dgdlParser.T__6)
            self.state = 164
            self.storeID()
            self.state = 165
            self.match(dgdlParser.T__3)
            self.state = 166
            self.match(dgdlParser.T__11)
            self.state = 167
            self.match(dgdlParser.T__6)
            self.state = 168
            self.storeOwner()
            self.state = 169
            self.match(dgdlParser.T__3)
            self.state = 170
            self.match(dgdlParser.T__12)
            self.state = 171
            self.match(dgdlParser.T__6)
            self.state = 172
            self.storeStructure()
            self.state = 173
            self.match(dgdlParser.T__3)
            self.state = 174
            self.match(dgdlParser.T__13)
            self.state = 175
            self.match(dgdlParser.T__6)
            self.state = 176
            self.storeVisibility()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==dgdlParser.T__3:
                self.state = 177
                self.match(dgdlParser.T__3)
                self.state = 178
                self.storeContent()


            self.state = 181
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
        self.enterRule(localctx, 22, self.RULE_storeID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
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
        self.enterRule(localctx, 24, self.RULE_storeOwner)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Identifier]:
                self.state = 185
                self.identifier()
                pass
            elif token in [dgdlParser.T__0]:
                self.state = 186
                self.match(dgdlParser.T__0)
                self.state = 187
                self.identifier()
                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 188
                    self.match(dgdlParser.T__3)
                    self.state = 189
                    self.identifier()
                    self.state = 192 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==dgdlParser.T__3):
                        break

                self.state = 194
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
        self.enterRule(localctx, 26, self.RULE_storeStructure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 28, self.RULE_storeVisibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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
        self.enterRule(localctx, 30, self.RULE_storeContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(dgdlParser.T__0)
            self.state = 203
            self.identifier()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dgdlParser.T__3:
                self.state = 204
                self.match(dgdlParser.T__3)
                self.state = 205
                self.identifier()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
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
        self.enterRule(localctx, 32, self.RULE_backtrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(dgdlParser.T__14)
            self.state = 214
            self.match(dgdlParser.T__0)
            self.state = 215
            self.onoff()
            self.state = 216
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
        self.enterRule(localctx, 34, self.RULE_onoff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
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
        self.enterRule(localctx, 36, self.RULE_minplayers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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
        self.enterRule(localctx, 38, self.RULE_maxplayers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [dgdlParser.Number]:
                self.state = 222
                self.number()
                pass
            elif token in [dgdlParser.T__17]:
                self.state = 223
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
        self.enterRule(localctx, 40, self.RULE_rules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(dgdlParser.T__18)
            self.state = 227
            self.match(dgdlParser.T__0)
            self.state = 228
            self.match(dgdlParser.T__9)
            self.state = 229
            self.match(dgdlParser.T__6)
            self.state = 230
            self.ruleID()
            self.state = 231
            self.match(dgdlParser.T__3)
            self.state = 232
            self.match(dgdlParser.T__19)
            self.state = 233
            self.match(dgdlParser.T__6)
            self.state = 234
            self.scopeType()
            self.state = 235
            self.match(dgdlParser.T__3)
            self.state = 236
            self.ruleBody()
            self.state = 237
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
        self.enterRule(localctx, 42, self.RULE_ruleID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
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
        self.enterRule(localctx, 44, self.RULE_scopeType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
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

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


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
        self.enterRule(localctx, 46, self.RULE_ruleBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.identifier()
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
        self.enterRule(localctx, 48, self.RULE_interaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
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
        self.enterRule(localctx, 50, self.RULE_upperChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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
        self.enterRule(localctx, 52, self.RULE_lowerChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
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
        self.enterRule(localctx, 54, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
        self.enterRule(localctx, 56, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(dgdlParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





