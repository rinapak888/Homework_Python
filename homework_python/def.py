#def fff(n): # def объявляет функцию, n - параметр функции
    #for i in range(0, n+1, 2):
        #print(i)

#fff(100) 


#def g():
    #name = 'Ann'
    #age = 27
    #admin = False
    #return name, age, admin
#u = g()
#print(u[0])
#print(u[1])
#print(u[2])


#u = ('Ann', 27, False)
#i = 0
#while i < len(u):
    #print(u[i])
    #i = i + 1

#for i in range(26):
    #print(chr(ord('A') + i))

#a, b = int(input()), int(input())
#for i in range(a, b+1):
    #print(chr(i), end=' ')

a = int(input())
total = 0
j = 1
b = 0
for i in range(1, a + 1):
    j = 1
    total += 1
    if total != 1:
        b = str(j)
        while j != total:
            j += 1
            b += str(j)
        while total != 1:
            total -= 1
            b += str(j)
        b = int(b) - 1
        print(b)
    else:
        print(1)

