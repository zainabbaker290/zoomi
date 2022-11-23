import turtle
import tkinter as tk
from tkinter import ttk
import math
import random


class GraphicalZoomi:
    def __init__(self, Battery, Sensors, Light, DirtCompartment, CleaningMode, Wheels, Room, BaseDock) -> None:
        self.battery = Battery
        self.sensors = Sensors
        self.light = Light
        self.dirt_compartment = DirtCompartment
        self.cleaning_mode = CleaningMode
        self.wheels = Wheels
        self.state = "deactivated"
        self.x = 0 
        self.y = 0
        self.lastX = 0 
        self.lastY = 0
        self.cleanedArea = []
        self.room = Room
        self.location = self.x, self.y
        self.base_dock = BaseDock
        self.rotation = 180
        self.initialiseTurtle()

    def draw_obstacles(self):
        for object in self.room.barrier:
            x = object.x
            y = object.y
            x2 =object.x + object.width
            y2 =object.y +object.height
            obstacleDraw =turtle.Turtle()
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

        for object in self.room.cliff:
            x = object.x
            y = object.y
            x2 =object.x + object.width
            y2 =object.y +object.height
            obstacleDraw =turtle.Turtle()
            obstacleDraw.speed(100)
            obstacleDraw.penup()
            obstacleDraw.hideturtle()
            obstacleDraw.goto(x,y)
            obstacleDraw.pendown()
            obstacleDraw.goto(x,y2)
            obstacleDraw.goto(x2,y2)
            obstacleDraw.goto(x2,y)
            obstacleDraw.goto(x,y)

    def initialiseTurtle(self):
        self.turtleDot = turtle.Turtle() 
        screen = turtle.Screen()
        turtle.setworldcoordinates(0,0,100,100)
        self.draw_obstacles()
        screen.tracer()
        self.turtleDot.goto(0, 0) 
        self.turtleDot.color('orange')
        self.turtleDot.speed(10) 
        self.turtleDot.width(2) 

    
    def set_zoomi_state(self,state):
        self.state = state 
        print("zoomi is now " + self.state)
    
    def base_dock_charges(self):
        while self.battery.get_battery_level() < 99:
            self.battery.charging_battery()
        return print("battery is fully charged at " + str(self.battery.get_battery_level()))


    def mid_clean_charge(self):
            print("zoomi is entering a sleep state")
            self.set_zoomi_state("sleep")
            print(self.state)
            print("en route to base dock")
            self.navigate_home()
            print("at home")
            self.light.set_light("orange")
            self.battery.charging_battery()
            self.base_dock_charges()
            self.set_zoomi_state("active")
        
    
    def zoomi_forward(self, forward_movement):
        self.y += forward_movement
        self.location = self.x,self.y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        if self.dirt_compartment.get_dirt_level() > 90:
            self.dirt_compartment.warn_user()
        self.turtleDot.goto(self.location)
        print(self.location)
        return self.location

    def zoomi_backward(self, backward_movement):
        self.y -= backward_movement
        self.location = self.x,self.y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        self.turtleDot.goto(self.location)
        print(self.location)
        return self.location
    
    def zoomi_right(self, right_movement):
        self.x += right_movement
        self.location = self.x,self.y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        self.turtleDot.goto(self.location)
        print(self.location)
        return self.location
    
    def zoomi_left(self,left_movement):
        self.x -= left_movement
        self.location = self.x,self.y
        self.battery.set_battery_level(-0.2)
        self.dirt_compartment.set_dirt_level(3)
        self.turtleDot.goto(self.location)
        print(self.location)
        return self.location
    
    def navigate_home(self):
        baseX=self.base_dock.x
        baseY=self.base_dock.y
        # while (baseX != self.x and baseY != self.y):
        #     print("ss")
        #     if baseX < self.x:
        #         self.x-1
        #     if baseX > self.x:
        #         self.x+1
        #     if baseY < self.y:
        #         self.y+1
        #     if baseY > self.y:
        #         self.y-1
        #     if self.collision_check():
        #         self.rotate(random.randint(0,360))
        #         if self.collision_check == False:
        #             self.moveto()
        #     if self.collision_check() == False:
        #         self.moveto()
        # if baseX == self.x and baseY == self.y:
        #     return
        self.x = baseX
        self.y = baseY
        self.move_to()

    def rotate(self, amount):
            self.rotation += amount
            if self.rotation > 360:
                self.rotation -= 360
            elif self.rotation < 0:
                self.rotation += 360

    def backup(self):
        self.turtleDot.goto(self.lastX,self.lastY)

    def move_to(self):
        self.lastY = self.y
        self.lastX = self.x
        self.location = self.x,self.y
        if self.location not in self.cleanedArea:
            self.cleanedArea.append(self.location)
        self.turtleDot.goto(self.location)

    def random_move(self, amnt):
            self.battery.set_battery_level(-0.01)
            self.dirt_compartment.set_dirt_level(0.001)
            self.x += amnt * math.cos(math.radians(self.rotation + 90))
            self.y -= amnt * math.sin(math.radians(self.rotation + 90))
            self.lastY = self.y
            self.lastX = self.x
            self.location = self.x,self.y
            if self.location not in self.cleanedArea:
                self.cleanedArea.append(self.location)
            self.turtleDot.goto(self.location)

    def collision_check(self):
        x = self.x
        y = self.y
        for object in self.room.barrier:
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                        self.backup()
                        self.rotate(180)
                        self.random_move(3)
                        self.sensors.barrier_detected()
                        print("obstacle detected")
                        return True
        for object in self.room.cliff:
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                        self.backup()
                        self.rotate(180)
                        self.random_move(3)
                        self.sensors.cliff_detected()
                        print("cliff detected")
                        return True


        if self.room.end_y <= self.y:
            self.y -=2
            return True
        if 0 >= self.y:
            self.y +=2
            return True
        if self.room.end_x <= self.x:
            self.x -=2
            print("wall hit")
            return True
        if 0 >= self.x:
            self.x +=2
            print("wall hit")
            return True

    def zoomi_movement(self):
        completionPercentage = len(self.cleanedArea)/self.room.area
        while (completionPercentage<90): #room not clean
            completionPercentage = len(self.cleanedArea)/self.room.area
            battery = self.battery.get_battery_level()
            dirtLevel = self.dirt_compartment.get_dirt_level()
            print(completionPercentage)
            if completionPercentage >0.90:
                print("finshed cleaning, going home")        
                self.navigate_home()
            if battery < 20.0:
                print("going for a mid_clean_charge")
                self.mid_clean_charge()
            if dirtLevel > 90.0:
                self.dirt_compartment.warn_user()
            if dirtLevel > 99.0:
                self.dirt_compartment.wait_for_user()
            self.random_move(1)
            if self.collision_check():
                self.rotate(random.randint(0,360))
                if self.collision_check == False:
                    self.random_move(1)
            if self.collision_check() == False:
                self.random_move(1)

        print("finshed cleaning, going home")        
        self.navigate_home()
        
   
    def activate_zoomi(self):
        self.initialiseTurtle()
        if self.battery.get_battery_level() <= 10:
            print("battery low, going home to recharge")
            self.mid_clean_charge()
        self.dirt_compartment.warn_user()
        self.set_zoomi_state("active")
        self.light.set_light("green")
        self.zoomi_movement()
        self.cleanedArea = []
        return self.set_zoomi_state("deactivated")
