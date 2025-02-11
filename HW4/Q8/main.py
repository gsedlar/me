"""
Gabrielle Sedlar
HW4 Q8
February 10, 2025

Task:  Utilizing the poke, poke_types and types datasets, remove all fire pokemon from the 
poke dataset. Print just the number of pokemon remaining to a file called q8.out. 

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')
ptyDF = pd.read_csv('../Data/pokemon_types.csv')
tyDF = pd.read_csv('../Data/types.csv')

pokeIndeces = []

for i,r in tyDF.iterrows(): #cycling through rows in types.csv until fire, then taking that id
    if r['identifier'] == 'fire':
        fire_id = r['id']

for i,r in ptyDF.iterrows(): #finding all pokemon_id's that are fire type
    if r['type_id'] == fire_id:
        pokeIndeces.append(r['pokemon_id'])

for n in pokeIndeces: #for each pokemon, if it's fire type, it's deleted from the dataframe. if not, it's kept.
    pokeDF = pokeDF[pokeDF['id'] != n] #because it's saved back into the original dataframe, the loop can work by going one index at a time

file = open('q8.out','w')
file.write(str(pokeDF))
file.close()



