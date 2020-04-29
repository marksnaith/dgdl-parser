from .effect import Effect

class AssignEffect(Effect):

    def __init__(self, user, role):
        self.type = "assign"
        self.user = user
        self.role = role
