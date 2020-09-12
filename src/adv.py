from room import Room
from player import Player
from item import Item

# create item objects that can be in the rooms or held by the player
rock = Item('Rock')
flashlight = Item('Flashlight')
toilet_paper = Item('Toilet Paper')
umbrella = Item('Umbrella')
bag = Item('Bag')
shoes = Item('Shoes')
computer = Item('Computer')
bottle = Item('Bottle')
guitar = Item('Guitar')


# dictionary of room objects
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. An open door looms on the western wall."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'bedroom': Room("The Master Bedroom", """Upon entering the open door, you find yourself in a large,
ornately decorated bedroom. Glass french doors filter in sunlight from the west. 
An archway with no light sits to the south.
Another door lies to the north."""),

    'bathroom': Room("The Bathroom", """You've found the ever important bathroom. Stop if you need, 
but otherwise, get back to the bedroom and keep searching! The door now lies to the south of you.""",
 computer),

    'closet': Room("The Closet", """You are now in a closet so large that a family of four
could live in it comfortably. With fine dresses on one end and suits on the other, this is not
the treasure you search for. The arch is now to the north of you."""),

    'balcony': Room("The balcony", """As you push your way through the french doors and into the 
crisp evening air, you find that there is nowhere to go but back. Return to the bedroom 
through the french doors that now lie to the east of you."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['bedroom']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']

room['bedroom'].s_to = room['closet']
room['bedroom'].n_to = room['bathroom']
room['bedroom'].w_to = room['balcony']
room['bedroom'].e_to = room['foyer']

room['bathroom'].s_to = room['bedroom']

room['balcony'].e_to = room['bedroom']

room['closet'].n_to = room['bedroom']

# create easier to follow representations of the room objects
outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']
bedroom = room['bedroom']
closet = room['closet']
bathroom = room['bathroom']
balcony = room['balcony']

# add items to different rooms
outside.add_object(rock)
foyer.add_object(umbrella)
bathroom.add_object(toilet_paper)
overlook.add_object(flashlight)
'''print(len(outside.objects))
print(len(foyer.objects))
print(len(bathroom.objects))
print(len(overlook.objects))'''

# test = Player('Nate', outside)
# print(test.current_room.n_to.name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please enter your player name: ')
print('------------------------------------')
print('------------------------------------')

# instantiate a new player with name
# and who is currently 'outside'
player = Player(name, outside)

# define while loop condition
x = 0
# Write a loop that:
while x == 0:
    # * Prints the current room name
    print(f'Current room: {player.current_room.name}')

    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

    # prints what items are available in the room
    print(f'Available items in this room: ')
    for item in player.current_room.objects:
        print(item)

    print(f'Items in your inventory: ')
    for item in player.inventory:
        print(item)

    # ADD A FOR LOOP HERE TO ADD DIFFERENT ITEMS TO YOUR INVENTORY
    # are there any objects in this room to begin with?
    if len(player.current_room.objects) > 0:
        for item in player.current_room.objects:
            print(f'Would you like to add <{item}> to you inventory?')
            answer = input('Please type y for yes or n for no: ')
            print('------------------------------------')
            if answer == 'y':
                # item = player.current_room.objects[0]
                # add object to player inventory
                player.grab(item)
                print(f'Nice! Now you have <{item.name}> in your inventory!')
                print('------------------------------------')
                # drop objects from the room
                player.current_room.drop_object(player.current_room.objects[0])
                # check to make sure the room now has no objects
                # * Prints the current room name
                print(f'Current room: {player.current_room.name}')

                # * Prints the current description (the textwrap module might be useful here).
                print(player.current_room.description)

                # prints what items are available in the room
                print(f'Available items in this room: ')
                for item in player.current_room.objects:
                    print(item)

                print(f'Items in your inventory: ')
                for item in player.inventory:
                    print(item)
                x = 0
            elif answer == 'n':
                print('Got it!')
                x = 0
            else:
                input('Invalid entry! Type y for yes or n for no')
    print('------------------------------------')


# give the player the option to drop items from their inventory
    if len(player.inventory) > 0:
        for item in player.inventory:
            print(f'Would you like to drop {item} from your inventory?')
            answer = input('Please type y for yes or n for no: ')
            print('------------------------------------')
            if answer == 'y':
                print('Here are the items that are currently in your inventory: ')
                # print the names of the inventory objects
                for item in player.inventory:
                    print(item.name)
                drop_item = input('Please type the name of the item you would like to drop EXACTLY as you see it spelled: ')

                # loop through the player inventory again
                for item in player.inventory:
                    # if the player entered the name of one of the items, drop it from inventory
                    if drop_item == item.name:
                        player.drop(item)
                        # add the dropped item back to the room
                        player.current_room.add_object(item)
                        print(f'You have succesfully dropped <{drop_item}> from your inventory')
                x = 0

            elif answer == 'n':
                print('Got it!')
                x = 0
            else:
                input('Invalid entry! Type y for yes or n for no')               
                # re-enter the original while loop
            

        

    print('------------------------------------')
    print('------------------------------------')
    # * Waits for user input and decides what to do.
    print('What direction would you like to go?')
    direction = input('Your options are n, s, e, w, or q to quit: ')
    print('------------------------------------')
    print('------------------------------------')
    
    x = 1

    while x == 1:
    # If the user enters a cardinal direction, attempt to move to the room there.
        # print(f'You chose {direction} as your direction')
        # print(player.current_room)
        # print('------------------------------------')

        if direction == 'n':
            north_room = player.current_room.n_to
            if north_room != 'unknown':
                player.current_room = north_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')


        elif direction == 's':
            south_room = player.current_room.s_to
            if south_room != 'unknown':
                player.current_room = south_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        elif direction == 'e':
            east_room = player.current_room.e_to
            if east_room != 'unknown':
                player.current_room = east_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        elif direction == 'w':
            west_room = player.current_room.w_to
            if west_room != 'unknown':
                player.current_room = west_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        # If the user enters "q", quit the game.
        elif direction == 'q':
            print('Thanks for playing!')
            x = 2
        
        else:
            # Print an error message if the movement isn't allowed.
            print('Unfortunately, that is an invalid direction!')
            direction = input('Your options are n, s, e, w, or q to quit: ')
            print('------------------------------------')
            print('------------------------------------')      
