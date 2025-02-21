"""
Gabrielle Sedlar
February 17, 2025
HW5 Q1

Task: Using the pokemon_species and generations datasets, create a single dataset. Write 
this new combined dataset to q1.out. Once you have a single dataset – get the following 
information and write the resulting dataframe in a csv format to q1.csv:
    - Pokemon name
    - Generation ID 
"""

import pandas as pd

ps = pd.read_csv('../data/pokemon_species.csv')
gen = pd.read_csv('../data/generations.csv')

#merge two dataframes
pg = ps.merge(gen,how='left',left_on='generation_id',right_on='id',suffixes=('_ps','_gen'))

#new dataframe with only the two columns
new_pg = pg[['identifier_ps','identifier_gen']]

#save combined dataset to q1.out
file = open('q1.out','w')
file.write(str(pg))
file.close()

#save dataframe with only two columns to q1.csv
file2 = open('q1.csv','w')
file2.write(str(new_pg))
file2.close()