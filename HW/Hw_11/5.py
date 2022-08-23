from datetime import timedelta, date


def date_gen(start_date: date, end_of_date: date, number):
    print("enter two date and one number of weekend")
    list_of_days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time = timedelta(days=1)
    while start_date <= end_of_date:
        if start_date.strftime("%A") == list_of_days[number]:
            yield start_date.strftime("%Y-%m-%d")
        start_date += time


var = date_gen(date(2021, 10, 11), date(2022, 10, 11), 0)

for i in var:
    print(next(var))
