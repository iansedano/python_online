'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

def cost_of_trip():
    print('how many miles will you be travelling?')
    miles = int(input())
    print('how many mpg does your vehicle do?')
    mpg = int(input())
    print('what is the price per gallon of fuel?')
    price = int(input())
    cost = (miles / mpg) * price
    print("the cost of your trip will be " + str(cost) + "$");

