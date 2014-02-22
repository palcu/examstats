#! /usr/bin/python

from bs4 import BeautifulSoup
import os
import os.path
import sys
import glob
import json
import csv

mapping = {
                1: 'name',
                2: 'county',
                3: 'school',
                4: 'admission_average',
                5: 'tsu',
                6: 'graduation_average',
                7: 'romanian',
                8: 'maths',
                9: 'option_3',
                10: 'option_3_grade',
                11: 'maternal_language',
                12: 'maternal_language_grade',
                13: 'accepted_highschool',
                14: 'specialization'
        }


field_delimiter = '\t'

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'no file wildcard specified'
        exit(1)

    file_wildcard = sys.argv[1]

    students = []
    files = glob.glob(os.path.join(os.getcwd(), file_wildcard))

    for file in files:
        soup = BeautifulSoup(open(file))

        table = soup.body.findAll('table')[3]
        student_rows = table.findAll('tr')

        for student_row in student_rows[1:]:
            student = {}
            for (k, v) in mapping.iteritems():
                student[v] = student_row.findAll('td')[k].text

            students.append(student)


    for student in students:
        for (k, v) in mapping.iteritems():
            print student[v], field_delimiter,
        print

