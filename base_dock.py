class BaseDock():
    def __init__(self):
        self.base_x = 0
        self.base_y = 0

    def call_zoomi_home(self):
        #zoomi base starts at (0,0)
        return (self.base_x, self.base_y)
