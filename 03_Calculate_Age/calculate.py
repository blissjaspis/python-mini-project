import time
from calendar import isleap

def calculateDaysInMonthWithLeap(month, is_leap):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and is_leap:
        return 29
    elif month == 2 and not is_leap:
        return 28

days = 0
now = time.localtime(time.time())
name = str(input("Input your name : "))
checkAgeOrdays = int(input("Choose what number you want to calculate, 1=Age. 2=Days : "))

if checkAgeOrdays == 1:
    calculateYearBirth = int(input("Insert year of your birth : "))
    age = now.tm_year - calculateYearBirth
else:
    age = int(input("Insert your age right now: "))
    calculateYearBirth = now.tm_year - age

for r in range(calculateYearBirth, now.tm_year - 1):
    days += 366 if isleap(r) else 365

for m in range(1, now.tm_mon - 1):
    days += calculateDaysInMonthWithLeap(m, isleap(now.tm_year))

days += now.tm_mday
print(f"Hi {name}, your age right now is {age} years old, if we convert it you had live {days} days")