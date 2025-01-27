"""
Gabrielle Sedlar
HW2 Q10
January 27, 2025

Task:  Let’s go dungeon crawling! Let’s create a dungeon that is 4 squares across and 2 
squares deep. 
At the start of your application, it should create the structure required for our dungeon. It should 
then randomly select one of these squares to begin you in and another random square to 
designate as the exit. 
Your application should: - 
Be smart enough to give the user the ability to move only in directions they are able. As 
an example, it should not allow you to move up if there is no space to move up. - - - 
It should track the number of moves you’ve needed to make from the time you started 
until the time you reach the exit. 
In addition to movement options, the user should be provided with an option to exit. 
When you reach the exit (or decide to exit), your application should write out whether 
you reached the exit (success=true) or if you decided to leave early (success=false) as 
well as the number of attempts that were made prior to either of those actions. 
    
"""

import numpy as np
import random

#initializes a blank 4x2 dungeon and blank entrance and exit points
dungeon = np.zeros((4,2))
enterDungeon = None 
exitDungeon = None
moves = 0 #will track number of moves needed to reach the exit

#randomly assigns entrance and exit, ensuring they are not the same location
while enterDungeon == exitDungeon: 
    enterDungeon = [random.choice(range(4)), random.choice(range(2))]
    exitDungeon = [random.choice(range(4)), random.choice(range(2))]

    
# #checkpoint 1: entrance and exit points are set
# print(enterDungeon)
# print(exitDungeon)


#initializes the position as the entrance to the dungeon
position = enterDungeon
movement = 0

#intro code
print('----------------------------------------------------------------')
print('Escape the Dungeon!')
print()
print()

#as long as the player is not at the exit, gameplay continues
while position != exitDungeon and movement != 5:
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
            print('Oops! You ran into a wall! Try again!')
    elif movement == 2:
        position[0] -= 1
        if position[0] < 0:
            position[0] += 1
            print('Oops! You ran into a wall! Try again!')
    elif movement == 3:
        position[1] -= 1
        if position[1] < 0:
            position[1] += 1
            print('Oops! You ran into a wall! Try again!')
    elif movement == 4:
        position[1] += 1
        if position[1] > 1:
            position[1] -= 1
            print('Oops! You ran into a wall! Try again!')
            

# #checkpoint 2: correct movements were taken, and moves variable was properly counted
# print(position)
# print(moves)


#if user reached the exit, a success message prints
if position == exitDungeon:
    print()
    print('Congragulations! You reached the exit!')
    print('You took ' + str(moves) + ' moves to reach the exit.')
    print()
    print('Thanks for playing!')
    print('-------------------------------------------------------------')

#if the user quit early, a failure message prints
else:
    print()
    print('You did not escape the dungeon.')
    print('You took ' + str(moves) + ' before giving up')
    print()
    print('Try again!')
    print('-------------------------------------------------------------')

    


