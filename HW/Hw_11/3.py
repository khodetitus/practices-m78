from datetime import datetime
import jdatetime

date1 = str(input('Enter date(yyyy-mm-dd): '))
my_date1 = datetime.strptime(date1, "%Y-%m-%d")
print(my_date1)

date2 = str(input('Enter date(yyyy-mm-dd): '))
my_date2 = datetime.strptime(date2, "%Y-%m-%d")
print(my_date2)

print(
    f"from date : {my_date2} until the from date {my_date1}:{(my_date2 - my_date1).total_seconds()} A second has passed")

date11 = my_date1.year
date22 = my_date2.year
counter = 0
while date11 < date22:
    if date11 % 4 == 0 and date11 % 100 != 0:
        counter += 1
    if date11 % 100 == 0 and date11 % 400 == 0:
        counter += 1
    date11 += 1

print(f"You have {counter} leap years on these two dates")

if date11 >= date22:
    print("Check your year input again.")

counters: int = 0
for i in range(date11, date22):
    counters += 1

print(f"changes hour in between date :{counters * 2}")

print(jdatetime.date.fromgregorian(year=my_date1.year, month=my_date1.month, day=my_date1.day))
print(jdatetime.date.fromgregorian(year=my_date2.year, month=my_date2.month, day=my_date2.day))
