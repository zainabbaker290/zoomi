import unittest
from unittest.mock import Mock

class TestBattery(unittest.TestCase):

    def test_charge_1(self):
        battery_level = 70
        self.assertLess(battery_level, 100)

    def test_charge_2(self):
        battery_level = 100
        self.assertGreaterEqual(battery_level, 100)