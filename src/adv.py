import textwrap
from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
def go_to(userInput, location):
    attribute = userInput + '_to'
    if hasattr(location, attribute):
      return getattr(location, attribute)
    print("Wrong way\n")
    return location

while True:
# * Prints the current room name
    print(player.location)
# * Prints the current description (the textwrap module might be useful here).
    for desc in textwrap.wrap(player.location.print_desc(), width=500):
        print(desc + "\n")
# * Waits for user input and decides what to do.
    userInput = input('Where do you want to go?\nType q or quit to end game; n, s, w, e to navigate to a new room .\n')
   
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if userInput in ['e', 'n', 'w', 's']:
        player.location =  go_to(userInput, player.location)
        continue
# Print an error message if the movement isn't allowed.
#
    if len(userInput) != 1:
        print("Error, location not found, please type either e, n, w, s")
# If the user enters "q", quit the game.
    if userInput.lower() == "q" or userInput.lower()== "quit" :
        break
