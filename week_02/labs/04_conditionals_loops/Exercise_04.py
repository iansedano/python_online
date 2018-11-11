'''
Print out every prime number between 1 and 100.

'''

def is_prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for x in range(2, n):
            if n % x == 0:
                prime = False
    return(prime)

for num in range(1,101):
    if is_prime(num) == True:
        print(str(num) + '; ', end = '')
