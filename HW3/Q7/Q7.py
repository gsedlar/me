"""
Gabrielle Sedlar
HW3 Q7
February 1, 2025

Task:  Using poke.csv, prompt the user for the name of a pokemon. If it exists within the 
dataset return the DataFrame containing data for only that pokemon. If it doesn't exist, 
instead return the message This pokemon does not exist. 

"""

import pandas as pd

df = pd.read_csv('../Data/poke.csv')

pokemon = input('Please enter the name of a pokemon: ').lower().strip() #asks user for pokemon, fixes formatting

if(df.identifier.isin([pokemon]).any() == True): #if the pokemon's name exists in the identifier list
    print(df[df.identifier.isin([pokemon])]) #prints the row of information for that pokemon
else:
    print('This pokemon does not exist.') #if the pokemon does not exist, prints a statement
