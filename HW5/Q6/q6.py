"""
Gabrielle Sedlar
HW5 Q6
February 19, 2025

Task:  Using the appropriate datasets, find what the most common secondary type of pokemon that 
exists is. Write the results out to q6.out showing the name and the number of that type.  

"""

import pandas as pd


p = pd.read_csv('../data/pokemon_types.csv')
ty = pd.read_csv('../data/types.csv')

df = p.merge(ty,how='left',left_on='type_id',right_on='id') #merge both datasets

#get rid of any non-secondary types
for i,r in df.iterrows():
    if r['slot'] != 2:
        df = df.drop(i)

#find the secondary type with the most pokemon, and the count of that type
result = df.groupby('identifier')['identifier'].count().sort_values(ascending=False).head(1)

#print results to q6.out
file = open('q6.out','w')
file.write(str(result))
file.close()
