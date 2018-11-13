'''
Write a function called middle that takes a list and returns a new
list that contains all but the first and last elements.

For example:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

Source: http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec128

Solution: http://thinkpython2.com/code/list_exercises.py

'''

def middle(_list):
    _middle = []
    i = 0
    while i < len(_list):
        if 0 < i < (len(_list) - 1):
            _middle.append(_list[i])
        i += 1
    print(_middle)

t = [1, 2, 3, 4]
middle(t)
