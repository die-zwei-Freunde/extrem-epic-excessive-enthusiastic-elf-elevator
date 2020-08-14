class Alignment():
    '''
    Interface for creating an Alignment.
    Needs a method for adjusting the Base stats.
    '''
    def __init__(self, verbose=False):
        self.verbose = verbose

    def adjust_stats(self, stats):
        '''
        Adjust the HP and STAM (stats) that you can get from
        the race instance (via .get_HP and .get_STAM)
        '''
        HP = self._adjust_HP(stats[0])
        ATT = self._adjust_ATT(stats[1])
        DEF = self._adjust_DEF(stats[2])
        MAG = self._adjust_MAG(stats[3])
        RES = self._adjust_RES(stats[4])
        INIT = self._adjust_INIT(stats[5])
        return HP, ATT, DEF, MAG, RES, INIT

    def _adjust_HP(self, HP):
        ''' Adjust the HP for the given alignment '''
        raise NotImplementedError()

    def _adjust_ATT(self, ATT):
        ''' Adjust the ATT for the given alignment '''
        raise NotImplementedError()

    def _adjust_DEF(self, DEF):
        ''' Adjust the DEF for the given alignment '''
        raise NotImplementedError()

    def _adjust_MAG(self, MAG):
        ''' Adjust the MAG for the given alignment '''
        raise NotImplementedError()

    def _adjust_RES(self, RES):
        ''' Adjust the RES for the given alignment '''
        raise NotImplementedError()

    def _adjust_INIT(self, INIT):
        ''' Adjust the INIT for the given alignment '''
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

####################################

class Fighter(Alignment):
    ''' Fighter Alignment class '''
    def __init__(self):
        super().__init__(False)

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
 
    def __repr__(self):
        return 'Fighter'

#####################################

class Mage(Alignment):
    ''' Mage Alignment class '''
    def __init__(self):
        super().__init__(False)

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



