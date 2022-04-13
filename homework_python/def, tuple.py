#n = int(input())
#a = n//100
#b = n//10%10
#c = n%10
#d = a//10
#e = a%10
#print(d, e, b, c)

#def print_s(n): # n - параметр функции, def - объявляет функцию
    #print(n * 2)
#print_s(2)

#def max(x,y):
    #if x > y:
        #return x
    #else:
        #return y # функция return останавливает исполнение программы
#x = input('Число 1:')
#y = input('Число 2:')
#print(max(x,y))


#a = {i ** 2 for i in range(10)}
#print(type(a))
#print(a)

#a = set('hello')
#b = frozenset('bye')
#a.add (1) # b не подойдет, поскольку является frozenset (неизменяемым множеством)
#print(a, b)


# Кортежи (tuple)
#a = (1,2,3,5)
#print(a[0:2]) # диапазон от 0 до 2

#a = (1,2,3,5)
#print(a[-1])

#u = ('Alla', 27, True)
#n, a, admin = u
#print(n) 


#def to_dict(l):
    #return {element: element for element in l}
#print(to_dict('work')) # каждый элемент списка является и ключом, и значением (?)

#my_dict = {'first_one': 'we can do it'}
#def biggest_dict(**kwargs):
    #my_dict.update(**kwargs) # позволяет обновить данные словаря или дополнить их
#biggest_dict(a=1, b=2, c=3, d=4)
#print(my_dict)

#def printThese(a,b,c=None):
   #print(a, "is stored in a")
   #print(b, "is stored in b")
   #print(c, "is stored in c")
#printThese(1,2)

#from collections import Counter
#def count_it(sequence):
    #return dict(Counter([int(num) for num in sequence]).most_common(3))

    