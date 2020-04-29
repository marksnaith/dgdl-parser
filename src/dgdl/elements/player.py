from .dgdl_element import DGDLElement


class Player(DGDLElement):

    def __init__(self, playerID, roles):
        self.playerID = playerID
        self.roles = roles
