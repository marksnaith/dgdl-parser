from ..dgdl_element import DGDLElement

class Requirement(DGDLElement):

    def get_test(self):
        return self.__dict__
