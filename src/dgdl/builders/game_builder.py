from dgdl.elements.game import Game
from . import *
from dgdl.antlr import *
from antlr4 import *
import sys
from io import StringIO
import json
import ast

class GameBuilder:

    def __init__(self):
        self.builders = [CompositionBuilder(),
                         RuleBuilder(),
                         InteractionBuilder()]

    def build(self, file=None, input=None):

        if input is not None:
            s = InputStream(input)
        elif file is not None:
            s = FileStream(file)
        else:
            return None

        parser = dgdlParser(CommonTokenStream(dgdlLexer(s)))

        # assign stderr to a temporary stream to capture errors
        sys.stderr = tmp = StringIO()
        tree = parser.game()
        sys.stderr = sys.__stderr__

        val = tmp.getvalue().strip()

        if val != "":
            errors = val.split("\n")
            return errors

        walker = ParseTreeWalker()

        game = {}

        for b in self.builders:
            walker.walk(b, tree)

            output = b.get_representation()

            if output is not None:
                game.update(output)

        return Game(**game)
