import time
class Battery:
    def __init__(self):
        #all zoomis start with 50% battery 
        self.battery_level = 50
    
    def get_battery_level(self):
        return self.battery_level
    
    def update(self, level):
        self.battery_level = self.battery_level + level
        return self.battery_level
    
    def charge(self):
        self.battery_level+=1
        print("currently charging")
        print("battery is now " + str(self.get_battery_level()))
        if self.battery_level > 100:
            self.battery_level = 100
        return self.get_battery_level()

