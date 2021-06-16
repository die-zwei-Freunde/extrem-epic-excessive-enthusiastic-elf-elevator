"""Game loop - heart of the project"""

import start_setup as setup
import classes.world.worldclass as wld
from logger import printf
import testing.input_testing as test
import classes.inventory.manager as inv
import classes.action.manager as act


class Game_loop:
    def __init__(self):
        self.players, self.quest = setup.start_setup()
        self.flag = ''
        self.world = wld.World(self.quest)
        self.inventory = inv.InventoryManager(self.players)

    def run(self):
        endpoint = False
        while not endpoint:
            story = self.world.next(self.flag)
            printf(story['prestring'])
            action = act.ActionManager(story['action'])
            self.players, loot, alive = action.start(self.players)
            for l in loot:
                self.inventory.add_item(l)
            if not alive:
                printf('you dead, no game anymore')
                endpoint = True
                continue

            decision = story['decision']
            keys = [key for key in decision.keys()]
            printf(story['poststring'])
            endpoint = story['Endpoint']

            if not endpoint:
                self.players = self.inventory.manage(self.players)
                for key in keys:
                    printf(key, ':', decision[key])
                inp = input(f'What will you choose? {keys} ')
                inp = test.test_decision(inp, keys)
                self.flag = self.flag + inp