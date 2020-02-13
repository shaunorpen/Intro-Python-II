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