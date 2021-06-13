"""World class"""

import json


class World:
    def __init__(self):
        with open('classes/world/config1.json', 'r') as fp:
            self.config = json.load(fp)
        self.fp = self.config['fp']

    def next(self, flag):
        file = self.config[flag]
        file = self.fp + file + '.json'

        with open(file, 'r') as fp:
            story = json.load(fp)
        return story