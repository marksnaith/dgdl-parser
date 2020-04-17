from antlr.grammar import *
from .game import Game

class ConcreteDGDLListener(dgdlListener):

    def __init__(self, system):
        self.system = system
        self.current_game = None
        pass

    def enterSystem(self, ctx:dgdlParser.SystemContext):
        identifier = ctx.systemID().identifier().Identifier().getText()
        self.system.identifier = identifier

    def enterGame(self, ctx:dgdlParser.GameContext):
        print("Entered game")
        identifier = ctx.gameID().identifier().Identifier().getText()
        self.current_game = Game(identifier)

    def exitGame(self, ctx:dgdlParser.GameContext):
        print("Exit game")
        self.system.games[self.current_game.identifier] = self.current_game
        current_game = None

    def get_system(self):
        return self.system
