class CleaningProfile():
    def __init__(self,power,speed,laps, Sensor):
        self.power = power
        self.speed = speed
        self.laps = laps
        self.sensor= Sensor
        self.floor = self.sensor.get_floor_type()

    def floor_detection(self, floor):
        self.floor = self.sensor.set_floor_type(floor)
    
    def get_floor(self):
        return self.floor

    def set_power(self,power):
        if power == "green":
            self.power = "low"
        elif power == "turbo":
            self.power = "max"
        else:
            self.power = "default"
    
    def get_power(self):
        return self.power
    
    def set_speed(self,speed):
        if speed == "quick clean":
            self.speed= "fast"
        elif speed == "deep clean":
            self.speed = "slow"
        else:
            self.speed = "default"
    
    def get_speed(self):
        return self.speed

    def set_laps(self,laps):
        self.laps = laps 
    
    def get_laps(self):
        return self.laps
    
    def __str__(self):
        return 'The power of the zoomi is currently on ' + self.get_power() + " and the speed is currently at " + self.get_speed() + ". " + " It is currently sensing a " + self.get_floor() + " floor type and will do " + str(self.get_laps()) + " laps"