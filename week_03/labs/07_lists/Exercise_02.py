'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

i = 0
j = 0

list_same = []
list_diff = []

while i < len(list_one):
    j = 0
    while j < len(list_two):
        if list_one[i] == list_two[j]:
            list_same.append(list_one[i])

