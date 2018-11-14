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

def histogram(s): # counts number of characters
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram('bronto  saurus'))

h = histogram('a')
print(h)
print(h.get('a', 0)) #get ('key', dafalut value)
print(h.get('b', 0))

'''As an exercise, use get to write histogram more concisely. You should be able to eliminate
the if statement. --- ??? '''

'''  NEED TO FINISH
def histogram2(s):
    d = dict()
    for c in s:

print(histogram2('bronto  saurus'))
'''

def print_hist(h):
    for c in h:
        print(c,h[c])

h = histogram('parrot')
print_hist(h)

print()

def print_hist_s(h):
    for c in sorted(h):
        print(c,h[c])

print_hist_s(h)


#lookup
#_value = _dict[_key]

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

print()

key = reverse_lookup(h, 2)
print(key)

#  key = reverse_lookup(h, 3) give lookuperror

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

inverse = invert_dict(h)
print(inverse)


known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(9))

