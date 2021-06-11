from classes.ability import skill

class Fireball(skill.Skill):
    '''
    Mage skill.
    Your basic mage skill.
    '''
    def __init__(self, name='Fireball', designation='MAG'):
        super().__init__(name, designation, attr='Fire')

    def _setup_damage(self):
        return 6

    def _setup_cooldown(self):
        return 3
