import turtle


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

    def draw(self):
        obstacleDraw = turtle.Turtle()
        x = self.x
        y = self.y
        x2 =self.x + self.width
        y2 =self.y +self.height
        obstacleDraw.speed(100)
        obstacleDraw.penup()
        obstacleDraw.hideturtle()
        obstacleDraw.goto(x,y)
        obstacleDraw.clear()
        obstacleDraw.begin_fill()
        turtle.pendown()
        obstacleDraw.goto(x,y2)
        obstacleDraw.goto(x2,y2)
        obstacleDraw.goto(x2,y)
        obstacleDraw.goto(x,y)
        obstacleDraw.end_fill()
        turtle.penup()
        obstacleDraw.hideturtle()

    def draw_walls(self):
        obstacleDraw = turtle.Turtle()
        obstacleDraw.color("red")
        self.right.draw(obstacleDraw)
        obstacleDraw = turtle.Turtle()
        obstacleDraw.color("blue")
        self.left.draw(obstacleDraw)
        obstacleDraw = turtle.Turtle()
        obstacleDraw.color("green")
        self.top.draw(obstacleDraw)
        obstacleDraw = turtle.Turtle()
        obstacleDraw.color("yellow")
        self.bottom.draw(obstacleDraw)

class wall():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self,obstacleDraw):
        x = self.x
        y = self.y
        x2 =self.x + self.width
        y2 =self.y +self.height
        obstacleDraw.speed(100)
        obstacleDraw.penup()
        obstacleDraw.hideturtle()
        obstacleDraw.goto(x,y)
        obstacleDraw.clear()
        obstacleDraw.begin_fill()
        turtle.pendown()
        obstacleDraw.goto(x,y2)
        obstacleDraw.goto(x2,y2)
        obstacleDraw.goto(x2,y)
        obstacleDraw.goto(x,y)
        obstacleDraw.end_fill()
        turtle.penup()
        obstacleDraw.hideturtle()