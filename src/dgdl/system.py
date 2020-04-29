# from antlr import *
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
