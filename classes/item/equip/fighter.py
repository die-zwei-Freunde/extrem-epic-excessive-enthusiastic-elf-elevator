from classes.item.equip import equippable


class BloodyGlovesOfDemiGodJan(equippable.Equippable):
    """Gloves covered in what appears to be the blood of the demi-god Jan. Especially interesting, as it is said
    that Jan is not able to bleed."""
    def __init__(self):
        name = "Runic Staff of Horror"
        race = ['all']
        alignment = ['Fighter']

        super().__init__(name, race, alignment)

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 1
        ATT = 2
        DEF = -1
        MAG = 0
        RES = -1
        INIT = -3

        return HP, ATT, DEF, MAG, RES, INIT