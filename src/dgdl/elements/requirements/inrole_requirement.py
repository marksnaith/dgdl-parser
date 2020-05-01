from .requirement import Requirement

class InRoleRequirement(Requirement):

    def __init__(self, negated, playerID, role):
        self.type = "inrole"
        self.playerID = playerID
        self.role = role
        self.negative = negated
