class Race():
    '''
    Interface for creating Race classes.
    Needs a method for setting up Base Stats.
    '''
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.stats = self._setup_stats()
        self.skills = self._setup_skills()

    def _setup_stats(self):
        ''' Setup base stats for the race'''
        raise NotImplementedError()

    def _setup_skills(self):
        ''' Setup list of skills, from classes.ability '''
        raise NotImplementedError()

    def get_race_skills(self):
        return self.skills

    def get_base_stats(self):
        return self.stats

    def set_HP(self):
        ''' YOU SHOULD NOT MESS WITH THE BASE STATS'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')

    def set_STAM(self):
        '''All your base are belong to us'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')
    


