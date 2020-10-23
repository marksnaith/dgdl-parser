"""
Copyright (C) 2020  Centre for Argument Technology (http://arg.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# from dgdl.antlr import *
# from antlr4 import *
# from .concrete_dgdl_listener import ConcreteDGDLListener
# from .dgdl_element import DGDLElement
#
# from .builders import *
#
# class System(DGDLElement):
#
#     def __init__(self):
#         self.identifier = ""
#         self.games = {}
#
#         self.builders = {
#             "composition": CompositionBuilder,
#             "rules": RuleBuilder,
#             "interactions": InteractionBuilder
#         }
#
#     def load(self, src):
#         parser = dgdlParser(CommonTokenStream(dgdlLexer(FileStream(src))))
#
#         tree = parser.system()
#
#         listener = ConcreteDGDLListener(self)
#         walker = ParseTreeWalker()
#         walker.walk(listener, tree)
#
#         builder = CompositionBuilder()
#         walker.walk(builder, tree)
#
#
#         self = listener.get_system(True)
#
#         #print(builder.composition)
#
#
#         print(self)
