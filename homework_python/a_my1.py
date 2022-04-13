a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = c-a
if e<0:
    e=e*(-1)
f = d-b
if f<0:
    f=f*(-1)
g = e-f
if g<0:
    g=g*(-1)
if g ==1:
    print("YES")
else:
    print("NO")

