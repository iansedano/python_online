'''

Write a function called cumsum that takes a list of numbers and returns
the cumu- lative sum; that is, a new list where the ith element is the
sum of the first i + 1 elements from the original list.

For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

Source: http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec128

Solution: http://thinkpython2.com/code/list_exercises.py

'''

def cumsum(_list):
    cum_list = []
    cum_sum = 0
    for _number in _list:
        cum_sum = cum_sum + _number
        cum_list.append(cum_sum)
    print(cum_list)

t = [1, 2, 3]
cumsum(t)
