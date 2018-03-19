#!/opt/local/bin/python

import datetime as dt

def add(*numbers):
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    return total

print(add(1,2,3,4,5,6))

def record_time( message, time = dt.datetime.now() ):
    print("{:}, time: {:}".format(message, time))

record_time("It is the morning")
record_time("it is the morning", "Feb 22nd, 1998")
