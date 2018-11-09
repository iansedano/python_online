'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

pop = 380123456
year = ((365 * 60) * 60 )* 60
deaths = year / 12
births = year / 6
immig = year / 40

new_pop = pop + (3 * (deaths + births + immig))

print(new_pop)
