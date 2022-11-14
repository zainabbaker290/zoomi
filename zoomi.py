class Zoomi:
    def __init__(self, Battery, Sensors, Light, DirtCompartment, CleaningMode, Wheels, BaseDock, Room) -> None:
        self.battery = Battery
        self.sensors = Sensors
        self.light = Light
        self.dirt_compartment = DirtCompartment
        self.cleaning_mode = CleaningMode
        self.wheels = Wheels
        self.base_dock = BaseDock
        self.state = "deactivated"
        self.zoomi_x = 0 
        self.zoomi_y = 0
        self.room = Room
        self.location = self.zoomi_x, self.zoomi_y
        self.saved_location = None

    def set_zoomi_state(self,state):
        self.state = state 
    
    def mid_clean_charge(self):
        self.set_zoomi_state("sleep")
        self.navigate_home(self.location)
        self.light.set_light("orange")
        return self.battery.get_battery_level()
    
    def zoomi_forward(self, forward_movement):
        self.zoomi_y += forward_movement
        self.location = self.zoomi_x,self.zoomi_y
        return self.location

    def zoomi_backward(self, backward_movement):
        self.zoomi_y -= backward_movement
        self.location = self.zoomi_x,self.zoomi_y
        return self.location
    
    def zoomi_right(self, right_movement):
        self.zoomi_x += right_movement
        self.location = self.zoomi_x,self.zoomi_y
        return self.location
    
    def zoomi_left(self,left_movement):
        self.zoomi_x -= left_movement
        self.location = self.zoomi_x,self.zoomi_y
        return self.location
    
    #use sensors here too just giving me headache rn 
    #i dont know how this is going to work, feel its going to do my diagram
    #check wheels maybe can put them into small zoomi things 
    #okay to fix diagram thing i did a whole x meets the spot thing like in a tresure hunt 
    #so when it reaches end point go home - relaistically not good 
    #okay need to find out how to add to dirt compartment 
    def zoomi_movement(self):
        while (self.zoomi_x < self.room.end_x) and (self.zoomi_y < self.room.end_y):
            while self.room.end_y >  self.zoomi_y:
                self.zoomi_forward(1)
                for value in self.room.barrier.values():
                    if self.zoomi_y == value:
                        self.zoomi_right(1)

            if self.room.end_y == self.zoomi_y:
                self.zoomi_right(1) 
                #turn the wheels
            
            while self.room._start_y < self.zoomi_y:
                self.zoomi_backward(1)
                for value in self.room.barrier.values():
                    if self.zoomi_y == value:
                        self.zoomi_right(1)
            
            if self.room._start_y == self.zoomi_y:
                self.zoomi_right(1) 
                #turn the wheels 
        
        self.navigate_home()
        
    def navigate_home(self,saved_location = None):
        if self.saved_location != None:
            self.saved_location = self.location
        self.zoomi_backward(self.zoomi_y)
        self.zoomi_left(self.zoomi_x)
        return self.location

    #getting stuck on tying it all together 
    #feeling hurgeqgnpiuget so pushing and living and then relooking 
    
    def activate_zoomi(self):
        if self.battery.get_battery_level() <= 10:
            self.mid_clean_charge()
        elif self.state == "sleep":
            self.zoomi_forward(self.saved_location[0])
            self.zoomi_right(self.saved_location[1])

        self.dirt_compartment.warn_user()
    
        #constantly pings battery level to see if its below 10%, if below, goes back to base 
        self.set_zoomi_state("active")
        self.light.set_light("green")
        self.battert.set_battery_level(-10)
        self.dirt_compartment.set_dirt_level(10)
        #how are we going to code this 
        #does cleaning mode that is activated 
        #constantly calls on sensors 
        #once finished return to base dock
    
        pass