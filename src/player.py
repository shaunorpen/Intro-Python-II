# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, carrying = []):
        self.name = name
        self.current_room = current_room
        self.carrying = carrying

    def move(self, direction):
        if hasattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            return False
        else:
            return True
    
    def get(self, item_name):
        item = next(item for item in self.current_room.items if item.name == item_name)
        if item:
            self.carrying.append(item)
            self.current_room.items.remove(item)
            return False
        else:
            return True

    def drop(self, item_name):
        item = next(item for item in self.carrying if item.name == item_name)
        if item:
            self.current_room.items.append(item)
            self.carrying.remove(item)
            return False
        else:
            return True