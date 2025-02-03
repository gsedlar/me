"""
Gabrielle Sedlar
HW3 Q12
February 3, 2025

Task:   We arrive to find our dear friend, Ash Ketchum, looking to get to know the world around 
him. He wants to be able to ask questions about the Pokemon that he is hunting and the 
locations that he'll need to travel to. In order to accomplish this, we need to build him a 
Python application, as every great Poke master requires, to help him track down this 
information. 

In order to accomplish this, when run, the application should provide him a menu that 
looks like the following: 
    Hello, Ash! 
    1) Search By Name 
    2) Search By Region 
    3) Exit 

If a user selects by name: 
    a. The user should be prompted for a pokemon name 
    b. It should be validated that the pokemon exist in our dataset 
    c. If it does not, tell Ash that this mysterious pokemon cannot be found 
    d. If it does exist, query our dataset and return the name, id, height and weight. This 
        should be returned in a dataframe. 

If a user selects by region: 
    e. Prompt the user for a name of a region 
    f. It should be validated that the region exists in our dataset 
    g. If it does not, tell Ash this this region does not exist 
    h. If it does exist, query our dataset and return the locations that belong to this 
        region. This should be returned in a dataframe, but contain only the location 
        names. 

After each option, Ash should be returned to the main menu where he can then decide 
to continue searching or Exit.

"""

import pandas as pd

#bringing in csv files as dataframes
locDF = pd.read_csv('../Data/locations.csv')
regDF = pd.read_csv('../Data/regions.csv')
pokeDF = pd.read_csv('../Data/poke.csv')

#intro text, including menu that is repeated after each option
print('-----------------------------------------------')
print('Hello, Ash!')
print('1. Search by Name')
print('2. Search By Region')
print('3. Exit')
print()

choice = int(input('Select your option: '))
print()

while(choice!=3): #if user selects exit, the program ends
    
    if choice == 1: #return name, id, height, and weight
    
        name = input('Please enter a pokemon name: ').strip().lower()
        
        if(pokeDF.identifier.isin([name]).any() == True): #if the pokemon's name exists in the identifier list
            
            for i, r in pokeDF.iterrows():  #searches through the rows in poke.csv
                if r['identifier'] == name: #if the row has the correct pokemon in the identifier column, prints out related information
                    print('The ID for ' + r['identifier'] + ' is ' + str(r['id']) + ', height is ' + str(r['height']) + ', and weight is ' + str(r['weight']))
                    
        else:
            print('This mysterious pokemon cannot be found.') #if the pokemon does not exist, prints a statement

                
        print()
        print('1. Search by Name')
        print('2. Search By Region')
        print('3. Exit')
        print()

        choice = int(input('Select your option: '))
        print()
        
        
    elif choice == 2: #return locations that belong to this region
        
        region = input('Please enter a region name: ')
        
        if(regDF.identifier.isin([region]).any() == True): #if region exists
            
            locations = [] #empty list for all locations that belong to the region
    
            reg_id = regDF.loc[regDF['identifier'] == region, 'id'].iloc[0] #associated region id for the region

            for i, r in locDF.iterrows():  #searches through the rows in locations.csv
                if r['region_id'] == reg_id:
                    locations.append(r['identifier']) #adds location to a list of all locations in that region
            
            print((locDF[locDF.identifier.isin(locations)]['identifier']))
                    
                    
        else:
            print('This region does not exist.') #if the region does not exist, prints a statement
        
        
        print()
        print('1. Search by Name')
        print('2. Search By Region')
        print('3. Exit')
        print()
    
        choice = int(input('Select your option: '))
        print()
        
        
    else:
        print('Invalid Input. Please reselect an option.')
        print('1. Search by Name')
        print('2. Search By Region')
        print('3. Exit')
        print()

        choice = int(input('Select your option: '))
        print()
        
    
#when the user selects exit, a final message is printed
print('Bye Ash!')
print('-------------------------------------------------')
    
