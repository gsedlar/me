"""
HW10 Q1
Gabrielle Sedlar
April 14, 2025
"""


import sqlite3

db_path = 'Q1.db'

create_pokemon = "CREATE TABLE IF NOT EXISTS pokemon(id integer PRIMARY KEY, name text NOT NULL UNIQUE, height integer, weight integer, base_experience integer)"

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(create_pokemon)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)


