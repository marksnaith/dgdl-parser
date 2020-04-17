from .dgdl_element import DGDLElement

class Game(DGDLElement):

    def __init__(self, identifier):
        self.identifier = identifier
        self.roles = []
        self.players = []
        self.players_min = {}
        self.players_max = {}
        self.stores = []
        self.rules = []

    def set_min_max_players(self, identifier, min, max):
        self.players_min[identifier] = min
        self.players_max[identifier] = max
