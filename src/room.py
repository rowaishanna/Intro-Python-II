# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to='unknown', s_to='unknown', e_to='unknown', w_to='unknown'):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.objects = []

    def __str__(self):
        object_names = []
        for item in self.objects:
            object_names.append(item.name) # prints out the objects name instead of the object
        return f"{self.name}, Available objects: {object_names}\n {self.description}"
    
    def __repr__(self):
        return f"Room({self.name}, {self.description})"

    def add_object(self, item):
        self.objects.append(item)
    
    def drop_object(self, item):
        self.objects.remove(item)