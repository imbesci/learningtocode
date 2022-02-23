def report_status(scheduled_time, estimated_time):
    '''(float, float)-> string
    Return the flight status(on time, early, delayed) when inputting the scheduled time and estimated time

    Pre-condition: 0.0 <= scheduled_time < 24.0
    Pre-condition: 0.0 <= arrival_time < 24.0
    >>> report_status(14.3, 14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
