<<<<<<< HEAD
name = 'Zenkova Ekaterina Alex'

def initials (s) :
    length = len (s)
    result = []
    start = 0
    for i in range (len(s)) :
        if s[i] == ' ':
           result.append (s[start:i])
           start = i + 1
        if i == len (s) - 1 :
            result.append(s[start:i])
    return result[0] + '' + result [1] [0:1] + '.' + result [2] [0:1]
=======
name = 'Zenkova Ekaterina Alex'

def initials (s) :
    length = len (s)
    result = []
    start = 0
    for i in range (len(s)) :
        if s[i] == ' ':
           result.append (s[start:i])
           start = i + 1
        if i == len (s) - 1 :
            result.append(s[start:i])
    return result[0] + '' + result [1] [0:1] + '.' + result [2] [0:1]
>>>>>>> 4884fe8a9a4c3ab1696cf586480f2b62e2299855
print (initials(name))