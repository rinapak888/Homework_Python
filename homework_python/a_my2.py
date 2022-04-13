#def sl(a, b, c=1):
    #D = {}
    #D = {a:'строка1'} 
    #D = {b:'строка2'} 
    #D = {c:''}
    #return D
#print(sl('первое', 'второе'))

a = int(input())
b = int(input())
for i in range(a, b+1):
    c = 0
    for j in range(1, i+1):
        if i % j == 0:
            c += 1
            if c == 2:
                print(i)




