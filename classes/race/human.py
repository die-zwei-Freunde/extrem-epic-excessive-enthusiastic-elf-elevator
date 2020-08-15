from classes.race import race
from classes.race import human_skills

class Human(race.Race):

    def __init__(self):
        super().__init__(verbose=False)

    def _setup_stats(self):
        HP = 2
        ATT = 4
        DEF = 3
        MAG = 3
        RES = 4
        INIT = 4

        return HP, ATT, DEF, MAG, RES, INIT

    def _setup_skills(self):
        return [human_skills.StrikeOfHonor()]

    def __repr__(self):
         return 'Human'
