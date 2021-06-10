from classes.ability import skill

class Tackle(skill.Skill):
    ''' Simplest Enemy attack'''
    def __init__(self, name='Blind Tackle', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 1

    def _setup_cooldown(self):
        return 2
