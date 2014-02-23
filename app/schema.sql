drop table if exists admitere_2009;

create table admitere_2009(
    name text,
    county text,
    school text,
    admission_average real,
    tsu real,
    graduation_average real,
    romanian real,
    maths real,
    option_3 text,
    option_3_grade real,
    maternal_language text,
    maternal_language_grade real,
    accepted_highschool text,
    specialization text
);

.separator ',,,,'
.import ../parsers/admitere-2009.csv admitere_2009
