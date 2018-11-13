'''

Write a function called nested_sum that takes a list of lists of
integers and adds up the elements from all of the nested lists.
For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21

Source: http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec128

Solution: http://thinkpython2.com/code/list_exercises.py

'''



def nested_sum(l_of_l):
    all_sum = 0
    for sublist in l_of_l:
        for num in sublist:
            all_sum = all_sum + num
    print(all_sum)


t = [[1, 2], [3], [4, 5, 6]]

nested_sum(t)
