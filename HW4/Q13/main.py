"""
Gabrielle Sedlar
HW4 Q13
February 9, 2025

Task:   Let's work on managing our dataset. Write an application that gives the user the 
following options: 
    a. Manage Dataset 
    b. Exit 

If the user chooses to Exit, write the poke dataset (with changes) to a file called q13.out 

If the user choose Manage Dataset, provide three additional options:
    - Add Pokemon
    - Delete Pokemon 
    - Update Pokemon 

The last two (Delete and Update) should prompt you for an ID. For delete, it should remove that 
pokemon from the dataset. For update, it should prompt you to update the pokemon name. 

For add, you should create a new record utilizing the existing columns of our dataset and 
prompt the user to provide values for each of them. Once the values are set, it should then add 
this new record to the existing dataset. 

After each action, you should be returned to the main menu, where the user can then decide to 
take similar actions or exit. As before, when the user exits – the dataframe (with whatever 
updates have been made) should be written to a file called q13.out

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')

#menus are stored as variables to avoid having to type multiple lines of code each time
menu = '\n1. Manage Dataset\n2. Exit\n'
menu2 = '\n1. Add Pokemon\n2. Delete Pokemon\n3. Update Pokemon\n'

#intro text
print('-------------------------------------------------')
print('Welcome!')
print(menu)
choice = int(input('Please select your first option: '))

while choice != 2: #when the user selects exit, the program stops
    if choice == 1: #manage dataset
    
        #user selects how they would like to manage the data
        print(menu2) 
        choice2 = int(input('How you would like to manage the data: '))
        
        if choice2 == 1: #add pokemon
            new = dict.fromkeys(pokeDF) #dictionary with keys of the column values
            
            for k in new: #asks for value for each column
                new[k] = input('Enter a value for ' + str(k) + ': ')
            
            newDF = pd.DataFrame([new]) #switches dictionary into dataframe
            pokeDF = pd.concat([pokeDF,newDF]) #concatenates both dataframes
        
        elif choice2 == 2: #delete pokemon
            ID = int(input('\nPlease enter the ID of the pokemon you would like to delete: '))
            pokeDF = pokeDF[pokeDF['id'] != ID] #replaces dataframe with a dataframe containing everything except the pokemon at the inputed id
            
        elif choice2 == 3: #update pokemon name
            ID = int(input('\nPlease enter the ID of the pokemon you would like to update: '))
            newName = input('What would you like to change this pokemons name to? ')
            pokeDF.loc[pokeDF['id'] == ID,'identifier'] = newName #replaces the pokemon at the inputed id with the inputed name
        
        else: #if the user enters a number not 1-3, an error message prints
            print('\nInvalid choice. Please reselect.')
           
    else: #if the user chooses an invalid option, they are prompted to retry
        print('\nInvalid choice. Choose again.')
        
    #reprints menu and allows another option to be selected
    print(menu)
    choice = int(input('Please select your next option: '))

#when the user selects exit, the dataframe is printed to the q13.out file
file = open('q13.out','w')
file.write(str(pokeDF))
file.close()