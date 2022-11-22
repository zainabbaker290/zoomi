class BaseDock():
    def __init__(self, Battery):
        self.base_x = 0
        self.base_y = 0 
        self.battery = Battery
    
    def call_zoomi_home(self):
        #zoomi base starts at (0,0)
        return (self.base_x, self.base_y)
