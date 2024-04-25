import numpy as np

class  circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def pole(self):
        return (self.r**2)*np.pi
    def urosnij(self, n):
        print('sto lat!')
        self.x = self.x + n
    def intersection(self, kolo):
        odl = np.sqrt((self.x-kolo.x)**2 + (self.y-kolo.y)**2)
        suma = self.r + kolo.r
        roz = abs(self.r - kolo.r)
        if odl == 0 and roz == 0:
            return np.inf
        elif (odl == suma) or (odl == roz):
            return 1
        elif (odl > suma) or (odl < roz):
            return 0
        elif odl < suma:
            return 2
        else: return 'idk'


kolko1 = circle(3,4,2)
kolko2 = circle(0,0,3)

print(kolko1.intersection(kolko2))