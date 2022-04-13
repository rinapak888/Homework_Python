# Множество (set) - неупорядоченная коллекция уникальных элементов (отсутствуют повторяющиеся значения)

#Создание множества
#a = {1, 2, 3, 1, 2, 3, 4, 5, 6, 7} # не содержится дублей
#b = {'n', 'nn', 'n', 'nnn'}
#print(a, type(a))
#print(b)


#Создание множества из строки
#c = set('brokenmyheart') # множество - это неупорядоченная коллекция
#print(c)


#Создание множества из списка
#d = set([1, 2, 3, 4, 5, 6, 7, 1])
#print(d)


#Создание множества с помощью range
#e = set(range(5))
#print(e)


#Пустое множество
#f = set()
#print(f, type(f))


#Множество из вложенного списка создать нельзя; только объекты неизмен. типа (!), списки - измен.


#Исключение дублей из списка
#a = [1, 2, 3, 1, 2, 3]
#a = list(set(a))
#print(a)


#Добавление элемента
#a = {1, 2, 3, 1, 2, 3, 4, 5}
#a.add(9)

#a.update([5,6,7])
#a.update(range(5,100))
#print(a)


#Удаление элемента
#a = {1, 2, 3, 1, 2, 3, 4, 5}
#a.discard(4)
#print(a)

#a = {1, 2, 3, 1, 2, 3, 4, 5}
#a.remove(4)
#print(a)


#Пустое множество
#a = {1, 2, 3, 1, 2, 3, 4, 5}
#print(a)
#a.clear()
#print(a)


#print(len(a))
#print(4 in a, 7 not in a)


#Пересечение множеств
#a = {1,2,3}
#b = {3,4,5}
#print(a & b)
#a &=b
#print(a,b)


#a = {1,2,3}
#b = {3,4,1,5}
#a.intersection_update(b) # изменение списка a
#print(a, b)


#Объединение множеств
#print(a | b) # + print(a.union(b)) 


#Множества равны, если все эл-ты м-ва a принадлежат м-ву b и наоборот
#print(a == b)


#Нельзя обратиться по индексу (!)


#a = input()
#b = set()
#while a != '':
    #s = a.split()
    #b.update(s) # добавление эл-в + их вывод внутри цикла
    #print(b)
    #a = input()

print([f'Квадрат числа {i} равен {i**2}' for i in range(int(input())+1)], sep='\n')




