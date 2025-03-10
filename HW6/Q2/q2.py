"""
Gabrielle Sedlar
March 3, 2025
HW6 Q2

Task: Utilizing the datasets that we've been working with, prompt a user for a string 
representation of a pokemon type. Ensure that this type exists within our dataset. If it 
does, draw a graph that shows how many pokemon of that type exist within each 
generation of the game. An example of this would be saying "32 electric pokemon 
existed in generation 1, 64 in generation 2, etc.".

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

p = pd.read_csv('../data/pokemon.csv')
pt = pd.read_csv('../data/pokemon_types.csv')
t = pd.read_csv('../data/types.csv')
ps = pd.read_csv('../data/pokemon_species.csv')
g = pd.read_csv('../data/generations.csv')

ppt = p.merge(pt, how='left',left_on='id',right_on='pokemon_id')
pptt = ppt.merge(t,how='left',left_on='type_id',right_on='id',suffixes=('_p','_t'))
psg = ps.merge(g,how='left',left_on='generation_id',right_on='id',suffixes=('_s','_g'))
mrg = pptt.merge(psg,how='left',left_on='species_id',right_on='id_s')
#mrg is a dataset containing pokemon, species, generation, and type


ty = input('Please enter a pokemon type: ') #prompt user for input

if t.identifier.isin([ty]).any() == True: #check the type exists
    print('yay')
    
    #getting dataframe with only the inputed type of pokemon
    df = mrg[mrg['identifier_t'] == ty] 
    
    result = df.groupby(['id_g'])['id_g'].count().reset_index(name='count') #get dataset of the count of each number in each generation
    
    #make and edit plot
    b = sns.barplot(data=result,x='id_g',y='count',palette='bright')
    plt.xlabel('Generation Number', fontsize=16)
    plt.ylabel('Number of Pokemon',fontsize=16)
    plt.title('Number of ' + ty.title() + ' Pokemon in Each Generation',fontsize=20,fontweight='bold')
    plt.tick_params(axis='both',which='major',labelsize=10)
    
else:
    print('This type does not exist. Please try again.')
    
