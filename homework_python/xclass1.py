class Bakery:
    milk = 0,5
    def __init__(self, eggs, flour):
        pass
        self.eggs=eggs
        self.flour=flour


class Cookie(Bakery): # Наследование класса
    def __init__(self, eggs, flour, cinna):
        super().__init__(eggs, )
        self.cinna=cinna
    def __def__(self, eggs, flour):
        super().__del__()
        print() 
    

class Car:
  steering_wheel = True 
  def init(self, color, ergine, wheels):
    self.color = color
    self. ergine = ergine
    self. wheels = wheels


car1 = Car('red', 'v8', 6) # Инициализация объекта
print(car1.color) # Выведет цвет
def drive(self, speed, a, b, list_of_load):
    time = (a.place-b.place)/speed
    for item in list_of_load:
        item.place = b
    return time


class Ferrari(Car):
    def __init__(self, color, engine, wheels):
        if not engine == 'v8' or engine == 'v12':
            print ('error')
            raise Exception
            return
        else:
            super().__init__( color, engine, wheels)
        self.manfcr = Ferrari

car2 = Ferrari('red', 'v8', 4)





class Person:
    def __init__(self, age, name,country):
        self.age = age
        self.name = name
        self.country = country
    def say (self):
        print (f'{self.age} I am {self.name} {self.country}')
        per_1 = Person (18, 'Ivan', 'Russia')
        print(per_1.age)
        per_1.say()

class Student(Person):
    def __init__(self, age, name, country, study):
        super().__init__(age, name, country)
        self.study=study
    def say (self):
        super().say()
        print (f'{self.study}')

            



        