import peewee

db = peewee.SqliteDatabase('examstats.db')

class Admitere(peewee.Model):
    year = peewee.TextField()

    name = peewee.TextField()
    county = peewee.TextField()
    school = peewee.TextField()
    admission_average = peewee.DoubleField()
    tsu = peewee.DoubleField()

    graduation_average = peewee.DoubleField()

    romanian_grade = peewee.DoubleField()
    maths_grade = peewee.DoubleField()

    option_3 = peewee.TextField()
    option_3_grade = peewee.DoubleField()

    maternal_language = peewee.TextField()
    maternal_language_grade = peewee.TextField()

    accepted_highschool = peewee.TextField()
    specialization = peewee.TextField()

    class Meta:
        database = db


