"""
HW10 Q10
Gabrielle Sedlar
April 14, 2025
"""


import sqlite3
import pandas as pd


db_path = 'Q10.db'

#making pokemon table in sql, based on data in pokemon.csv, with proper parameters
p = pd.read_csv('../data/pokemon.csv')
p.rename(columns={'identifier': 'name'}, inplace=True) #renaming identifier name just to avoid confusion
p.drop(columns=['species_id', 'order', 'is_default'], inplace=True) #dropping extra columns to avoid errors later

create_pokemon = "CREATE TABLE IF NOT EXISTS pokemon(id integer PRIMARY KEY, name text NOT NULL UNIQUE, height integer CHECK(height>1), weight integer CHECK(weight<1000), base_experience integer)"
    #checks that height and weight are in the correct ranges
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(create_pokemon)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    print('unable to connect to database', e)
    
    
conn = sqlite3.connect(db_path) 
p_filtered = p[(p['height'] > 1) & (p['weight'] < 1000)] #only pokemon with values in correct ranges are added
p_filtered.to_sql(name='pokemon', con=conn, if_exists='append', index=False)
conn.close()



#asking user for a new entry
id = int(input("Enter Pokémon ID: "))
name = input("Enter Pokémon name: ")
height = int(input("Enter Pokémon height (>1): "))
weight = int(input("Enter Pokémon weight (<1000): "))
base_experience = int(input("Enter base experience: "))

insert_pokemon = "INSERT INTO pokemon (id, name, height, weight, base_experience) VALUES (?, ?, ?, ?, ?)"

try:
    conn = sqlite3.connect(db_path)
    c=conn.cursor()
    c.execute(insert_pokemon, (id, name, height, weight, base_experience))
    conn.commit()
    conn.close()
    
    print(name.title() + ' inserted successfully!')
    
except sqlite3.IntegrityError as e: #if the data is inputed wrong, if there's a duplicate, or if the values aren't in the correct ranges
        print("Failed to insert pokemon. ",e)
        if "UNIQUE constraint failed" in str(e): #if the id or name is repeated, because they're set to primary and unique, an error is given
            print("This ID or name already exists.")
        elif "CHECK constraint failed" in str(e): #if the height or weight isn't in the correct range, an error will be given
            print("Height must be > 1 and weight must be < 1000.")
except ValueError:
    print("Invalid input. Please enter values for ID, name, height, weight, and base experience.")
except Exception as e: #if all else fails, this prints
    print("An unexpected error occurred: ",e)














