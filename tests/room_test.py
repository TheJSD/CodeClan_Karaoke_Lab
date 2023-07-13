import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1")
        self.guest1 = Guest("Mike")
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