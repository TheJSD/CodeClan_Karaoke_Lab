class Room:
    def __init__(self, name, room_limit):
        self.name = name
        self.list_of_songs = []
        self.guests_in_room = []
        self.room_limit = room_limit
    
    def check_in_guest(self, guest):
        if len(self.guests_in_room) < 4:
            self.guests_in_room.append(guest)

    def check_out_guest(self, guest):
        self.guests_in_room.remove(guest)

    def add_song(self,song):
        self.list_of_songs.append(song)