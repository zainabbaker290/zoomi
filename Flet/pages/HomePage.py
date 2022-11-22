from math import pi

from pages.MasterPage import MasterPage
from database import *
from theme import *
from widgets import *

from flet import (AlertDialog, Card, Column, ElevatedButton, Icon, Image, Row, SnackBar, Text, TextButton,
                  colors, icons)


class HomePage(MasterPage):
    def __init__(self,page):
        self.page = page
        super().__init__()
        self.zoomiBatteryPercentage = 100
        self.zoomiState= "active"
        self.zoomiBagPercentage = 100
        self.zoomiFlipped= False
        

    def build(self):
        profileSelection_dropdown.on_change = self.check_for_custom
        self.startCycleMenu =self.startCycleMenu()
        batteryIcon = self.determineBatteryIcon()
        capacityIcon = self.determineCapacityIcon()
        statusIcon = self.determineStatusIcon()
        return Column(
                    controls=[
                        # Row(controls=[
                        #     Text(value="My Zoomi Robot", style="titleLarge"),
                        #     statusIcon
                        #     ]
                        # ),
                        Card(content=
                                Column(
                                    controls=[
                                    Row(controls=[
                                        Text(value="Welcome Home",style="titleLarge"),
                                     ]
                                     ),
                                    Image(src=f"roomba.png",width=200,height=200),
                                    Row(controls=[
                                         Text(value=self.zoomiState,style="titleMedium"),
                                         statusIcon
                                     ]
                                     ),
                                    Row(
                                        controls=[
                                            Row(controls=[
                                                Text(value="Battery"),
                                                batteryIcon]),
                                            Row(controls=[
                                                Text(value="Capacity"),
                                                capacityIcon])
                                        ]
                                    ),
                                    
                                    
                                    ]
                                )           
                            ),
                            ElevatedButton("Start Cycle", on_click=self.open_start_cycle_menu)
                            ],
                            
                            horizontal_alignment="center")
    
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
    
    def check_for_custom(self,e):
            if profileSelection_dropdown.value == "Custom":
                    self.startCycleMenu.content = withCustomStartMenu
                    self.page.update()
            else:
                self.startCycleMenu.content = noCustomStartMenu
                self.page.update()

    def open_start_cycle_menu(self,e):
        update_profile_selection_dropdown()
        profileSelection_dropdown.value = "Default"
        self.startCycleMenu.content= noCustomStartMenu
        profileSelection_dropdown.data = "start"
        self.open_dlg(self.startCycleMenu)

    def determineBatteryIcon(self):
        if self.zoomiBatteryPercentage == 100:
            return Icon(name=icons.BATTERY_FULL,color=colors.GREEN,rotate=pi/2)
        else:
            return Icon(name=icons.BATTERY_UNKNOWN)

    def determineCapacityIcon(self):
        if self.zoomiBagPercentage <100:
            return Icon(name=icons.CHECK, color=colors.GREEN)
        else:
            return Icon(name=icons.WARNING, color=colors.RED)

    def determineStatusIcon(self):
        if self.zoomiState == "active":
            return Icon(name=icons.CIRCLE, color=colors.GREEN)
        if self.zoomiState == "deactivated":
            return Icon(name=icons.CIRCLE, color=colors.ORANGE)
        if self.zoomiState == "sleep":
            return Icon(name=icons.PAUSE_CIRCLE)

    def start_cycle(self,e):
        if profileSelection_dropdown.value=="Custom":
            userInputs=[mode_dropdown,laps_dropdown,speed_dropdown]
            if not self.verify_inputs(userInputs):
                return 
        self.page.snack_bar=SnackBar(Text("Your Cleaning Cycle Has Started!"))
        self.page.snack_bar.open = True
        self.close_dlg(e)
        print("dd")
        self.page.update()
