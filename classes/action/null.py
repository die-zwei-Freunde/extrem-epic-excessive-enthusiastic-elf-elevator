from classes.action import action


class NullAction(action.Action):
    def __init(self, type):
        super().__init__(type)

    def start(self, players):
        return players, [], True