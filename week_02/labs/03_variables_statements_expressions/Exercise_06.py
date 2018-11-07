'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''

distance = 12
seconds = (30 * 60) + 30
hour = (seconds / 60 ) / 60
coef = 1 / hour
miles = distance / 1.6
miles_per_hour = coef * miles
print(miles_per_hour)

