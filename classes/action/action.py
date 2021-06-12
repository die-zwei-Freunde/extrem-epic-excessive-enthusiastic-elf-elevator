class Action:
    def __init__(self, type):
        self.type = type

    def start(self, players):
        """Main routine to start an action. Has to return the player dictionary (editted) and a list of lootables."""
        raise NotImplementedError('You did not implement this routine, the main one, hahaha.')
