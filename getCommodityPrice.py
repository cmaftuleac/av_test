import csv
import numpy
import sys
import time
import datetime

start, finish, metal = sys.argv[1:]

start_ts = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d").timetuple())
finish_ts = time.mktime(datetime.datetime.strptime(finish, "%Y-%m-%d").timetuple())

reader = csv.reader(open('gold.csv'))
prices = []
for row in reader:
    if int(row[0])>start_ts and int(row[0])<finish_ts:
        prices.append(float(row[1]))
print metal, numpy.mean(prices), numpy.var(prices)
