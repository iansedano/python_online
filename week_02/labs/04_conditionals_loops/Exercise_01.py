'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

def is_even():
    print('write a whole number between 1 and 1,000,000,000 but don\'t use commas')
    usr_num = int(input())
    while usr_num > 1000000000 and usr_num < 1:
        print('your number is not a whole number between 1 and 1,000,000,000 - try a different number')
        usr_num = int(input())
    if (usr_num % 2) == 0:
        print('your number is even')
    else:
        print('your number is odd')

