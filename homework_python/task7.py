<<<<<<< HEAD
from random import randint
 
n = 10
a = []
for i in range(n):
    a.append(randint(0, 12))


print(a)
for i in range(n-1):
    for k in range(n-i-1):
        if a[k] > a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]

=======
from random import randint
 
n = 88
a = []
for i in range(n):
    a.append(randint(0, 1000))
print(a)
 
for i in range(n-1):
    for k in range(n-i-1):
        if a[k] > a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]
 
>>>>>>> 4884fe8a9a4c3ab1696cf586480f2b62e2299855
print(a)