class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.favourite_song = None
    
    def pay_fee(self, amount):
        self.wallet -= amount

    def assign_fav_song(self, song):
        self.favourite_song = song


    def whoo(self, room):
        if room.guest_in_room_check(self) == True:
            for song in room.list_of_songs:
                if self.favourite_song == song:
                    return "WHOOOOOO!"
        return False
