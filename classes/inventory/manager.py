from classes.inventory import inventory
import classes.item as ci

from logger import printf

class InventoryManager:
    def __init__(self, players):
        self.inventory = inventory.Inventory(players)

    def add_item(self, item_id):
        if not item_id in ci.CLASSES:
            raise KeyError('You may not have added your item in the __init__.py of classes.item.')

        item = ci.CLASSES[item_id]()
        self.inventory.add_item(item)

    def manage(self, players):
        printf('Starting inventory...')
        editting = True
        while editting:
            mode = self.make_decision()
            if mode == 0:
                printf(self.inventory)
                self.observe_items()
            elif mode == 1:
                player = self.get_player(players)
                if not player:
                    pass
                player, player_id = player
                item = self.get_item()
                if not item:
                    pass
                player = self.inventory.equip_item_to_player(player, item)
                players[player.name] = player

            elif mode == 2:
                player = self.get_player(players)
                if not player:
                    pass
                player, player_id = player
                item = self.get_item()
                if not item:
                    pass
                player = self.inventory.remove_item_from_player(item, player)
                players[player.name] = player

            elif mode == 3:
                player = self.get_player(players)
                if not player:
                    pass
                player, player_id = player
                item = self.get_item()
                if not item:
                    pass

                player = self.inventory.use_item_on_player(player, item)
                players[player.name] = player

            elif mode == 4:
                editting = False

        return players

    def observe_items(self):
        while True:
            dec = input('Do you want to inspect a specific item? (y/n)\n')
            if dec != 'y' or dec != 'yes':
                return 0

            item = self.get_item()
            if not item:
                return 0
            printf(item)


    def get_item(self):
        while True:
            item_id = input('Specify the item: \n')
            if item_id == 'exit':
                return False
            if item_id in self.inventory.equippables:
                return item_id
            else:
                item_list = [name for name in self.inventory.equippables.keys()]
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
            dec = input('What do you want to do?\nView [0] --- Equip [1] --- Strip [2] --- Use [3] --- Exit [4]\n')
            try:
                mode = int(dec)
                break
            except:
                printf('Your decision was not understood. Use the numbers associated.')

        return mode