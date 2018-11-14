'''
Starting from Exercise 11.3 from the textbook (p. 106):

Modify print_hist to print the keys and their values in alphabetical order
without using the sorted() function.

def print_hist(h):
    for c in h:
        print(c, h[c])

'''
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

def print_hist(h):
    for c in h:
        print(c,h[c])

h = histogram('parrot')
print_hist(h)
