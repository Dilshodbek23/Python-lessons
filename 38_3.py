# Python Standard Libraries

# A function that returns how many years, months, days have passed from my birthday to the present day (conditionally leap years were not taken into account).

import datetime as dt


now = dt.datetime.now()
birthday = dt.datetime(1985, 11, 23)
years = now.year - birthday.year
months = now.month - birthday.month
days = now.day - birthday.day
if months<0:
    years -= 1
    months += 12
if days<0 and months % 2 == 1:
    months -= 1
    days += 30 
elif days<0 and months % 2 == 1:
    months -= 1
    days += 31    
print(f"{years} years {months} months {days} days have passed since my birthday.")
