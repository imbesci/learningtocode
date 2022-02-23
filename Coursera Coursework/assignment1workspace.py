def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2-time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    time_1hours=time_1/3600
    time_2hours=time_2/3600
    return time_2hours-time_1hours


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    hourstoseocnds=hours*3600
    mintoseconds= minutes*60
    totalseconds=hourstomin+mintoseconds+seconds
    return totalseconds/3600



def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24



### Write your get_hours function definition here:
def get_hours(time_in_seconds):
    '''(float, int)->int
    Return the current hour past midnight when given the parameter time past midnight in seconds'''
    currenthour= time_in_seconds//3600
    return currenthour



### Write your get_minutes function definition here:
def get_minutes(time_in_seconds):
    '''(float, int)->int
    Return the current minute of the current hour when given the parameter time past midnight in seconds'''
    cumminutes = time_in_seconds//60
    currentminute = cumminutes%60
    return currentminute



### Write your get_seconds function definition here:
def get_seconds(time_in_seconds):
    '''(float, int)-> int
    Return the current second of the current minute when given the cumulative time past midnight in seconds'''
    removeminutes = time_in_seconds%60
    return removeminutes

