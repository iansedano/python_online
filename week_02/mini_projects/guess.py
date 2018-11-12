'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''

import random

solved = False
guess_me = random.randint(1, 100)

print('I\'m thinking of a number between 1 and 100 \nGuess which!')
guess = int(input())

while solved == False:
    print('guess again!')
    guess = int(input())
    if guess == guess_me:
        solved = True

print('that\'s the one!')




