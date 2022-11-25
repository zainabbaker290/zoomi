class obstacle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = width*height
        self.right =wall(x+width-1,y,1,height)
        self.left =wall(x,y,1,height)
        self.top = wall(x,y+height-1,width,1)
        self.bottom = wall(x,y,width,1)

class wall(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height