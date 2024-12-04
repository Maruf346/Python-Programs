from datetime import datetime, date, time, timedelta

year1 = int(input("Enter year1: "))
month1 = int(input("Enter month1: "))
date1 = int(input("Enter date1: "))

year2 = int(input("Enter year2: "))
month2 = int(input("Enter month2: "))
date2 = int(input("Enter date2: "))

dt1 = date(year1, month1, date1)
dt2 = date(year2, month2, date2)

delta = dt2 - dt1

print("Difference in days: ", delta.days)