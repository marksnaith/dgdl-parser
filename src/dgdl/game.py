


class Game:

    def __init__(self, identifier):
        self.identifier = identifier
        pass

    def __repr__(self):
        repr = {
            "identifier": self.identifier
        }
        return repr

    def __str__(self):
        return str(self.__repr__())
