from classes.alignment.alignment import Alignment
from classes.ability.alignment import mage


class Mage(Alignment):
    ''' Mage Alignment class '''
    def __init__(self):
        super().__init__(False)

    def _setup_skills(self):
        return [mage.Fireball()]

    def _adjust_HP(self, HP):
        ''' Adjust the HP for the given alignment '''
        return HP + 1

    def _adjust_ATT(self, ATT):
        ''' Adjust the ATT for the given alignment '''
        return ATT 

    def _adjust_DEF(self, DEF):
        ''' Adjust the DEF for the given alignment '''
        return DEF 

    def _adjust_MAG(self, MAG):
        ''' Adjust the MAG for the given alignment '''
        return MAG + 3

    def _adjust_RES(self, RES):
        ''' Adjust the RES for the given alignment '''
        return RES + 2

    def _adjust_INIT(self, INIT):
        ''' Adjust the INIT for the given alignment '''
        return INIT - 1

    def __repr__(self):
        return 'Mage'
