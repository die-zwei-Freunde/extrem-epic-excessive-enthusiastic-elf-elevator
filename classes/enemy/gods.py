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
        HP = 999
        ATT = 999
        DEF = 999
        MAG = 999
        RES = 999
        INIT = 1
        LUCK = 999

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class Piwo(enemy.Enemy):
    '''

    '''
    def __init__(self, name=None):
        self.id = 'GodPiwo'

        super().__init__(name)

    def _setup_skills(self):
        return [HandOfJustice()]

    def _setup_stats(self):
        HP = 999
        ATT = 999
        DEF = 999
        MAG = 999
        RES = 999
        INIT = 1
        LUCK = 999

        return HP, ATT, DEF, MAG, RES, INIT, LUCK
