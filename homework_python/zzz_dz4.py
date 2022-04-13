import os
import subprocess #запуск процессов; запуск приложения и передача аргументов 

def search():
    command = input('Нужная вам команда: ')
    com = subprocess.getoutput('cat ~/.bash_history | grep {0}'.format(command)).split('\n')[::-1] #cat - отображение содержимого файла, grep - поиск инф-и в файле, переменная, где записана команда; с последней по первую команду - срез
    print(com) 
    for i in com:
        if command in i:
            print(i)
            action = input('Что сделать? Выполнить команду - y, пропустить - n, выйти из программы - q: ')
            if action == 'y':
                os.system(i) #выполняет команду в терминале; вернуть код состояния выполнения команды и вывести результат выполнения команды
                break
            elif action== 'q':
                exit() 
        
search()