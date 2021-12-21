import datetime

dates = []
start_day = datetime.date(2021, 12, 1)
end_day = datetime.date(2021, 12, 31)
while start_day <= end_day:
    if start_day.day % 2 == 0:
        dates.append(datetime.datetime.strftime(start_day, '%Y-%m-%d'))
    start_day += datetime.timedelta(days=1)
print(dates)
