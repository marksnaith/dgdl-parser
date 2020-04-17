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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\4\6\4\60\n\4\r\4\16\4")
        buf.write("\61\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\2\2\2=\2\30\3\2\2\2\4#\3\2\2\2\6%\3\2\2\2\b\65")
        buf.write("\3\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16;\3\2\2\2\20=\3\2\2")
        buf.write("\2\22?\3\2\2\2\24A\3\2\2\2\26C\3\2\2\2\30\31\5\4\3\2\31")
        buf.write("\33\7\3\2\2\32\34\5\6\4\2\33\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37 \7\4\2\2")
        buf.write(" !\3\2\2\2!\"\7\2\2\3\"\3\3\2\2\2#$\5\24\13\2$\5\3\2\2")
        buf.write("\2%&\5\b\5\2&\'\7\3\2\2\'+\5\n\6\2(*\5\f\7\2)(\3\2\2\2")
        buf.write("*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,/\3\2\2\2-+\3\2\2\2.\60")
        buf.write("\5\16\b\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3")
        buf.write("\2\2\2\62\63\3\2\2\2\63\64\7\4\2\2\64\7\3\2\2\2\65\66")
        buf.write("\5\24\13\2\66\t\3\2\2\2\678\5\24\13\28\13\3\2\2\29:\5")
        buf.write("\24\13\2:\r\3\2\2\2;<\5\24\13\2<\17\3\2\2\2=>\7\7\2\2")
        buf.write(">\21\3\2\2\2?@\7\6\2\2@\23\3\2\2\2AB\7\5\2\2B\25\3\2\2")
        buf.write("\2CD\7\b\2\2D\27\3\2\2\2\5\35+\61")
        return buf.getvalue()


class dgdlParser ( Parser ):

    grammarFileName = "dgdl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'listener'", "'speaker'", 
                     "'initial'", "'turnwise'", "'movewise'", "'set'", "'queue'", 
                     "'stack'", "'public'", "'private'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "LowerChar", "UpperChar", "Number", "WS", "MOVEACTION", 
                      "MOVETIME", "ONOFF", "LISTENER", "SPEAKER", "INITIAL", 
                      "TURNWISE", "MOVEWISE", "SET", "QUEUE", "STACK", "PUBLIC", 
                      "PRIVATE", "STRINGLITERAL", "COMMENT", "LINE_COMMENT" ]

    RULE_system = 0
    RULE_systemID = 1
    RULE_game = 2
    RULE_gameID = 3
    RULE_composition = 4
    RULE_rules = 5
    RULE_interaction = 6
    RULE_upperChar = 7
    RULE_lowerChar = 8
    RULE_identifier = 9
    RULE_number = 10

    ruleNames =  [ "system", "systemID", "game", "gameID", "composition", 
                   "rules", "interaction", "upperChar", "lowerChar", "identifier", 
                   "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Identifier=3
    LowerChar=4
    UpperChar=5
    Number=6
    WS=7
    MOVEACTION=8
    MOVETIME=9
    ONOFF=10
    LISTENER=11
    SPEAKER=12
    INITIAL=13
    TURNWISE=14
    MOVEWISE=15
    SET=16
    QUEUE=17
    STACK=18
    PUBLIC=19
    PRIVATE=20
    STRINGLITERAL=21
    COMMENT=22
    LINE_COMMENT=23

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
            self.state = 22
            self.systemID()
            self.state = 23
            self.match(dgdlParser.T__0)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.game()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.Identifier):
                    break

            self.state = 29
            self.match(dgdlParser.T__1)
            self.state = 31
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
            self.state = 33
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
            self.state = 35
            self.gameID()
            self.state = 36
            self.match(dgdlParser.T__0)
            self.state = 37
            self.composition()
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 38
                    self.rules() 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.interaction()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dgdlParser.Identifier):
                    break

            self.state = 49
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
            self.state = 51
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

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(dgdlParser.IdentifierContext,0)


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
        self.enterRule(localctx, 10, self.RULE_rules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
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
        self.enterRule(localctx, 12, self.RULE_interaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
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
        self.enterRule(localctx, 14, self.RULE_upperChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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
        self.enterRule(localctx, 16, self.RULE_lowerChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 18, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
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
        self.enterRule(localctx, 20, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(dgdlParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





