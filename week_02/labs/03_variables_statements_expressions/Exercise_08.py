'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''
def c_to_f():
    print('type in temp in C')
    c = input()
    c = int(c)
    f = c * 1.8 + 32
    print(str(c) + ' degrees celsius = ' + str(f) + ' degrees fahrenheit')
    return;
