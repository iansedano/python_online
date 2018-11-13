'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''
list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]



def compare_lists(list_x, list_y):
    list_same = []
    list_diff = []
    i = 0
    j = 0
    while i < len(list_x):
        j = 0
        while j < len(list_two):
            if list_x[i] == list_y[j]:
                if list_x[i] not in list_same:
                    list_same.append(list_x[i])
            else:
                if list_x[i] not in list_diff:
                    list_diff.append(list_x[i])
            j += 1
        i += 1
    print(list_same)
    print(list_diff)

compare_lists(list_one, list_two)
