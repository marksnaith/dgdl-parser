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

from dgdl.antlr import *
from .base_dgdl_builder import BaseDGDLBuilder
from dgdl.elements import *

class CompositionBuilder(BaseDGDLBuilder):

    def __init__(self):
        self.composition = {
            "gameID": None,
            "roles": [],
            "players": [],
            "stores": [],
            "turntaking": "strict",
            "backtracking": False,
            "interactions": [],
            "extURI": {}
        }
        self.current_player = None

    def enterGame(self, ctx):
        self.composition["gameID"] = ctx.gameID().getText()

    def enterRoleList(self, ctx:dgdlParser.RoleListContext):
        ''' Build the roles in the composition
            This will also add roles declared in player{} definitions '''

        for r in ctx.role():
            self.composition["roles"].append(r.getText())

    def enterParticipants(self, ctx:dgdlParser.ParticipantsContext):
        min = int(ctx.minplayers().number().getText())
        max = ctx.maxplayers().number()

        # max can be undefined so number() might be None
        if max is not None:
            max = int(max.getText())
        else:
            max = 'undefined'

        self.composition["participants"] = {"min": min, "max": max}

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

        roles = ctx.playerRoleList()

        if roles is not None:
            roles = [r.getText() for r in roles.role()]
        else:
            roles = []

        self.composition["players"].append(Player(id, roles))

    def enterStore(self, ctx):
        id = ctx.storeID().getText()
        owner = ctx.storeOwner()

        owners = [o.getText() for o in owner.identifier()]
        structure = ctx.storeStructure().getText()
        visibility = ctx.storeVisibility().getText()

        content = ctx.storeContent()

        if content is not None:
            content = [c.getText() for c in content.contentVar()] + [s.getText() for s in content.STRINGLITERAL()]
        else:
            content = []

        self.composition["stores"].append(Store(id, owners, structure, visibility, content))

    def enterBacktrack(self, ctx):
        if ctx.onoff() is not None:
            onoff = ctx.onoff().getText()

            if onoff == "on":
                self.composition["backtracking"] = True

    def enterTurntaking(self, ctx):
        if ctx.turntakingtype() is not None:
            self.composition["turntaking"] = ctx.turntakingtype().getText()

    def enterExtURI(self, ctx):
        id = ctx.extUriID().getText()
        uri = ctx.uri().STRINGLITERAL().getText()

        self.composition["extURI"][id] = uri[1:-1]

    def get_representation(self):
        return self.composition
