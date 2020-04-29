from .dgdl_element import DGDLElement

class Interaction(DGDLElement):

    def __init__(self, id, addressee=None, content=None, opener=None):
        self.id = id
        self.addressee = addressee
        self.content = content
        self.opener = opener
        self.effects = []
        self.conditional = None
