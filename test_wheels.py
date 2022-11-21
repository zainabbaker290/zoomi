import unittest
from unittest import mock
from unittest.mock import Mock
#import wheels #only in basedock branch


class TestWheels(unittest.TestCase):

    def test_turn_wheels_1(self):
        wheels = 360
        self.assertNotEqual(wheels, 360)
    
    def test_turn_wheels_2(self):
        wheels = 80
        self.assertNotEqual(wheels, 360)