#! /usr/bin/python

import requests
import os
import os.path
import argparse
import time

admitere_url_fmt ='http://www.admitere.edu.ro/{year}/staticRepI/j/{county}/cina/page_{page_num}.html'
bac_url_fmt = 'http://bacalaureat.edu.ro/{year}/rapoarte/{county}/rezultate/alfabetic/page_{page_num}.html'

file_fmt = '{exam}-{year}-{county}-{page_num}.html'

counties = ('AB', 'AG', 'AR', 'B', 'BC', 'BH', 'BN', 'BR', 'BT', 'BV', 'BZ',
'CJ', 'CL', 'CS', 'CT', 'CV', 'DB', 'DJ', 'GJ', 'GL', 'GR', 'HD', 'HR', 'IF',
'IL', 'IS', 'MH', 'MM', 'MS', 'NT', 'OT', 'PH', 'SB', 'SJ', 'SM', 'SV', 'TL',
'TM', 'TR', 'VL', 'VN', 'VS')

valid_exams = ('admitere', 'bacalaureat')


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--exam', help='admitere/bacalaureat', required=True)
    parser.add_argument('--year', help='year to scrape data from',
            required=True)
    parser.add_argument('--county', help='county to scrape data for',
            required=True)

    args = parser.parse_args()

    if args.county not in counties:
        print '{0} is not a county code'.format(args.county)

    if args.exam not in valid_exams:
        print '{0} is not a valid exam name'.format(args.exam)

    # TODO: validate year


    # Download result pages
    url_fmt = None
    if args.exam == 'admitere':
        url_fmt = admitere_url_fmt
    else:
        url_fmt = bac_url_fmt

    previous_status = 200
    page_num = 1

    while previous_status == 200:
        print '[{0}] - page {1}'.format(args.county, page_num), 

        start_time = time.clock()

        url = url_fmt.format(exam=args.exam, year=args.year, county=args.county, page_num=page_num)
        filename = file_fmt.format(exam=args.exam, year=args.year, county=args.county, page_num=page_num)

        if not os.path.isfile(filename):
            r = requests.get(url)
            f = open(filename, 'w')

            f.write(r.text.encode('utf8'))

            print "({0})".format(r.status_code),
            previous_status = r.status_code

            if r.status_code != 200:
                os.remove(filename)

        else:
            print "(already downloaded)",

        end_time = time.clock()
        print " - {0}s".format(end_time - start_time)

        page_num += 1



