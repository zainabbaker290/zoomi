
class DirtCompartment:
    def __init__(self):
        self.dirt_level = 0

    def update(self,level):
        self.dirt_level += level
        if self.dirt_level > 100:
            self.warn_user()
            self.dirt_level = 100

    def get_dirt_level(self):
        return self.dirt_level

