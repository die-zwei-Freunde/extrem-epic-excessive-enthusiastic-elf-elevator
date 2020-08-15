from classes.ability import skill

class StrikeOfHonor(skill.Skill):
    '''
    Human skill.
    Humanssss have honor. They strike. We are. Number One.
    '''
    def __init__(self, name='Strike of Honor', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 3

    def _setup_cooldown(self):
        return 1
