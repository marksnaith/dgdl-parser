from .requirement import Requirement

class EventRequirement(Requirement):

    def __init__(self, negated, eventpos, moveID, content=None, user=None):
        self.type = "event"
        self.negated = negated
        self.eventpos = eventpos
        self.moveID = moveID
        self.content = content
        self.user = user
