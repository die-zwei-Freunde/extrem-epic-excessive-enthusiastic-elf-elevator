from classes.item.equip import equippable


class BloodyGlovesOfDemiGodJan(equippable.Equippable):
    """Gloves covered in what appears to be the blood of the demi-god Jan. Especially interesting, as it is said
    that Jan is not able to bleed."""
    def __init__(self):
        name = "Bloody Gloves of a Demi-God"
        race = ['all']
        alignment = ['Fighter']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'both_hands'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 1
        ATT = 2
        DEF = -1
        MAG = 0
        RES = -1
        INIT = -3
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class StandardDagger(equippable.Equippable):
    """Pretty standard dagger you can find by just walking down any 10 year old childs bedroom. Pretty fucked those
    youths nowadays."""
    def __init__(self):
        name = "Dagger"
        race = ['all']
        alignment = ['Fighter']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'left_hand'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 1
        DEF = -1
        MAG = 0
        RES = 0
        INIT = -1
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class Stillet(equippable.Equippable):
    """A long dagger, made from the blood of your enemies. It takes a lot of blood, as there is not that much iron in
    a gallon of blood."""
    def __init__(self):
        name = "Stillet"
        race = ['all']
        alignment = ['Fighter']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'left_hand'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 0
        ATT = 4
        DEF = -1
        MAG = 0
        RES = 0
        INIT = -2
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class BloodCloakDagger(equippable.Equippable):
    """A dagger from the very accomplished blacksmith von Blood-Cloak. Wait, you dont know him? Good for you, I guess."""
    def __init__(self):
        name = "Blood Coat Dagger"
        race = ['all']
        alignment = ['Fighter']

        super().__init__(name, race, alignment)

    def _setup_type(self):
        return 'left_hand'

    def _setup_stat_increase(self):
        """Return the stat changes; if the stat changes, return 0 for that stat."""
        HP = 1
        ATT = 7
        DEF = 1
        MAG = 0
        RES = 0
        INIT = -2
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK