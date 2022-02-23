def timeCalc(start, duration):
    ampm = start.split(':')[1].split(' ')[1]
    currentTime = [int(start.split(':')[0]), int(start.split(':')[1].split(' ')[0])]
    addedTime = [int(duration.split(':')[0]), int(duration.split(':')[1])]
    if ampm == 'PM':
        currentTime[0] += 12
    newHour, newMin = str(currentTime[0] + addedTime[0]), str(currentTime[1] + addedTime[1]).zfill(2)
    if int(newMin)>59:
        newHour = str(int(newHour) + 1).zfill(2)
        if int(newMin) == 60:
            newMin = str(0).zfill(2)
        else:
            newMin = str(int(newMin) - 60).zfill(2)
    return [newHour, newMin]

def add_time(start, duration, day:str = 'na'):
    #CONST ARRAY LOOKUP FOR DAYS OF WEEK
    daysOfWeek = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    #CALCULATE NEW TIME
    newTime = timeCalc(start, duration)
    #RETURNS (Days Past, remaining current hour)
    expandedTime = divmod(int(newTime[0]), 24)
    #UPDATED VARS FOR FINAL STRING
    hour = expandedTime[1]
    daysLater = ''
    ampm = 'AM'
    #CHECK IF DAY CHANGES
    if expandedTime[0] == 0:
        pass
    elif expandedTime[0] == 1:
        daysLater = '(next day)'
    elif expandedTime[0] > 1:
        numStr = str(expandedTime[0])
        daysLater = f'({numStr} days later)'
    #CHECK IF TIME IN 24H SETTING IS PAST 12, AND COVERT TO 12H TIMEFRAME
    if (expandedTime[1]) == 0:
        hour = 12
    if (expandedTime[1] >= 12):
        ampm = 'PM'
        if (expandedTime[1] >= 13):
            hour = expandedTime[1] - 12
            newTime = [hour, newTime[1]]
    #ADDING DAY FORMATTING
    if (day != 'na'):
        dayStrip = day.strip().lower()
        currentIndex = daysOfWeek.index(dayStrip) + 1
        newDay = ((currentIndex + expandedTime[0]) % 7) - 1
        return f'{hour}:{newTime[1]} {ampm}, {daysOfWeek[newDay].capitalize()} {daysLater}'.rstrip()
    
    else:
        return f'{hour}:{newTime[1]} {ampm} {daysLater}'.rstrip()
