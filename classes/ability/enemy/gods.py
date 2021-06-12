from classes.ability import skill


class RighteuosFireOfGlory(skill.Skill):
    ''' Simplest Enemy attack'''
    def __init__(self, name='Righteuos Fire', designation='MAG'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 1000000

    def _setup_cooldown(self):
        return 1


class HandOfJustice(skill.Skill):
    ''' Simplest Enemy attack'''
    def __init__(self, name='Hand of Justice', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 1000000

    def _setup_cooldown(self):
        return 1