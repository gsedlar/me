"""
Gabrielle Sedlar
March 10, 2025
HW6 Q4

Task: Utilizing the same formula above, draw a single graph that shows the average strength 
of a pokemon type, the minimum strength of that type and the maximum strength of that 
type at each level. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

p = pd.read_csv('../data/pokemon.csv')
pt = pd.read_csv('../data/pokemon_types.csv')
t = pd.read_csv('../data/types.csv')
ps = pd.read_csv('../data/pokemon_species.csv')
e = pd.read_csv('../data/experience.csv')

ppt = p.merge(pt, how='left',left_on='id',right_on='pokemon_id')
pptt = ppt.merge(t,how='left',left_on='type_id',right_on='id',suffixes=('_p','_t'))
pse = ps.merge(e,how='left',left_on='growth_rate_id',right_on='growth_rate_id',suffixes=('_s','_e'))
mrg = pptt.merge(pse,how='left',left_on='species_id',right_on='id')
#mrg is a dataset containing pokemon, species, experience, and type


ty = input('Please enter a pokemon type: ') #prompt user for input

if t.identifier.isin([ty]).any() == True: #check the type exists
    print('yay')
    
    #getting dataframe with only the inputed type of pokemon
    df = mrg[mrg['identifier_t'] == ty] 
    
    #dataframe with new strength column added
    df = df.assign(strength = lambda x: (x['height'] * 5 + x['weight'] * 2 + (x['base_experience'] + x['experience'])))
    
    
    #group data by level, get av strength for each level
    result_av = df.groupby('level')['strength'].mean().reset_index(name='av_stren')
    result_min = df.groupby('level')['strength'].min().reset_index(name='min_stren')
    result_max = df.groupby('level')['strength'].max().reset_index(name='max_stren')
    result = pd.merge(result_av, result_min, on='level')
    result = pd.merge(result, result_max, on='level')
            
    #make and edit plot
    sns.lineplot(data=result, x='level', y='av_stren', color='b', linestyle='-', markersize=8, label='Average Strength')
    sns.lineplot(data=result, x='level', y='min_stren', color='r', linestyle='--', markersize=8, label='Min Strength')
    sns.lineplot(data=result, x='level', y='max_stren', color='g', linestyle='-.', markersize=8, label='Max Strength')

    plt.xlabel('Level', fontsize=16)
    plt.ylabel('Average Strength',fontsize=16)
    plt.title('Strength of ' + ty.title() + ' Pokemon on Each Level',fontsize=20,fontweight='bold')
    plt.tick_params(axis='both',which='major',labelsize=10)
    plt.xticks(np.arange(0,101,5))
    plt.yscale('log') #makes the graph look better, fit all the data bc all the strength values are so large
    
else:
    print('This type does not exist. Please try again.')

