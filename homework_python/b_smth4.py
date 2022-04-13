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
print (initials(name))