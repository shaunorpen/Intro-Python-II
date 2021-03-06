import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     [Item("torch"), Item("rope"), Item("sandwich")]),

    'foyer':    Room("Foyer", 
                     "Dim light filters in from the south. Dusty passages run north and east.",
                     [Item("sword")]),

    'overlook': Room("Grand Overlook", 
                     "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", 
                     "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", 
                     "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                     [Item("treasure")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Clear screen util

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

clear_screen()

player_name = input("What's your name?\n\n")

player = Player(player_name, room["outside"])

welcome_message = f"\nThanks, {player.name}. Welcome to your adventure!"

print(welcome_message)
print("*" * len(welcome_message))

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

try_again = False

while True:

    if try_again == False:
        print(f"\nYou're currently in the {player.current_room.name}. {player.current_room.description}")
        
        if len(player.current_room.items) > 0:
            print(f"\nThis room contains the following items: {', '.join(str(item.name) for item in player.current_room.items)}")

        if len(player.carrying) > 0:
            print(f"\nYou are carrying the following items: {', '.join(str(item.name) for item in player.carrying)}")

        print("\nWhich direction would you like to go?\n\n[N]orth\n[S]outh\n[E]ast\n[W]est\n\n[Q]uit\n")
    else:
        print("You can't do that. Try again!")
    
    instruction = input().lower().split()

    if instruction[0] == "q":
        clear_screen()
        break
    elif instruction[0] in ("n", "s", "e", "w"):
        try_again = player.move(instruction[0])
    elif instruction[0] == 'get':
        try_again = player.get(instruction[1])
    elif instruction[0] == 'drop':
        try_again = player.drop(instruction[1])
    else:
        try_again = True
        continue