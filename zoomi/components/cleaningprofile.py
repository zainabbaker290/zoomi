class CleaningProfile():
    def __init__(self,mode,speed,laps, Sensor):
        self.mode = mode
        self.speed = speed
        self.laps = laps
        self.sensor= Sensor
        self.floor = self.sensor.get_floor_type()
    
    def floor_detection(self, floor):
        self.floor = self.sensor.set_floor_type(floor)
    
    def get_floor(self):
        return self.floor

    def set_mode(self,mode):
        if mode == "Green":
            self.mode = "low"
        elif mode == "Turbo":
            self.mode = "max"
        else:
            self.mode = "Default"
    
    def get_mode(self):
        return self.mode
    
    def set_speed(self,speed):
        if speed == "Quick Clean":
            self.speed= "fast"
        elif speed == "Deep Clean":
            self.speed = "slow"
        else:
            self.speed = "default"
    
    def get_speed(self):
        return self.speed

    def set_laps(self,laps):
        if laps == "One Lap":
            self.laps = 1
        if laps == "Two Laps":
            self.laps = 2
        if laps == "Three Laps":
            self.laps = 3 

    def get_laps(self):
        return self.laps
    
    def __str__(self):
        return 'The mode of the zoomi is currently on ' + self.get_mode() + " and the speed is currently at " + self.get_speed() + ". " + " It is currently sensing a " + self.get_floor() + " floor type and will do " + str(self.get_laps())