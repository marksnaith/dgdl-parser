from .requirement import Requirement

class InspectRequirement(Requirement):

    def __init__(self, negated, storepos, content, storeID, user=None, storetime=None):
        self.type = "inspect"
        self.negated = negated
        self.storepos = storepos
        self.content = content
        self.storeID = storeID
        self.user = user
        self.storetime = storetime
