"""World class"""

import json


class World():
    def __init__(self):
        with open('classes/world/config.json', 'r') as fp:
            self.config = json.load(fp)

    def next(self, flag):
        file = self.config[flag]
        file = 'classes/world/story/' + file + '.json'

        with open(file, 'r') as fp:
            story = json.load(fp)
        return story