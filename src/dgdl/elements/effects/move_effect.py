from .effect import Effect

class MoveEffect(Effect):

    def __init__(self, action, time, moveID, addressee=None, content=None, user=None):
        self.type = "move"
        self.action = action
        self.time = time
        self.moveID = moveID
        self.addressee = addressee
        self.content = content
        self.user = user
