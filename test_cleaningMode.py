import unittest
from unittest.mock import Mock
import cleaning_mode


class TestCleaning(unittest.TestCase):

    def test_set_power_green(self):
        result_green = Mock()
        cleaning_mode.CleaningMode.set_power(result_green, "green")

    def test_set_power_turbo(self):
        result_turbo = Mock()
        cleaning_mode.CleaningMode.set_power(result_turbo, "turbo")
        
    def test_set_power_default(self):
        result_default = Mock()
        cleaning_mode.CleaningMode.set_power(result_default, "default")

    def test_set_speed_fast(self):
        result_fast = Mock()
        cleaning_mode.CleaningMode.set_speed(result_fast, "quick clean")

    def test_set_speed_slow(self):
        result_slow = Mock()
        cleaning_mode.CleaningMode.set_speed(result_slow, "deep clean")

    def test_set_speed_deafult(self):
        result_default = Mock()
        cleaning_mode.CleaningMode.set_speed(result_default, "default")

    def test_set_laps_within_range(self):
        results_laps = Mock()
        cleaning_mode.CleaningMode.set_laps(results_laps, int)