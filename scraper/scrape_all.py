#!/usr/bin/python

import subprocess

counties = ('AB', 'AG', 'AR', 'B', 'BC', 'BH', 'BN', 'BR', 'BT', 'BV', 'BZ',
'CJ', 'CL', 'CS', 'CT', 'CV', 'DB', 'DJ', 'GJ', 'GL', 'GR', 'HD', 'HR', 'IF',
'IL', 'IS', 'MH', 'MM', 'MS', 'NT', 'OT', 'PH', 'SB', 'SJ', 'SM', 'SV', 'TL',
'TM', 'TR', 'VL', 'VN', 'VS')

valid_exams = ('admitere', 'bacalaureat')

bac_years = ('2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
'2012', '2013')
admitere_years = ('2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
'2012', '2013')

cmd_fmt = 'python scrape.py --exam {exam} --year {year} --county {county}'

if __name__ == '__main__':
    for exam in valid_exams:
        exam_years = None
        if exam == 'admitere':
            exam_years = admitere_years
        else:
            exam_years = bac_years

        for year in exam_years:
            for county in counties:
                subprocess.call(cmd_fmt.format(exam=exam, year=year,
                    county=county).split())
