from . import RuleInteractionBuilder
from dgdl.elements import Rule
from dgdl.antlr import *

class RuleBuilder(RuleInteractionBuilder):

    def __init__(self):
        super().__init__()
        self.rules = []
        self.current_rule = None

    def enterRules(self, ctx):

        id = ctx.ruleID().getText()
        scope = ctx.scopeType().getText()

        self.current_rule = Rule(id, scope)

    def exitRules(self, ctx):
        self.rules.append(self.current_rule)
        self.current_rule = None

    def add_effect(self, effect):
        if self.current_rule is not None:
            self.current_rule.effects.append(effect)

    def add_conditional(self, conditional):
        if self.current_rule is not None:
            self.current_rule.conditional = conditional

    def get_representation(self):
        return {"rules": self.rules}
