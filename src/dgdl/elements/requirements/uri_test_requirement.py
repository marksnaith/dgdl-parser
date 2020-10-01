from .requirement import Requirement

class URITestRequirement(Requirement):

    def __init__(self, negated, id):
        self.type = "uriTest"
        self.negated = negated
        self.id = id
