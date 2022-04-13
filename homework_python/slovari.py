#Коллекция в Python — программный объект (переменная-контейнер), хранящая набор значений одного или различных типов, позволяющий обращаться к этим значениям.

# Словарь (dict) - неупорядоченная коллекция произвольных объектов с доступом по ключу.
# dict - изменяемый объект: в любой момент можно изменить значение ключа
# Ключом не может быть изменяемый тип данных (пр.: списки)                   
                    
                    
                    # Создание словаря

#a = ['moscow', 'peter', 'pen']
#d = {
    #'moscow': 495,
    #'peter': 812,
    #'pen': 8412
#}
#print(d)


                    # Создание словаря (второй способ); при условии, что ключ - строка

#a = [['moscow', 495], ['peter', 812], ['pen', 8412]] # вложенный список
#r = dict(moscow=495, peter=812, pen=8412)
#t = dict (a)
#print(t)


                    # Метод fromkeys, создание пустого словаря
#a = [['moscow', 495], ['peter', 812], ['pen', 8412]]
#r = dict(moscow=495, peter=812, pen=8412)
#t = dict (a)
#q = dict.fromkeys (['a', 'b', 'c'], 100) # 100 - присвоенное значение
#print(q)
#v = {} 
#print(v, type(v))


                    # Добавление элемента в словарь
#d = {
#1 : 45,
#'hello': 'two',
#3 : [1, 2, 3]
#}
#d[4] = 'four'
#print(d)


                    # Несколько значений в одном ключе
#person = {}
#s = "zenkova ekaterina sochi pizdec 5 4 3 4 4 5"
#s = s.split ()
#person ['lastname'] = s[0]
#person ['firstname'] = s[1]
#person ['city'] = s[2]
#person ['college'] = s[3]
#person ['marks'] = []
#for i in s [4:]:
#    person ['marks'].append(int(i))
#print(person)


                    # Удаление элемента из словаря
#d = {
#1 : 45,
#'hello': 'two',3 : [1, 2, 3]
#}
#del d[1]
#print(d)


                    # Длина словаря, проверка наличия ключа в словаре
#d = {
#1 : 45,
#'hello': 'two',3 : [1, 2, 3]
#}
#print(len(d))
#print(1 in d, 5 in d, 7 not in d)


                    # Элементы списка, индекс с 0 (!)
#a = ['1', '2', '3'] - 0, 1 , 2


                    # Добавление элемента, использование условия
#a = ['moscow', 'peter', 'pen']
#d = {
    #'moscow': 495,
    #'peter': 812,
    #'pen': 8412
#}
#if 1 in d:
    #print(d[1])
#else:
    #d[5] = 'five'
#print(d)


                    # Вызов словаря, чистка словаря
#for i in d:
    #print(i, d[i])
#d.clear()


                    # Возврат значения ключа
#print(d)
#print(d.get(5, 'no such key'))


                    # Возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None)
#print(d)
#print(d.setdefault(6, 'six'))
#print(d)

#print(d.items())
#for p in d.items():
    #print(p) # Вывод всех пар в виде кортежей

#for key in d.keys():
    #print(key, d[key]) 

#print(d.pop('pen')) # Удаляет ключ и возвращает значение
#print(d.popitem()) # Удаляет и возвращает случайную пару (ключ, значение)
#print(d.keys()) # Возвращает ключи в словаре


def p (str, b):
    k = 0
    a = str
    for i in range(len(a)):
        if a[i] == b:
            k += 1
    return(k)


print(p('aaa', 'a'))
                