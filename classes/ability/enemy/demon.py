from classes.ability import skill


class DemonFire(skill.Skill):
    '''A demon always likes his enemys cooked'''
    def __init__(self, name='Demon Fire', designation='MAG'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 15

    def _setup_cooldown(self):
        return 2


class DemonStrike(skill.Skill):
    '''A magic creature that slashes must be out of magic.'''
    def __init__(self, name='Demon Slash', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 10

    def _setup_cooldown(self):
        return 2
