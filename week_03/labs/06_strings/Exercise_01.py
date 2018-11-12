'''
You might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

Demonstrate below:
- strip
- replace
- find

Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html


Exercise 8.2. There is a string method called count that is similar to the function in Section 8.7.
Read the documentation of this method and write an invocation that counts the number of a’s in
'banana'.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

'''

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
