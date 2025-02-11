"""
Gabrielle Sedlar
HW4 Q11
February 10, 2025

Task:  Using the poke dataset, write the following code. This particular dataset has a number 
of special characters in it, specifically in their names! You can tell they're special 
because they themselves have a special character in their names, a -. We want a list 
with just the name themselves. For instance, we may have a record for 
special-charmander and we would want to convert that to pikachu. Return a list of 
just identifiers with just the names of these pokemon and remove any duplicates. Write 
the dataframe out to q11.out.

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')


#anytime there is a - in the identifier column, only the first part (before the hyphen) is kept
pokeDF['identifier'] = pokeDF['identifier'].str.split('-', n=1).str[0]

#delete any duplicate identifiers
pokeDF = pokeDF.drop_duplicates(subset='identifier')

file = open('q11.out','w')
file.write(str(pokeDF['identifier'].tolist()))
file.close()