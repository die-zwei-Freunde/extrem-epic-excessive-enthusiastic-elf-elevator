from classes.enemy import enemy

class BasicGoblin(enemy.Enemy):
    '''
    Your basic goblin. Very weak in mind and physique, but strong in
    body odor.
    '''
    def __init__(self, name=None):
        self.id = 'Basic Goblin'

        super().__init__(name)

    def _setup_stats(self):
        HP = 1
        ATT = 1
        DEF = 1
        MAG = 1
        RES = 1
        INIT = 10

        return HP, ATT, DEF, MAG, RES, INIT

class TankGoblin(enemy.Enemy):
    '''
    The tanky one. A bit thick, but also thicccc.
    '''
    def __init__(self, name=None, MAX_HP=2, MAX_STAM=1):
        self.id = 'Tank Goblin'

        super().__init__(name, MAX_HP, MAX_STAM)

    def _setup_stats(self):
        HP = 5
        ATT = 1
        DEF = 3
        MAG = 1
        RES = 2
        INIT = 15

        return HP, ATT, DEF, MAG, RES, INIT
