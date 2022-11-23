# import turtle package
import turtle
import tkinter as tk
from tkinter import ttk
# function for movement of an object 
         

# Driver Code
if __name__ == "__main__" :
    
    # create a screen object
    root = tk.Tk()
    root.title("My drawing Program")
    canvas = tk.Canvas(root, bg="white", height=1000, width=1000)
    screen = turtle.TurtleScreen(canvas)
    # set screen size
    turtle.setworldcoordinates(0,0,100,100)

    # screen updaion 
    screen.tracer(0)           

    # create a turtle object object
    move = turtle.Turtle() 

    # set a turtle object color
    move.color('orange')

    # set turtle object speed
    move.speed(0) 

    # set turtle object width
    move.width(2)     


    # turtle object in air
    move.penup()               

    # set initial position
    move.goto(0, 0) 

    # move turtle object to surface
    move.pendown()             

    # infinite loop
    while True :
        
        # clear turtle work
        move.clear()  
        
        # forward motion by turtle object
        move.forward(0.5)      