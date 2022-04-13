from random import choice
import string

def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result
print (create(2))