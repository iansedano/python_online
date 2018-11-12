'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

counter = 10
my_list = []

while counter > 0:
    print('type a number')
    my_number = int(input())
    my_list.append(my_number)
    counter = counter - 1

print(my_list)
