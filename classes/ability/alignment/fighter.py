from classes.ability import skill

class QuickStrike(skill.Skill):
    '''
    Fighter skill.
    Quick strike, low cooldown, low power
    '''
    def __init__(self, name='Quick Strike', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 2

    def _setup_cooldown(self):
        return 1
