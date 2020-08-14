"""Playerclass"""
from classes.race.race import *
from classes.alignment.alignment import *

class Player():
 
    def __init__(self, name, race, alignment):
        """Sorts the arguments to variables
        Arg: 
            race: race chosen by the player
            alignment: alignment chosen by the player"""
        self.name = name
        self.race = self._setup_race(race)
        self.alignment = self._setup_alignment(alignment)
        
        self.HP, self.ATT, self.DEF, \
                 self.MAG, self.RES, self.INIT = self.setup_stats()
        self.MAX_HP = self.HP
        self.MAX_ATT = self.ATT
        self.MAX_DEF = self.DEF
        self.MAX_MAG = self.MAG
        self.MAX_RES = self.RES
        self.MAX_INIT = self.INIT

    def _setup_alignment(self, align_id):
        if align_id == 'fighter':
            return Fighter()
        if align_id == 'mage':
            return Mage()

        else:
            raise ValueError('The alignment_id {} was not understood.'.format(align_id))


    def _setup_race(self, race_id):
        if race_id == 'orc':
            return Orc()
        if race_id == 'human':
            return Human()

        else:
            raise ValueError('The race_id {} was not understood.'.format(race_id))

    def setup_stats(self):
        """sets personal player stats at the start
        Arg:
            race: sets your ground stats
            alignment: gives you bonus stats
        Out:
            HP: hitpoints
            STAM: stamina"""

        base_stats = self.race.get_base_stats()

        stats = self.alignment.adjust_stats(base_stats)
        
        return stats

    def change_max_stat(self, stat_name, val):
        '''
        Change the maximum stat/HP by e.g. equipping an item
        '''
        raise NotImplementedError()
    

    def change_stat(self, stat_name, val):
        """tool to change the temporarily stats of a player
        Arg:
            stat_name: name of the stat to be changed
            val: value of the change
        Out:
            new value of the stat thats been changed"""
        
        setattr(self, stat_name, val)

    def get_stats(self):
        return self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT

    def __repr__(self):

        """Displays the stats of a player
        returns a string that can be printed and holds the current stats of the player"""
        return """{}:\n Race: {}, Alignment: {}, \n HP: {},\n ATT: {},\n DEF: {},\n MAG: {},\n RES: {},\n INIT: {}\n """.format(\
            self.name, self.race, self.alignment, self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT)
