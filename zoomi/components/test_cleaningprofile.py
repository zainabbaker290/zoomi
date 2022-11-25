import unittest
from unittest.mock import Mock
import cleaningprofile as cleaningprofile


class TestCleaning(unittest.TestCase):

    def test_set_power_green(self):
        result_green = Mock()
        cleaningprofile.CleaningProfile.set_power(result_green, "green")

    def test_set_power_turbo(self):
        result_turbo = Mock()
        cleaningprofile.CleaningProfile.set_power(result_turbo, "turbo")
        
    def test_set_power_default(self):
        result_default = Mock()
        cleaningprofile.CleaningProfile.set_power(result_default, "default")

    def test_set_speed_fast(self):
        result_fast = Mock()
        cleaningprofile.CleaningProfile.set_speed(result_fast, "quick clean")

    def test_set_speed_slow(self):
        result_slow = Mock()
        cleaningprofile.CleaningProfile.set_speed(result_slow, "deep clean")

    def test_set_speed_deafult(self):
        result_default = Mock()
        cleaningprofile.CleaningProfile.set_speed(result_default, "default")

    def test_set_laps_within_range(self):
        results_laps = Mock()
        cleaningprofile.CleaningProfile.set_laps(results_laps, int)