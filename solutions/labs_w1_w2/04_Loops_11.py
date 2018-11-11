'''
Apply a Cesar cipher of 7 to the 'secret' variable.

p.s.: http://www.montypython.net/scripts/dentist.php

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

abc = list('abcdefghijklmnopqrstuvwxyz')
encrypted = ""

for char in secret:
    if char.lower() in abc:
        for i, c in enumerate(abc):
            if c == char.lower():
                new_char = abc[(i+cipher) % len(abc)]
                encrypted += new_char
    else:
        encrypted += char

print(encrypted)
