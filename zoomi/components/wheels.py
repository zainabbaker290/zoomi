class Wheels:
    def __init__(self):
        self.wheels = 0

    def turn_wheels(self):
        if self.wheels == 360:
            self.wheels = 0 
        else:
            self.wheels += 90 