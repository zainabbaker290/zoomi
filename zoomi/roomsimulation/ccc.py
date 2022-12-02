def initialise_cleaning_profile(self):
        if self.currentSpeed == "Quick Clean":
            self.delay = 0
        elif self.currentSpeed == "Deep Clean":
            self.delay = 0.04
        else:
            self.delay = 0.02
        if self.currentMode == "Turbo":
            self.powerConsumptionModifier = -0.02
            self.suctionPowerModifier = 0.02
        elif self.currentMode == "Green":
            self.powerConsumptionModifier = -0.005
            self.suctionPowerModifier = 0.005
        else:
            self.powerConsumptionModifier = -0.01
            self.suctionPowerModifier = 0.01
        if self.currentLaps == "One Lap":
            self.currentLaps = 1
        elif self.currentLaps == "Two Laps":
            self.currentLaps = 2
        elif self.currentLaps == "Three Laps":
            self.currentLaps = 3