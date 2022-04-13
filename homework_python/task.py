<<<<<<< HEAD
from random import choice
import string

def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result
=======
from random import choice
import string

def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result
>>>>>>> 4884fe8a9a4c3ab1696cf586480f2b62e2299855
print (create(2))