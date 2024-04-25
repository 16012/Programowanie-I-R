import numpy as np
from random import random

class person():
    MaxDistance = 1.0
    MaxIllDistance = 0.1
    def __init__(self, r, status):
        self.x = r[0]
        self.y = r[1]
        self.status = status
    def Move(self):
        if self.status in ('z','n'):
            krok = MaxDistance * random()
        else:
            krok = MaxIllDistance * random()
        ang = 2*np.pi*random()
        dx = krok*np.cos(ang)
        dy = krok*np.sin(ang)
        self.x += dx
        self.y += dy