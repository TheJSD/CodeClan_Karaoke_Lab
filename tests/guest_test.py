import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1", 4, 10)
        self.song1 = Song("Rock and Roll McDonalds")
        self.guest1 = Guest("Mike", 25)

    def test_pay_fee(self):
        self.guest1.pay_fee(10)
        self.assertEqual(15, self.guest1.wallet)

    def test_assigned_fav_song(self):
        song2 = Song("I whipped Spiderman's Ass")
        self.guest1.assign_fav_song(self.song1)
        self.assertEqual(self.song1, self.guest1.favourite_song)

    def test_woo(self):
        self.room1.add_song(self.song1)
        self.room1.check_in_guest(self.guest1)
        self.guest1.assign_fav_song(self.song1)
        self.assertEqual("WHOOOOOO!", self.guest1.whoo(self.room1))