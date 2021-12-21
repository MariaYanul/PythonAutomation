from typing import Callable
from datetime import datetime
import datetime

# Task #3


# dates = []
start_day = datetime.date(2021, 12, 1)
end_day = datetime.date(2021, 12, 31)
# while start_day <= end_day:
#     dates.append(datetime.datetime.strftime(start_day, '%Y-%m-%d'))
#     start_day += datetime.timedelta(days=1)
# print(dates)

for i in range(start_day, end_day):
    print(i)

#
# days = [start_day + datetime.timedelta(days=x) for x in range((end_day-start_day).days + 1)]
# for day in days:
#     print(day.strftime('%Y%m%d'))
# newls = [int(i) for i in days]
# print(newls)

# def days_in_month():
#     month = datetime.month()
#     for even_day in month:
#         if even_day % 2 == 0:
#             print(even_day)
#     return
# days_in_month(12)




# Task #1

# row = range(1, 1000)
#
# def decor(function: Callable):
#     def decoratee():
#         start_time = datetime.now()
#         function()
#         end_time = datetime.now()
#         print('Duration: {}'.format(end_time - start_time))
#     return decoratee

# @decor
# def nums():
#     for item in row:
#         print(item**2)
#     return
#
# nums()

# Task #2

# ls = [1, 2, 3, 4, 5]
#
# def testFunc():
#     for i in range(len(ls), 15):
#         ls.append(i + 1)
#         if len(ls) >= 10:
#             raise Exception('List can contain only 10 elements')
#
# try:
#     testFunc()
# except Exception as err:
#     print(err)
# finally:
#     print('ok')
# print(ls)


# for i in ls:
#     ls.append()
#     i =+1
# if len(ls) >= 10:
#     raise Exception("Sorry, no numbers below zero")


