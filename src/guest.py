class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
    
    def pay_fee(self, amount):
        self.wallet -= amount

    def whoo_check(self, room):
        for guest in room.guests_in_room:
            if self == guest:
                for song in room.list_of_songs:
                    if self.favourite_song == song.name:
                        return "WHOOOOOO!"
                    else: return False
            else: return False