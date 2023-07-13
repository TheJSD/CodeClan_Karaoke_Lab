import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Rock and Roll McDonalds")

    def test_has_name(self):
        self.assertEqual("Rock and Roll McDonalds", self.song1.name)