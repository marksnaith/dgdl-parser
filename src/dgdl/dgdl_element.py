


class DGDLElement:

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__repr__())
