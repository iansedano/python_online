'''
Complete the task in section 12.4 - Variable-length argument tuples - (p. 118).

Write a function called sumall that takes any number of int arguments
and returns their sum.

'''
def sumall(*args):
    _sum = 0
    for i in args:
        _sum = _sum + i
    print(_sum)

sumall(324,324,54,356,754,34)
