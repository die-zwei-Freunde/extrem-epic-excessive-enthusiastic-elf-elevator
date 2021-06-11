class Item:
    '''Abstract Base class for any items; equippable and useable.'''
    def __init__(self, id, race, alignment, ):
        self.id = id
        self.race = race
        self.align = alignment

    def get_possible_races(self):
        '''Get the list of all possible races that may use/equip this item.'''
        return self.race

    def get_possible_alignments(self):
        '''Get the list of all possible alignments that may use/equip this item.'''
        return self.align