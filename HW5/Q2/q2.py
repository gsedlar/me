"""
Gabrielle Sedlar
February 17, 2025
HW5 Q2

Task: Like we have in past weeks – build an application that allows a user to build a team of 
pokemon. This team can consist of a maximum of 6 pokemon. A user should be able to provide 
up to 6 pokemon names and they must exist within the pokemon dataset. Your menu should 
provide for the following options:
    - Add pokemon 
    - Generate random team 
    - Delete Pokemon 
    - Exit 

When a user decides to exit, draw a graph showing the base_experience for each member 
still existing in the team. 
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

p = pd.read_csv('../data/pokemon.csv')

menu = '\n1. Add pokemon\n2. Generate random team\n3. Delete Pokemon\n4. Exit\n'
team = []

print(menu)
choice = int(input('Please select your first option: '))

while choice != 4:
    if choice == 1: #add pokemon
        if len(team) > 5:
            print('Too many team members')
        else:
            entry = input('\nWho would you like to add to your team? ')
            
            if(p.identifier.isin([entry]).any() == True): #if the pokemon's name exists in the identifier list
                team.append(entry) #adds the pokemon to the team
            else:
                print('\nThis pokemon does not exist.') #if the pokemon does not exist, prints a statement
        
        print(menu)
        choice = int(input('Please select your next option: '))
        
    elif choice == 2: #generate random team
        team = p['identifier'].sample(6).tolist() #takes 6 random identifiers from the dataframe and converts them to a list
        
        print(menu)
        choice = int(input('Please select your next option: '))
        
    elif choice == 3: #delete pokemon
        dropPoke = input('Please enter the name of the pokemon you would like to drop: ')
        
        team.remove(dropPoke) #removes the inputted pokemon from the list
        
        print(menu)
        choice = int(input('Please select your next option: '))
        
    else:
        print('\nInvalid input. Please try again.')
        print(menu)
        choice = int(input('Please select your next option: '))
  
#new dataframe just with team data
team_data = p[p['identifier'].isin(team)]

#create and format/design bar graph
b = sns.barplot(data=team_data,x='identifier',y='base_experience',palette='pastel')
plt.xlabel('Pokemon Name',fontsize = 16)
plt.ylabel('Base Experience',fontsize=16)
plt.title('Base Experience for Your Team',fontsize=20)
plt.tick_params(axis='x',which='major',labelsize=8)

plt.show()