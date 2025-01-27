"""
Gabrielle Sedlar
HW2 Q9
January 26, 2025

Task: Building from q8, let’s provide a menu to continue managing this team. We should have 
the following options: 
    1) Add Pokemon 
    2) List Team 
    3) Drop Member 
    4) Exit 
Your application should do and store everything just as we do in q8. However now if a user 
chooses option 2, you should output a list of just the pokemon names on the team alongside an 
ID that can be referred to for their position in the team. An example output would look like: 
    1) Pikachu 
    2) Bulbasaur 
    3) Charmander 
If the user chooses option 3, they should be prompted for an ID of the member that they want to 
remove from the team. Once provided, you should then drop that member from the team. 

"""

#initializes variables
team = {}
pokemon = ''
choice = 0

#open and read both files to prevent them from being opened and read over and over again
with open('poke.csv', 'r') as file:
    pokemonData = file.readlines()
with open('locations.csv','r') as file2:
    locationData = file2.readlines()

while choice != 4:
    print('\nChoose your option:')
    print('      1) Add Pokemon')
    print('      2) List Team')
    print('      3) Drop Member')
    print('      4) Exit')
    choice = int(input('Please enter the number corresponding to your desired action: '))
    print()
    
    if choice == 1:
        if (len(team)<6):
            pokemon = input('Please enter the name of a pokemon: ')
            pokemon = pokemon.strip().lower()
            for line in pokemonData:
                myArray = line.split(',')
                identifier = myArray[0]
                pokemonName = myArray[1]
                
                #before adding a matching pokemon to the list, program finds the location from the excel sheet and adds it to the dictionary
                if (pokemon==pokemonName):
                    for line in locationData:
                        locationArray = line.split(',')
                        if identifier==locationArray[0]:
                            location = locationArray[2]
                    team[pokemonName] = location
                
        else:
            'Team full. Pick another option'
    elif choice == 2: 
        i = 1
        for key in team:
            print (str(i) + ') ' + key)
            i = i+1
    elif choice == 3:
        deleteID = int(input('Please enter the ID number of the pokemon you would like to delete'))
        myList = (team.keys())
        deletePokemon = myList[deleteID-1]
        team.pop(deletePokemon)
        
    else:
        print('Invalid choice. Please try again.')
    
        