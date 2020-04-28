from dgdl.builders import *


class Game:

    def __init__(self, dgdlfile):
            self.builders = {
                "composition": CompositionBuilder,
                "rules": RuleBuilder,
                "interactions": InteractionBuilder
            }

    def build(self):
        return
