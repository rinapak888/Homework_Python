import random
import sqlite3

connection = sqlite3.connect("victorina.db") #Способ создания БД в Python с помощью SQLite. Создадим файл .db (стандартный способ управления базой SQLite).
cursor = connection.cursor() #Сей метод получения курсора принимает один необязательный параметр factory. Если он указан, это должен быть вызываемый объект, возвращающий объект cursor или его подкласс.

for j in range(1, 6): #Включительно 5 уровней.
    table = "select * from level" + str(j) + " where id =" + str(random.randint(1, 2)) 

    for i in range(len(cursor.execute(table).fetchall()[0]) - 2):
        print(cursor.execute(table).fetchall()[0][i + 1]) #Метод cursor.execute() выполняет команду SQL. fetchall() возвращает число записей в виде упорядоченного списка.
    try: #Для обработки исключений используется конструкция try - except. Блок try - выполняем инструкцию, которая может породить исключение, в блоке except мы их перехватываем.
        ans = int(input('Валяй: '))
    except:
        print("Такого ответа не предусмотрено")
        exit()
    if ans > 0 and ans < 5:
        if cursor.execute(table).fetchall()[0][6] == cursor.execute(table).fetchall()[0][ans + 1]:
            print("Ответ верный :D")
        else:
            print("Ответ неверный :(")
            exit()
    else:
        print("Такого ответа нет!!!")
        exit()
print("Уиииии!!!")
connection.commit() #Если все операции в транзакции завершены, используйте connection.commit() для сохранения изменений в БД. Если метод не использовать, то все эффекты взаимодействия с данными не будут применены.
cursor.close() #Метод cursor.close() закрывает курсор сейчас, а не всякий раз, когда вызывается метод __del__. С этого момента курсор будет непригодным для использования. Возникнет исключение ProgrammingError, если с закрытом курсором будет предпринята какая-либо операция.
connection.close()
