'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''
_file = open('words.txt', 'r')

#print(_file.read())
#print(repr(_file.read(100)))

for line in _file:
    if len(line) > 20:
        print(line, end = '')

_file.close()
