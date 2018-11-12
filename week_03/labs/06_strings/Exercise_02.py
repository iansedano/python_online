'''
There is a string method called 'count' that is similar to the following
code:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

Read the documentation of the 'count' method and write an invocation that
counts the number of a’s in 'banana' that uses the in-built 'count'.

Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html#sec104


Exercise 8.3. A string slice can take a third index that speciﬁes the “step size”; that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1]generates a reversed string.
Use this idiom to write a one-line version of is_palindromefrom Exercise 6.3.

'''

def is_palindrome(word):
    if word == word[::-1]:
        print('you have a palindrome')
    else:
        print('this word is not a palindrome')

is_palindrome('hannah')
