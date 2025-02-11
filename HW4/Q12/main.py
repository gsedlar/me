"""
Gabrielle Sedlar
HW4 Q12
February 10, 2025

Task:  In a similar vein to question 11, we actually do want to treat these Pokemon as special! 
Instead of removing the special characters, we actually just want to clean this data up. 
Instead of seeing a pokemon as special-charmander we actually want to see it as 
Special Charmander. We similarly want to see all other (normal) members of the 
dataset in a similar case (i.e. charmander -> Charmander). Finish cleaning this 
dataset up and then print the dataframe to q12.out. 
"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

#replace hyphen with a space and capitalize the first letter of every word (title case)
pokeDF['identifier'] = pokeDF['identifier'].str.replace('-', ' ').str.title()

#save dataframe to output file
file = open('q12.out','w')
file.write(str(pokeDF))
file.close()