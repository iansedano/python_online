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
'''

string = '  hakunah matata  '

strip_string = string.strip()
print(strip_string)

rep_string = string.replace('k', 'kk')
print(rep_string)

find_string = string.find('t',5,15)
print(find_string)
