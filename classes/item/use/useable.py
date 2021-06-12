from classes.item import item


class Useable(item.Item):
    """Base class for creating an useable object."""
    def __init__(self, name, race, alignment):
        super().__init__(name, race, alignment)
        self.designation = 'useable'
        self.effect = self.use()

    def use(self):
        """Specify the effect of your one-use item by dictionary:
        {stat: change (int)}. You may increase your current health (aka healing), or your
        max_hp (stat : MAX_HP, MAX_ATT, ...)."""
        raise NotImplementedError('Specify the effect of your usable item.')

    def __repr__(self):
        string = f"Item: {self.id}.\nRaces: {self.race}, Alignments: {self.align}\nStat changes: \n{self.effect}."
        return string