class Inventory:
    """Inventory class that stores all items and groups them."""
    def __init__(self, players):
        self.equippables = {}
        self.useables = {}

        self.assignments = self._setup_assign(players)

    def use_item_on_player(self, player, item_id):
        if not self.useables:
            print('There are no useable items.')
            return player

        item = self.useables[item_id]
        player.use_item(item)
        del self.useables[item_id]

        return player

    def get_specific_item(self, item_id):
        if item_id in self.equippables:
            return self.equippables[item_id]
        else:
            return None

    def equip_item_to_player(self, player, item_id):
        player_dict = self.assignments[player.name]
        item = self.equippables[item_id]
        if player.get_alignment_id().capitalize() not in item.align and not 'all' in item.align:
            print('You cannot equip this item, your alignment is not right.')
            return player

        if item.equipped:
            print('This item is already equipped (to someone else, maybe).')

        if self.check_if_equippable(player_dict, item_id) and not item.equipped:
            player.equip_item(self.equippables[item_id])
            self.equippables[item_id].equipped = True

            if item.type == 'both_hands':
                self.assignments[player.name]['left_hand'] = item
                self.assignments[player.name]['right_hand'] = item
            else:
                self.assignments[player.name][item.type] = item

        elif not self.check_if_equippable(player_dict, item_id) and not item.equipped:
            choice = input(f'You are already full; want to swap items? (y/n)\n')
            if choice == 'y' or choice == 'yes':
                if item.type == 'both_hands':
                    old_item_type = ('left_hand', 'right_hand')
                else:
                    old_item_type = [item.type]
                for typ in old_item_type:
                    old_item = player_dict[typ]
                    if old_item:
                        self.remove_item_from_player(old_item.id, player)

                self.equippables[item_id].equipped = True
                if item.type == 'both_hands':
                    self.assignments[player.name]['left_hand'] = item
                    self.assignments[player.name]['right_hand'] = item
                else:
                    self.assignments[player.name][item.type] = item
                player.equip_item(self.equippables[item_id])

            else:
                print('Cannot equip this item!')
                pass

        return player

    def remove_item_from_player(self, item_id, player):
        item = self.equippables[item_id]

        if item.equipped:
            player.strip_item(item_id)
            if item.type == 'both_hands':
                self.assignments[player.name]['left_hand'] = None
                self.assignments[player.name]['right_hand'] = None
            else:
                self.assignments[player.name][item.type] = None
            self.equippables[item_id].equipped = False

        else:
            print('Item not equipped!')
            pass

        return player

    def add_item(self, item):
        item_id = self._setup_item_id(item)
        if item.designation == 'equippable':
            self.equippables[item_id] = item
        elif item.designation == 'useable':
            self.useables[item_id] = item

        else:
            raise NotImplementedError(f'Item designation {item.designation} not understood.')

        return item_id

    def remove_item(self, item_id):
        if item_id in self.equippables:
            del self.equippables[item_id]
        elif item_id in self.useables:
            del self.useables[item_id]

        else:
            raise KeyError('Item not found in inventory.')

    def _setup_item_id(self, item):
        if item.designation == 'equippable':
            search = self.equippables
        elif item.designation == 'useable':
            search = self.useables

        suffix = ''
        counter = 1
        while True:
            if not item.id+suffix in search.keys():
                item_id = item.id + suffix
                break
            else:
                suffix = f' ({counter})'
                counter += 1

        return item_id

    def check_if_equippable(self, dictionary, item_id):
        item = self.equippables[item_id]
        if item.type == 'both_hands':
            if not dictionary['left_hand'] and not dictionary['right_hand']:
                return True
        else:
            return not bool(dictionary[item.type])

    def _setup_assign(self, players):
        ass = {}
        for player in players:
            player_dict = {}
            player_dict['left_hand'] = None
            player_dict['right_hand'] = None
            player_dict['head'] = None
            player_dict['body'] = None
            player_dict['boots'] = None
            player_dict['ring'] = None
            player_dict['earring'] = None
            player_dict['other'] = None

            ass[player] = player_dict

        return ass

    def get_assignments(self):
        return self.assignments

    def __repr__(self):
        intro = "Inventory: \n"
        eq = f"Equippable items:\n{[key for key in self.equippables.keys()]}.\n"
        us = f"Useable items:\n{[key for key in self.useables.keys()]}.\n"

        return intro + eq + us