from classes.enemy import enemy
from classes.ability.enemy import demon


class Demon(enemy.Enemy):
    '''
    A small demon is still a demon, its very agile and loves to blast his enemys away with magic.
    '''
    def __init__(self, name=None):
        self.id = 'Demon'

        super().__init__(name)

    def _setup_skills(self):
        return [demon.DemonFire(), demon.DemonStrike()]

    def _setup_stats(self):
        HP = 30
        ATT = 5
        DEF = 7
        MAG = 5
        RES = 10
        INIT = 6

        return HP, ATT, DEF, MAG, RES, INIT