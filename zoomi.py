class Zoomi:
    def __init__(self, Battery, Sensors, Light, DirtCompartment, CleaningMode, Wheels, BaseDock) -> None:
        self.battery = Battery
        self.sensors = Sensors
        self.light = Light
        self.dirt_compartment = DirtCompartment
        self.cleaning_mode = CleaningMode
        self.wheels = Wheels
        self.base_dock = BaseDock
        self.state = "deactivated"

    def set_zoomi_state(self,state):
        self.state = state 
    
    def mid_clean_charge(self):
        self.set_zoomi_state("sleep")
        self.sensors.navigate_home()
        self.light.set_light("orange")
        return self.battery.get_battery_level()
    

    def activate_zoomi(self):
        if self.battery.get_battery_level() <= 10:
            self.mid_clean_charge()
            self.set_zoomi_state("activated")

        self.dirt_compartment.warn_user()
        
        #checks state its in --> if state sleep, means it needs to finish clean 
        
        #constantly pings battery level to see if its below 10%, if below, goes back to base 

        #naviagtes around room 
        #does cleaning mode that is activated 
        #constantly calls on sensors 
        #once finished return to base dock
        #removes some battery percentage and adds dirt to dirt compartment
    
        pass