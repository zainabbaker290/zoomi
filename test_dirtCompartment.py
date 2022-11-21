import unittest
from unittest import mock
from unittest.mock import Mock
import dirt_compartment

class TestDirtCompartment(unittest.TestCase):

    def test_warn_user_1(self):
        dirt_level = 50
        self.assertLess(dirt_level, 90)

    def test_warn_user_2(self):
        dirt_level = 90
        self.assertGreaterEqual(dirt_level, 90)