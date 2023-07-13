class Room:
    def __init__(self, name, room_limit, fee):
        self.name = name
        self.list_of_songs = []
        self.guests_in_room = []
        self.room_limit = room_limit
        self.fee = fee
        self.money_spent_in_room = 0
    
    def check_in_guest(self, guest):
        if len(self.guests_in_room) < 4:
            self.charge_fee(guest, self.fee)
            self.guests_in_room.append(guest)

    def check_out_guest(self, guest):
        self.guests_in_room.remove(guest)

    def add_song(self,song):
        self.list_of_songs.append(song)
    
    def charge_fee(self, guest, amount):
        guest.pay_fee(amount)
        self.money_spent_in_room += amount