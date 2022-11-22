class Sensors:
    def __init__(self, Wheels):
        #assumes wooden floor unless detects something else
        self.floor_type = "wooden"
        self.cliff = False 
        self.barrier = False
        self.upside_down = False
        self.wheels = Wheels

    def set_floor_type(self, floor_type):
        if floor_type == "carpet":
            self.floor_type = "carpet"
        else:
            self.floor_type = "wooden"
    
    def get_floor_type(self):
        return self.floor_type

    def cliff_detected(self):
        self.wheels.turn_wheels()
        self.cliff = False 

    def get_cliff_detected(self):
        return self.cliff

    def barrier_detected(self):
        self.wheels.turn_wheels()
        self.barrier= False

    def get_barrier_detected(self):
        return self.barrier

    def upside_detected(self):
        return self.upside_down == True 
    
    def reset_upside_down(self):
        return self.upside_down == False



