import unittest
from unittest import mock
from unittest.mock import Mock
import dirtcompartment as dirtcompartment

class TestDirtCompartment(unittest.TestCase):

    def test_update_1(self):
        dirt_level = 90
        self.assertNotEqual(dirt_level, 100)
        
    def test_update_2(self):
        dirt_level = 100
        self.assertEqual(dirt_level, 100)