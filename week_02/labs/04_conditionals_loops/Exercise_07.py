'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''

x = 1000
y = 0
total = 0

while x > 1:
    y = y + 1
    if y == 3:
        total = total + x
        y = 0
    else:
        y = y + 1
    x = x - 1

print(total)
