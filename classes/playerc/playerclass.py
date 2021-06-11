"""Playerclass"""
from classes.race import *
from classes.alignment import *


class Player:
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

        self.skills = self._setup_skills()

        self.items = {}

    def equip_item(self, item):
        self.increase_stat('HP', item.dHP)
        self.increase_stat('MAX_HP', item.dHP)

        self.increase_stat('ATT', item.dATT)
        self.increase_stat('MAX_ATT', item.dATT)

        self.increase_stat('DEF', item.dDEF)
        self.increase_stat('MAX_DEF', item.dDEF)

        self.increase_stat('MAG', item.dMAG)
        self.increase_stat('MAX_MAG', item.dMAG)

        self.increase_stat('RES', item.dRES)
        self.increase_stat('MAX_RES', item.dRES)

        self.increase_stat('INIT', item.dINIT)
        self.increase_stat('MAX_INIT', item.dINIT)

        if self.INIT <= 0:
            self.INIT = 1
            self.MAX_INIT = 1

        self.items[item.id] = item

    def strip_item(self, item_id):
        if not item_id in self.items:
            raise KeyError('Item not equipped.')

        item = self.items[item_id]

        self.decrease_stat('HP', item.dHP)
        self.decrease_stat('MAX_HP', item.dHP)

        self.decrease_stat('ATT', item.dATT)
        self.decrease_stat('MAX_ATT', item.dATT)

        self.decrease_stat('DEF', item.dDEF)
        self.decrease_stat('MAX_DEF', item.dDEF)

        self.decrease_stat('MAG', item.dMAG)
        self.decrease_stat('MAX_MAG', item.dMAG)

        self.decrease_stat('RES', item.dRES)
        self.decrease_stat('MAX_RES', item.dRES)

        self.decrease_stat('INIT', item.dINIT)
        self.decrease_stat('MAX_INIT', item.dINIT)

        if self.INIT <= 0:
            self.INIT = 1
            self.MAX_INIT = 1

        del self.items[item.id]

    def use_item(self, item):
        effect = item.use()
        for key, val in effect.items():
            self.increase_stat(key, val)

            if self.HP > self.MAX_HP:
                self.HP = self.MAX_HP

    def apply_cooldown(self, name):
        for idx in range(len(self.skills)):
            self.skills[idx].reduce_cooldown()
            if self.skills[idx].name == name:
                self.skills[idx].on_cooldown()

    def _setup_alignment(self, align_id):
        if align_id == 'Fighter':
            return Fighter()
        if align_id == 'Mage':
            return Mage()

        else:
            raise ValueError('The alignment_id {} was not understood.'.format(align_id))


    def _setup_race(self, race_id):
        if race_id == 'Orc':
            return Orc()
        if race_id == 'Human':
            return Human()

        else:
            raise ValueError('The race_id {} was not understood.'.format(race_id))

    def _setup_skills(self):
        race_skills = self.race.get_race_skills()
        align_skills = self.alignment.get_alignment_skills()

        return race_skills + align_skills

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

    def get_skills(self):
        return self.skills

    def get_stats(self):
        return self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT

    def increase_stat(self, stat_name, incr):
        setattr(self, stat_name, getattr(self, stat_name) + incr)

    def decrease_stat(self, stat_name, incr):
        setattr(self, stat_name, getattr(self, stat_name) - incr)

    def __repr__(self):

        """Displays the stats of a player
        returns a string that can be printed and holds the current stats of the player"""
        return """{}:\n Race: {}, Alignment: {}, \n HP: {},\n ATT: {},\n DEF: {},\n MAG: {},\n RES: {},\n INIT: {}\n """.format(\
            self.name, self.race, self.alignment, self.HP, self.ATT, self.DEF, self.MAG, self.RES, self.INIT)
