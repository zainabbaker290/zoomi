class Room:
    def __init__(self,end_x, end_y,barrier,cliff):
        self._start_x = 0
        self._start_y = 0 
        self.width = end_x
        self.height = end_y
        self.end_x = end_x
        self.end_y = end_y
        self.barrier = barrier #list
        self.cliff = cliff #list
        self.area = end_x * end_y
        for object in self.barrier:
            self.area =  self.area - object.area
        for object in self.cliff:   
            self.area =  self.area - object.area