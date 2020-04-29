from dgdl.builders import GameBuilder
import json
import ast

class DGDLParser:

    def __init__(self):
        self.parsed = {}

    def parse(self, input_file):
        self.parsed = GameBuilder().build(input_file)

    def json(self):
        return json.dumps(ast.literal_eval(str(self.parsed)), indent=2)
