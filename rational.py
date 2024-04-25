import numpy as np

class RationalNumber:
    def __init__(self, p=0, q=1):
        d = np.gcd(p,q)
        p = (p * np.sign(q))/d
        q = abs(q)/d
        self.p = p
        self.q = q
    def __float__(self):
        return float(self.p/self.q)
    def __str__(self):
        return f'{self.p}/{self.q}'
    def __add__(self, other):
        
            p = self.p*other.q+other.p*self.q
            q = self.p*other.q
            return RationalNumber(p,q)
    def __iadd__(self):
        pass