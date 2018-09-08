'''
Print out every prime number between 1 and 100.

'''

# check for tricks:
# - http://www.counton.org/explorer/primes/checking-if-a-number-is-prime/
# - http://planetmath.org/howtofindwhetheragivennumberisprimeornot
primes_below_100 = [2, 3, 5, 7]

for num in range(1, 101):
    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0):
        pass
    else:
        print(num)


# another solution using a nested loop structure:
for number in range(2, 100):
    is_prime = True  # adding a flag to keep track of the state of the number
    for i in range(2, number):
        # if it is divisible by any number, it's not a prime
        if number % i == 0:
            is_prime = False
            break  # exit the inner loop - one divisibility is enough!
    # if the inner loop's conditional didn't catch on any instance, the is_prime
    # flag remains 'True' and we know we've got a prime at hand!
    if is_prime:
        print(number)
        
