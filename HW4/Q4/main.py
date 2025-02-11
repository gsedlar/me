"""
Gabrielle Sedlar
HW4 Q4
February 9, 2025

Task:  Write a program that utilizes the poke dataset. Load this data in and find the strongest 
pokemon that starts with the letter p. If multiple pokemon have the same strength, you 
should return them in reverse alphabetical order. Write the results out to a file called 
q4.out 

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

PDF = pokeDF[pokeDF["identifier"].str.startswith('p')] #new dataframe with only pokemon whose names start with p

strength = 0
strongestList = []


for i,r in PDF.iterrows(): #gets largest strength
    if r['base_experience'] > strength:
        strength = r['base_experience']

#adds each pokemon with the highest strength to a list
for i,r in PDF.iterrows(): #not combined with other for loop so that the strength is gotten first, then the list is made
    if r['base_experience'] == strength:
        strongestList.append(r['identifier'])

strongestList.sort(reverse=True) #sorts list in reverse alphabetical order

file = open('q4.out','w')
file.write(str(strongestList)) #adds list to the output file
file.close()  
        