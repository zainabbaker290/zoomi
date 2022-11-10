class Sensors:
    def __init__(self, Wheels):
        #assumes wooden floor unless detects something else
        self.floor_type = "wooden"
        self.location = (0,0)
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

    # a bit confused if this should be zoomi class or what 
    def navigate_home():

        #navigates back home to base 
        #get base co
        #get zoomi co 
        #do distance forumla 
        #call other sensors
        pass 

    def set_location(self,location):
        #saves location its in 
        pass 

    def get_location():
        #saves location its in 
        pass 


