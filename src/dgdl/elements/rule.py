from .dgdl_element import DGDLElement

class Rule(DGDLElement):

    def __init__(self, id, scope):
        self.ruleID = id
        self.scope = scope
        self.effects = []
        self.conditional = None
