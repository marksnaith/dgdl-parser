dgdl_handlers = {}

def dgdl_handler(element):
    element = element.lower()

    def wrapper(fn):
        dgdl_handlers[element] = fn

        return fn

    return wrapper

class Dialogue:

    def __init__(self):
        #self.effect_handlers = {
        #            "move": self.handle_move_effect,
        #            "assign": self.handle_assign_effect,
        #            "conditional": self.handle_conditional_effect
        #}
        pass


    def perform_interaction(self, data):

        effects = interaction.get_effects(data["interactionID"])
        self.handle_effects(effects, data)

        return

    def handle_effects(self, effects, data):
        for e in effects:
            response = e.perform(data)

            if "type" in response:
                if response["type"] in self.effect_handlers:
                    self.effect_handlers(response, data)

    @dgdl_handler("move")
    def handle_move_effect(self, data, interaction_data):
        return

    def handle_assign_effect(self, data, interaction_data):
        return

    def handle_conditional(self, data, interaction_data):

        self.handlers = {
            "roleinspection": test_role_inspection,
            "event": test_event
        }

        passed = True #assume True until False

        for condition in data["conditions"]:
            type = condition["type"]

            if type in self.handlers:
                passed = self.handlers[type](condition)

                if not passed:
                    break #no point in testing any others


        if passed:
            return self.handle_effects(data["effects"])
        else:
            if data["elseif"] is not None:
                response = data["elseif"].perform(data)
                return handle_conditional(response)
            elif data["else"]:
                self.handle_effects(data["else"])


        def test_role_inspection(data):
            return False

        def test_event(data):
            return False

        return
