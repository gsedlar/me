"""
Gabrielle Sedlar
March 10, 2025
HW6 Q5

Task: Utilizing the datasets and formulas above, draw a set of graphs in the shape of an X like 
the diagram described below: 
    X    X           
      X             
    X    X  
The graphs on the left should represent a single pokemon and the ones on the right should 
describe a second pokemon. These pokemon should be provided by the user. The graphs on 
the top row should show the height, weight and base experience for each pokemon. The bottom 
row should show their experience across levels 0 to 100. Based upon the average experience 
they achieve added to the strength we've calculated, the center graph should simply contain the 
name of the pokemon with the greater value.

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

p = pd.read_csv('../data/pokemon.csv')
ps = pd.read_csv('../data/pokemon_species.csv')
e = pd.read_csv('../data/experience.csv')

pse = ps.merge(e,how='left',left_on='growth_rate_id',right_on='growth_rate_id',suffixes=('_s','_e'))
mrg = p.merge(pse,how='left',left_on='species_id',right_on='id',suffixes=('_p','_pse'))
#mrg is a dataset containing pokemon, species, and experience

p1 = input('Please enter your first pokemon: ')

if p.identifier.isin([p1]).any() == True: #verify first pokemon exists
    print('Good choice!')
    
    p2 = input('Please enter your second pokemon: ')
    if p.identifier.isin([p2]).any() == True: #verify second pokemon exists
        print('Nice!')
        
        p1_data = p[p['identifier'] == p1].iloc[0] #get p1's row of data
        p2_data = p[p['identifier'] == p2].iloc[0] #get p2's row of data

        
        #top left plot, representing height, weight, and base experience for pokemon 1
        plt.subplot(3,3,1)
        plt.bar(['Height', 'Weight', 'Exp'], [p1_data['height'], p1_data['weight'], p1_data['base_experience']])
        plt.xlabel('Stat', fontsize=10)
        plt.ylabel('Value',fontsize=10)
        plt.title(p1.title() + 's Stats',fontsize=13,fontweight='bold')
        plt.tick_params(axis='both',which='major',labelsize=8)
        
        
        #top right plot, representing height, weight, and base experience for pokemon 2
        plt.subplot(3,3,3) 
        plt.bar(['Height', 'Weight', 'Exp'], [p2_data['height'], p2_data['weight'], p2_data['base_experience']])
        plt.xlabel('Stat', fontsize=10)
        plt.ylabel('Value',fontsize=10)
        plt.title(p2.title() + 's Stats',fontsize=13,fontweight='bold')
        plt.tick_params(axis='both',which='major',labelsize=8)
        
        
        #bottom left plot, representing experience across levels 1-100 for pokemon 1
        plt.subplot(3,3,7)
        df1 = mrg[mrg['identifier_p'] == p1]
        sns.lineplot(data=df1, x='level', y='experience', color='b', linestyle='-', markersize=8)
        plt.yscale('log') #this was the only solution I could find to a problem where the yticks kept being 0.0 to 1.5, with intervals of 0.5.
                            #idk why this was happening, but this was the only way the labels would show up correctly
        plt.xlabel('Level',fontsize=10)
        plt.ylabel('Experience',fontsize=10)
        plt.title(p1.title() + 's Exp At Each Level',fontsize=11,fontweight='bold')
        
        
        #bottom right plot, representing experience across levels 1-100 for pokemon 2
        plt.subplot(3,3,9)
        df2 = mrg[mrg['identifier_p'] == p2]
        sns.lineplot(data=df2, x='level', y='experience', color='b', linestyle='-', markersize=8)
        plt.yscale('log') #this was the only solution I could find to a problem where the yticks kept being 0.0 to 1.5, with intervals of 0.5.
                            #idk why this was happening, but this was the only way the labels would show up correctly
        plt.xlabel('Level',fontsize=10)
        plt.ylabel('Experience',fontsize=10)
        plt.title(p2.title() + 's Exp At Each Level',fontsize=11,fontweight='bold')
        
        
        #deciding which pokemon is stronger
        s = p.assign(strength = lambda x: (x['height'] * 5 + x['weight'] * 2 + (x['base_experience'])))
        p1_strength = s[s['identifier'] == p1]['strength'].values[0] + df1.experience.mean()
        p2_strength = s[s['identifier'] == p2]['strength'].values[0] + df2.experience.mean()
        
        if p1_strength > p2_strength:
            stronger_pokemon = p1.title()
        else:
            stronger_pokemon = p2.title()
        
        #putting the stronger pokemon in the center
        plt.subplot(3,3,5)
        plt.text(0.3,0.5,stronger_pokemon)
    
    else:
        print('Invalid pokemon. Please try again.')

else:
    print('Invalid pokemon. Please try again.')
