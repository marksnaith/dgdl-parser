from antlr.grammar import *
from antlr4 import *
from .concrete_dgdl_listener import ConcreteDGDLListener
from .dgdl_element import DGDLElement

class System(DGDLElement):

    def __init__(self):
        self.identifier = ""
        self.games = {}

    def load(self, src):
        parser = dgdlParser(CommonTokenStream(dgdlLexer(FileStream(src))))

        tree = parser.system()

        listener = ConcreteDGDLListener(self)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self = listener.get_system(True)

        print(self)
