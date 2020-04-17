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


    # Enter a parse tree produced by dgdlParser#roleList.
    def enterRoleList(self, ctx:dgdlParser.RoleListContext):
        pass

    # Exit a parse tree produced by dgdlParser#roleList.
    def exitRoleList(self, ctx:dgdlParser.RoleListContext):
        pass


    # Enter a parse tree produced by dgdlParser#role.
    def enterRole(self, ctx:dgdlParser.RoleContext):
        pass

    # Exit a parse tree produced by dgdlParser#role.
    def exitRole(self, ctx:dgdlParser.RoleContext):
        pass


    # Enter a parse tree produced by dgdlParser#participants.
    def enterParticipants(self, ctx:dgdlParser.ParticipantsContext):
        pass

    # Exit a parse tree produced by dgdlParser#participants.
    def exitParticipants(self, ctx:dgdlParser.ParticipantsContext):
        pass


    # Enter a parse tree produced by dgdlParser#player.
    def enterPlayer(self, ctx:dgdlParser.PlayerContext):
        pass

    # Exit a parse tree produced by dgdlParser#player.
    def exitPlayer(self, ctx:dgdlParser.PlayerContext):
        pass


    # Enter a parse tree produced by dgdlParser#playerID.
    def enterPlayerID(self, ctx:dgdlParser.PlayerIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#playerID.
    def exitPlayerID(self, ctx:dgdlParser.PlayerIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#store.
    def enterStore(self, ctx:dgdlParser.StoreContext):
        pass

    # Exit a parse tree produced by dgdlParser#store.
    def exitStore(self, ctx:dgdlParser.StoreContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeID.
    def enterStoreID(self, ctx:dgdlParser.StoreIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeID.
    def exitStoreID(self, ctx:dgdlParser.StoreIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeOwner.
    def enterStoreOwner(self, ctx:dgdlParser.StoreOwnerContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeOwner.
    def exitStoreOwner(self, ctx:dgdlParser.StoreOwnerContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeStructure.
    def enterStoreStructure(self, ctx:dgdlParser.StoreStructureContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeStructure.
    def exitStoreStructure(self, ctx:dgdlParser.StoreStructureContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeVisibility.
    def enterStoreVisibility(self, ctx:dgdlParser.StoreVisibilityContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeVisibility.
    def exitStoreVisibility(self, ctx:dgdlParser.StoreVisibilityContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeContent.
    def enterStoreContent(self, ctx:dgdlParser.StoreContentContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeContent.
    def exitStoreContent(self, ctx:dgdlParser.StoreContentContext):
        pass


    # Enter a parse tree produced by dgdlParser#backtrack.
    def enterBacktrack(self, ctx:dgdlParser.BacktrackContext):
        pass

    # Exit a parse tree produced by dgdlParser#backtrack.
    def exitBacktrack(self, ctx:dgdlParser.BacktrackContext):
        pass


    # Enter a parse tree produced by dgdlParser#onoff.
    def enterOnoff(self, ctx:dgdlParser.OnoffContext):
        pass

    # Exit a parse tree produced by dgdlParser#onoff.
    def exitOnoff(self, ctx:dgdlParser.OnoffContext):
        pass


    # Enter a parse tree produced by dgdlParser#minplayers.
    def enterMinplayers(self, ctx:dgdlParser.MinplayersContext):
        pass

    # Exit a parse tree produced by dgdlParser#minplayers.
    def exitMinplayers(self, ctx:dgdlParser.MinplayersContext):
        pass


    # Enter a parse tree produced by dgdlParser#maxplayers.
    def enterMaxplayers(self, ctx:dgdlParser.MaxplayersContext):
        pass

    # Exit a parse tree produced by dgdlParser#maxplayers.
    def exitMaxplayers(self, ctx:dgdlParser.MaxplayersContext):
        pass


    # Enter a parse tree produced by dgdlParser#rules.
    def enterRules(self, ctx:dgdlParser.RulesContext):
        pass

    # Exit a parse tree produced by dgdlParser#rules.
    def exitRules(self, ctx:dgdlParser.RulesContext):
        pass


    # Enter a parse tree produced by dgdlParser#ruleID.
    def enterRuleID(self, ctx:dgdlParser.RuleIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#ruleID.
    def exitRuleID(self, ctx:dgdlParser.RuleIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#scopeType.
    def enterScopeType(self, ctx:dgdlParser.ScopeTypeContext):
        pass

    # Exit a parse tree produced by dgdlParser#scopeType.
    def exitScopeType(self, ctx:dgdlParser.ScopeTypeContext):
        pass


    # Enter a parse tree produced by dgdlParser#ruleBody.
    def enterRuleBody(self, ctx:dgdlParser.RuleBodyContext):
        pass

    # Exit a parse tree produced by dgdlParser#ruleBody.
    def exitRuleBody(self, ctx:dgdlParser.RuleBodyContext):
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