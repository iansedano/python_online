'''
Complete the following Exercise:

Exercise 3.3.

Note: This exercise should be done using only the statements and other features we have learned so far.

1. Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

print('+', '-')

By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:

print('+', end=' ')
print('-')

The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

2. Write a function that draws a similar grid with four rows and four columns.


'''
first_row_sep = '+ - - - - +'
first_row = '|         |'
row_sep_add_column = ' - - - - +'
row_add_column = '         |'

def print_sep_row(c):
    print(first_row_sep, end = '')
    c2 = c - 1
    while c2 > 0:
        print(row_sep_add_column, end = '')
        c2 = c2 - 1
    print()

def print_row(c):
    x = 4
    while x > 0:
        print(first_row, end = '')
        c2 = c - 1
        while c2 > 0:
            print(row_add_column, end = '')
            c2 = c2 - 1
        print()
        x = x - 1

def print_table(c, r):
    print_sep_row(c)
    while r > 0:
        print_row(c)
        print_sep_row(c)
        r = r - 1

print_table(4,4)

