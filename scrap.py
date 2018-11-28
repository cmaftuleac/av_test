#!/usr/bin/env python2.7
import urllib2
from BeautifulSoup import BeautifulSoup
import csv 

metals = ['gold','silver']

url = "https://www.investing.com/commodities/%s-historical-data"

for metal in metals:
    write_to = open('%s.csv' % metal, 'wb')
    writer = csv.writer(write_to, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    req = urllib2.Request(url % metal, headers={'User-Agent' : "Beautiful Soup"})
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find('table', id='curr_table')
    for row in table.findAll('tr')[1:]:
        cells = row.findAll('td')
        p = [cell['data-real-value'].replace(',','') for cell in cells[:2]]
        print p
        writer.writerow(p)
    write_to.close()

