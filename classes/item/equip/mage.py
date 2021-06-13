from classes.item.equip import equippable


class RunicStaff(equippable.Equippable):
    """Staff of Runes Cape. Very old, you wouldn't want to get hit by it, it might break."""
    def __init__(self):
        name = "Runic Staff of Horror"
        race = ['all']
        alignment = ['Mage']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'left_hand'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 1
        DEF = 0
        MAG = 10
        RES = 4
        INIT = 0
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class CrookedWand(equippable.Equippable):
    """A crooked wand of magic. More like a stick, actually. Sticks and stones may brake your bones, but this one
    probably wont."""
    def __init__(self):
        name = "Wand"
        race = ['all']
        alignment = ['Mage']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'both_hands'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 0
        DEF = 0
        MAG = 1
        RES = 0
        INIT = 1
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class WandOfAvalon(equippable.Equippable):
    """The long staff of Avalon. Apparently made from the wood of Avalon. Jep, exactly."""
    def __init__(self):
        name = "Wand of Avalon"
        race = ['all']
        alignment = ['Mage']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'both_hands'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 0
        DEF = 0
        MAG = 4
        RES = 0
        INIT = 1
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class RodOfHellfire(equippable.Equippable):
    """A wand that is actually not on fire, contrary to what the name suggests. It is actually named after an old
    philosopher, that got drunk with Hellfire while creating this wand. Pathetic."""
    def __init__(self):
        name = "Rod of Hellfire"
        race = ['all']
        alignment = ['Mage']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'both_hands'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 0
        DEF = 0
        MAG = 7
        RES = 1
        INIT = 1
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK