from classes.item import item


class Equippable(item.Item):
    """Item that can be equipped and thus has extended interfaces."""
    def __init__(self, name, race, alignment):
        super().__init__(name, race, alignment)
        self.designation = 'equippable'
        self.equipped = False

        self.type = self._setup_type()
        self.dHP, self.dATT, self.dDEF, self.dMAG, self.dRES, self.dINIT = self._setup_stat_increase()
        self.restrictions = self._setup_restrictions()

    def get_dHP(self):
        return self.dHP

    def get_dATT(self):
        return self.dATT

    def get_dDEF(self):
        return self.dDEF

    def get_dMAG(self):
        return self.dMAG

    def get_dRES(self):
        return self.dRES

    def get_dINIT(self):
        return self.dINIT

    def _setup_type(self):
        """Setup the type of equippable item (left_hand, right_hand, both_hands,
         head, body, boots, ring, earring, other)"""
        raise NotImplementedError('Specify the type of equippable item; see documentation on the right naming scheme.')

    def _setup_stat_increase(self):
        """Setup the stat increase/decrease that the item implies."""
        raise NotImplementedError(f'Specify the stat changes the Equippable Item {self.id} has on the player.')

    def _setup_restrictions(self):
        """Overwrite this method if you want to introduce Stat restrictions to your item.
        In that case, return a dictionary of {stat: min_level}."""
        return None

    def __repr__(self):
        string = f"Item: {self.id}.\nRaces: {self.race}, Alignments: {self.align}\nStat changes: HP: {self.dHP}, " \
                 f"ATT: {self.dATT}, DEF: {self.dDEF},\nMAG: {self.dMAG}, RES: {self.dRES}, INIT: {self.dINIT}."
        return string
