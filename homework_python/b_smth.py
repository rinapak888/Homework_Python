a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if 1 <= a <= 8 and 1 <= b <= 8:
    if a == b == 1:
        if a1 == 2 and b1 == 1 or a1 == 2 and b1 == 2 or a1 == 1 and b1 == 2:
            print('YES')
        else: print('NO')
    elif a == 8 and b == 1:
        if a1 == 7 and b1 == 1 or a1 == 7 and b1 == 2 or a1 == 8 and b1 == 2:
            print('YES')
        else: print('NO')
    elif a == 1 and b == 8:
        if a1 == 1 and b1 == 7 or a1 == 2 and b1 == 8 or a1 == 2 and b1 == 7:
            print('YES')
        else: print('NO')            
    elif a == b == 8:
        if a1 == 7 and b1 == 8 or a1 == 8 and b1 == 7 or a1 == b1 == 7:
            print('YES')
        else: print('NO')
    elif 2 <= a <= 7 and b == 1:
        if a1 == a - 1 and b1 == b or a1 == a + 1 and b1 == b or a1 == a - 1 and b1 == b + 1 or a1 == a and b1 == b + 1 or a1 == a + 1 and b1 == b + 1:
            print('YES')
        else: print('NO')
    elif a == 1 and 2 <= b <= 7:
        if a1 == a and b1 == b - 1 or a1 == a and b1 == b + 1 or a1 == a + 1 and b1 == b - 1 or a1 == a + 1 and b1 == b or a1 == a + 1 and b1 == b + 1:
            print('YES')
        else: print('NO')
    elif 2 <= a <= 7 and b == 8:
        if a1 == a - 1 and b1 == b or a1 == a + 1 and b1 == b or a1 == a - 1 and b1 == b - 1 or a1 == a and b1 == b - 1 or a1 == a + 1 and b1 == b - 1:
            print('YES')
        else: print('NO')
    elif a == 8 and 2 <= b <= 7:
        if a1 == a and b1 == b - 1 or a1 == a and b1 == b + 1 or a1 == a - 1 and b1 == b - 1 or a1 == a - 1 and b1 == b or a1 == a - 1 and b1 == b + 1:
            print('YES')
        else: print('NO')    
    elif 2 <= a <= 7 and 2 <= b <= 7:
        if a - 1 <= a1 <= a + 1 and b - 1 <= b1 <= b + 1:
            print('YES')
        else: print('NO')                
else:
    print('NO')

    