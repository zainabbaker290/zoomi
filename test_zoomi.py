import unittest
from unittest.mock import Mock
import zoomi


class TestZoomi(unittest.TestCase):

    def test_base_dock_charges_1(self):
        location = False
        call_zoomi_home = True
        battery_level = 100
        self.assertNotEqual(location, call_zoomi_home)
        self.assertGreaterEqual(battery_level, 100)

    def test_base_dock_charges_2(self):
        location = True
        call_zoomi_home = True
        battery_level = 80
        self.assertEqual(location, call_zoomi_home)
        self.assertLess(battery_level, 100)


    def test_navigate_home_not_None(self):
        result_location = Mock()
        zoomi.Zoomi.navigate_home(result_location, [2,3])

    def test_navigate_home_None(self):
        result_location = Mock()
        zoomi.Zoomi.navigate_home(result_location, None)

    def test_zoomi_movement_1(self):
        #while no
        zoomi_x = 10
        end_x = 5
        zoomi_y = 9
        end_y = 4
        self.assertGreater(zoomi_x, end_x)
        self.assertGreater(zoomi_y, end_y)

    def test_zoomi_movement_2(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        self.assertLess(zoomi_y, end_y)
        #while no + if no
        zoomi_y = 6
        self.assertGreaterEqual(zoomi_y, end_y)
        #while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_3(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for no
        barrier_values = 10
        Bvalues = 10
        self.assertGreaterEqual(Bvalues, barrier_values)
        #for no
        cliff_values = 10
        Cvalues = 10
        self.assertGreaterEqual(Cvalues, cliff_values)
        #if no
        self.assertNotEqual(end_y, zoomi_y)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_4(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 5
        self.assertLess(Bvalue, barrier_values)
        #if no 
        self.assertNotEqual(zoomi_y, Bvalue)
        #for no
        cliff_values = 10
        Cvalues = 10
        self.assertGreaterEqual(Cvalues, cliff_values)
        #if no
        self.assertNotEqual(end_y, zoomi_y)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_5(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for no
        cliff_values = 10
        Cvalues = 10
        self.assertGreaterEqual(Cvalues, cliff_values)
        #if no
        self.assertNotEqual(end_y, zoomi_y)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_6(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalues = 6
        self.assertLess(Cvalues, cliff_values)
        #if no
        self.assertNotEqual(end_y, zoomi_y)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_7(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_8(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        ##while no + if no
        start_y = 8
        self.assertGreaterEqual(start_y, zoomi_y)

    def test_zoomi_movement_9(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for no
        B2value = 10
        barrier_values2 = 10
        self.assertEqual(B2value, barrier_values2)
        #for no
        C2value = 10
        cliff_values2 = 10
        self.assertEqual(C2value, cliff_values2)
        #if no 
        self.assertNotEqual(start_y, zoomi_y)

    def test_zoomi_movement_10(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for yes 
        B2value = 5
        barrier_values2 = 10
        self.assertLess(B2value, barrier_values2)
        #if no
        self.assertNotEqual(zoomi_y, B2value)
        #for no
        C2value = 10
        cliff_values2 = 10
        self.assertEqual(C2value, cliff_values2)
        #if no 
        self.assertNotEqual(start_y, zoomi_y)

    def test_zoomi_movement_11(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for yes 
        B2value = 4
        barrier_values2 = 10
        self.assertLess(B2value, barrier_values2)
        #if yes 
        self.assertEqual(zoomi_y, B2value)
        #for no
        C2value = 10
        cliff_values2 = 10
        self.assertEqual(C2value, cliff_values2)
        #if no 
        self.assertNotEqual(start_y, zoomi_y)

    def test_zoomi_movement_12(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for yes 
        B2value = 4
        barrier_values2 = 10
        self.assertLess(B2value, barrier_values2)
        #if yes 
        self.assertEqual(zoomi_y, B2value)
        #for yes 
        C2value = 7
        cliff_values2 = 10
        self.assertLess(C2value, cliff_values2)
        #if no
        self.assertNotEqual(zoomi_y, C2value)
        #if no
        self.assertNotEqual(start_y, zoomi_y)

    def test_zoomi_movement_13(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for yes 
        B2value = 4
        barrier_values2 = 10
        self.assertLess(B2value, barrier_values2)
        #if yes 
        self.assertEqual(zoomi_y, B2value)
        #for yes 
        C2value = 4
        cliff_values2 = 10
        self.assertLess(C2value, cliff_values2)
        #if yes 
        self.assertEqual(zoomi_y, C2value)
        #if no
        self.assertNotEqual(start_y, zoomi_y)

    def test_zoomi_movement_14(self):
        #while yes 
        zoomi_x = 2
        end_x = 5
        zoomi_y = 1
        end_y = 4
        self.assertLess(zoomi_x, end_x)
        #while yes
        self.assertLess(zoomi_y, end_y)
        #for yes 
        barrier_values = 10
        Bvalue = 1
        self.assertLess(Bvalue, barrier_values)
        #if yes 
        self.assertEqual(zoomi_y, Bvalue)
        #for yes 
        cliff_values = 10
        Cvalue = 1
        self.assertLess(Cvalue, cliff_values)
        #if yes 
        self.assertEqual(zoomi_y, Cvalue)
        #if yes 
        zoomi_y = 4
        self.assertEqual(end_y, zoomi_y)
        #while yes 
        start_y = 3
        self.assertLess(start_y, zoomi_y)
        #for yes 
        B2value = 4
        barrier_values2 = 10
        self.assertLess(B2value, barrier_values2)
        #if yes 
        self.assertEqual(zoomi_y, B2value)
        #for yes 
        C2value = 4
        cliff_values2 = 10
        self.assertLess(C2value, cliff_values2)
        #if yes 
        self.assertEqual(zoomi_y, C2value)
        #if yes 
        zoomi_y = 3
        self.assertEqual(start_y, zoomi_y)

    def test_activate_zoomi_1(self):
        battery_level = 10
        self.assertLessEqual(battery_level, 10)

    def test_activate_zoomi_2(self):
        state = "sleep"
        self.assertEqual(state, "sleep")

    def test_activate_zoomi_3(self):
        battery_level = 15
        state = Mock()
        self.assertGreater(battery_level, 10)
        self.assertNotEqual(state, "sleep")