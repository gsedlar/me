"""
Gabrielle Sedlar
HW4 Q3
February 9, 2025

Task:  Write a program utilizing the poke dataset. Load this dataset and find all pokemon with 
names beginning with vowels. Once found, write this dataframe out to a file called 
q3.out. 

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

#making a dataframe for each vowel (maybe there's a better way to do this, but idk)
ADF = pokeDF[pokeDF["identifier"].str.startswith('a')] 
EDF = pokeDF[pokeDF["identifier"].str.startswith('e')]
IDF = pokeDF[pokeDF["identifier"].str.startswith('i')]
ODF = pokeDF[pokeDF["identifier"].str.startswith('o')]
UDF = pokeDF[pokeDF["identifier"].str.startswith('u')]

#concatenating the new dataframe with all individual dfs
newDF = pd.concat([ADF,EDF,IDF,ODF,UDF])

#prints dataframe to a file called q3.out
file = open('q3.out','w')
file.write(str(newDF))
file.close()