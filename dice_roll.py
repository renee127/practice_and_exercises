"""Simple dice roll game.
"""

from random import randrange

# get user choice of number of sides
num_of_sides = input('How many sides dose the die have? ')
num_of_rolls = input('How many dice? ')
roll = input('Ready to roll? Y or N: ')

# initialize a list for storing dice rolls
rolls = []

# loop to generate dice roll values, print them
if roll == 'Y' or roll == 'y':
    for i in range(int(num_of_rolls)):   
        rolls.append(randrange(1, int(num_of_sides)))
        i += 1
    print('You rolled: ' + str(rolls)) # could format better...

else:
    # if user enters anything but Y or y, exit
    print('bye')





# 

