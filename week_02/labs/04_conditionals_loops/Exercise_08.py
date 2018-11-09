'''
Demonstrate the use of the "break" statement to exit a loop.

'''

print('type in a numer between 1 and 100 to sum all numbers from 1 to that number')
x = int(input())
total = 0

for y in range(1,100):
    if y == x:
        break
    else:
        total = total + y
