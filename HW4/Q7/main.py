"""
Gabrielle Sedlar
HW4 Q7
February 10, 2025

Task:  Write a program that utilizes the poke dataset. Return a dataframe that sets pokemon 
names in uppercase if their height is greater than 100, sets pokemon names in titlecase 
for those between 50 and 60, and sets pokemon names in lowercase for those less than 
50. After making the necessary changes, write this dataframe to a file called q7.out. 

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

for i,r in pokeDF.iterrows(): #program looks at one row at a time
    if r['height'] > 100:
        pokeDF.at[i, 'identifier'] = r['identifier'].upper() #if the height is over 100, the identifier column changes to all uppercase
    elif (r['height'] > 50) & (r['height'] < 60):
        pokeDF.at[i, 'identifier'] = r['identifier'].title() #if the height is between 50 and 60, the identifier column changes to tilecase
    elif r['height'] < 50:
        pokeDF.at[i,'identifier'] = r['identifier'].lower() #if the height is below 50, the identifier column changes to lowercase
    
#write dataframe to q7.out
file = open('q7.out','w')
file.write(str(pokeDF))
file.close()