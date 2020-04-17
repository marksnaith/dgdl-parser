from antlr.grammar import *
from antlr4 import *
from .concrete_dgdl_listener import ConcreteDGDLListener


class System:

    def __init__(self):
        self.identifier = ""
        self.games = {}

    def load(self, src):
        parser = dgdlParser(CommonTokenStream(dgdlLexer(FileStream(src))))

        tree = parser.system()

        listener = ConcreteDGDLListener(self)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self = listener.get_system()

        print(self)

    def __str__(self):
        repr = {
            "identifier": self.identifier,
            "games": {}
        }

        for k,v in self.games.items():
            repr["games"][k] = v.__repr__()

        return str(repr)
