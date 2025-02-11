"""
Gabrielle Sedlar
HW4 Q5
February 9, 2025

Task:   Building on problem 4, allow a user to provide some set of letters. Find all pokemon 
beginning with this input and then return the one with the highest strength. If multiple 
pokemon are returned, you should return them in alphabetical order. Write the results of 
data to q5.out.
    
"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

pokeList = []

#get dataframe with pokemon that start with inputed set of letters
letters = input('Enter the beginning letter(s) of the pokemon youd like: ')
DF = pokeDF[pokeDF["identifier"].str.startswith(letters)] 


strength = 0
strongestList = []

for i,r in DF.iterrows(): #gets largest strength
    if r['base_experience'] > strength:
        strength = r['base_experience']

#adds each pokemon with the highest strength to a list
for i,r in DF.iterrows(): #not combined with other for loop so that the strength is gotten first, then the list is made
    if r['base_experience'] == strength:
        strongestList.append(r['identifier'])

strongestList.sort(reverse=True) #sorts list in reverse alphabetical order

file = open('q5.out','w')
file.write(str(strongestList)) #adds list to the output file
file.close()  

