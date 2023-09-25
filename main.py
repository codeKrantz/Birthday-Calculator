#import date and time
from datetime import datetime

#getting basic information
print("What Year where you born?")
Year = int(input())

print("What Month were you born?")
Month = input().lower()
if Month == "test":
    Month = 1

print("What Day were you born?")
Day = int(input())

#calculating date
Birthday = datetime(Year, Month, Day)
print(Birthday)