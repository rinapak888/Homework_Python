class Engine:
    def init(self, a, power, volume, weight):
        self.a = a
        self.power = power
        self.volume = volume
        self.weight = weight

class Wheel:
    def init(self, weight, mfr, radins, g):
        self.weight = weight
        self.mfr = mfr
        self.radins = radins
        self.g = g
    

class Steering:
    def init(self, mfr, shape, q, weight):
        self.mfr = mfr
        self.shape = shape
        self.q = q
        self.weight = weight
        self.place = 'right' 
        if (mfr == 'ang' or mfr == 'jap'):
            print('good')

import typing
class Car:
    def __init__(self, eng: Engine, whs: list [Wheel], st: Steering):
        w_all = sum ([item.weight for item in [eng, st] extend (whs)])
        


        
    