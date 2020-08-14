'''
Introducing: the enemy.
It is ... not your friend, I guess.
'''


class Enemy():
    '''
    Enemy (short: NME)
    base class for future enemies which will be clubbed to death for entertainment.
    Maybe they should scream a bit?
    '''
    def __init__(self, name):
        self.name = name

        self.HP, self.ATT, self.DEF, \
                 self.MAG, self.RES, self.INIT = self._setup_stats()
        self.MAX_HP = self.HP
        self.MAX_ATT = self.ATT
        self.MAX_DEF = self.DEF
        self.MAX_MAG = self.MAG
        self.MAX_RES = self.RES
        self.MAX_INIT = self.INIT
        

    def _setup_stats(self):
        '''
        Change this if you want to randomly adjust random
        the HP of the enemy (like, every enemy has a 10%
        to have one more max_HP
        '''
        raise NotImplementedError('You thought you could get away with this?!')
    

    def get_stats(self):
        return self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT
    

    def set_stat(self, attr, val):
        setattr(self, attr, val)


    def __repr__(self):
        return "Name: {},\n Type: {},\n HP: {},\n ATT: {},\n DEF: {},\n MAG: {},\n RES: {},\n INIT: {}\n".format(\
            self.name, self.id, self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT)



