from .effect import Effect

class UnassignEffect(Effect):

    def __init__(self, user, role):
        self.type = "unassign"
        self.user = user
        self.role = role
