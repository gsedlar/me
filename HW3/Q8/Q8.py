"""
Gabrielle Sedlar
HW3 Q8
February 1, 2025

Task:  Using poke.csv, prompt the user for a number. If the data provides isn't a number, 
return the message "Please provide a number". If the user again provides input that isn't 
a number, then return the message "Error" and exit immediately. 

If the input is a number, return the data for the pokemon at the index of that number and 
the pokemon that has that value as their id. This should all be returned within a single 
DataFrame object. 

"""

import pandas as pd

df = pd.read_csv('../Data/poke.csv')

number = input('Please enter a number: ')
count = 0

while count != 2: #if the user entered a wrong input twice, the program exits

    if number.isdigit() == True: #if the input is number, the pokemon data is printed
        number = int(number)
        
        print(df[(df.index == number) | (df.id == number)]) #prints pokemon with index of the inputed number
            #use or to also print the pokemon with the id number equal to the inputed number
        
        count = 2 #while loop ends because the desired output has printed
    else:
        if count == 0: #if this is the first time the user inputs something wrong, they get another try
            number = input('Incorrect input. Please provide a number: ')
        else:
            print('Error') #if this is the second time the user inputs something wrong, the program exits and prints Error
        count += 1  
        

