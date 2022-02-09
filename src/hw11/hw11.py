from functools import reduce
from operator import itemgetter

print('Filter')
numbers = range(-30, 10)
less_than_zero = list(filter(lambda x: x < 0, numbers))
print(less_than_zero)


print('Map')
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


print('Reduce')
result = reduce((lambda x, y: x * y), items)
print(result)


print('Sorted')
for_sorting = [{'name': 'Andrii', 'age': 39}, {'name': 'Sophia', 'age': 10}, {'name': 'Svitlana', 'age': 23},
                     {'name': 'Kiril', 'age': 28}, {'name': 'Edmund', 'age': 57}, {'name': 'Oleksa', 'age': 42}]
newlist = sorted(for_sorting, key=itemgetter('name'))
print(newlist)
