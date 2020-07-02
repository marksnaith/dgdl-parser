from dgdl.builders import GameBuilder
import json
import ast

class DGDLParser:

    def __init__(self):
        self.parsed = {}

    def parse(self, file=None, src=None):
        self.parsed = GameBuilder().build(**kwargs)
        return self.parsed

    def json(self):
        return json.dumps(ast.literal_eval(str(self.parsed)), indent=2)
