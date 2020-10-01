from dgdl.antlr import *
from .base_dgdl_builder import BaseDGDLBuilder
from dgdl.elements import Conditional
from dgdl.elements.effects import *
from dgdl.elements.requirements import *

class RuleInteractionBuilder(BaseDGDLBuilder):

    ''' Base class for building Rules and Interactions. They share a common
        RuleBody type for effects but need specific respective implementations
        for how to handle their delcarations'''

    def __init__(self):
        self.current_effect_target = None
        self.conditionals = []
        self.current_conditional = None

        self.conditional_requirements = []
        self.current_conditional_requirement = {}

        self.current_conditional_negated = False

    def enterRuleBody(self, ctx):
        self.current_effect_target = self.add_effect

    def enterConditional(self, ctx):
        self.current_conditional = Conditional()
        self.current_effect_target = self.current_conditional.add_effect

    def enterCondelseif(self, ctx):
        elseif = Conditional()
        self.current_effect_target = elseif.add_effect
        self.current_conditional.add_elseif(elseif)

    def enterCondelse(self, ctx):
        self.current_effect_target = self.current_conditional.add_else_effect

    def exitConditional(self, ctx):
        self.add_conditional(self.current_conditional)

    def enterCondition(self, ctx):
        if ctx.NEG() is not None:
            if ctx.NEG().getText() == '!':
                self.current_conditional_negated = True

    def exitCondition(self, ctx):
        self.current_conditional_negated = False

    def enterRoleInspection(self, ctx):

        playerID = ctx.playerID().getText()
        role = ctx.role().getText()

        self.current_conditional.add_requirement(InRoleRequirement(self.current_conditional_negated, playerID, role))

    def enterStoreInspection(self, ctx):
        storepos = ctx.storepos().getText()
        content = ctx.storeContent()
        content = [c.getText() for c in content.contentVar()] + [s.getText() for s in content.STRINGLITERAL()]
        storeID = ctx.storeID().getText()

        user = ctx.user()
        if user is not None:
            user = user.getText()

        storetime = ctx.storetime()
        if storetime is not None:
            storetime = storetime.getText()

        inspect = InspectRequirement(self.current_conditional_negated, storepos, content, storeID, user, storetime)
        self.current_conditional.add_requirement(inspect)

    def enterEvent(self, ctx):
        eventpos = ctx.eventpos().getText()
        moveID = ctx.moveID().getText()
        content = ctx.eventContent()

        if content is not None:
            content = [c.getText() for c in content.runtimeVar()] + [c.getText() for c in content.STRINGLITERAL()]

        user = ctx.user()

        if user is not None:
            user = user.getText()

        event = EventRequirement(self.current_conditional_negated, eventpos, moveID, content, user)
        self.current_conditional.add_requirement(event)

    def enterMove(self, ctx):

        action = ctx.moveaction().getText()
        time = ctx.movetime().getText()
        id = ctx.moveID().getText()

        addressee = ctx.addressee()
        content = ctx.content()
        user = ctx.user()

        if addressee is not None:
            addressee = addressee.getText()

        if content is not None:
            content = [c.getText() for c in content.contentVar()] + [c.getText() for c in content.runtimeVar()]

        if user is not None:
            user = user.getText()

        self.current_effect_target(MoveEffect(action, time, id, addressee, content, user))

    def enterStoreOp(self, ctx):
        action = ctx.storeaction().getText()
        content = ctx.storeContent()
        content = [c.getText() for c in content.contentVar()] + [s.getText() for s in content.STRINGLITERAL()]
        id = ctx.storeID().getText()

        self.current_effect_target(StoreOpEffect(action, content, id))

    def enterStatusUpdate(self, ctx):
        status = ctx.status().getText()
        id = ctx.identifier().getText()

        self.current_effect_target(StatusUpdateEffect(status, id))

    def enterAssignment(self, ctx):
        user = ctx.user().getText()
        role = ctx.role().getText()

        self.current_effect_target(AssignEffect(user, role))

    def enterUnassignment(self, ctx):
        user = ctx.user().getText()
        role = ctx.role().getText()

        self.current_effect_target(UnassignEffect(user, role))

    def enterSave(self, ctx):
        content = ctx.storeContent()
        content = [c.getText() for c in content.contentVar()] + [s.getText() for s in content.STRINGLITERAL()]

        variable = ctx.runtimeVar().identifier().getText()

        self.current_effect_target(SaveEffect(content, variable))

    def enterUriTest(self, ctx):
        id = ctx.extUriID().getText()

        uri = URITestRequirement(self.current_conditional_negated, id)
        self.current_conditional.add_requirement(uri)

    # Methods to be overridden by child classes
    def add_effect(self, effect):
        return

    def add_conditional(self, conditional):
        return
