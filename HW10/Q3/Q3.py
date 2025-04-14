"""
HW10 Q3
Gabrielle Sedlar
April 14, 2025
"""


import sqlite3


db_path = 'Q3.db'

select_poke= "SELECT * FROM pokemon WHERE id>10 AND id<=35" #between 10-35, including 35

try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(select_poke)
    rows = c.fetchall()
    print(rows) #returning the rows to the user
    conn.commit()
    conn.close()
    
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)




