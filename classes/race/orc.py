from classes.race import race
from classes.ability.race import orc


class Orc(race.Race):

    def __init__(self):
        super().__init__()

    def _setup_stats(self):
        HP = 9
        ATT = 5
        DEF = 4
        MAG = 1
        RES = 3
        INIT = 12
        LUCK = 0

        return HP, ATT, DEF, MAG, RES, INIT, LUCK

    def _setup_skills(self):
        return [orc.BigSlash()]
  
    def __repr__(self):
         return 'Orc'
