from math import pi
import pickle

from pages.MasterPage import MasterPage
from database import *
from theme import *
from widgets import *
import socket
import select
import errno
import sys
import time
import threading

from flet import (AlertDialog, Card, Column, ElevatedButton, Icon, Image, Row, SnackBar, Text, TextButton,
                  colors, icons)


class HomePage(MasterPage):
    def __init__(self, page):
        self.page = page
        super().__init__()
        self.zoomiBagPercentage = 1000
        self.zoomiState = ""
        self.StateDisplay = "Offline"
        self.zoomiBatteryPercentage = 1000
        self.BatteryPercentageDisplay = ""
        self.BagPercentageDisplay = ""
        self.zoomiFlipped = False
        self.timeOfLastPing = 0
        self.alerted = False

    def build(self):
        profileSelection_dropdown.on_change = self.check_for_custom
        self.startCycleMenu = AlertDialog(
            modal=True,
            title=Text("Start Cleaning Cycle?"),
            content=[],
            actions=[
                TextButton("Begin", on_click=self.start_cycle),
                TextButton("Cancel", on_click=self.close_dlg)
            ]
        )
        self.endCycleMenu = AlertDialog(
            modal=True,
            title=Text("End Cleaning Cycle Early?"),
            content=Column(controls=[Text(value="Are you sure you would like to quit the cycle early? You will not be able to resume the cycle after it is cancelled!")],alignment="center",width=100, height=100),
            actions=[
                TextButton("Quit Cycle", on_click=self.quit_cycle),
                TextButton("Cancel", on_click=self.close_dlg)
            ]
        )
        self.display_zoomi_stats()
        batteryIcon = self.determineBatteryIcon()
        capacityIcon = self.determineCapacityIcon()
        statusIcon = self.determineStatusIcon()
        startOrEndButton = self.determine_button()
        return Column(
            controls=[
                Card(content=Column(
                    controls=[
                        Row(controls=[
                            Text(value="Welcome Home!",
                                 style="titleLarge"),
                        ], alignment="center"
                        ),
                        Image(src=f"roomba.png", width=200, height=200),
                        Row(controls=[
                            Text(value=self.StateDisplay,
                                 style="titleMedium"),
                            statusIcon
                        ], alignment="center"
                        ),
                        Row(
                            controls=[
                                Row(controls=[
                                    Text(value="Battery"), Text(
                                        value=self.BatteryPercentageDisplay),
                                    batteryIcon]),
                                Row(controls=[
                                    Text(value="Capacity"), Text(
                                        value=self.BagPercentageDisplay),
                                    capacityIcon])
                            ], alignment="center"
                        ),


                    ], horizontal_alignment="center"
                )
                ),
                startOrEndButton,
            ],

            horizontal_alignment="center")

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(
            target=self.connect_to_server, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        return

    def refresh_display(self):
        self._build()
        self.update()
        self.page.update()

    def connect_to_server(self):
        global HEADER_LENGTH
        HEADER_LENGTH = 10
        IP = "127.0.0.1"
        PORT = 1234
        my_username = "flet app"
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)
        username = my_username.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)
        while True:
            if time.time() - self.timeOfLastPing > 10:
                self.declare_connection_lost()
            elif time.time() - self.timeOfLastPing > 5:
                self.declare_weak_connection()
            
            message = False
            if message:
                message = pickle.dumps(message)
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self.client_socket.send(message_header + message)
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
                    message = pickle.loads(
                        self.client_socket.recv(message_length))
                    if username!="flet app":
                        self.timeOfLastPing = time.time()
                        self.parse_message(message)
                        print(f"{username} > {message}")

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    sys.exit()
                continue
            # except Exception as e:
            #     print("General error", str(e))
            #     sys.exit

    def declare_connection_lost(self):
        self.zoomiState = ""
        self.zoomiBagPercentage = 1000
        self.zoomiBatteryPercentage = 1000
        self.display_zoomi_stats()
        self._build()
        self.update()
        self.page.update()

    def declare_weak_connection(self):
        self.zoomiState = "weak"
        self.display_zoomi_stats()
        self._build()
        self.update()
        self.page.update()
        
    def determine_button(self):
        if self.zoomiState == "":
            return ElevatedButton(
                    "Start Cycle", on_click=self.open_start_cycle_menu,disabled=True, tooltip="Zoomi is offline. Connect him to start cleaning!")
        elif self.zoomiState == "ending" or self.zoomiState == "endingEarly":
            return ElevatedButton(
                    "End Cycle", on_click=self.open_end_cycle_menu, disabled=True, tooltip="Zoomi is already finishing cleaning")
        elif self.zoomiState == "preparing" or self.zoomiState == "requestedClean":
            return ElevatedButton(
                    "Cancel", on_click=self.cancel_cycle)
        elif self.zoomiState == "bagFull":
            return ElevatedButton(
                    "End Cycle", on_click=self.open_end_cycle_menu, disabled=True, tooltip="Please empty Zoomi's bag first")
        elif self.zoomiState == "deactivated":
             return ElevatedButton(
                    "Start Cycle", on_click=self.open_start_cycle_menu)
        else:
            return ElevatedButton(
                    "End Cycle", on_click=self.open_end_cycle_menu)

    def display_zoomi_stats(self):
        if self.zoomiBagPercentage > 100:
            self.BagPercentageDisplay = "Unknown"
        else:
            self.BagPercentageDisplay = str(self.zoomiBagPercentage)

        if self.zoomiBatteryPercentage > 100:
            self.BatteryPercentageDisplay = "Unknown"
        else:
            self.BatteryPercentageDisplay = str(self.zoomiBatteryPercentage)
        if self.zoomiState == "requestedClean":
            self.StateDisplay = "Requesting Clean..."
        elif self.zoomiState == "weak":
            self.StateDisplay = "Waiting for Update..."
        elif self.zoomiState == "":
             self.StateDisplay = "Offline"
        elif self.zoomiState == "endingEarly":
            self.StateDisplay = "Ending Clean Early..."
        elif self.zoomiState == "ending":
             self.StateDisplay = "Finishing Clean..."
        elif self.zoomiState == "preparing":
             self.StateDisplay = "Starting Clean..."
        elif self.zoomiState == "deactivated":
             self.StateDisplay = "Ready to Clean!"
        elif self.zoomiState == "active":
             self.StateDisplay = "Cleaning!"
        elif self.zoomiState == "bagFull":
             self.StateDisplay = "Dirt Compartment is Full!"
        elif self.zoomiState == "batteryEmpty":
             self.StateDisplay = "Charging..."
        elif self.zoomiState == "cancelled":
             self.StateDisplay = "Cancelling..."
        else:
            self.StateDisplay = self.zoomiState


    def parse_message(self,message):
        if message["purpose"] == 'update':
            status = message["status"] 
            battery = message["battery"]
            capacity = message["capacity"]
            change = False
            if status == "active":
                self.alerted =False
            if status == "bagFull":
                if self.alerted == False:
                    self.page.snack_bar = SnackBar(
                    Text("Zoomis Bag is Full! Please Empty it for Zoomi to continue cleaning."))
                    self.page.snack_bar.open = True
                    self.alerted = True
            if status == "batteryEmpty":
                if self.alerted == False:
                    self.page.snack_bar = SnackBar(
                    Text("Zoomis Battery is empty! Zoomi will recharge before he will continue cleaning."))
                    self.page.snack_bar.open = True
                    self.alerted = True
            if self.zoomiBatteryPercentage != battery:
                change = True
                self.zoomiBatteryPercentage = battery
            if self.zoomiState != status:
                change = True
                self.zoomiState = status
            if self.zoomiBagPercentage != capacity:
                self.zoomiBagPercentage = capacity
                change = True
            if change == True:
                self._build()
                self.update()
                self.page.update()

        elif message['purpose'] == 'requestdefault':
            default = fetch_default_profile_from_DB()
            mode = default["Mode"]
            speed = default["Speed"]
            laps = default["Laps"]
            message = {"command": "storedefault",
                       "mode": mode, "speed": speed, "laps": laps}
            self.send_message(message)

        elif message["purpose"] == "finished":
            self.page.snack_bar.open = False
            self.page.snack_bar = SnackBar(
            Text("Zoomi is finished Cleaning!"))
            self.page.snack_bar.open = True
            self.refresh_display()

    def send_message(self,message):
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

    def startCycleMenu(self):
        return AlertDialog(
            modal=True,
            title=Text("Start Cleaning Cycle?"),
            content=[],
            actions=[
                TextButton("Begin", on_click=self.start_cycle),
                TextButton("Cancel", on_click=self.close_dlg)
            ]
        )

    def check_for_custom(self, e):
        if profileSelection_dropdown.value == "Custom":
            self.startCycleMenu.content = withCustomStartMenu
            self.page.update()
        else:
            self.startCycleMenu.content = noCustomStartMenu
            self.page.update()

    def open_start_cycle_menu(self, e):
        update_profile_selection_dropdown()
        profileSelection_dropdown.value = "Default"
        self.startCycleMenu.content = noCustomStartMenu
        profileSelection_dropdown.data = "start"
        self.open_dlg(self.startCycleMenu)

    def open_end_cycle_menu(self, e):
        self.open_dlg(self.endCycleMenu)

    def determineBatteryIcon(self):
        if self.zoomiState == "batteryEmpty":
            return Icon(name=icons.BATTERY_FULL, color=colors.PURPLE, rotate=pi/2)
        elif self.zoomiBatteryPercentage == 100:
            return Icon(name=icons.BATTERY_FULL, color=colors.GREEN, rotate=pi/2)
        else:
            return Icon(name=icons.BATTERY_UNKNOWN)

    def determineCapacityIcon(self):
        if self.zoomiBagPercentage < 100:
            return Icon(name=icons.CHECK, color=colors.GREEN)
        else:
            return Icon(name=icons.WARNING, color=colors.RED)

    def determineStatusIcon(self):
        if self.zoomiState == "active":
            return Icon(name=icons.CIRCLE, color=colors.GREEN)
        elif self.zoomiState == "deactivated":
            return Icon(name=icons.CIRCLE, color=colors.YELLOW)
        elif self.zoomiState == "preparing":
            return Icon(name=icons.DOWNLOADING, color=colors.GREEN)
        elif self.zoomiState == "requestedClean":
            return Icon(name=icons.DOWNLOADING, color=colors.ORANGE)
        elif self.zoomiState == "bagFull" or self.zoomiState == "batteryEmpty":
            return Icon(name=icons.DOWNLOADING, color=colors.PURPLE)
        elif self.zoomiState == "cancelled":
            return Icon(name=icons.DOWNLOADING, color=colors.RED)
        else:
            return Icon(name=icons.CIRCLE, color=colors.BLUE_GREY)

    def start_cycle(self, e):
        if profileSelection_dropdown.value == "Custom":
            userInputs = [mode_dropdown, laps_dropdown, speed_dropdown]
            if not self.verify_inputs(userInputs):
                return
        self.page.snack_bar = SnackBar(
            Text("Your Cleaning Cycle Has Started!"))
        self.page.snack_bar.open = True
        self.close_dlg(e)
        self.ask_to_start()
        self.page.update()

    def cancel_cycle(self, e):
        self.page.snack_bar = SnackBar(
            Text("Your cycle will be cancelled"))
        self.zoomiState = "cancelled"
        self.page.snack_bar.open = True
        self.ask_to_end()
        self.refresh_display()
        
    def quit_cycle(self, e):
        self.page.snack_bar = SnackBar(
            Text("Your Cleaning Cycle Has Been Quit"))
        self.page.snack_bar.open = True
        self.close_dlg(e)
        self.ask_to_end()
        self.refresh_display()

    def ask_to_start(self):
        if profileSelection_dropdown.value == "Default":
            message = {"command": "start", "default": True,
                       "mode": "", "speed": "", "laps": ""}
            message = pickle.dumps(message)
            if message:
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self.client_socket.send(message_header + message)
        elif profileSelection_dropdown.value == "Custom":
            mode = mode_dropdown.value
            laps = laps_dropdown.value
            speed = speed_dropdown.value
            message = {"command": "start", "default": False,
                       "mode": mode, "speed": speed, "laps": laps}
            message = pickle.dumps(message)
            if message:
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self.client_socket.send(message_header + message)
        else:
            selectedProfile = profileSelection_dropdown.value

            profiles = fetch_profiles_from_DB()
            for object in profiles:
                print(selectedProfile)
                print(object)
                if profiles[object]["Name"] == selectedProfile:
                    mode = profiles[object]["Mode"]
                    speed = profiles[object]["Speed"]
                    laps = profiles[object]["Laps"]
            message = {"command": "start", "default": False,
                       "mode": mode, "speed": speed, "laps": laps}
            message = pickle.dumps(message)
            if message:
                message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                    "utf-8")
                self.client_socket.send(message_header + message)
        self.zoomiState = "requestedClean"
        self.refresh_display()

    def ask_to_end(self):
        message = {"command": "stop", "default": "",
                    "mode": "", "speed": "", "laps": ""}
        message = pickle.dumps(message)
        if message:
            message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
                "utf-8")
            self.client_socket.send(message_header + message)
       