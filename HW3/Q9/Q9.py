"""
Gabrielle Sedlar
HW3 Q9
February 1, 2025

Task:  Revisiting a problem from HW2, let's recreate our team builder using pandas. Our menu 
should have four options: 
    a. Add To Team 
    b. Drop From Team 
    c. Print Team 
    d. Exit 

Similar to last week, a team can only have six members of the team. If you attempt to 
add more than that, you should return the message "Too many team members". The 
pokemon also needs to exist within our dataset. If it does not, you should return the 
message "This pokemon does not exist". If it does, you can add it to your team. 

Using the solution from last week, you can manage the team in the same way. If a user 
wants to drop a member from the team – they should be able to provide some identifier 
that you indicate to drop them from the team. 

If choosing to print the team,you should return a DataFrame showing rows for each of 
the current members of the team. 

After each option, the user should be returned to the main menu until they decide to exit.  

"""

import pandas as pd

pokemonDF = pd.read_csv('../Data/poke.csv')
team = []

#menu options, repeated until they choose to exit (option 4)
print('1. Add To Team')
print('2. Drop From Team')
print('3. Print Team')
print('4. Exit')
choice = int(input('Please choose your first option: '))
print()

while choice != 4:
    if choice == 1: #add to team
        if len(team) > 5:
            print('Too many team members')
        else:
            entry = input('Who would you like to add to your team? ')
            print()
            
            if(pokemonDF.identifier.isin([entry]).any() == True): #if the pokemon's name exists in the identifier list
                team.append(entry) #adds the pokemon to the team
            else:
                print('This pokemon does not exist.') #if the pokemon does not exist, prints a statement
        
        print()
        print('1. Add To Team')
        print('2. Drop From Team')
        print('3. Print Team')
        print('4. Exit')
        choice = int(input('Please choose your next option: '))
        
        
    elif choice == 2: #drop from team
    
        dropPoke = input('Please enter the name of the pokemon you would like to drop: ')
        
        team.remove(dropPoke) #removes the inputted pokemon from the list
                        
        print('1. Add To Team')
        print('2. Drop From Team')
        print('3. Print Team')
        print('4. Exit')
        choice = int(input('Please choose your next option: '))
        
        
    elif choice == 3: #print team
    
        print(pokemonDF[pokemonDF.identifier.isin(team)])
        
        print('1. Add To Team')
        print('2. Drop From Team')
        print('3. Print Team')
        print('4. Exit')
        choice = int(input('Please choose your next option: '))
        
        
    else:
        print('Invalid input. Try again.')
        print('1. Add To Team')
        print('2. Drop From Team')
        print('3. Print Team')
        print('4. Exit')
        choice = int(input('Please choose your next option: '))

print('Thank you for using this program. Have a great day!')