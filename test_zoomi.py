import unittest
from unittest.mock import Mock
import zoomi


class TestZoomi(unittest.TestCase):

    def test_navigate_home_not_Null(self):
        result_location = Mock()
        zoomi.Zoomi.navigate_home(result_location, [2,3])