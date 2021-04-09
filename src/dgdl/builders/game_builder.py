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
