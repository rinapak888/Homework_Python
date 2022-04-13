class Washing:
    def __init__(self, water):
        self.water = water #объявление переменной внутри класса

    def wash(self, item):
        print(f"I'm washing {item} with {self.water} l of water")

class Driving:
    def drive(self, a, b):
        print(f"I'm driving from {a} in {b}")

class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color

class Driving_Machine(Driving, Machine):
    pass

class Washing_Machine(Washing, Machine):
    def init(self, water, brand, price, year, color):
        super(Washing_Machine, self).__init__(water)
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color
    

        print(f'{self.speed}, {self.modes}, {self.temp}, {self.time}')

