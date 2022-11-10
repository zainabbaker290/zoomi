class CleaningMode():
    def __init__(self, Sensor):
        self.power = "default"
        self.speed = "default"
        self.zoomi_laps = 1
        self.sensor= Sensor
        self.floor = self.sensor.get_floor_type()

    def floor_detection(self, floor):
        self.floor = self.sensor.set_floor_type(floor)

    def set_power(self,power):
        if power == "green":
            self.power = "low"
        elif power == "turbo":
            self.power = "max"
        else:
            self.power = "default"
    
    def set_speed(self,speed):
        if speed == "quick clean":
            self.speed= "fast"
        elif speed == "deep clean":
            self.speed = "slow"
        else:
            self.speed = "default"

    def set_laps(self,laps):
        self.zoomi_laps = laps 