from classes.inventory import inventory
import classes.item as ci

from logger import printf

class InventoryManager:
    def __init__(self, players):
        self.inventory = inventory.Inventory(players)
        self.setup_starting_inventory(players)

    def add_item(self, item_id):
        if not item_id in ci.CLASSES:
            raise KeyError(f'You may not have added your item {item_id} in the __init__.py of classes.item.')

        item = ci.CLASSES[item_id]()
        item_id = self.inventory.add_item(item)
        return item_id

    def manage(self, players):
        printf('Starting inventory...')
        editting = True
        while editting:
            mode = self.make_decision()
            if mode == 0:
                printf(self.inventory)
                self.observe_items()
            elif mode == 1:
                if not self.inventory.equippables:
                    printf('There are no equippable items.')
                    continue
                player = self.get_player(players)
                if not player:
                    continue
                player, player_id = player
                item = self.get_item()
                if not item:
                    continue
                player = self.inventory.equip_item_to_player(player, item)
                players[player.name] = player
                printf(player)

            elif mode == 2:
                if not self.inventory.equippables:
                    printf('There are no equippable items.')
                    continue
                player = self.get_player(players)
                if not player:
                    continue
                player, player_id = player
                item = self.get_item()
                if not item:
                    continue
                player = self.inventory.remove_item_from_player(item, player)
                players[player.name] = player
                printf('Successfull!')
                printf(player)

            elif mode == 3:
                if not self.inventory.useables:
                    printf('There are no useable items.')
                    continue
                player = self.get_player(players)
                if not player:
                    continue
                player, player_id = player
                item = self.get_item('u')
                if not item:
                    continue

                player = self.inventory.use_item_on_player(player, item)
                players[player.name] = player
                printf('Successfull!')
                printf(player)

            elif mode == 4:
                player = self.get_player(players)
                if not player:
                    continue
                player, player_id = player
                self._show_stats(player)

            elif mode == 5:
                editting = False

        return players

    def _show_stats(self, player):
        import copy
        printf(player)
        a = copy.deepcopy(self.inventory.get_assignments()[player.name])
        for key, value in a.items():
            if value:
                a[key] = a[key].id

        string = f"Assignments: \nLeft hand: {a['left_hand']},\nRight hand: {a['right_hand']},\n" \
                 f"Head: {a['head']},\nBody: {a['body']},\nBoots: {a['boots']},\nRing: {a['ring']},\n" \
                 f"Earring: {a['earring']},\nOther: {a['other']}."

        printf(string)


    def observe_items(self):
        while True:
            dec = input('Do you want to inspect a specific item? (y/n)\n')
            if dec == 'n' or dec == 'no':
                return 0

            item = self.get_item('all')
            if not item:
                return 0
            if item in self.inventory.useables:
                printf(self.inventory.useables[item])
            elif item in self.inventory.equippables:
                printf(self.inventory.equippables[item])


    def get_item(self, key='e'):
        while True:
            item_id = input('Specify the item: \n')
            if item_id == 'exit':
                return False
            if key == 'e':
                if item_id in self.inventory.equippables:
                    return item_id
                else:
                    item_list = [name for name in self.inventory.equippables.keys()]
                    printf(f'Your decision was not understood. Use one of {item_list}.')
            elif key == 'u':
                if item_id in self.inventory.useables:
                    return item_id
                else:
                    item_list = [name for name in self.inventory.useables.keys()]
                    printf(f'Your decision was not understood. Use one of {item_list}.')

            elif key == 'all':
                if item_id in self.inventory.useables or item_id in self.inventory.equippables:
                    return item_id
                else:
                    item_list = [name for name in self.inventory.useables.keys()]
                    item_list += [name for name in self.inventory.equippables.keys()]
                    printf(f'Your decision was not understood. Use one of {item_list}.')


    def get_player(self, players):
        while True:
            player_id = input('Specify the player: \n')
            if player_id == 'exit':
                return False
            try:
                player = players[player_id]
                break
            except:
                player_names = [name for name in players.keys()]
                printf(f'Your decision was not understood. Use the name of the players ({player_names})')

        return player, player_id

    def make_decision(self):
        while True:
            dec = input('What do you want to do?\nView [0] --- Equip [1] --- Strip [2] --- Use [3] --- Check [4] --- Exit [5]\n')
            try:
                mode = int(dec)
                break
            except:
                printf('Your decision was not understood. Use the numbers associated.')

        return mode

    def setup_starting_inventory(self, players):
        for player in players.values():
            if player.get_alignment_id() == 'mage':
                item_id = 'Wand'
            elif player.get_alignment_id() == 'fighter':
                item_id = 'Dagger'

            item_id = self.add_item(item_id)
            self.inventory.equip_item_to_player(player, item_id)


def main():
    from classes.playerc import playerclass

    p = playerclass.Player('ME', 'Human', 'Fighter')
    p.increase_stat('HP', -2)
    ps = {p.name: p}

    i = InventoryManager(ps)
    i.add_item('Small health potion')
    i.add_item('Bloody Gloves of a Demi-God')
    i.add_item('Runic Staff of Horror')
    i.add_item('Small health potion')
    i.add_item('Small health potion')
    i.add_item('Small health potion')
    i.add_item('Small health potion')

    ps = i.manage(ps)
    print(ps)

if __name__ == '__main__':
    main()