#import date and time
from datetime import datetime

#getting basic information
print("What Year where you born?")
Year = int(input())

print("What Month were you born?")
Month = input().lower()
if Month == "january":
    Month = 1
elif Month == "february":
    Month = 2
elif Month == "march":
    Month = 3
elif Month == "april":
    Month = 4
elif Month == "may":
    Month = 5
elif Month == "june":
    Month = 6
elif Month == "july":
    Month = 7
elif Month == "august":
    Month = 8
elif Month == "september":
    Month = 9
elif Month == "october":
    Month = 10
elif Month == "november":
    Month = 11
elif Month == "december":
    Month = 12

print("What Day were you born?")
Day = int(input())

#calculating date
Birthday = datetime(Year, Month, Day)
print("Your birthday is " + str(Birthday))

#calculating how long it has been since original birthday
time_Since = datetime.now() - Birthday
print("It has been:")
print(time_Since)
print("Since your original birthday")