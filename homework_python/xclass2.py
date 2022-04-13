class A:
    def shout(self):
        print('WTN')
    def say(self):
        print ('I am obj A')

class B:
    def yell(self):
        print('Eze')
    def say (self):
        print('I am obj A')

class C (A,B):
    pass 
C.shout()
C.yell()
C.say()


class exQuote:
    def __init__(self, quote):
        self.quote=quote
    def say(self):
        return self.quote + '!'

class exQuote:
    def __init__(self, quote):
        self.quote=quote
    def say(self):
        return self.quote + '?'

a=exQuote()
b=exQuote()
a.say
b.say



class counter:
    __current=0
    def __init__(self):
        self__current=0

c=counter()
print(c. __conter__current)

def __add(self): #защишещенные поля
    self. __current=1
c=counter()
c. __add()



c=counter()
for item in list:
    c.add()
    c.get_current()


class H:
#__h_name
#@property # метод как атрибут, возвращает защищен. поле

#class S(H):
    def init(self, age, name, country, study, num_parent):
        self.age=age
        self.name=name
        self.country=country
        self.study=study


def __eq__(self, s): #метод принимает сам объект
    return
    (self.name==s.name) and (self.age==s.age)


class dot:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __le__(self, other):
        if self.x == other.x:
            return self.y > other.y
        elif self.y == other.y:
            return self.x > other.x
        return false
    def __ye__(self, other):
        if self.x == other.x:
            return self.y < other.y
        elif self.y == other.y:
            return self.x < other.x
        return false

        

        










        