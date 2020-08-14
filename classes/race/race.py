class Race():
    '''
    Interface for creating Race classes.
    Needs a method for setting up Base Stats.
    '''
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.stats = self._setup_stats()

    def _setup_stats(self):
        ''' Setup base stats for the race'''
        raise NotImplementedError()

    def get_base_stats(self):
        return self.stats

    def set_HP(self):
        ''' YOU SHOULD NOT MESS WITH THE BASE STATS'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')

    def set_STAM(self):
        '''All your base are belong to us'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')

##########################################################
    
class Orc(Race):

    def __init__(self):
        super().__init__()

    def _setup_stats(self):
        HP = 4
        ATT = 5
        DEF = 3
        MAG = 1
        RES = 2
        INIT = 6

        return HP, ATT, DEF, MAG, RES, INIT 
  
    def __repr__(self):
         return 'Orc'

###########################################################

class Human(Race):

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

    def __repr__(self):
         return 'Human'
