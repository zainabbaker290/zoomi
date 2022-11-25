import unittest
from unittest.mock import Mock
import sensors as sensors


class TestSensors(unittest.TestCase):

    def test_set_floor_type_carpet(self):
        result_carpet = Mock()
        sensors.Sensors.set_floor_type(result_carpet, "carpet")

    def test_set_floor_type_wooden(self):
        result_wooden = Mock()
        sensors.Sensors.set_floor_type(result_wooden, "wooden")