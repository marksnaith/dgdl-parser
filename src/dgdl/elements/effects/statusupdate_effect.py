from .effect import Effect

class StatusUpdateEffect(Effect):

    def __init__(self, status, id):
        self.type = "statusupdate"
        self.status = status
        self.id = id
