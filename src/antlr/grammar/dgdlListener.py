# Generated from grammar/dgdl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dgdlParser import dgdlParser
else:
    from dgdlParser import dgdlParser

# This class defines a complete listener for a parse tree produced by dgdlParser.
class dgdlListener(ParseTreeListener):

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


    # Enter a parse tree produced by dgdlParser#effects.
    def enterEffects(self, ctx:dgdlParser.EffectsContext):
        pass

    # Exit a parse tree produced by dgdlParser#effects.
    def exitEffects(self, ctx:dgdlParser.EffectsContext):
        pass


    # Enter a parse tree produced by dgdlParser#effect.
    def enterEffect(self, ctx:dgdlParser.EffectContext):
        pass

    # Exit a parse tree produced by dgdlParser#effect.
    def exitEffect(self, ctx:dgdlParser.EffectContext):
        pass


    # Enter a parse tree produced by dgdlParser#move.
    def enterMove(self, ctx:dgdlParser.MoveContext):
        pass

    # Exit a parse tree produced by dgdlParser#move.
    def exitMove(self, ctx:dgdlParser.MoveContext):
        pass


    # Enter a parse tree produced by dgdlParser#moveaction.
    def enterMoveaction(self, ctx:dgdlParser.MoveactionContext):
        pass

    # Exit a parse tree produced by dgdlParser#moveaction.
    def exitMoveaction(self, ctx:dgdlParser.MoveactionContext):
        pass


    # Enter a parse tree produced by dgdlParser#movetime.
    def enterMovetime(self, ctx:dgdlParser.MovetimeContext):
        pass

    # Exit a parse tree produced by dgdlParser#movetime.
    def exitMovetime(self, ctx:dgdlParser.MovetimeContext):
        pass


    # Enter a parse tree produced by dgdlParser#moveID.
    def enterMoveID(self, ctx:dgdlParser.MoveIDContext):
        pass

    # Exit a parse tree produced by dgdlParser#moveID.
    def exitMoveID(self, ctx:dgdlParser.MoveIDContext):
        pass


    # Enter a parse tree produced by dgdlParser#addressee.
    def enterAddressee(self, ctx:dgdlParser.AddresseeContext):
        pass

    # Exit a parse tree produced by dgdlParser#addressee.
    def exitAddressee(self, ctx:dgdlParser.AddresseeContext):
        pass


    # Enter a parse tree produced by dgdlParser#content.
    def enterContent(self, ctx:dgdlParser.ContentContext):
        pass

    # Exit a parse tree produced by dgdlParser#content.
    def exitContent(self, ctx:dgdlParser.ContentContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeOp.
    def enterStoreOp(self, ctx:dgdlParser.StoreOpContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeOp.
    def exitStoreOp(self, ctx:dgdlParser.StoreOpContext):
        pass


    # Enter a parse tree produced by dgdlParser#storeaction.
    def enterStoreaction(self, ctx:dgdlParser.StoreactionContext):
        pass

    # Exit a parse tree produced by dgdlParser#storeaction.
    def exitStoreaction(self, ctx:dgdlParser.StoreactionContext):
        pass


    # Enter a parse tree produced by dgdlParser#statusUpdate.
    def enterStatusUpdate(self, ctx:dgdlParser.StatusUpdateContext):
        pass

    # Exit a parse tree produced by dgdlParser#statusUpdate.
    def exitStatusUpdate(self, ctx:dgdlParser.StatusUpdateContext):
        pass


    # Enter a parse tree produced by dgdlParser#status.
    def enterStatus(self, ctx:dgdlParser.StatusContext):
        pass

    # Exit a parse tree produced by dgdlParser#status.
    def exitStatus(self, ctx:dgdlParser.StatusContext):
        pass


    # Enter a parse tree produced by dgdlParser#roleAssignment.
    def enterRoleAssignment(self, ctx:dgdlParser.RoleAssignmentContext):
        pass

    # Exit a parse tree produced by dgdlParser#roleAssignment.
    def exitRoleAssignment(self, ctx:dgdlParser.RoleAssignmentContext):
        pass


    # Enter a parse tree produced by dgdlParser#assignment.
    def enterAssignment(self, ctx:dgdlParser.AssignmentContext):
        pass

    # Exit a parse tree produced by dgdlParser#assignment.
    def exitAssignment(self, ctx:dgdlParser.AssignmentContext):
        pass


    # Enter a parse tree produced by dgdlParser#unassignment.
    def enterUnassignment(self, ctx:dgdlParser.UnassignmentContext):
        pass

    # Exit a parse tree produced by dgdlParser#unassignment.
    def exitUnassignment(self, ctx:dgdlParser.UnassignmentContext):
        pass


    # Enter a parse tree produced by dgdlParser#user.
    def enterUser(self, ctx:dgdlParser.UserContext):
        pass

    # Exit a parse tree produced by dgdlParser#user.
    def exitUser(self, ctx:dgdlParser.UserContext):
        pass


    # Enter a parse tree produced by dgdlParser#conditional.
    def enterConditional(self, ctx:dgdlParser.ConditionalContext):
        pass

    # Exit a parse tree produced by dgdlParser#conditional.
    def exitConditional(self, ctx:dgdlParser.ConditionalContext):
        pass


    # Enter a parse tree produced by dgdlParser#requirements.
    def enterRequirements(self, ctx:dgdlParser.RequirementsContext):
        pass

    # Exit a parse tree produced by dgdlParser#requirements.
    def exitRequirements(self, ctx:dgdlParser.RequirementsContext):
        pass


    # Enter a parse tree produced by dgdlParser#condelseif.
    def enterCondelseif(self, ctx:dgdlParser.CondelseifContext):
        pass

    # Exit a parse tree produced by dgdlParser#condelseif.
    def exitCondelseif(self, ctx:dgdlParser.CondelseifContext):
        pass


    # Enter a parse tree produced by dgdlParser#condelse.
    def enterCondelse(self, ctx:dgdlParser.CondelseContext):
        pass

    # Exit a parse tree produced by dgdlParser#condelse.
    def exitCondelse(self, ctx:dgdlParser.CondelseContext):
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


    # Enter a parse tree produced by dgdlParser#contentVar.
    def enterContentVar(self, ctx:dgdlParser.ContentVarContext):
        pass

    # Exit a parse tree produced by dgdlParser#contentVar.
    def exitContentVar(self, ctx:dgdlParser.ContentVarContext):
        pass



del dgdlParser