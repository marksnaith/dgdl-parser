from .effects.effect import Effect
from .requirements import *

class Conditional(Effect):

    def __init__(self):
        self.requirements = []
        self.effects = []
        self.elseif = None
        self.else_effects = []

    def add_effect(self, effect):
        self.effects.append(effect)

    def add_elseif(self, elseif):
        if self.elseif is None:
            self.elseif = elseif
        else:
            self.elseif.add_elseif(elseif)

    def add_else_effect(self, effect):
        if self.elseif is None:
            self.else_effects.append(effect)
        else:
            self.elseif.add_else_effect(effect)

    def add_requirement(self, requirement):
        self.requirements.append(requirement)

    def perform(self, interaction_data):

        for requirement in self.requirements:
            result = requirement.build(interaction_data)

        return {"effect":"conditional",
                "data":{
                    "conditions":[{
                        "type":"roleinspection",
                        "playerID": "abc",
                        "role": "def",
                        "negative":True
                        }
                    ],
                    "effects": self.effects,
                    "elseif": self.elseif,
                    "else": self.else_effects
                }
               }
