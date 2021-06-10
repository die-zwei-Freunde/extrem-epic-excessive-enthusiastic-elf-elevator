from classes.ability import skill

class BigSlash(skill.Skill):
    '''
    Orc skill.
    Slashes, but big, I guess. Most basic one I could think of,
    but it's for orcs, so its big
    '''
    def __init__(self, name='Big Slash', designation='ATT'):
        super().__init__(name, designation)

    def _setup_damage(self):
        return 4

    def _setup_cooldown(self):
        return 2



