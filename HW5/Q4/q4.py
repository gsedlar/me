"""
Gabrielle Sedlar
HW5 Q4
February 18, 2025

Task:  Using the appropriate datasets, create a dataset that allows you to get a pokemons base 
experience and their primary color. Write this new dataset to q4.out. Grab a random selection 
of 10 of these pokemon and then draw a graph showing the name of the pokemon and their 
base_experience. The color for each bar should be set to what the primary color of that 
pokemon is. The x axis should be the name of the pokemon and the y axis should show the 
base_experience of the pokemon. Use appropriate labels and a title to allow the user to easily 
discover what your graph is visualizing. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


poke = pd.read_csv('../data/pokemon.csv')
pspec = pd.read_csv('../data/pokemon_species.csv')
cols = pd.read_csv('../data/pokemon_colors.csv')

#merge three data sets
merged = poke.merge(pspec,how='left',left_on='species_id',right_on='id',suffixes=('_poke','_spec'))
merged = merged.merge(cols,how='left',left_on='color_id',right_on='id')

#new dataframe with base experience, pokemon, and color, send to q4.out
df = merged[['identifier_poke','base_experience','identifier']]
file = open('q4.out','w')
file.write(str(df))
file.close()

sel = df.sample(10) #random 10 rows

cols = {} #colors empty dictionary

#fills the cols dictionary with the appropriate color for each pokemon
for i,r in sel.iterrows():
    cols[r['identifier_poke']] = r['identifier']
    
#barplot with pokemon on x axis, base experience on y axis, and colors set to the assigned color
b = sns.barplot(data=sel,x='identifier_poke',y='base_experience',palette=cols)

#edit the design of the barplot
plt.xticks(rotation=90)
plt.xlabel('Pokemon Name',fontsize=16)
plt.ylabel('Base Experience',fontsize=16)
plt.title('Base Experience of Various Pokemon',fontsize=20,fontweight='bold')



