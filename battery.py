import time
class Battery:
    def __init__(self):
        #all zoomis start with 50% battery 
        self.battery_level = 50
    
    def get_battery_level(self):
        return self.battery_level
    
    def set_battery_level(self):
        self.battery_level = self.battery_level + 10
        return self.battery_level
    
    def countdown(self,t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    
    def charging_battery(self):
        self.countdown(1)
        self.set_battery_level() 
        print("currently charging")
        print("battery is now " + str(self.get_battery_level()))
        return self.get_battery_level()

