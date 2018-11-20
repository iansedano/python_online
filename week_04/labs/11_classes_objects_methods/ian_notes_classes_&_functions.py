print('\n\n/////****CLASSES_AND_FUNCTIONS****////')

print('\n\n/////TIME////')

class Time:
    """ Represents the time of day

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_timex(t):
    print(str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))

print_timex(time)

def print_time(t):
    print('{}:{}:{}'.format(t.hour,t.minute,t.second))
print_time(time)


def time_in_hours(x):
    s_to_h = x.second / 60 / 60
    m_to_h = x.minute / 60
    t_in_h = x.hour + s_to_h + m_to_h
    return(int(t_in_h))

def is_after(t1,t2):
    return(time_in_hours(t1) > time_in_hours(t2))

ta = Time()
ta.hour = 12
ta.minute = 59
ta.second = 30

tb = Time()
tb.hour = 11
tb.minute = 59
tb.second = 30

print(is_after(ta,tb))


print('\n\n/////PURE FUNCTIONS////')

def add_time(t1, t2): #pure function because does not modify objects sent to it
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)

print('\n\n/////MODIFIERS////')


def increment(time, seconds):
    time.seconds += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

#///

def div_and_remainder(num, div): # this is divmod(num, div)
    divprod = num / div
    remainder = num % div
    clean_num = num - (num % div)
    clean_divprod = clean_num / div
    return (clean_divprod, remainder)

def seconds_to_hms(seconds_to_add):

    min_and_sec = div_and_remainder(seconds_to_add, 60)
    seconds = min_and_sec[1]
    minutes = min_and_sec[0]

    h_and_min = div_and_remainder(minutes, 60)
    minutes = h_and_min[1]
    hours = h_and_min[0]
    return(hours, seconds, minutes)

def time_to_seconds(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds



def increment(time,seconds):
    actual_time_in_seconds = time_to_seconds(time) + seconds
    hms = seconds_to_hms(actual_time_in_seconds)

    time.hour = hms[0]
    time.minute = hms[1]
    time.second = hms[2]

print_time(start)
increment(start,234187)
print_time(start)


