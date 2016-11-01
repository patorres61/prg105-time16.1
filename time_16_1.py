# Phyllis Torres
# 16.1 Time Assignment
# Due 11/10/2016

# create a time class

class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

    def __init__(self):
        pass


def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

time = Time()
time.hour = 10
time.minute = 30
time.second = 5

print ('The hour field is 10, the minute field is 30, and the second field is 5. \n')
print ('This input will be reformatted to a conventional format: \n')

print_time(time)

