from dgdl.builders import GameBuilder
import json
import ast

class DGDLParser:

    def __init__(self):
        self.parsed = {}

    def parse(self, file=None, input=None):
        self.parsed = GameBuilder().build(**{"file":file, "input":input})
        return self.parsed

    def json(self):
        return json.dumps(ast.literal_eval(str(self.parsed)), indent=2)
