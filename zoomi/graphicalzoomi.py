import turtle
import tkinter as tk
from tkinter import ttk
import math
import random
import time
import socket
import select
import errno
import sys
import time
import pickle
import threading


class GraphicalZoomi:
    def __init__(self, Battery, Sensors, Light, DirtCompartment, defaultCleaningProfile, CleaningMode, Wheels, Room, BaseDock) -> None:
        self.battery = Battery
        self.sensors = Sensors
        self.light = Light
        self.dirtCompartment = DirtCompartment
        self.defaultCleaningProfile = defaultCleaningProfile
        self.cleaningProfile = CleaningMode
        self.wheels = Wheels
        self.currentMode = ""
        self.currentSpeed = ""
        self.currentLaps = ""
        self.state = "deactivated"
        self.powerConsumptionModifier = 0
        self.x = 0
        self.y = 0
        self.lastX = 0
        self.lastY = 0
        self.cleanedArea = []
        self.room = Room
        self.location = self.x, self.y
        self.base_dock = BaseDock
        self.rotation = 180
        self.cancelled = False
        self.stoppedEarly = False
        self.powerConsumptionModifier = 0
        self.suctionPowerModifier = 0
        self.initialise_cleaning_profile()
        self.connect_to_server()

    def end_of_cycle_reset(self):
        self.send_clean_ended()
        self.currentMode = ""
        self.currentSpeed = ""
        self.currentLaps = ""
        self.stoppedEarly = False
        self.powerConsumptionModifier = 0
        self.suctionPowerModifier = 0

    def recieve_messages(self):
        while True:
            print("recieving")
            # username_header = self.client_socket.recv(HEADER_LENGTH)
            # if not len(username_header):
            #     print("connection closed by the server")
            #     sys.exit()

            # username_length = int(username_header.decode("utf-8"))
            # username = self.client_socket.recv(
            #     username_length).decode("utf-8")
            # message_header = self.client_socket.recv(HEADER_LENGTH)
            # message_length = int(message_header.decode("utf-8"))
            # message = pickle.loads(self.client_socket.recv(
            #     message_length))
            # print(f"{username} > {message}")
            # self.parse_message(message)

    def connect_to_server(self):
        global HEADER_LENGTH
        HEADER_LENGTH = 10
        IP = "127.0.0.1"
        PORT = 1234
        my_username = "zoomi"
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)
        username = my_username.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)
        lastmsg = {}
        self.start = False
        self.request_default_profile()
        while True:
            message = {"purpose": "update", "status": self.state, "battery": round(
                self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level())}
            if message != lastmsg:
                time.sleep(4.5)
            else:
                time.sleep(1)
            message = pickle.dumps(message)
            if message:
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self. client_socket.send(message_header + message)
            try:
                while True:
                    # recieve things
                    username_header = self.client_socket.recv(HEADER_LENGTH)
                    if not len(username_header):
                        print("connection closed by the server")
                        sys.exit()

                    username_length = int(username_header.decode("utf-8"))
                    username = self.client_socket.recv(
                        username_length).decode("utf-8")
                    message_header = self.client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode("utf-8"))
                    message = pickle.loads(self.client_socket.recv(
                        message_length))
                    print(f"{username} > {message}")
                    self.parse_message(message)
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    sys.exit()
                continue
            except Exception as e:
                print("General error", str(e))
                sys.exit

    def request_default_profile(self):
        message = message = {"purpose": "requestdefault"}
        self.send_message(message)

    def parse_message(self, message):
        command = message["command"]
        if command == "start":
            self.accept_start(message)
        if command == "storedefault":
            self.update_default_profile(message)
        else:
            return

    def update_default_profile(self, message):
        mode = message["mode"]
        speed = message["speed"]
        laps = message["laps"]
        self.defaultCleaningProfile.mode = mode
        self.defaultCleaningProfile.speed = speed
        self.defaultCleaningProfile.laps = laps

    def accept_start(self, message):
        default = message["default"]
        if default == True:
            self.currentMode = self.defaultCleaningProfile.mode
            self.currentLaps = self.defaultCleaningProfile.laps
            print(self.currentLaps)
            self.currentSpeed = self.defaultCleaningProfile.speed
            self.initialise_cleaning_profile()
            print(self.cleaningProfile)
            self.start = True
            self.th = threading.Thread(target=self.recieve_messages, args=(), daemon=True)
            self.th.start()
            self.activate_zoomi()
        else:
            mode = message["mode"]
            speed = message["speed"]
            laps = message["laps"]
            self.currentMode = mode
            self.currentSpeed = speed
            self.currentLaps = laps
            self.initialise_cleaning_profile()
            print(self.cleaningProfile)
            self.start = True
            self.th = threading.Thread(target=self.recieve_messages, args=(), daemon=True)
            self.th.start()
            self.activate_zoomi()

    def draw_obstacles(self):
        for object in self.room.barrier:
            object.draw()

    def initialiseTurtle(self):
        self.turtleDot = turtle.Turtle()
        screen = turtle.Screen()
        screen.clear()
        turtle.setworldcoordinates(0, 0, self.room.width, self.room.height)
        self.draw_obstacles()
        self.turtleDot.shape("circle")
        self.turtleDot.shapesize(1.5, 1.5, 1)
        self.turtleDot.goto(0, 0)
        self.turtleDot.color('purple')
        self.turtleDot.speed(10)
        self.turtleDot.width(10)
        screen.tracer()

    def initialise_cleaning_profile(self):
        if self.currentSpeed == "Quick Clean":
            self.delay = 0
            self.powerConsumptionModifier += -0.02
            self.suctionPowerModifier += 0.02
        elif self.currentSpeed == "Deep Clean":
            self.powerConsumptionModifier = +-0.005
            self.suctionPowerModifier += 0.005
            self.delay = 0.04
        else:
            self.delay = 0.02
            self.powerConsumptionModifier += -0.01
            self.suctionPowerModifier += 0.01

        if self.currentMode == "Turbo":
            self.powerConsumptionModifier += -0.02
            self.suctionPowerModifier += 0.02
        elif self.currentMode == "Green":
            self.powerConsumptionModifier = +-0.005
            self.suctionPowerModifier += 0.005
        else:
            self.powerConsumptionModifier += -0.01
            self.suctionPowerModifier += 0.01

        if self.currentLaps == "One Lap":
            self.currentLaps = 1
        elif self.currentLaps == "Two Laps":
            self.currentLaps = 2
        elif self.currentLaps == "Three Laps":
            self.currentLaps = 3

    def set_zoomi_state(self, state):
        self.state = state
        self.send_status_update()
        print("zoomi is now " + self.state)

    def mid_clean_charge(self):
        self.set_zoomi_state("batteryEmpty")
        self.navigate_home()
        self.light.set_light("orange")
        while self.battery.get_battery_level() < 100:
            time.sleep(0.1)
            self.battery.charge()
            self.send_status_update()
        self.set_zoomi_state("active")

    def mid_clean_empty(self):
        print("zoomi is entering a sleep state")
        self.set_zoomi_state("bagFull")
        self.send_status_update()
        print(self.state)
        self.light.set_light("orange")
        waitingPeriod = 0
        while waitingPeriod < 10:
            time.sleep(1)
            waitingPeriod += 1
            self.send_status_update()
        self.dirtCompartment.dirt_level = 0
        self.set_zoomi_state("active")

    def horizontal_collision(self):
        x = self.x
        y = self.y
        for barrier in self.room.barrier:
            object = barrier.right
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                print("right")
                return True
            object = barrier.left
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                print("left")
                return True

    def vertical_collision(self):
        x = self.x
        y = self.y
        for barrier in self.room.barrier:
            object = barrier.top
            if object.x-1 < x < object.x+object.width+1 and object.y-2 < y < object.y+object.height+2:
                print("top")
                return True
            object = barrier.bottom
            if object.x-1 < x < object.x+object.width+1 and object.y+2 < y < object.y+object.height-2:
                print("bottom")
                return True

    def navigate_home(self):
        self.x = int(self.x)
        self.y = int(self.y)
        baseX = self.base_dock.x
        baseY = self.base_dock.y
        while (baseX != self.x or baseY != self.y):
            self.send_status_update()
            while (self.vertical_collision()):
                self.y -= 1
                self.move_to()
            while (self.horizontal_collision()):
                self.x -= 1
                self.move_to()
            if baseX < self.x:
                self.x -= 1
            if baseX > self.x:
                self.x += 1
            if baseY < self.y:
                self.y -= 1
            if baseY > self.y:
                self.y += 1
            self.move_to()
            while (self.vertical_collision()):
                self.x -= 1
                self.move_to()
            while (self.horizontal_collision()):
                self.y -= 1
                self.move_to()
        if baseX == self.x and baseY == self.y:
            return

    def rotate(self, amount):
        self.rotation += amount
        if self.rotation > 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360

    def backup(self):
        self.turtleDot.goto(self.lastX, self.lastY)

    def move_to(self):
        time.sleep(self.delay)
        self.battery.set_battery_level(self.powerConsumptionModifier)
        self.dirtCompartment.set_dirt_level(self.suctionPowerModifier)
        self.lastY = self.y
        self.lastX = self.x
        self.location = self.x, self.y
        if self.location not in self.cleanedArea:
            self.cleanedArea.append(self.location)
        self.turtleDot.goto(self.location)

    def random_move(self, amnt):
        time.sleep(self.delay)
        self.battery.set_battery_level(self.powerConsumptionModifier)
        self.dirtCompartment.set_dirt_level(self.suctionPowerModifier)
        self.x += amnt * math.cos(math.radians(self.rotation + 90))
        self.y -= amnt * math.sin(math.radians(self.rotation + 90))
        self.lastY = self.y
        self.lastX = self.x
        self.location = self.x, self.y
        savedLocation = int(self.x), int(self.y)
        if savedLocation not in self.cleanedArea:
            self.cleanedArea.append(savedLocation)
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
                return True
        for object in self.room.cliff:
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                self.backup()
                self.rotate(180)
                self.random_move(3)
                self.sensors.cliff_detected()
                return True
        if self.room.end_y <= self.y:
            self.y -= 2
            return True
        if 0 >= self.y:
            self.y += 2
            return True
        if self.room.end_x <= self.x:
            self.x -= 2
            return True
        if 0 >= self.x:
            self.x += 2
            return True

    def zoomi_movement(self):
        sinceLastMessage = 0
        self.completionPercentage = len(self.cleanedArea)/self.room.area
        while (self.completionPercentage < 0.90):
            if self.stoppedEarly == False:
                self.completionPercentage = len(self.cleanedArea)/self.room.area
                battery = self.battery.get_battery_level()
                dirtLevel = self.dirtCompartment.get_dirt_level()
                if battery < 10.0:
                    print("going for a mid_clean_charge")
                    self.mid_clean_charge()
                if dirtLevel > 99.0:
                    print("my dirt compartment is full!")
                    self.mid_clean_empty()
                self.random_move(1)
                if self.collision_check():
                    self.rotate(random.randint(0, 360))
                    if self.collision_check == False:
                        self.random_move(1)
                if self.collision_check() == False:
                    self.random_move(1)
                if sinceLastMessage > 50:
                    self.send_status_update()
                    sinceLastMessage = 0
                else:
                    sinceLastMessage += 1
                try:
                    while True:
                        username_header = self.client_socket.recv(
                            HEADER_LENGTH)
                        if not len(username_header):
                            print("connection closed by the server")
                            sys.exit()

                        username_length = int(username_header.decode("utf-8"))
                        username = self.client_socket.recv(
                            username_length).decode("utf-8")

                        message_header = self.client_socket.recv(HEADER_LENGTH)
                        message_length = int(message_header.decode("utf-8"))
                        message = pickle.loads(
                            self.client_socket.recv(message_length))
                        print(f"{username} > {message}")
                        if message['command'] == 'stop':
                            self.set_zoomi_state("ending")
                            self.send_status_update()
                            self.stoppedEarly = True
                            self.cleanedArea = []
                            return
                except IOError as e:
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        print("reading error", str(e))
                        sys.exit()
                    continue
                except Exception as e:
                    print("General error", str(e))
                    sys.exit
            if self.stoppedEarly == True:
                print("stopping early!")
                self.cleanedArea = []
                return
        self.cleanedArea = []
        return

    def send_message(self, message):
        global HEADER_LENGTH
        HEADER_LENGTH = 10
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

    def send_status_update(self):
        message = {"purpose": "update", "status": self.state, "battery": round(
            self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level())}
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

    def send_clean_ended(self):
        message = {"purpose": "finished", "status": self.state, "battery": round(
            self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level())}
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

    def activate_zoomi(self):
        self.set_zoomi_state("preparing")
        self.initialiseTurtle()
        self.set_zoomi_state("active")
        self.light.set_light("green")
        totalLaps = self.currentLaps
        print(totalLaps)
        completedLaps = 0
        while self.stoppedEarly == False and completedLaps < totalLaps:
            self.zoomi_movement()
            completedLaps +=1
            self.zoomi_movement()
        if self.stoppedEarly == False:
            self.set_zoomi_state("ending")
            self.navigate_home()
            self.set_zoomi_state("deactivated")
            self.end_of_cycle_reset()
            return
        if self.stoppedEarly == True:
            self.set_zoomi_state("endingEarly")
            self.navigate_home()
            self.set_zoomi_state("deactivated")
            self.end_of_cycle_reset()
            return
