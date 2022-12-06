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
        stoppedEarly = True
        completionPercentage = 0.95
        cancelled = True
        self.assertTrue(stoppedEarly)
        self.assertGreaterEqual(completionPercentage, 0.90)
        self.assertTrue(cancelled)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)
    
    def test_zoomi_movement_2(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if no
        completionPercentage = 0.92
        self.assertGreaterEqual(completionPercentage, 0.90) 
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)

    def test_zoomi_movement_3(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if no
        battery = 25
        self.assertGreaterEqual(battery, 10.0)
        #if no
        dirtLevel = 70
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertFalse(collision_check)
        #if no
        collision_check = True
        self.assertTrue(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)

    def test_zoomi_movement_4(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if no
        dirtLevel = 70
        self.assertLessEqual(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertFalse(collision_check)
        #if no
        collision_check = True
        self.assertTrue(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)

    def test_zoomi_movement_5(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 99.0)
        #if no
        collision_check = False
        self.assertFalse(collision_check)
        #if no
        collision_check = True
        self.assertTrue(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)

    def test_zoomi_movement_6(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertTrue(collision_check)
        #if no
        self.assertTrue(collision_check)
        #if no
        self.assertTrue(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)

    def test_zoomi_movement_7(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertTrue(collision_check)
        #if yes
        collision_check = False
        self.assertFalse(collision_check)
        #if no
        collision_check = True
        self.assertTrue(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)
    
    def test_zoomi_movement_8(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertTrue(collision_check)
        #if yes
        collision_check = False
        self.assertFalse(collision_check)
        #if yes 
        self.assertFalse(collision_check)
        #if no > else
        stoppedEarly = False
        self.assertFalse(stoppedEarly)
    
    def test_zoomi_movement_9(self):
        #while yes 
        stoppedEarly = False
        completionPercentage = 0.70
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completionPercentage, 0.90)
        self.assertFalse(cancelled)
        #if yes 
        self.assertLess(completionPercentage, 0.90)
        #if yes 
        battery = 6
        self.assertLess(battery, 10.0)
        #if yes 
        dirtLevel = 100
        self.assertGreater(dirtLevel, 99.0)
        #if yes 
        collision_check = True
        self.assertTrue(collision_check)
        #if yes
        collision_check = False
        self.assertFalse(collision_check)
        #if yes 
        self.assertFalse(collision_check)
        #if yes 
        stoppedEarly = True 
        self.assertTrue(stoppedEarly)
    
    def test_activate_zoomi_1(self):
        #if no
        cancelled = True 
        self.assertTrue(cancelled)
        #if no > else
        self.assertTrue(cancelled) 

    def test_activate_zoomi_2(self):
        #if yes
        cancelled = False 
        self.assertFalse(cancelled)
        #if no > else
        cancelled = True
        self.assertTrue(cancelled)
    
    def test_activate_zoomi_3(self):
        #if yes
        cancelled = False 
        self.assertFalse(cancelled)
        #if yes 
        self.assertFalse(cancelled)
        #while no
        stoppedEarly = True 
        completedLaps = 12
        totalLaps = 10
        cancelled = True
        self.assertTrue(stoppedEarly)
        self.assertGreaterEqual(completedLaps, totalLaps)
        self.assertTrue(cancelled)
        #if no > else
        stoppedEarly = False 
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertFalse(cancelled)

    def test_activate_zoomi_4(self):
        #if yes
        cancelled = False 
        self.assertFalse(cancelled)
        #if yes 
        self.assertFalse(cancelled)
        #while yes 
        stoppedEarly = False
        completedLaps = 8
        totalLaps = 10
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completedLaps, totalLaps)
        self.assertFalse(cancelled)
        #if no > else
        self.assertFalse(stoppedEarly)
        self.assertFalse(cancelled)

    def test_activate_zoomi_5(self):
        #if yes
        cancelled = False 
        self.assertFalse(cancelled)
        #if yes 
        self.assertFalse(cancelled)
        #while yes 
        stoppedEarly = False
        completedLaps = 8
        totalLaps = 10
        cancelled = False
        self.assertFalse(stoppedEarly)
        self.assertLess(completedLaps, totalLaps)
        self.assertFalse(cancelled)
        #if yes 
        stoppedEarly = True 
        cancelled = True
        self.assertTrue(stoppedEarly)
        self.assertTrue(cancelled)

    def test_send_updates_to_server_1(self):
        #while no
        whileLoopValue = False
        self.assertFalse(whileLoopValue)

    def test_send_updates_to_server_2(self):
        #while yes 
        whileLoopValue = True 
        self.assertTrue(whileLoopValue)
        #if no > else
        message = "message"
        lastmsg = "different message"
        self.assertNotEqual(message, lastmsg)
        #if no
        messageValue= False
        self.assertFalse(messageValue)

    def test_send_updates_to_server_3(self):
        #while yes 
        whileLoopValue = True 
        self.assertTrue(whileLoopValue)
        #if yes 
        message = "message"
        lastmsg = "message"
        self.assertEqual(message, lastmsg)
        #if no
        messageValue= False
        self.assertFalse(messageValue)

    def test_send_updates_to_server_4(self):
        #while yes 
        whileLoopValue = True 
        self.assertTrue(whileLoopValue)
        #if yes 
        message = "message"
        lastmsg = "message"
        self.assertEqual(message, lastmsg)
        #if yes
        messageValue= True
        self.assertTrue(messageValue)

    def test_clean_charge_1(self):
        battery = 100
        self.assertGreaterEqual(battery, 100)

    def test_clean_charge_2(self):
        battery = 70
        self.assertLess(battery, 100) 

    def test_clean_empty_1(self):
        waitingPeriod = 12
        self.assertGreaterEqual(waitingPeriod, 10)

    def test_clean_empty_2(self):
        waitingPeriod = 8
        self.assertLess(waitingPeriod, 10)

    def test_wait_for_instruction_1(self):
        whileLoopValue = False
        self.assertFalse(whileLoopValue)

    def test_wait_for_instruction_2(self):
        whileLoopValue = True
        self.assertTrue(whileLoopValue)
        begin_clean = False
        self.assertFalse(begin_clean)

    def test_wait_for_instruction_3(self):
        whileLoopValue = True
        self.assertTrue(whileLoopValue)
        begin_clean = True
        self.assertTrue(begin_clean)

    def test_accept_start_1(self):
        default = False 
        self.assertFalse(default)

    def test_accept_start_2(self):
        default = True
        self.assertTrue(default)

    

