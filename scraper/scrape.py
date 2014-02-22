#! /usr/bin/python

import requests
import os.path
import time

url_fmt ='http://www.admitere.edu.ro/2013/staticRepI/j/{county}/cina/page_{page_num}.html'
file_fmt = '{county}-{page_num}.html'

counties = ('AB', 'AG', 'AR', 'B', 'BC', 'BH', 'BN', 'BR', 'BT', 'BV', 'BZ',
'CJ', 'CL', 'CS', 'CT', 'CV', 'DB', 'DJ', 'GJ', 'GL', 'GR', 'HD', 'HR', 'IF',
'IL', 'IS', 'MH', 'MM', 'MS', 'NT', 'OT', 'PH', 'SB', 'SJ', 'SM', 'SV', 'TL',
'TM', 'TR', 'VL', 'VN', 'VS')


if __name__ == '__main__':

    for county in counties:
        previous_status = 200
        page_num = 1

        while previous_status == 200:
            print '[{0}] - page {1}'.format(county, page_num), 
            # print "{0} out of {1}".format(page_num, NUM_PAGES), 

            start_time = time.clock()

            url = url_fmt.format(county=county, page_num=page_num)
            filename = file_fmt.format(county=county, page_num=page_num)

            if not os.path.isfile(filename):
                r = requests.get(url)
                f = open(filename, 'w')

                f.write(r.text.encode('utf8'))

                print "({0})".format(r.status_code),
                previous_status = r.status_code

            else:
                print "(already downloaded)",

            end_time = time.clock()
            print " - {0}s".format(end_time - start_time)

            page_num += 1

