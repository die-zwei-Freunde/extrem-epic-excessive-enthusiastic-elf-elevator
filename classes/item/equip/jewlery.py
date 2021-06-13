from classes.item.equip import equippable


class RingOfMagic(equippable.Equippable):
    """Small trinket of magic, fit for anyone's finger. And every finger at that, which might be the most magical
    about it."""
    def __init__(self):
        name = "Ring of Magic"
        race = ['all']
        alignment = ['all']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'ring'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 0
        DEF = 0
        MAG = 3
        RES = 1
        INIT = 0
        LUCK = 1

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class RingOfPower(equippable.Equippable):
    """One ring, to punch someone slightly harder. Some say it is magic, some say it just hurts more if you punch
    someone with metal-wrapped knuckles."""
    def __init__(self):
        name = "Ring of Power"
        race = ['all']
        alignment = ['all']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'ring'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 3
        DEF = 1
        MAG = 0
        RES = 0
        INIT = 0
        LUCK = 1

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class EarringOfDefense(equippable.Equippable):
    """A very specific trinket that was once used by a wall. Maybe one day I will tell you the story of the
    great wall of Lycano."""
    def __init__(self):
        name = "Earring of Defense"
        race = ['all']
        alignment = ['all']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'earring'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 0
        DEF = 5
        MAG = 0
        RES = 5
        INIT = 1
        LUCK = 1

        return HP, ATT, DEF, MAG, RES, INIT, LUCK