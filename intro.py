from my_module import *
import datetime
import os
import antigravity

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)
# print(sys.path)

today = datetime.date.today()
print(today)

print(os.__file__)
print(antigravity.geohash)