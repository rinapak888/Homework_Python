import random


Penza = {"population": 12000, "territory" : 10000}
Sochi = {"population": 13000, "territory" : 11000}
print ("Penza", Penza, "Sochi", Sochi)

def create_region (names, cities):
    d = {}
    for name, city in zip (names,cities) :
        d [name] = city
        return d
def create_region (names,cities):
    return {name: city for name, city in zip(names, cities)}
cities = [create_region(random (50))for _ in range (50)]
names = []






