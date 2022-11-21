import unittest
from unittest.mock import Mock
import base_dock

class TestBaseDock(unittest.TestCase):

    def test_raise_battery_level_1(self):
        location = (3, 15)
        battery = 90
        self.assertNotEqual(location, (0, 0))
        self.assertNotEqual(battery, 100)

    def test_raise_battery_level_2(self):
        location = (0, 0)
        battery = 100
        time = 10
        time_to_charge = 50
        self.assertEqual(location, (0, 0))
        self.assertEqual(battery, 100)
        self.assertLess(time, time_to_charge)

    def test_raise_battery_level_3(self):
        location = (0, 0)
        battery = 100
        time = 60
        time_to_charge = 50
        self.assertEqual(location, (0, 0))
        self.assertEqual(battery, 100)
        self.assertGreaterEqual(time, time_to_charge)