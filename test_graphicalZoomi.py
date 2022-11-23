import unittest
from unittest.mock import Mock

class TestGraphicalZoomi(unittest.TestCase):

    def test_draw_obstacles_1(self):
        b_object = 10
        room_barrier = 10
        self.assertGreaterEqual(b_object, room_barrier)
        c_object = 10
        room_cliff = 10
        self.assertGreaterEqual(c_object, room_cliff)

    def test_draw_obstacles_2(self):
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        c_object = 10
        room_cliff = 10
        self.assertGreaterEqual(c_object, room_cliff)

    def test_draw_obstacles_3(self):
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        c_object = 3
        room_cliff = 10
        self.assertLess(c_object, room_cliff)

    def test_base_dock_charges_1(self):
        battery_level = 100
        self.assertGreaterEqual(battery_level, 99)

    def test_base_dock_charges_2(self):
        battery_level = 80
        self.assertLess(battery_level, 99)

    def test_zoomi_forward_1(self):
        dirt_level = 95
        self.assertGreaterEqual(dirt_level, 90)

    def test_zoomi_forward_2(self):
        dirt_level = 85
        self.assertLess(dirt_level, 90)

    #navigate home????

    def test_rotate_1(self):
        rotation = 400
        self.assertGreater(rotation, 360)

    def test_rotate_2(self):
        rotation = -120
        self.assertLess(rotation, 0)

    def test_rotate_3(self):
        rotation = 240
        self.assertLess(rotation, 360)  
        self.assertGreater(rotation, 0)  

    def test_collision_check_1(self):
        #for no
        b_object = 10
        room_barrier = 10
        self.assertGreaterEqual(b_object, room_barrier)
        #for no
        c_object = 10
        room_cliff = 10
        self.assertGreaterEqual(c_object, room_cliff)
        #if no
        room_end_y = 3
        y = 2
        self.assertGreater(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_2(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if no
        x = 12
        b_obj_x = 15
        self.assertGreaterEqual(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 12
        b_obj_y = 16
        self.assertGreaterEqual(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for no
        c_object = 10
        room_cliff = 10
        self.assertGreaterEqual(c_object, room_cliff)
        #if no
        room_end_y = 3
        y = 2
        self.assertGreater(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_3(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for no
        c_object = 10
        room_cliff = 10
        self.assertGreaterEqual(c_object, room_cliff)
        #if no
        room_end_y = 3
        y = 2
        self.assertGreater(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_4(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if no
        x = 12
        c_obj_x = 15
        self.assertGreaterEqual(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 12
        c_obj_y = 16
        self.assertGreaterEqual(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if no
        room_end_y = 3
        y = 2
        self.assertGreater(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_5(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if yes 
        x = 21
        c_obj_x = 15
        self.assertLess(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 25
        c_obj_y = 16
        self.assertLess(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if no
        room_end_y = 3
        y = 2
        self.assertGreater(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_6(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if yes 
        x = 21
        c_obj_x = 15
        self.assertLess(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 25
        c_obj_y = 16
        self.assertLess(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if yes 
        room_end_y = 3
        self.assertLessEqual(room_end_y, y)
        #if no
        self.assertLess(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_7(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if yes 
        x = 21
        c_obj_x = 15
        self.assertLess(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 25
        c_obj_y = 16
        self.assertLess(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if yes 
        room_end_y = 3
        self.assertLessEqual(room_end_y, y)
        #if yes 
        y = 0
        self.assertGreaterEqual(0, y)
        #if no
        room_end_x = 8
        x = 7
        self.assertGreater(room_end_x, x)
        #if no
        self.assertLess(0, x)
    
    def test_collision_check_8(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if yes 
        x = 21
        c_obj_x = 15
        self.assertLess(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 25
        c_obj_y = 16
        self.assertLess(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if yes 
        room_end_y = 3
        self.assertLessEqual(room_end_y, y)
        #if yes 
        y = 0
        self.assertGreaterEqual(0, y)
        #if yes 
        room_end_x = 12
        self.assertLessEqual(room_end_x, x)
        #if no
        self.assertLess(0, x)

    def test_collision_check_9(self):
        #for yes 
        b_object = 6
        room_barrier = 10
        self.assertLess(b_object, room_barrier)
        #if yes
        x = 16
        b_obj_x = 15
        self.assertLess(b_obj_x-1, x)
        b_obj_width = 13
        self.assertLess(x,(b_obj_x+b_obj_width))
        y = 20
        b_obj_y = 16
        self.assertLess(b_obj_y-1, y)
        b_obj_height = 16
        self.assertLess(y, (b_obj_y+b_obj_height+1))
        #for yes
        c_object = 7
        room_cliff = 10
        self.assertLess(c_object, room_cliff)
        #if yes 
        x = 21
        c_obj_x = 15
        self.assertLess(c_obj_x-1, x)
        c_obj_width = 13
        self.assertLess(x,(c_obj_x+c_obj_width))
        y = 25
        c_obj_y = 16
        self.assertLess(c_obj_y-1, y)
        c_obj_height = 16
        self.assertLess(y, (c_obj_y+c_obj_height+1))
        #if yes 
        room_end_y = 3
        self.assertLessEqual(room_end_y, y)
        #if yes 
        y = 0
        self.assertGreaterEqual(0, y)
        #if yes 
        room_end_x = 12
        self.assertLessEqual(room_end_x, x)
        #if yes
        x = 0
        self.assertGreaterEqual(0, x)


    def test_zoomi_movement_1(self):
        #while no
        completionPercentage = 95
        self.assertGreaterEqual(completionPercentage, 90)

    def test_zoomi_movement_2(self):
        #while yes 
        completionPercentage = 0.90
        self.assertLess(completionPercentage, 90)   
        #if no
        self.assertLessEqual(completionPercentage, 0.90) 
        #if no
        battery = 25
        self.assertGreaterEqual(battery, 20.0)
        #if no
        dirtLevel = 70
        self.assertLessEqual(dirtLevel, 90.0)
        #if no 
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertNotEqual(collision_check, True)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_3(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if no
        battery = 25
        self.assertGreaterEqual(battery, 20.0)
        #if no
        dirtLevel = 70
        self.assertLessEqual(dirtLevel, 90.0)
        #if no 
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertNotEqual(collision_check, True)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_4(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if no
        dirtLevel = 70
        self.assertLessEqual(dirtLevel, 90.0)
        #if no 
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertNotEqual(collision_check, True)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_5(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if yes 
        dirtLevel = 95
        self.assertGreater(dirtLevel, 90.0)
        #if no
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertNotEqual(collision_check, True)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_6(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 90.0)
        #if yes 
        self.assertGreater(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertNotEqual(collision_check, True)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_7(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 90.0)
        #if yes 
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertEqual(collision_check, True)
        #if no
        self.assertNotEqual(collision_check, False)
        #if no
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_8(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 90.0)
        #if yes 
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertEqual(collision_check, True)
        #if yes 
        collision_check = False
        self.assertEqual(collision_check, False)
        #if no
        collision_check = True
        self.assertNotEqual(collision_check, False)

    def test_zoomi_movement_9(self):
        #while yes 
        completionPercentage = 20
        self.assertLess(completionPercentage, 90)
        #if yes 
        self.assertGreater(completionPercentage, 0.90)
        #if yes 
        battery = 15
        self.assertLess(battery, 20.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 90.0)
        #if yes 
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertEqual(collision_check, True)
        #if yes 
        collision_check = False
        self.assertEqual(collision_check, False)
        #if yes
        self.assertEqual(collision_check, False)

    def test_activate_zoomi_1(self):
        #if no
        battery_level = 20
        self.assertGreater(battery_level, 10)
        #if no
        laps = 0
        self.assertLessEqual(laps, 1)
        #if no
        self.assertLessEqual(laps, 2)

    def test_activate_zoomi_2(self):
        #if yes 
        battery_level = 10
        self.assertLessEqual(battery_level, 10)
        #if no
        laps = 0
        self.assertLessEqual(laps, 1)
        #if no
        self.assertLessEqual(laps, 2)

    def test_activate_zoomi_3(self):
        #if yes 
        battery_level = 10
        self.assertLessEqual(battery_level, 10)
        #if yes 
        laps = 2
        self.assertGreater(laps, 1)
        #if no
        self.assertLessEqual(laps, 2)

    def test_activate_zoomi_4(self):
        #if yes 
        battery_level = 10
        self.assertLessEqual(battery_level, 10)
        #if yes 
        laps = 3
        self.assertGreater(laps, 1)
        #if yes 
        self.assertGreater(laps, 2)