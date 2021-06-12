from classes.enemy import enemy
from classes.ability.enemy.gods import RighteuosFireOfGlory, HandOfJustice



class Jan(enemy.Enemy):
    '''

    '''
    def __init__(self, name=None):
        self.id = 'GodJan'

        super().__init__(name)

    def _setup_skills(self):
        return [RighteuosFireOfGlory()]

    def _setup_stats(self):
        HP = 420
        ATT = 69
        DEF = 96
        MAG = 222
        RES = 333
        INIT = 2

        return HP, ATT, DEF, MAG, RES, INIT


class Piwo(enemy.Enemy):
    '''

    '''
    def __init__(self, name=None):
        self.id = 'GodPiwo'

        super().__init__(name)

    def _setup_skills(self):
        return [HandOfJustice()]

    def _setup_stats(self):
        HP = 444
        ATT = 400
        DEF = 42
        MAG = 222
        RES = 999
        INIT = 1

        return HP, ATT, DEF, MAG, RES, INIT
