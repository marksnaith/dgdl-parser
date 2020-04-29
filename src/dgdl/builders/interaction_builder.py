from . import RuleInteractionBuilder
from dgdl.elements import Interaction
from dgdl.antlr import *

class InteractionBuilder(RuleInteractionBuilder):

    def __init__(self):
        super().__init__()
        self.interactions = []
        self.current_interaction = None

    def enterInteraction(self, ctx):
        id = ctx.moveID().getText()
        addressee = ctx.user()

        if addressee is not None:
            addressee = addressee.getText()

        content = ctx.content()

        if content is not None:
            content = [c.getText() for c in content.contentVar()]

        opener = ctx.opener()

        if opener is not None:
            opener = opener.STRINGLITERAL().getText()

        self.current_interaction = Interaction(id, addressee, content, opener)

    def exitInteraction(self, ctx):
        self.interactions.append(self.current_interaction)
        self.current_interaction = None


    def add_effect(self, effect):
        if self.current_interaction is not None:
            self.current_interaction.effects.append(effect)

    def add_conditional(self, conditional):
        if self.current_interaction is not None:
            self.current_interaction.conditional = conditional


    def get_representation(self):
        return {"interactions": self.interactions}
