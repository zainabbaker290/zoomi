from math import pi
import pickle

from pages.MasterPage import MasterPage
from database import *
from theme import *
from widgets import *
import socket
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
        self.currentModeDisplay = ""
        self.currentLapsDisplay = ""
        self.currentSpeedDisplay = ""
        self.zoomiBagPercentage = 1000
        self.zoomiState = ""
        self.StateDisplay = "Offline"
        self.zoomiBatteryPercentage = 1000
        self.zoomiCurrentLap = 0
        self.zoomiCurrentCompletionPercentage = 0
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
            content=Column(controls=[Text(
                value="You will not be able to resume the cycle after it is cancelled!")],
                alignment="center",
                width=100,
                height=100),
            actions=[
                TextButton("Quit Cycle", on_click=self.quit_cycle),
                TextButton("Cancel", on_click=self.close_dlg)
            ]
        )
        self.display_zoomi_stats()
        currentCleanInformationDisplay = self.display_current_clean_info()
        batteryIcon = self.determineBatteryIcon()
        capacityIcon = self.determine_capacity_icon()
        statusIcon = self.determine_status_icon()
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
                                 style="titleLarge"),
                            statusIcon
                        ], alignment="center"
                        ),
                        Row(controls=[
                            currentCleanInformationDisplay
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
        self.page.th = threading.Thread(
            target=self.connect_to_server, args=(), daemon=True)
        self.page.th.start()

    def will_unmount(self):
        self.running = False

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
        while self.running == True:
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
                    if username != "flet app":
                        self.timeOfLastPing = time.time()
                        self.parse_message(message)

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    sys.exit()
                continue
            except Exception as e:
                sys.exit

    def declare_connection_lost(self):
        self.zoomiState = ""
        self.zoomiBagPercentage = 1000
        self.zoomiBatteryPercentage = 1000
        self.display_zoomi_stats()
        self.refresh_display()

    def declare_weak_connection(self):
        self.zoomiState = "weak"
        self.display_zoomi_stats()
        self.refresh_display()

    def determine_button(self):
        if self.zoomiState == "" or self.zoomiState == "weak":
            return ElevatedButton(
                "Start Cycle", on_click=self.open_start_cycle_menu, disabled=True, tooltip="Zoomi is offline. Connect him to start cleaning!")
        elif self.zoomiState == "ending" or self.zoomiState == "endingEarly":
            return ElevatedButton(
                "End Cycle", on_click=self.open_end_cycle_menu, disabled=True, tooltip="Zoomi is already finishing cleaning")
        elif self.zoomiState == "preparing" or self.zoomiState == "requestedClean":
            return ElevatedButton(
                "Cancel", on_click=self.cancel_cycle)
        elif self.zoomiState == "cancelled":
            return ElevatedButton(
                "Cancelled", on_click=self.cancel_cycle, disabled=True)
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
        elif self.zoomiState == "quitting":
            self.StateDisplay = "Quitting..."
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

    def parse_message(self, message):
        if message["purpose"] == 'update':
            status = message["status"]
            battery = message["battery"]
            capacity = message["capacity"]
            completion = message["completion"]
            lap = message["lap"]
            self.currentModeDisplay = message["mode"]
            self.currentSpeedDisplay = message["speed"]
            self.currentLapsDisplay = message["laps"]
            change = False
            if status == "active":
                self.alerted = False
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
            if self.zoomiBatteryPercentage != battery:
                change = True
                self.zoomiBatteryPercentage = battery
            if self.zoomiState != status:
                change = True
                self.zoomiState = status
            if self.zoomiBagPercentage != capacity:
                self.zoomiBagPercentage = capacity
                change = True
            if self.zoomiCurrentCompletionPercentage != completion:
                self.zoomiCurrentCompletionPercentage = completion
                change = True
            if self.zoomiCurrentLap != lap:
                self.zoomiCurrentLap = lap
                change = True
            if change == True:
                self._build()
                self.update()
                self.page.update()

        elif message['purpose'] == 'requestdefault':
            self.send_default_profile()

        elif message["purpose"] == "finished":
            self.page.snack_bar.open = False
            self.page.snack_bar = SnackBar(
                Text("Zoomi is finished Cleaning!"))
            self.page.snack_bar.open = True
            self.refresh_display()
        else:
            return

    def send_default_profile(self):
        default = fetch_default_profile_from_DB()
        mode = default["Mode"]
        speed = default["Speed"]
        laps = default["Laps"]
        message = {"command": "storedefault",
                   "mode": mode, "speed": speed, "laps": laps}
        self.send_message(message)

    def send_message(self, message):
        message = pickle.dumps(message)
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode(
            "utf-8")
        self.client_socket.send(message_header + message)

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
        if self.zoomiState == "":
            return Icon(name=icons.BATTERY_UNKNOWN)
        elif self.zoomiBatteryPercentage == 100:
            return Icon(name=icons.BATTERY_FULL, color=colors.GREEN, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 90:
            return Icon(name=icons.BATTERY_6_BAR_ROUNDED, color=colors.GREEN, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 80:
            return Icon(name=icons.BATTERY_5_BAR_ROUNDED, color=colors.GREEN, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 60:
            return Icon(name=icons.BATTERY_4_BAR_ROUNDED, color=colors.GREEN, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 40:
            return Icon(name=icons.BATTERY_3_BAR_ROUNDED, color=colors.ORANGE, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 20:
            return Icon(name=icons.BATTERY_2_BAR_ROUNDED, color=colors.ORANGE, rotate=pi/2)
        elif self.zoomiBatteryPercentage > 1:
            return Icon(name=icons.BATTERY_1_BAR_ROUNDED, color=colors.RED, rotate=pi/2)
        elif self.zoomiBatteryPercentage == 100:
            return Icon(name=icons.BATTERY_FULL, color=colors.GREEN, rotate=pi/2)
        else:
            return Icon(name=icons.BATTERY_UNKNOWN)

    def display_current_clean_info(self):
        if self.currentLapsDisplay == "Two Laps":
            totalLaps = 2
        elif self.currentLapsDisplay == "Three Laps":
            totalLaps = 3
        else:
            totalLaps = 1

        completionDisplay = int((self.zoomiCurrentCompletionPercentage +
                                int(self.zoomiCurrentCompletionPercentage/9))/totalLaps)
        display = Column(
            controls=[
                Row(controls=[
                    Text(value=f"{completionDisplay}% Complete",
                         style="titleMedium"),
                    Text(
                        value=f"Lap {self.zoomiCurrentLap}/{totalLaps}", style="titleMedium")
                ]
                ),
                Row(controls=[Text(
                    f"Mode: {self.currentModeDisplay}   Speed: {self.currentSpeedDisplay}   Laps: {self.currentLapsDisplay}", style="labelLarge")]),
            ], horizontal_alignment="center"
        )
        if self.zoomiState == "active" or self.zoomiState == "bagFull" or self.zoomiState == "batteryEmpty":
            display.visible = True
        else:
            display.visible = False
        return display

    def determine_capacity_icon(self):
        if self.zoomiBagPercentage < 80:
            return Icon(name=icons.CHECK, color=colors.GREEN)
        elif self.zoomiBagPercentage > 80:
            return Icon(name=icons.WARNING_ROUNDED, color=colors.RED)
        else:
            return Icon(name=icons.WARNING, color=colors.RED)

    def determine_status_icon(self):
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
        self.ask_to_cancel()
        self.refresh_display()

    def quit_cycle(self, e):
        self.page.snack_bar = SnackBar(
            Text("Your Cleaning Cycle Has Been Quit"))
        self.page.snack_bar.open = True
        self.close_dlg(e)
        self.ask_to_end()
        self.refresh_display()

    def request_default_clean(self):
        message = {"command": "start", "default": True,
                   "mode": "", "speed": "", "laps": ""}
        self.send_message(message)

    def request_custom_clean(self):
        mode = mode_dropdown.value
        laps = laps_dropdown.value
        speed = speed_dropdown.value
        message = {"command": "start", "default": False,
                   "mode": mode, "speed": speed, "laps": laps}
        self.send_message(message)

    def request_profile_clean(self):
        selectedProfile = profileSelection_dropdown.value
        profiles = fetch_profiles_from_DB()
        for object in profiles:
            if profiles[object]["Name"] == selectedProfile:
                mode = profiles[object]["Mode"]
                speed = profiles[object]["Speed"]
                laps = profiles[object]["Laps"]
        message = {"command": "start", "default": False,
                   "mode": mode, "speed": speed, "laps": laps}
        self.send_message(message)

    def ask_to_start(self):
        if profileSelection_dropdown.value == "Default":
            self.request_default_clean()
        elif profileSelection_dropdown.value == "Custom":
            self.request_custom_clean()
        else:
            self.request_profile_clean()
        self.zoomiState = "requestedClean"
        self.refresh_display()

    def ask_to_end(self):
        self.zoomiCurrentCompletionPercentage = 0
        self.zoomiCurrentLap = 0
        self.zoomiState = "quitting"
        self.refresh_display()
        message = {"command": "stop", "default": "",
                   "mode": "", "speed": "", "laps": ""}
        self.send_message(message)

    def ask_to_cancel(self):
        self.zoomiCurrentCompletionPercentage = 0
        self.zoomiCurrentLap = 0
        message = {"command": "cancel", "default": "",
                   "mode": "", "speed": "", "laps": ""}
        self.send_message(message)
