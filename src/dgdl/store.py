from .dgdl_element import DGDLElement

class Store(DGDLElement):

    def __init__(self):
        self.identifier = None
        self.owner = []
        self.content = []
