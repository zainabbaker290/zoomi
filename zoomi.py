
class Zoomi:
    def __init__(self, Battery, Sensors, Light, DirtCompartment, CleaningMode, Wheels, Room, BaseDock) -> None:
        self.battery = Battery
        self.sensors = Sensors
        self.light = Light
        self.dirt_compartment = DirtCompartment
        self.cleaning_mode = CleaningMode
        self.wheels = Wheels
        self.state = "deactivated"
        self.zoomi_x = 0 
        self.zoomi_y = 0
        self.room = Room
        self.location = self.zoomi_x, self.zoomi_y
        self.saved_location = None
        self.base_dock = BaseDock

    def set_zoomi_state(self,state):
        self.state = state 
        print("zoomi is now " + self.state)
    
    def base_dock_charges(self):
        while self.location == self.base_dock.call_zoomi_home() and self.battery.get_battery_level() < 100:
            self.battery.charging_battery()
        return print("battery is fully charged at " + str(self.battery.get_battery_level()))
    
    def zoomi_forward(self, forward_movement):
        self.zoomi_y += forward_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        if self.dirt_compartment.get_dirt_level() > 90:
            self.dirt_compartment.warn_user()
        return self.location

    def zoomi_backward(self, backward_movement):
        self.zoomi_y -= backward_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        return self.location
    
    def zoomi_right(self, right_movement):
        self.zoomi_x += right_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        return self.location
    
    def zoomi_left(self,left_movement):
        self.zoomi_x -= left_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        return self.location
    
    def navigate_home(self,saved_location = None):
        if self.saved_location != None:
            self.saved_location = self.location
        self.zoomi_backward(self.zoomi_y)
        self.zoomi_left(self.zoomi_x)
        self.base_dock_charges()
        return self.location

    def mid_clean_charge(self):
        print("zoomi is entering a sleep state")
        self.set_zoomi_state("sleep")
        print(self.state)
        print("en route to base dock")
        self.navigate_home(self.location)
        print("at home")
        self.light.set_light("orange")
        self.battery.charging_battery()
        self.base_dock_charges()
    
    def zoomi_forward(self, forward_movement):
        self.zoomi_y += forward_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        if self.dirt_compartment.get_dirt_level() > 90:
            self.dirt_compartment.warn_user()
        print(self.location)
        return self.location

    def zoomi_backward(self, backward_movement):
        self.zoomi_y -= backward_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        print(self.location)
        return self.location
    
    def zoomi_right(self, right_movement):
        self.zoomi_x += right_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        print(self.location)
        return self.location
    
    def zoomi_left(self,left_movement):
        self.zoomi_x -= left_movement
        self.location = self.zoomi_x,self.zoomi_y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        print(self.location)
        return self.location
    
    def navigate_home(self,saved_location = None):
        if self.saved_location != None:
            self.saved_location = self.location
        self.zoomi_backward(self.zoomi_y)
        self.zoomi_left(self.zoomi_x)
        self.base_dock_charges()
        return self.location

    def mid_clean_charge(self):
        print("zoomi is entering a sleep state")
        self.set_zoomi_state("sleep")
        print(self.state)
        print("en route to base dock")
        self.navigate_home(self.location)
        print("at home")
        self.light.set_light("orange")
        self.battery.charging_battery()
        self.base_dock_charges()

    def zoomi_movement(self):
        while (self.zoomi_x < self.room.end_x) and (self.zoomi_y < self.room.end_y):
            print("moving")
            while self.room.end_y >  self.zoomi_y:
                self.zoomi_forward(1)
                if self.battery.get_battery_level() < 0:
                    print("going for a mid_clean_charge")
                    return self.mid_clean_charge()
                if self.dirt_compartment.get_dirt_level() > 90:
                    self.dirt_compartment.warn_user()
                for value in self.room.barrier.values():
                    if self.zoomi_y == value:
                        self.sensors.barrier_detected()
                        print("barrier detected")
                        self.zoomi_right(1)
                for value in self.room.cliff.values():
                    if self.zoomi_y == value:
                        self.sensors.cliff_detected()
                        print("cliff detected")
                        self.zoomi_right(1)

            if self.room.end_y == self.zoomi_y:
                self.wheels.turn_wheels()
                self.zoomi_right(1) 
                
            
            while self.room._start_y < self.zoomi_y:
                self.zoomi_backward(1)
                if self.battery.get_battery_level() < 0:
                    print("going for a mid_clean_charge")
                    return self.mid_clean_charge()
                if self.dirt_compartment.get_dirt_level() > 90:
                    self.dirt_compartment.warn_user()
                for value in self.room.barrier.values():
                    if self.zoomi_y == value:
                        self.sensors.barrier_detected()
                        print("barrier detected")
                        self.zoomi_right(1)
                for value in self.room.cliff.values():
                    if self.zoomi_y == value:
                        self.sensors.cliff_detected()
                        print("cliff detected")
                        self.zoomi_right(1)
            
            if self.room._start_y == self.zoomi_y:
                self.wheels.turn_wheels()
                self.zoomi_right(1) 

        print("finshed cleaning, going home")        
        self.navigate_home()
        
    def activate_zoomi(self):
        if self.battery.get_battery_level() <= 10:
            print("battery low, going home to recharge")
            self.mid_clean_charge()
        elif self.state == "sleep":
            print("returning to last cleaned location")
            self.zoomi_forward(self.saved_location[0])
            self.zoomi_right(self.saved_location[1])

        self.dirt_compartment.warn_user()

        self.set_zoomi_state("active")
        self.light.set_light("green")
        self.zoomi_movement()
        return self.set_zoomi_state("deactivated")
