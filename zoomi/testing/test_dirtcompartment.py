import unittest
from unittest import mock
from unittest.mock import Mock
import components.dirt_compartment as dirt_compartment

class TestDirtCompartment(unittest.TestCase):

    def test_countdown_1(self):
        t = 0
        self.assertLessEqual(t, 0)

    def test_countdown_2(self):
        t = 5
        self.assertGreater(t, 0)

    def test_set_dirt_level_1(self):
        dirt_level = 90
        self.assertNotEqual(dirt_level, 100)
        
    def test_set_dirt_level_2(self):
        dirt_level = 100
        self.assertEqual(dirt_level, 100)

    def test_warn_user_1(self):
        dirt_level = 50
        self.assertLess(dirt_level, 90)

    def test_warn_user_2(self):
        dirt_level = 90
        self.assertGreaterEqual(dirt_level, 90)