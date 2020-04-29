#from dgdl import System
from dgdl.builders import GameBuilder
from dialogue import *
from dgdl.dgdl_parser import DGDLParser

if __name__ == "__main__":
    s = DGDLParser()
    s.parse('grammar/testgame.dgdl')

    print(s.json())
