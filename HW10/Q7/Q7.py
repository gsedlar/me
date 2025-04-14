"""
HW10 Q7
Gabrielle Sedlar
April 14, 2025
"""

import sqlite3
import pandas as pd


db_path = 'Q7.db'

p = pd.read_csv('../data/pokemon.csv')
t = pd.read_csv('../data/pokemon_types.csv') #need to connect pokemon_id to type_id
n = pd.read_csv('../data/pokemon_type_names.csv')
filtered_n = n[(n['local_language_id'] == 9)][['type_id', 'name']] #still filtering based on english names

pt = p.merge(t,how='left',left_on='id',right_on='pokemon_id')
ptn = pt.merge(filtered_n,how='left',left_on='type_id',right_on='type_id') #all three df merged


try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    ptn.to_sql('pokemon_types', conn, if_exists='replace', index=False) #adding data into the pokemon_types table
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)

