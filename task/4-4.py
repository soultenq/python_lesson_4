#!/Users/ten/local/venv3/bin/python
import re
from datetime import datetime
from functools import reduce

file = open('log', mode='r')

array=list()

for line in file:
    line=line.rstrip()
    times=line.split(' ')
    logtime = datetime.strptime(str(times[0]) + ' ' + str(times[1]), '%Y-%m-%d %H:%M:%S,%f')
    array.append(logtime)

max = reduce(lambda a, b: a if a > b else b, array)
print(max)
