import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1", 4, 10)
        self.guest1 = Guest("Mike", 25)
        self.song1 = Song("Rock and Roll McDonalds")

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual([self.guest1], self.room1.guests_in_room)
    
    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual([], self.room1.guests_in_room)

    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual([self.song1], self.room1.list_of_songs)
    
    def test_room_limit_check(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest1) # adding in the same guest because it was faster than making multiple seperate guests
        self.room1.check_in_guest(self.guest1) # extra guest
        self.assertEqual([self.guest1, self.guest1, self.guest1, self.guest1], self.room1.guests_in_room)
    
    def test_charge_fee(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(15, self.guest1.wallet)
        self.assertEqual(10, self.room1.money_spent_in_room)