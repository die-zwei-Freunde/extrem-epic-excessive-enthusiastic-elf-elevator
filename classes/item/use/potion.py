from classes.item.use import useable


class SmallHealthPotion(useable.Useable):
    """Small health potion from a very handsome but very scetchy gentleman down the street."""
    def __init__(self):
        name = "Small health potion"
        race = ['all']
        alignment = ['all']

        super().__init__(name, race, alignment)

    def use(self):
        """Increase the current health by 5."""
        return {'HP': 5}