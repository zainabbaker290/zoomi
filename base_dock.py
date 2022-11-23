class BaseDock():
    def __init__(self):
        self.x = 0
        self.y = 0

    def call_zoomi_home(self):
        #zoomi base starts at (0,0)
        return (self.x, self.y)
