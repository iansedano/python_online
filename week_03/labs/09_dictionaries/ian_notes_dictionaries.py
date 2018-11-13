eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp) # order of entries unpredictable

# print(eng2sp['four'])  gives error
print(len(eng2sp))

print('\n')

print('one' in eng2sp)
print('uno' in eng2sp)

print('\n')

# to see values
_values = eng2sp.values()
print('uno' in _values)

# 'in' operator uses differente algorithms for lists and dicts
