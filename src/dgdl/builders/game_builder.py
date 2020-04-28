from dgdl.game import Game
from . import *
from antlr.grammar import *
from antlr4 import *

class GameBuilder:

    def __init__(self):
        self.builders = [CompositionBuilder(),
                         RuleBuilder(),
                         InteractionBuilder()]

    def build(self, src):
        parser = dgdlParser(CommonTokenStream(dgdlLexer(FileStream(src))))

        tree = parser.game()

        #listener = ConcreteDGDLListener(self)
        walker = ParseTreeWalker()

        for b in self.builders:
            walker.walk(b, tree)

            print(b.get_representation())
