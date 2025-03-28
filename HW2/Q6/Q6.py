"""
Gabrielle Sedlar
HW2 Q6
January 26, 2025

Task: Create a python application that reads from the attached file called poke.csv. Your 
application should prompt the user for the name of a pokemon. The user should be able 
to provide the name of a pokemon in any case and if there is a match within that file it 
should print both the ID and the name of the pokemon to a file called q6.out. If the 
name of the pokemon doesn’t exist, nothing should be printed to the file but a message 
should be printed to the user alerting them that the pokemon doesn’t exist. 

"""

#defines function to search for a match to the input
def search(name):
    
    #opens file
    with open('../Data/poke.csv','r') as file:
        
        #converts each line to a list based on where the commas are
        for line in file:
            myArray = line.split(',')
            
            #defines which column the id and pokemon are in
            identifier = myArray[0]
            pokemonName = myArray[1]
            
            #if a match, the file is opened, data is added, and the file is closed
            if (name==pokemonName):
                file = open('q6.out','w')
                file.write(identifier + '\n')
                file.write(pokemonName)
                file.close()
                return pokemonName
            
        #if there was a match, the name will be returned. if not, it will return nothing
        return
                
            
pokemon = input('Please enter the name of a pokemon: ')
pokemon = pokemon.strip().lower()

#call function
match = search(pokemon)

#if there's no match, a line of text is printed
if (match!=pokemon):
    print('This pokemon does not exist.')
        
    