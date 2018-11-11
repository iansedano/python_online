'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

def ex05():
    print('type upper bound')
    upper = int(input()) + 1
    print('type lower bound')
    lower = int(input())
    x = lower
    rng = upper - lower
    all_sum = 0
    for x in range(lower, upper):
        all_sum = all_sum + x
    print(all_sum)
    print(all_sum / rng)
