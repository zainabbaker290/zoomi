from datetime import datetime, timedelta

class BaseDock():
    def __init__(self, Battery):
        self.base_x = 0
        self.base_y = 0 
        self.battery = Battery
        self.zoomi_location = Zoomi.location
    
    def call_zoomi_home(self):
        #zoomi base starts at (0,0)
        return (self.base_x, self.base_y)

    def raise_battery_level(self):
        while self.zoomi_location == (self.base_x, self.base_y) and self.battery.get_battery_level() < 100:
            now = datetime.now()
            time_to_charge = now + timedelta(seconds=10)
            if datetime.now() >= time_to_charge:
                self.battery.set_battery_level() 
        return self.battery.get_battery_level()