"""
Gabrielle Sedlar
HW2 Q7
January 26, 2025

Task: Create a python application that is similar to our class example. However, this time we 
are building a team of pokemon. The rules of our team are that there can only be a 
maximum of 6 members of the team and that they need to exist within our dataset. Once 
a user enters the word exit, your application should then output the team members to 
q7.out. 

"""
#initialize empty list for team
team = []

#open file and read data so that the code doesn't have to keep opening it
with open('poke.csv', 'r') as file:
    data = file.readlines()
    
#initialize empty pokemon name
pokemon = ''

#pokemon are continually added until either the team reaches a size of 6 or the user says to exit
while (len(team)<6 and pokemon!='exit'):
    pokemon = input('Please enter the name of a pokemon, type EXIT to stop: ')
    pokemon = pokemon.strip().lower()
    for line in data:
        myArray = line.split(',')
        pokemonName = myArray[1]
        if (pokemon==pokemonName):
            team.append(pokemonName)
    
#the team is printed to the file
storage = open('q7.out','w')
storage.write(str(team))
storage.close()
            
        
