class Room:
    def __init__(self, name):
        self.name = name
        self.list_of_songs = []
        self.guests_in_room = []
    
    def check_in_guest(self, guest):
        self.guests_in_room.append(guest)

    def check_out_guest(self, guest):
        self.guests_in_room.remove(guest)

    def add_song(self,song):
        self.list_of_songs.append(song)