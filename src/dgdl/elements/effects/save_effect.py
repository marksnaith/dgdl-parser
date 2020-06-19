from .effect import Effect

class SaveEffect(Effect):

    def __init__(self, content, variable):
        self.content = content
        self.variable = variable
