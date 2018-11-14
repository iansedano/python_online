'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

super_dict = {}

for e in dict_1:
    super_dict[e] = dict_1[e]

for e in dict_2:
    super_dict[e] = dict_2[e]

for e in dict_3:
    super_dict[e] = dict_3[e]

print(super_dict)

for e in super_dict:
    print(str(e) + ':' + str(super_dict[e]))

