'''
Apply a Cesar cipher of 7 to the 'secret' variable.

p.s.: http://www.montypython.net/scripts/dentist.php

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
abc = 'abcdefghijklmnopqrstuvwxyz'
length = len(secret)

for x in range(0, length):
    char = secret[x]
    if char == ' ':
        print(' ', end='')
    else:
        letter = int(abc.find(char))
        cesar = letter - 7
        newchar = abc[cesar]
        print(newchar, end= '')


