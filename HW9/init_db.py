"""
HW9
Gabrielle Sedlar
April 7, 2025
"""



import sqlite3

db_path = 'data/school.db'

create_student = 'CREATE TABLE IF NOT EXISTS STUDENT (id integer, name text, email text, phone integer, year integer, status text);'
create_teacher = 'CREATE TABLE IF NOT EXISTS STUDENT (id integer, name text, email text, phone integer);'
create_class = 'CREATE TABLE IF NOT EXISTS STUDENT (id integer, name text, department text not null, teacherID integer);'

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(create_student)
    c.execute(create_teacher)
    c.execute(create_class)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)