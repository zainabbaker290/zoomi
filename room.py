class Room:
    def __init__(self,end_x, end_y,barrier,cliff):
        self._start_x = 0
        self._start_y = 0 
        self.end_x = end_x
        self.end_y = end_y
        self.barrier = barrier #dictionary
        self.cliff = cliff #dictionary
    