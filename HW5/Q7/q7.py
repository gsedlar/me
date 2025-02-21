"""
Gabrielle Sedlar
HW5 Q7
February 19, 2025

Task: Using the appropriate datasets, create a list of all mythical and legendary pokemon. Write this 
dataframe to a file called q7.out 

"""

import pandas as pd

pspec = pd.read_csv('../data/pokemon_species.csv')

#create a dataframe with all mythical, another with all legendary
myth = pspec[pspec['is_mythical'] == 1]
leg = pspec[pspec['is_legendary'] == 1]

#combine both datasets
ml = pd.concat([myth,leg])

#write to q7.out
file = open('q7.out','w')
file.write(str(ml))
file.close()

