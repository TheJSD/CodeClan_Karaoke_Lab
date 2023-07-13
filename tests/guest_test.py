import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Mike", 25, "Rock and Roll McDonalds")

    def test_pay_fee(self):
        self.guest1.pay_fee(10)
        self.assertEqual(15, self.guest1.wallet)

    def test_woo(self):
        room1 = Room("Room 1", 4, 10)
        song1 = Song("Rock and Roll McDonalds")
        room1.add_song(song1)
        room1.check_in_guest(self.guest1)
        self.assertEqual("WHOOOOOO!", self.guest1.whoo_check(room1))