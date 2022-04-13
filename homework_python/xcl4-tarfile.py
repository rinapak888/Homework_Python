#ls -l | grep name

import tarfile 

#t = tarfile.open('archive.tar', 'w')
#t.add('1.txt')
#t.close()

t = tarfile.open('new.tar.gz','w|gz')
f = open('new.txt','w')
s = 'это тестовая строка'
for i in range(1000000):
    f.write(s+'\n')
    print(i)
t.add('new.txt')

#ls -l | grop new

#command = 'ls -l |grep new'
#os.system(command)

#t = tarfile.open('new.tar.gz', 'w|gz')
#создать архив - ('archive.tar.gz', 'w|gz') 
#добавить файл в архив - t.add('new.txt') 
#t.close()



