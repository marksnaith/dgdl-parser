from .dgdl_element import DGDLElement

class Game(DGDLElement):

    def __init__(self, gameID, roles, participants, players, stores, turntaking, backtracking, extURI, rules, interactions):
        self.gameID = gameID
        self.roles = roles
        self.participants = participants
        self.players = players
        self.stores = stores
        self.turntaking = turntaking
        self.backtracking = backtracking
        self.extURI = extURI
        self.rules = rules
        self.interactions = interactions
