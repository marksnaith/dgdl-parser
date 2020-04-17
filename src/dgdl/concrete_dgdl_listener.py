from antlr.grammar import *
from .game import Game
from .player import Player
from .store import Store
from .rule import Rule

class ConcreteDGDLListener(dgdlListener):

    def __init__(self, system):
        self.system = system
        self.current_game = None
        self.current_player = None
        self.current_rule = None
        self.warnings = []

    def enterSystem(self, ctx:dgdlParser.SystemContext):
        identifier = ctx.systemID().identifier().getText()
        self.system.identifier = identifier

    def enterGame(self, ctx:dgdlParser.GameContext):
        print("Entered game")
        identifier = ctx.gameID().identifier().getText()
        self.current_game = Game(identifier)

    def exitGame(self, ctx:dgdlParser.GameContext):
        print("Exit game")
        self.system.games[self.current_game.identifier] = self.current_game
        current_game = None

    def enterRoleList(self, ctx:dgdlParser.RoleListContext):
        if self.current_player is None:
            for r in ctx.role():
                self.current_game.roles.append(r.getText())
        else:
            for r in ctx.role():
                role = r.getText()
                if role not in self.current_game.roles:
                    self.record_warning("Role " + role + " assigned to player " + self.current_player.identifier + " does not exist in the game")
                self.current_player.roles.append(role)

    def enterParticipants(self, ctx:dgdlParser.ParticipantsContext):
        print("Entered participants")
        min = int(ctx.minplayers().number().getText())
        max = ctx.maxplayers().number()

        # max can be undefined so number() might be None
        if max is not None:
            max = int(max.getText())
        else:
            max = 'undefined'

        self.current_game.min_participants = min
        self.current_game.max_participants = max

    def enterPlayer(self, ctx:dgdlParser.PlayerContext):
        self.current_player = Player()
        print("Entered player")
        identifier = ctx.playerID().identifier().getText()
        self.current_player.identifier = identifier
        min = ctx.minplayers()
        max = ctx.maxplayers()

        if min is not None:
            min = int(min.number().getText())
        else:
            min = 'undefined'

        if max is not None:
            max = int(max.number().getText())
        else:
            max = 'undefined'

        self.current_game.set_min_max_players(identifier, min, max)

    def exitPlayer(self, ctx:dgdlParser.PlayerContext):
        print("Exited player")
        self.current_game.players.append(self.current_player)
        self.current_player = None

    def enterStore(self, ctx:dgdlParser.StoreContext):
        print("Entered store")
        self.current_store = Store()
        self.current_store.identifier = ctx.storeID().identifier().getText()

        owner = ctx.storeOwner().identifier()

        for o in owner:
            self.current_store.owner.append(o.getText())

        self.current_store.structure = ctx.storeStructure().getText()
        self.current_store.visibility = ctx.storeVisibility().getText()

        content = ctx.storeContent()

        if content is not None:
            for c in content.identifier():
                self.current_store.content.append(c.getText())

    def exitStore(self, ctx:dgdlParser.StoreContext):
        self.current_game.stores.append(self.current_store)
        self.current_store = None

    def enterBacktrack(self, ctx:dgdlParser.BacktrackContext):
        self.current_game.backtracking = ctx.onoff().getText()

    def enterRules(self, ctx:dgdlParser.RulesContext):
        print("Entered rules")
        self.current_rule = Rule()

        self.current_rule.identifier = ctx.ruleID().identifier().getText()
        self.current_rule.scope = ctx.scopeType().getText()

    def exitRules(self, ctx:dgdlParser.RulesContext):
        self.current_game.rules.append(self.current_rule)
        self.current_rule = None

    def record_warning(self, txt):
        self.warnings.append(txt)

    def get_system(self, print_warnings=False):
        if print_warnings:
            for w in self.warnings:
                print("WARNING: " + w)
        return self.system
