"""
Gabrielle Sedlar
HW3 Q4
February 1, 2025

Task:  Extend Q3 by adding validation. If a user provides a name that doesn't exist within your 
dataset, you should return the line "User does not exist" before returning the user to the 
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
print('3. Show Total Scores')
print('4. Exit')
option = int(input('Choose your option: '))

#if the user selects exit, the while loop stops
while option != 4:
    if option == 1: #asks user for a name and their score, adds it to the corresponding lists
        namesList.append(input('Please enter the next name: '))
        scoresList.append(int(input('Please enter their score: ')))
       
        print() #repeats the menu and asks for a new option
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Show Total Scores')
        print('4. Exit')
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
        print('3. Show Total Scores')
        print('4. Exit')
        option = int(input('Choose your option: '))
        
    elif option == 3: #asks user for a name, then gives that person's total summed score
        name = input('Whose scores would you like to total? ')
        totalScore = 0
        
        if name not in namesList: #if the name isn't in the list the user is prompted for another option
            print()
            print(name + ' does not exist. Try again.')
        else: 
            for i, n in enumerate(namesList): #cycles through the list to find all indexes of the user-inputed name
                if n == name: #if the names match...
                    totalScore += scoresList[i] #...adds score to the total score
            print(name + 's total score is ' + str(totalScore))
        
        print() #repeats menu and asks for next option
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Show Total Scores')
        print('4. Exit')
        option = int(input('Choose your option: '))     
    
    else: #if the user enters a number other than 1-4, the program prompts for a new option
        print('Invalid input. Try again.')
        print()
        print('-----------------------------------------------')
        print('1. Add Score')
        print('2. Check Scores')
        print('3. Show Total Scores')
        print('4. Exit')
        option = int(input('Choose your option: '))

#once the user selects 4 (exit), the program stops
print('-------------------------------------------------')
print('What happens when you cross a Python with a Cobra?')
print('A syntax error!')
print('Thanks for using this program! Have a great day!')