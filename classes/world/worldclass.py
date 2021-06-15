"""World class"""

import json


class World:
    def __init__(self, quest):
        with open('classes/world/story/' + quest + '/config.json', 'r') as fp:
            self.config = json.load(fp)
        self.fp = self.config['fp'][:14] + 'story/' + self.config['fp'][14:]

    def next(self, flag):
        file = self.config[flag]
        file = self.fp + file + '.json'

        with open(file, 'r') as fp:
            story = json.load(fp)
        return story