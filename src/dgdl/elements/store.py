from .dgdl_element import DGDLElement

class Store(DGDLElement):

    def __init__(self, storeID, owner, structure, visibility, content):
        self.storeID = storeID
        self.owner = owner
        self.structure = structure
        self.visibility = visibility
        self.content = content
