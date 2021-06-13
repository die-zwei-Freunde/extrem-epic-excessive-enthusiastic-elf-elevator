from classes.enemy import enemy
from classes.ability.enemy import demon


class Demon(enemy.Enemy):
    '''
    A small demon is still a demon, its very agile and loves to blast his enemys away with magic.
    '''
    def __init__(self, name=None):
        self.id = 'Demon'

    def _setup_skills(self):
        return [demon.DemonFire(), demon.DemonStrike()]

    def _setup_stats(self):
        HP = 50
        ATT = 20
        DEF = 15
        MAG = 30
        RES = 20
        INIT = 6

        return HP, ATT, DEF, MAG, RES, INIT