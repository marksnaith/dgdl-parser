from antlr.grammar import *
from .base_dgdl_builder import BaseDGDLBuilder

class CompositionBuilder(BaseDGDLBuilder):

    def __init__(self):
        self.composition = {
            "roles": [],
            "players": [],
            "stores": [],
            "backtracking": False
        }
        self.current_player = None

    def enterRoleList(self, ctx:dgdlParser.RoleListContext):
        ''' Build the roles in the composition
            This will also add roles declared in player{} definitions '''

        for r in ctx.role():
            self.composition["roles"].append(r.getText())

    def enterParticipants(self, ctx:dgdlParser.ParticipantsContext):
        print("Entered participants")
        min = int(ctx.minplayers().number().getText())
        max = ctx.maxplayers().number()

        # max can be undefined so number() might be None
        if max is not None:
            max = int(max.getText())
        else:
            max = 'undefined'

        self.composition["min_participants"] = min
        self.composition["max_participants"] = max


    def enterPlayer(self, ctx):
        id = ctx.playerID().identifier().getText()

        min = ctx.minplayers()
        max = ctx.maxplayers()

        if min is not None:
            min = int(min.getText())

        if max is not None:
            max = max.getText()

            if max == 'undefined':
                max = None
            else:
                max = int(max)

        roles = ctx.roleList()

        if roles is not None:
            roles = [r.getText() for r in roles.role()]
        else:
            roles = []

        self.composition["players"].append({
                "playerID": id,
                "roles": roles
        })

    def enterStore(self, ctx):
        id = ctx.storeID().getText()
        owner = ctx.storeOwner()

        owners = [o.getText() for o in owner.identifier()]
        structure = ctx.storeStructure().getText()
        visibility = ctx.storeVisibility().getText()

        content = ctx.storeContent()

        if content is not None:
            content = [c.getText() for c in content.identifier()]
        else:
            content = []

        self.composition["stores"].append({
            "id": id,
            "owner": owners,
            "structure": structure,
            "visibility": visibility,
            "content": content
        })

    def enterBacktrack(self, ctx):
        if ctx.onoff() is not None:
            onoff = ctx.onoff().getText()

            if onoff == "on":
                self.composition["backtracking"] = True

    def get_representation(self):
        return self.composition
