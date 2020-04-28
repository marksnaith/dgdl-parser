from .dgdl_element import DGDLElement

class Conditional(DGDLElement):

    def __init__(self):
        self.requirements = []
        self.elseif = None
        self.else_effects = []

    def add_elseif(self, elseif):
        if self.elseif is None:
            self.elseif = elseif
        else:
            self.elseif.add_elseif(elseif)
