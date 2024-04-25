import numpy as np

class velocity:
    def __init__(self, v=0):
        if -1<=v<=1:
            self.beta = v
        else:
            raise ValueError('velocity input must be a number between -1 and 1')
    def gamma(self):
        return 1/np.sqrt(1 - self.beta**2)
    def __add__(self, other):
        return velocity((self.beta+other.beta)/(1+self.beta*other.beta))
    def __iadd__(self, other):
        self.bet=(self.beta+other.beta)/(1+self.beta*other.beta)
    def __str__(self):
        return str(self.beta)
    
v1 = velocity(1)
v2 = velocity(0.2)
v3 = velocity(0.7)

print(v1+v3)