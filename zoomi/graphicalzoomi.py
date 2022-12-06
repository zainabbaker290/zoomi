import turtle
import math
import random
import time
import socket
import errno
import sys
import time
import pickle
import threading

class GraphicalZoomi:
    def __init__(self, Battery, DirtCompartment, defaultCleaningProfile, Room, BaseDock) -> None:
        self.battery = Battery
        self.baseDock = BaseDock
        self.dirtCompartment = DirtCompartment
        self.defaultCleaningProfile = defaultCleaningProfile
        self.currentMode = ""
        self.currentSpeed = ""
        self.currentLaps = ""
        self.state = "deactivated"
        self.totalLaps = 0
        self.x = 0
        self.y = 0
        self.lastX = 0
        self.lastY = 0
        self.cleanedArea = []
        self.room = Room
        self.location = self.x, self.y
        self.baseDock = BaseDock
        self.rotation = 180
        self.cancelled = False
        self.stoppedEarly = False
        self.batteryDrainRate = 0
        self.dirtCollectionRate = 0
        self.beginClean = False
        self.completionPercentage = 0
        self.completedLaps = 0
        self.client_socket = ""
        self.wait_for_instructions()

    def end_of_cycle_reset(self):
        self.completedLaps = 0
        self.completionPercentage = 0
        self.beginClean = False
        self.send_clean_ended()
        self.currentMode = ""
        self.currentSpeed = ""
        self.currentLaps = ""
        self.stoppedEarly = False
        self.cancelled = False
        self.batteryDrainRate = 0
        self.dirtCollectionRate = 0

    def wait_for_instructions(self):
        self.th = threading.Thread(
            target=self.connect_to_server, args=(), daemon=True)
        self.th.start()
        self.th2 = threading.Thread(
            target=self.send_updates_to_server, args=(), daemon=True)
        self.th2.start()
        time.sleep(1)
        self.request_default_profile()
        while True:
            if self.beginClean == True:
                self.accept_start(self.instructions)

    def send_updates_to_server(self):
        global HEADER_LENGTH
        HEADER_LENGTH = 10
        IP = "127.0.0.1"
        PORT = 1234
        my_username = "zoomi2"
        self.client_socket_send = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket_send.connect((IP, PORT))
        self.client_socket_send.setblocking(True)
        username = my_username.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket_send.send(username_header + username)
        self.lastmsg = {}
        print("Recieving Messages!!")
        while True:
            message = {"purpose": "update", "status": self.state, "battery": round(
                self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level()), "completion": round(self.completionPercentage*100), "lap": self.completedLaps+1,"mode" : self.currentMode, "speed" : self.currentSpeed,"laps": self.currentLaps}
            if message == self.lastmsg:
                time.sleep(2)
            else:
                time.sleep(0)
            message = {"purpose": "update", "status": self.state, "battery": round(
                self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level()), "completion": round(self.completionPercentage*100), "lap": self.completedLaps+1,"mode" : self.currentMode, "speed" : self.currentSpeed,"laps": self.currentLaps}
            self.lastmsg = message
            message = pickle.dumps(message)
            if message:
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self.client_socket_send.send(message_header + message)
            

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
        print("Zoomi Online!")
        while True:
            try:
                while True:
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
                    if username == "flet app":
                        self.parse_message(message)
                    if username == "server":
                        if message["name"] == "flet app" and message["info"] == "online":
                            self.request_default_profile()
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    sys.exit()
                continue
    def request_default_profile(self):
        message = message = {"purpose": "requestdefault"}
        self.send_message(message)

    def parse_message(self, message):
        command = message["command"]
        if command == "start":
            self.beginClean = True
            self.instructions = message
        elif command == "storedefault":
            self.update_default_profile(message)
        elif command == 'stop':
            self.stoppedEarly = True
        elif command == "cancel":
            self.set_zoomi_state("cancelled")
            self.cancelled = True
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
            self.currentSpeed = self.defaultCleaningProfile.speed
            self.initialise_cleaning_profile()
            self.activate_zoomi()
        else:
            mode = message["mode"]
            speed = message["speed"]
            laps = message["laps"]
            self.currentMode = mode
            self.currentSpeed = speed
            self.currentLaps = laps
            self.initialise_cleaning_profile()
            self.activate_zoomi()

    def draw_obstacles(self):
        for object in self.room.barrier:
            object.draw()
        for object in self.room.cliff:
            print("z")
            object.draw_hollow()

    def initialise_turtle(self):
        screen = turtle.Screen()
        screen.clear()
        self.turtleDot = turtle.Turtle()
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
            self.batteryDrainRate += -0.01
            self.dirtCollectionRate += 0.01
        elif self.currentSpeed == "Deep Clean":
            self.batteryDrainRate = +-0.0025
            self.dirtCollectionRate += 0.0025
            self.delay = 0.02
        else:
            self.delay = 0.01
            self.batteryDrainRate += -0.005
            self.dirtCollectionRate += 0.005

        if self.currentMode == "Turbo":
            self.batteryDrainRate += -0.01
            self.dirtCollectionRate += 0.01
        elif self.currentMode == "Green":
            self.batteryDrainRate = +-0.0025
            self.dirtCollectionRate += 0.0025
        else:
            self.batteryDrainRate += -0.005
            self.dirtCollectionRate += 0.005
        if self.currentLaps == "One Lap":
            self.totalLaps = 1
        elif self.currentLaps == "Two Laps":
            self.totalLaps = 2
        elif self.currentLaps == "Three Laps":
            self.totalLaps = 3

    def set_zoomi_state(self, state):
        self.state = state
        self.send_status_update()

    def mid_clean_charge(self):
        self.set_zoomi_state("batteryEmpty")
        self.navigate_home()
        while self.battery.get_battery_level() < 100:
            time.sleep(0.1)
            self.battery.charge()
        self.set_zoomi_state("active")

    def mid_clean_empty(self):
        self.set_zoomi_state("bagFull")
        waitingPeriod = 0
        while waitingPeriod < 10:
            time.sleep(1)
            waitingPeriod += 1
        self.dirtCompartment.empty()
        self.set_zoomi_state("active")

    def horizontal_collision(self):
        x = self.x
        y = self.y
        for barrier in self.room.barrier:
            object = barrier.right
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                return True
            object = barrier.left
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                return True
        for cliff in self.room.cliff:
            object = cliff.right
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                return True
            object = cliff.left
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                return True

    def vertical_collision(self):
        x = self.x
        y = self.y
        for barrier in self.room.barrier:
            object = barrier.top
            if object.x-1 < x < object.x+object.width+1 and object.y-2 < y < object.y+object.height+2:
                return True
            object = barrier.bottom
            if object.x-1 < x < object.x+object.width+1 and object.y+2 < y < object.y+object.height-2:
                return True
        for cliff in self.room.cliff:
            object = cliff.top
            if object.x-1 < x < object.x+object.width+1 and object.y-2 < y < object.y+object.height+2:
                return True
            object = cliff.bottom
            if object.x-1 < x < object.x+object.width+1 and object.y+2 < y < object.y+object.height-2:
                return True

    def navigate_home(self):
        self.x = int(self.x)
        self.y = int(self.y)
        baseX = self.baseDock.x
        baseY = self.baseDock.y
        while (baseX != self.x or baseY != self.y):
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
        self.battery.update(self.batteryDrainRate)
        self.dirtCompartment.update(self.dirtCollectionRate)
        self.lastY = self.y
        self.lastX = self.x
        self.location = self.x, self.y
        if self.location not in self.cleanedArea:
            self.cleanedArea.append(self.location)
        self.turtleDot.goto(self.location)

    def random_move(self, amnt):
        time.sleep(self.delay)
        self.battery.update(self.batteryDrainRate)
        self.dirtCompartment.update(self.dirtCollectionRate)
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
                return True
        for object in self.room.cliff:
            if object.x-1 < x < object.x+object.width+1 and object.y-1 < y < object.y+object.height+1:
                self.backup()
                self.rotate(180)
                self.random_move(3)
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
        self.set_zoomi_state("active")
        self.completionPercentage = len(self.cleanedArea)/self.room.area
        while self.stoppedEarly == False and self.completionPercentage < 0.90 and self.cancelled == False:
            if self.completionPercentage < 0.90:
                self.completionPercentage = len(
                    self.cleanedArea)/self.room.area
                battery = self.battery.get_battery_level()
                dirtLevel = self.dirtCompartment.get_dirt_level()
                if battery < 10.0:
                    self.mid_clean_charge()
                if dirtLevel > 99.0:
                    self.mid_clean_empty()
                self.random_move(1)
                if self.collision_check():
                    self.rotate(random.randint(0, 360))
                    if self.collision_check == False:
                        self.random_move(1)
                if self.collision_check() == False:
                    self.random_move(1)

        if self.stoppedEarly == True:
            self.stoppedEarly = True
            return
        else:
            self.cleanedArea = []
            return

    def send_message(self, message):
        global HEADER_LENGTH
        HEADER_LENGTH = 10
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket_send.send(message_header + message)

    def send_status_update(self):
        message = {"purpose": "update", "status": self.state, "battery": round(
            self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level())}
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket_send.send(message_header + message)

    def send_clean_ended(self):
        message = {"purpose": "finished", "status": self.state, "battery": round(
            self.battery.get_battery_level()), "capacity": round(self.dirtCompartment.get_dirt_level())}
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

    def activate_zoomi(self):
        if self.cancelled == False:
            self.set_zoomi_state("preparing")
            self.initialise_turtle()
        if self.cancelled == False:
            self.set_zoomi_state("active")
            self.completedLaps = 0
            while self.stoppedEarly == False and self.completedLaps < self.totalLaps and self.cancelled == False:
                self.zoomi_movement()
                self.completedLaps += 1
            if self.stoppedEarly == True or self.cancelled == True:
                self.end_of_cycle_reset()
                self.set_zoomi_state("endingEarly")
                self.navigate_home()
                self.set_zoomi_state("deactivated")
                return
            else:
                self.end_of_cycle_reset()
                self.set_zoomi_state("ending")
                self.navigate_home()
                self.set_zoomi_state("deactivated")
                return
        else:
            self.set_zoomi_state("deactivated")
            self.navigate_home()
            self.end_of_cycle_reset()
            return

