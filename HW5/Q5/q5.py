"""
Gabrielle Sedlar
HW5 Q5
February 19, 2025

Task:  Similar to what we just did, let's draw a graph showing the number of each primary type of 
pokemon that exist in a game. Create a new column called type_color that you use a lambda 
function to set. You can use whatever logic you would like to set the color based on available 
type names (i.e. you could create a function that returns a certain color based off of the names 
available in the types dataset). Once you have this new dataframe with the type_color 
applied, write this dataframe to q5.out. With this data in hand, create a new graph that shows 
the results (name of the type and its count) with each column being the color that was applied to 
that type. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random


p = pd.read_csv('../data/pokemon_types.csv')
ty = pd.read_csv('../data/types.csv')

df = p.merge(ty,how='left',left_on='type_id',right_on='id') #merge both datasets

#get rid of any non-primary types
for i,r in df.iterrows():
    if r['slot'] != 1:
        df = df.drop(i)

types = df.groupby('identifier')['identifier'].count() #get df with all types and how many pokemon in each

#create colors list, shuffle them, and then assign to type_color with
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 
    'pink', 'black', 'cyan', 'magenta', 'lime', 'olive', 'teal', 
    'maroon', 'navy', 'indigo', 'gold', 'turquoise', 'crimson']
random.shuffle(colors)

types_df = types.to_frame() #convert to dataframe

#assign a random color to each type, then delete the color so there are no duplicates
types_df = types_df.assign(type_color = lambda x: [colors.pop(0) for r in range(len(x))]) 

#write the dataframe to q5.out
file = open('q5.out','w')
file.write(str(types_df))
file.close()


type_colors = types_df['type_color'].tolist() #make list of colors

b = sns.barplot(data=types_df, x=types_df.index, y='identifier', palette=type_colors) #barplot with count of each type, with associated color

#edit the design of the barplot
plt.xticks(rotation=90)
plt.xlabel('Type of Pokemon',fontsize=16)
plt.ylabel('Number of Pokemon',fontsize=16)
plt.title('Number of Each Type of Pokemon',fontsize=20,fontweight='bold')
