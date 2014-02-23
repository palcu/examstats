#! /usr/bin/python

import storage
import csv

storage.db.connect()
storage.Admitere.create_table()

with open('../parsers/admitere-2009.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        s = storage.Admitere(year='2009', name=row[0], county=row[1],
                school=row[2], admission_average=row[3], tsu=row[4],
                graduation_average=row[5], romanian_grade=row[6],
                maths_grade=row[7], option_3=row[8], option_3_grade=row[9],
                maternal_language=row[10], maternal_language_grade=row[11],
                accepted_highschool=row[12], specialization=row[13])

        s.save()

