#!/usr/bin/python

import subprocess

counties = ('AB', 'AG', 'AR', 'B', 'BC', 'BH', 'BN', 'BR', 'BT', 'BV', 'BZ',
'CJ', 'CL', 'CS', 'CT', 'CV', 'DB', 'DJ', 'GJ', 'GL', 'GR', 'HD', 'HR', 'IF',
'IL', 'IS', 'MH', 'MM', 'MS', 'NT', 'OT', 'PH', 'SB', 'SJ', 'SM', 'SV', 'TL',
'TM', 'TR', 'VL', 'VN', 'VS')

valid_exams = ('admitere', 'bacalaureat')

admitere_years = ('2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
'2012', '2013')

cmd_fmt = './parse_admitere.py csv \'admitere-{year}-{county}-*.html\' >\
 admitere-{year}-{county}.csv'

if __name__ == '__main__':
        # OVERRIDE
        exam_years = ('2013', '2014')

        for year in exam_years:
            for county in counties:
                print "echo \"{0}\"".format(cmd_fmt.format(year=year,
                    county=county))
                print cmd_fmt.format(year=year, county=county)
