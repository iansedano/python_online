'''
Define a class which has at least two methods:
get_string: to get a string from console input
print_string: to print the string in upper case.
Also include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Adapted from source: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

'''

class SimpleStrings:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


my_str = SimpleStrings()
my_str.get_string()
my_str.print_string()
