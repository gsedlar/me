"""
HW10 Q2
Gabrielle Sedlar
April 14, 2025
"""


import sqlite3
import pandas as pd

db_path = 'Q2.db'
p = pd.read_csv('../data/pokemon.csv')

create_pokemon = "CREATE TABLE IF NOT EXISTS pokemon(id integer PRIMARY KEY, name text NOT NULL UNIQUE, height integer, weight integer, base_experience integer)"

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(create_pokemon)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)
    
    
conn = sqlite3.connect(db_path) 
p.to_sql(name='pokemon', con=conn, if_exists='replace', index=False)


