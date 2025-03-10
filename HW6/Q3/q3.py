"""
Gabrielle Sedlar
March 7, 2025
HW6 Q3

Task: Using the formula of (5*height+2*weight+base_experience) to calculate a pokemon's 
strength, draw a graph that shows the average strength of a given pokemon type over 
each generation. Your application should prompt a user for this type and draw the 
appropriate graph based upon that input. 

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
    
    #getting dataframe with only the inputed type of pokemon
    df = mrg[mrg['identifier_t'] == ty] 
    
    #dataframe with new strength column added
    df = df.assign(strength = lambda x: (x['height'] * 5 + x['weight'] * 2 + x['base_experience']))
    
    #group data by generation, get av strength for each gen
    result = df.groupby('id_g')['strength'].mean().reset_index(name='av_stren') 
            
    #make and edit plot
    b = sns.barplot(data=result,x='id_g',y='av_stren',palette='bright')
    plt.xlabel('Generation Number', fontsize=16)
    plt.ylabel('Average Strength',fontsize=16)
    plt.title('Average Strength of ' + ty.title() + ' Pokemon in Each Generation',fontsize=20,fontweight='bold')
    plt.tick_params(axis='both',which='major',labelsize=10)
    
else:
    print('This type does not exist. Please try again.')
