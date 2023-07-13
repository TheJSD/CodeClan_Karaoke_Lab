import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Mike", 25)

    def test_pay_fee(self):
        self.guest1.pay_fee(10)
        self.assertEqual(15, self.guest1.wallet)