"""
Gabrielle Sedlar
HW3 Q2
January 31, 2025

Task:  Create an application that keeps track of a user's score in a set of games. Your 
application should interact with the user and provide them three options: 
    a. Add Score 
    b. Check Scores 
    c. Exit 
    
For option one, you should ask the user to provide a name for the user and the score for 
that game. After the user provides their inputs, they should then be returned to the main 
menu. They should be able to provide as many entries as they like until they opt for 
option three (exit). 

For option two, you should ask the user to provide a name for the user. You should then 
return a DataFrame containing the scores for that particular user before returning to the 
main menu. 

"""

import pandas as pd

#initializes empty lists for names and scores
namesList = []
scoresList = []

#starting code - the menu is repeated after each option is selected and completed
print('-----------------------------------------------')
print('Welcome! Please choose from the options below: ')
print('1. Add Score')
print('2. Check Scores')
print('3. Exit')
option = int(input('Choose your option: '))

#if the user selects exit, the while loop stops
while option != 3:
    if option == 1: #asks user for a name and their score, adds it to the corresponding lists
        namesList.append(input('Please enter the next name: '))
        scoresList.append(int(input('Please enter their score: ')))
       
        print() #repeats the menu and asks for a new option
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Exit')
        option = int(input('Choose your option: '))
        
    elif option == 2: #asks user for whose scores they want to check, then prints their scores
        scoresDict = { #enters the two lists into a dictionary
            'Name':namesList,
            'Score':scoresList
            }
        df = pd.DataFrame(scoresDict) #converts dictionary into datafram
        print(df[df.Name.isin([input('Whose scores would you like to check? ')])])  
        
        print() #repeats menu and asks for next option
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Exit')
        option = int(input('Choose your option: '))
        
    else: #if the user enters a number other than 1-3, the program prompts for a new option
        print('Invalid input. Try again.')
        print()
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Exit')
        option = int(input('Choose your option: '))

#once the user selects 3, the program stops
print('-------------------------------------------------')
print('What happens when you cross a Python with a Cobra?')
print('A syntax error!')
print('Thanks for using this program! Have a great day!')