"""Game loop - heart of the project"""

import start_setup as setup
import classes.world.worldclass as wld
from logger import printf
import testing.input_testing as test


class Game_loop:
    def __init__(self):
        self.players = setup.start_setup()
        self.flag = ''
        wld.World()

    def run(self):
        endpoint = False
        while not endpoint:
            story = wld.World().next(self.flag)
            printf(story['prestring'])
            action = story['action']
            decision = story['decision']
            keys = [key for key in decision.keys()]
            printf(story['poststring'])
            endpoint = story['Endpoint']

            if not endpoint:
                for key in keys:
                    printf(decision[key])
                inp = input(f'What will you choose? {keys} ')
                inp = test.test_decision(inp, keys)
                self.flag = self.flag + inp