import numpy.random as nr
import numpy as np


class Die:
    def __init__(self, eyes=6):
        self.eyes = eyes

    def roll(self, luck=0):
        raise NotImplementedError('Implement your roll for your die.')


class D20(Die):
    def __init__(self):
        super().__init__(eyes=20)

    def roll(self, luck=0):
        sigma = 5
        mean = 10.5

        luck_factor = 0.5 * luck
        eye = nr.normal(mean + luck_factor, sigma)

        if eye <= 1:
            eye = 1
        elif eye >= self.eyes:
            eye = self.eyes

        return np.int(np.rint(eye))

