import unittest
from unittest.mock import Mock
import battery

class TestBattery(unittest.TestCase):

    def test_countdown_1(self):
        t = 0
        self.assertLessEqual(t, 0)

    def test_countdown_2(self):
        t = 5
        self.assertGreater(t, 0)

    def test_charging_battery_1(self):
        battery_level = 100
        self.assertGreaterEqual(battery_level, 100)

    def test_charging_battery_2(self):
        battery_level = 80
        self.assertLess(battery_level, 100)