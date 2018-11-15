'''
This exercise pertains to the so-called Birthday Paradox,
which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox

If there are 23 students in your class, what are the chances that two
of you have the same birthday? You can estimate this probability by
generating random samples of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in
the random module.

Source: http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec128

Solution: http://thinkpython2.com/code/birthday.py

'''

import random
random_bdays = []

def sample_b():
    random_bdays = []
    for b in range(0,23):
        random_bdays.append(random.randint(1, 366))
    same_bdays = []
    diff_bdays = []
    for b in random_bdays:
        _count = random_bdays.count(b)
        if _count > 1:
            if b not in same_bdays:
                same_bdays.append(b)
        else:
            if b not in diff_bdays:
                diff_bdays.append(b)
    return(len(same_bdays))

def list_of_prob(sample_size):
    i = sample_size
    _list = []
    while i > 0:
        sample_size = 0
        _sample = 0
        while _sample < 1:
            _sample = sample_b()
            sample_size += 1
        _list.append(_sample / sample_size)
        i -= 1
    return(_list)

def list_avg(list_to_avg):
    _sum = 0
    for i in list_to_avg:
        _sum = _sum + i
    average = len(list_to_avg) / _sum
    return(average)

print(list_avg(list_of_prob(10000)))





