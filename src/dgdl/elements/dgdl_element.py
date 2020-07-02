
class DGDLElement:
    ''' Base class for all DGDL elements

        Provides a common __repr__() method for obtaining representations
        of elements.
    '''

    def __repr__(self):
        ''' Returns a string representation of this class,
            excluding attributes that begin with "_" '''

        repr = {}

        for k in self.__dict__:
            if k[0] != "_":
                repr[k] = self.__dict__[k]

        return repr

    def __str__(self):
        return str(self.__repr__())
