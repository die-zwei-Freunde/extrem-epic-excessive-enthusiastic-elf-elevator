from classes.action import action


class TreasureAction(action.Action):
    def __init__(self, type, loot):
        super().__init__(type)

        self.loot = loot

    def start(self, players):
        return players, self.loot, True