from .effect import Effect

class StoreOpEffect(Effect):

    def __init__(self, storeaction, storecontent, storeID):
        self.type = "storeop"
        self.storeaction = storeaction
        self.storecontent = storecontent
        self.storeID = storeID
