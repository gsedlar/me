"""
HW10 Q4
Gabrielle Sedlar
April 14, 2025
"""


import sqlite3
import pandas as pd

db_path = 'Q4.db'
t = pd.read_csv('../data/pokemon_types.csv')
n = pd.read_csv('../data/pokemon_type_names.csv')
filtered_n = n[(n['local_language_id'] == 9)][['type_id', 'name']] #filtering the pokemon_types_names file to only include where local languge is 9, also only including name and id
filtered_n = filtered_n.rename(columns={'type_id': 'id'}) #renaming type_id column to id

r = "CREATE TABLE IF NOT EXISTS pokemon_types(id integer PRIMARY KEY, name text)"

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(r)
    filtered_n.to_sql('pokemon_types', conn, if_exists='replace', index=False) #adding the editted df into the existing table, pokemon_types
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)
    

