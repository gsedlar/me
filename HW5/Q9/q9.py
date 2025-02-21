"""
Gabrielle Sedlar
HW5 Q9
February 20, 2025

Task: We're back to dungeon crawling! Using a similar approach to the assignment in HW1, create 
a 4 x 4 dungeon. When the dungeon is generated, you should designate the spot that the user 
starts in and the spot that they must get to in order to exit. DO NOT SHOW THE USER WHICH 
SPACE IS THE EXIT. 

Now, before allowing the user to begin, allow them to build a team of up to 6 members OR allow 
them to generate a team of 6 members. They will also need to select a location – this could be a 
specific location OR it could be an entire region. Now select a random selection of pokemon to 
put in each square of your dungeon. This random selection should ensure that only a single 
pokemon sits in each square. 

Now as a user makes their way through their dungeon, if they land on a spot that is not an exit – 
the first pokemon that is available must battle the one that they encounter. If the 
base_experience of their pokemon is greater than the one they encounter – they can proceed! 
Otherwise their pokemon must be removed from their team. If a users team reaches 0, they are 
forced to exit and failure should be written to status.out. If a user decides to exit, you 
should write failure to status.out. If a user reaches the exit, then write success to 
status.out along with the number of members that are still in their team. 

"""

import pandas as pd
import numpy as np
import random

p = pd.read_csv('../data/pokemon.csv')


dungeon = np.empty((4,4),dtype=object) #create 4x4 dungeon
enterDungeon = None 
exitDungeon = None
moves = 0 #will track number of moves needed to reach the exit

#randomly assigns entrance and exit, ensuring they are not the same location
while enterDungeon == exitDungeon: 
    enterDungeon = [random.choice(range(4)), random.choice(range(4))]
    exitDungeon = [random.choice(range(4)), random.choice(range(4))]


#choose or generate a team of 6 pokemon
print('1. Choose team')
print('2. Generate random team')
choice = int(input('Please select an option: '))
if choice == 1:
    team = []
    while len(team) < 6:
        pokemon = input('Please enter the next pokemon: ')
        if(p.identifier.isin([pokemon]).any() == True): #if the pokemon's name exists in the identifier list
            team.append(pokemon) #adds the pokemon to the team
        else:
            print('Invalid pokemon. Please retry.')
else:
    team = p.sample(6)['identifier'].tolist()
    

loc = input('Choose a location or region: ') #user enters a location or region


#16 random pokemon to put in the empty array
dung_poke = p.sample(16)['identifier'].values

#assign the 16 pokemon to the 16 squares in the dungeon array
poke_index = 0
for i in range(4):
    for j in range(4):
        dungeon[i, j] = dung_poke[poke_index]
        poke_index += 1
        
        
        
#some code is copied from HW2 Q10
position = enterDungeon
movement = 0

#intro code
print('----------------------------------------------------------------')
print('Escape the Dungeon!')
print()
print()

#as long as the player is not at the exit, gameplay continues
while position != exitDungeon and movement != 5 and len(team) != 0:
    out = False
    moves += 1
    print('    1. Move one space right')
    print('    2. Move one space left')
    print('    3. Move one space up')
    print('    4. Move one space down')
    print('    5. Quit')
    print()
    movement = int(input('Choose your action from the list above: '))
    print()
    if movement == 1:
        position[0] += 1
        if position[0] > 3:
            position[0] -= 1
            out = True
            print('Oops! You ran into a wall! Try again!')
    elif movement == 2:
        position[0] -= 1
        if position[0] < 0:
            position[0] += 1
            out = True
            print('Oops! You ran into a wall! Try again!')
    elif movement == 3:
        position[1] -= 1
        if position[1] < 0:
            position[1] += 1
            out = True
            print('Oops! You ran into a wall! Try again!')
    elif movement == 4:
        position[1] += 1
        if position[1] > 3:
            position[1] -= 1
            out = True
            print('Oops! You ran into a wall! Try again!')
    else: #print failure message
        print('Invalid input. Try again.')
        out = True
    
    if out == False:
        #battle pokemon at that square, no need to account for if they ran into a wall, if they beat it once they can beat it again
        battler = team[0]
        opponent = dungeon[position[0], position[1]]
        
        #get row for each pokemon
        bat_data = p[p['identifier'] == battler].iloc[0]
        opp_data = p[p['identifier'] == opponent].iloc[0]
    
        #get base experience for each pokemon
        bat_exp = bat_data['base_experience']
        opp_exp = opp_data['base_experience']
        
        if bat_exp > opp_exp: #proceed if they win
            print(battler.title() + ' defeated ' + opponent.title() + '. Good job!')
        else: #remove team member if they lose
            print(opponent.title() + ' defeated ' + battler.title() + '. They are removed from your team.')        
            team.remove(battler)
   
    
file = open('status.out','w')

if movement == 5: #player quit the game
    print('You chose to quit the game.')
    
    #write failure to status.out
    file.write('Failure. Player chose to quit the game.')

elif len(team) == 0: #team is empty
    print('Oh no! Your whole team was defeated! You failed.')
    file.write('Failure. Team was defeated.')

else: #player reached exit
    print('Yay! You won!')
    file.write('Success! Player reached the exit.\n')
    file.write('There are ' + str(len(team)) + ' pokemon left in the team.')


file.close()


