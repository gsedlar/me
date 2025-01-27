"""
Gabrielle Sedlar
HW2 Q8
January 26, 2025

Task: Building from q7, let’s continue to build our team. However we now also want to track 
what locations we can find these team members in. We can do this by looking for the 
matching pokemon_id in the provided datafile locations.csv that corresponds to the 
ID of our selected pokemon. Use a dictionary to store this information. When a user 
provides the exit input, you should output all of our data to q8.out 

"""

#empty dictionary for team and locations
team = {}

#open and read both files to prevent them from being opened and read over and over again
with open('poke.csv', 'r') as file:
    pokemonData = file.readlines()
with open('locations.csv','r') as file2:
    locationData = file2.readlines()

pokemon = ''

#same function as q7
while (len(team)<6 and pokemon!='exit'):
    pokemon = input('Please enter the name of a pokemon, type EXIT to stop: ')
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


#team is written as text to the file
storage = open('q8.out','w')
storage.write(str(team))