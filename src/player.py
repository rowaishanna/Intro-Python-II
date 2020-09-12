# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # day two code
        self.inventory = []

    def __str__(self):
        items = []
        for item in self.inventory:
            items.append(item.name) # prints out the objects name instead of the object
        return f"Player: {self.name}, Current Room: {self.current_room}, Inventory: {items}"

    def __repr__(self):
        return f"Name: {self.name}, Current Room: {self.current_room}"

    # day two code
    def grab(self, item):
        self.inventory.append(item)
    
    def drop(self, item):
        self.inventory.remove(item)


'''# test code
from item import Item
flashlight = Item('Flashlight')
player = Player('Ace', 'Office', inventory=[flashlight])
phone = Item('Phone')
backpack = Item('Backpack')
player.grab(phone)
player.grab(backpack)
print(player)
player.drop(phone)
print(player)
'''