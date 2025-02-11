"""
Gabrielle Sedlar
HW4 Q6
February 9, 2025

Task:  Write a program that utlizes the poke, poke_types and types datasets. You should 
prompt the user for a pokemon. Determine what type of pokemon this is (i.e. fire, water, 
etc.) and then print the count of all types of these pokemon, and the names of the 
strongest and weakest pokemon of this type. If the user provides a pokemon that does 
not exist, you should respond with "pokemon does not exist". Any/all of these outputs 
should be written to a file called q6.out.

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')
ptyDF = pd.read_csv('../Data/pokemon_types.csv')

file = open('q6.out','w')

pokemon = input('Please enter a pokemon: ')

#check if the pokemon exists
if pokeDF.identifier.isin([pokemon]).any() == False:
    file.write('This pokemon does not exist.')
    
else:  
    #initiate str variables for strongest and weakest pokemon
    strongest = 'nothing yet'
    weakest = 'nothing yet'
    
    #set max and min variables to values that will definitely be changed
    max_strength = 0
    min_strength = 999
    
    count = 0
    
    #get pokemon id
    poke_id = pokeDF.loc[pokeDF['identifier'] == pokemon, 'id'].iloc[0] 
    
    #get type id
    type_id = ptyDF.loc[ptyDF['pokemon_id'] == poke_id, 'type_id'].iloc[0]
    
    for i, r in ptyDF.iterrows(): #search rows in pokemon_types for all pokemon with that type
        if r['type_id'] == type_id:
            temp_id = r['pokemon_id'] #have to go back to pokemon data, use temp_id to store pokemon_id
            
            for i, r in pokeDF.iterrows(): #finds the correct pokemon and sees if it is strongest or weakest
                if r['id'] == temp_id:
                    
                    if (r['base_experience'] > max_strength):
                        max_strength = r['base_experience']
                        strongest = r['identifier']
                    if (r['base_experience'] < min_strength):
                        min_strength = r['base_experience']
                        weakest = r['identifier']
                    
            
            #if it's the correct type, it adds it to the count for later
            count += 1
    
    #write all necessary information to the output file    
    file.write('Total count of pokemon with the same type: ' + str(count) + '\n')
    file.write('The strongest pokemon of this type is ' + str(strongest) + '\n') 
    file.write('The weakest pokemon of this type is ' + str(weakest))

#close file regardless of what was written in it
file.close()
