from classes.enemy import enemy
from classes.ability.enemy import goblin


class BasicGoblin(enemy.Enemy):
    '''
    Your basic goblin. Very weak in mind and physique, but strong in
    body odor.
    '''
    def __init__(self, name=None):
        self.id = 'Basic Goblin'

        super().__init__(name)

    def _setup_skills(self):
        return [goblin.Tackle()]

    def _setup_stats(self):
        HP = 15
        ATT = 13
        DEF = 8
        MAG = 2
        RES = 8
        INIT = 11
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK


class TankGoblin(enemy.Enemy):
    '''
    The tanky one. A bit thick, but also thicccc.
    '''
    def __init__(self, name=None):
        self.id = 'Tank Goblin'

        super().__init__(name)

    def _setup_skills(self):
        return [goblin.Tackle()]

    def _setup_stats(self):
        HP = 20
        ATT = 13
        DEF = 10
        MAG = 2
        RES = 10
        INIT = 13
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK
