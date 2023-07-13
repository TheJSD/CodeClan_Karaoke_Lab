import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1")
        self.guest1 = Guest("Mike")

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual([self.guest1], self.room1.guests_in_room)