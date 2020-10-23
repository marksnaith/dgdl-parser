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
