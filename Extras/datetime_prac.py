import datetime
import pytz

# tday = datetime.date.today()  #todays current date
# tdelta = datetime.timedelta(days = 7) #this is a change in time in days =7,just the length of 7 days


# print(tday - tdelta) #this shows the date 7 days ago

# #date2 = date1 + timedelta
# #timedelta = date1 + date2

# bday = datetime.date(2021, 9, 13)
# till_bday = bday - tday
# print(till_bday.total_seconds()) #prints the total number of seconds til bday date of this year


# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)

# t = datetime.datetime(2016, 7, 26, 12, 30, 45,100000) #can in put date (year, month, day) and time (hours, minutes, seconds, miliseconds)
# print(t.year)
# tdelta = datetime.timedelta(days = 7)
# print(t + tdelta)



# dt_today= datetime.datetime.today() #returns local date time with local timezone of none
# dt_now= datetime.datetime.now() #you can pass in a timezone here
# dt_utcnow= datetime.datetime.utcnow() #current UTC time, but tzinfo (timezone info is none)



# print(dt_today)
# print(dt_now)
# print(dt_utcnow)


# # timezone aware datetime using UTC
# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo = pytz.UTC)
# print(dt)
# dt_now= datetime.datetime.now(tz = pytz.UTC)
# print(dt_now)
# dt_utcnow= datetime.datetime.utcnow().replace(tzinfo= pytz.UTC)
# print(dt_utcnow)

# dt_est = dt_now.astimezone(pytz.timezone('US/Eastern'))
# print(dt_est)


# dt_est = datetime.datetime.now() #get naive unlocalized time
# est_tz = pytz.timezone('US/Eastern') #store the US/Eastern timeozne as a var
# dt_est = est_tz.localize(dt_est) #localize the time to a specific timezone (EST)
# dt_pac = dt_est.astimezone(pytz.timezone('US/Pacific')) #convert localized timezone to PST
# print(dt_est)
# print(dt_pac)

dt_est = datetime.datetime.now(tz = pytz.timezone('US/Eastern'))

# print(dt_est.isoformat()) #some international standard format
# print(dt_est.strftime('%B %d, %Y')) #strftime (datetime -> str) in the format you want


# dt_str = 'September 13, 2016'
# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y') #strptime (str-> datetime). 2nd var tells what inputs you gave it
# print(dt)