import time
class DirtCompartment:
    def __init__(self):
        self.dirt_level = 0

    def countdown(self,t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def set_dirt_level(self,level):
        self.dirt_level += level
        if self.dirt_level > 100:
            self.warn_user()
            self.dirt_level = 100

    def get_dirt_level(self):
        return self.dirt_level

    def warn_user(self):
        if self.dirt_level >= 90:
            return "please empty dirt compartment"

    def wait_for_user(self):
        print("Waiting for user to empty compartment...")
        self.countdown(10)
        self.dirt_level = 0
        print("compartment has been emptied!")
