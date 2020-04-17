# Generated from grammar/dgdl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dgdlParser import dgdlParser
else:
    from dgdlParser import dgdlParser

# This class defines a complete listener for a parse tree produced by dgdlParser.
class dgdlListener(ParseTreeListener):

    # Enter a parse tree produced by dgdlParser#system.
    def enterSystem(self, ctx:dgdlParser.SystemContext):
        pass

    # Exit a parse tree produced by dgdlParser#system.
    def exitSystem(self, ctx:dgdlParser.SystemContext):
        pass


    # Enter a parse tree produced by dgdlParser#systemID.
    def enterSystemID(self, ctx:dgdlParser.SystemIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#systemID.
    def exitSystemID(self, ctx:dgdlParser.SystemIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#game.
    def enterGame(self, ctx:dgdlParser.GameContext):
        pass

    # Exit a parse tree produced by dgdlParser#game.
    def exitGame(self, ctx:dgdlParser.GameContext):
        pass


    # Enter a parse tree produced by dgdlParser#gameID.
    def enterGameID(self, ctx:dgdlParser.GameIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#gameID.
    def exitGameID(self, ctx:dgdlParser.GameIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#composition.
    def enterComposition(self, ctx:dgdlParser.CompositionContext):
        pass

    # Exit a parse tree produced by dgdlParser#composition.
    def exitComposition(self, ctx:dgdlParser.CompositionContext):
        pass


    # Enter a parse tree produced by dgdlParser#rules.
    def enterRules(self, ctx:dgdlParser.RulesContext):
        pass

    # Exit a parse tree produced by dgdlParser#rules.
    def exitRules(self, ctx:dgdlParser.RulesContext):
        pass


    # Enter a parse tree produced by dgdlParser#interaction.
    def enterInteraction(self, ctx:dgdlParser.InteractionContext):
        pass

    # Exit a parse tree produced by dgdlParser#interaction.
    def exitInteraction(self, ctx:dgdlParser.InteractionContext):
        pass


    # Enter a parse tree produced by dgdlParser#upperChar.
    def enterUpperChar(self, ctx:dgdlParser.UpperCharContext):
        pass

    # Exit a parse tree produced by dgdlParser#upperChar.
    def exitUpperChar(self, ctx:dgdlParser.UpperCharContext):
        pass


    # Enter a parse tree produced by dgdlParser#lowerChar.
    def enterLowerChar(self, ctx:dgdlParser.LowerCharContext):
        pass

    # Exit a parse tree produced by dgdlParser#lowerChar.
    def exitLowerChar(self, ctx:dgdlParser.LowerCharContext):
        pass


    # Enter a parse tree produced by dgdlParser#identifier.
    def enterIdentifier(self, ctx:dgdlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by dgdlParser#identifier.
    def exitIdentifier(self, ctx:dgdlParser.IdentifierContext):
        pass


    # Enter a parse tree produced by dgdlParser#number.
    def enterNumber(self, ctx:dgdlParser.NumberContext):
        pass

    # Exit a parse tree produced by dgdlParser#number.
    def exitNumber(self, ctx:dgdlParser.NumberContext):
        pass



del dgdlParser