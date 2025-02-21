"""
Gabrielle Sedlar
HW5 Q8
February 20, 2025

Task: Building from q7, create a dataset of all mythical and legendary pokemon. Create a new 
column for these pokemon called Strength that is based upon their base_experience multiplied 
by 5 added to the sum of their height and weight multiplied by 5. Return a dataframe with the 
strongest 5 of these creatures and write the dataframe to q8.out. Then draw a graph 
comparing these values. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

spec = pd.read_csv('../data/pokemon_species.csv')
p = pd.read_csv('../data/pokemon.csv')

pspec = p.merge(spec,how='left',left_on='identifier',right_on='identifier',suffixes=('_poke','_spec'))

#create a dataframe with all mythical, another with all legendary
myth = pspec[pspec['is_mythical'] == 1]
leg = pspec[pspec['is_legendary'] == 1]

#combine both datasets
ml = pd.concat([myth,leg])

#add strength column
pspec = pspec.assign(strength = lambda x: (x['base_experience'] * 5 + (x['weight'] + x['height']) * 5))

#get top 5 strongest pokemon
top5 = pspec.sort_values(by=['strength'],ascending=False).head(5)

#write to q8.out
file = open('q8.out','w')
file.write(str(top5))
file.close()

#draw/design graph with these values
b = sns.barplot(data=top5,x='identifier',y='strength',palette='bright')
plt.xlabel('Pokemon Name', fontsize=16)
plt.ylabel('Strength',fontsize=16)
plt.title('Comparing Strength of Mythical and Legendary Pokemon',fontsize=20,fontweight='bold') #italics is fontstyle
plt.tick_params(axis='both',which='major',labelsize=12)
plt.xticks(rotation=90)
