from classes.alignment.alignment import Alignment
from classes.ability.alignment import fighter


class Fighter(Alignment):
    ''' Fighter Alignment class '''
    def __init__(self):
        #name = 'fighter'
        super().__init__('fighter', False)

    def _setup_skills(self):
        return [fighter.QuickStrike()]

    def _adjust_HP(self, HP):
        ''' Adjust the HP for the given alignment '''
        return HP + 1

    def _adjust_ATT(self, ATT):
        ''' Adjust the ATT for the given alignment '''
        return ATT + 2

    def _adjust_DEF(self, DEF):
        ''' Adjust the DEF for the given alignment '''
        return DEF + 1

    def _adjust_MAG(self, MAG):
        ''' Adjust the MAG for the given alignment '''
        return MAG

    def _adjust_RES(self, RES):
        ''' Adjust the RES for the given alignment '''
        return RES 

    def _adjust_INIT(self, INIT):
        ''' Adjust the INIT for the given alignment '''
        return INIT - 2

    def _adjust_LUCK(self, LUCK):
        return LUCK
 
    def __repr__(self):
        return 'Fighter'
