class Battery:
    def __init__(self):
        #all zoomis start with 50% battery 
        self.battery_level = 50
        pass
    
    def get_battery_level(self):
        return self.battery_state
    
    def set_battery_level(self):
        self.battery_level = self.battery_level + 10
        return self.battery_level
