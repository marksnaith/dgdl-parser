"""
Copyright (C) 2020  Centre for Argument Technology (http://arg.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
