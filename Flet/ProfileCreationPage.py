import flet
import sqlite3
from math import pi
from flet.transform import Scale
from flet import (AppBar, Dropdown, UserControl,theme, ElevatedButton, Image,Icon, Page, Row, Text, FilledTonalButton , IconButton, FloatingActionButton, border_radius,
                  TextField, View, colors, dropdown, icons,AlertDialog,Card, filled_tonal_button,margin,padding, Container, TextButton, Column, alignment, SnackBar, NavigationBar, NavigationDestination)
from scheduleWidgets import *
from profileWidgets import *
from profiles import *
from schedules import *
from home import *
from theme import *
from MasterPage import MasterPage

class ProfileCreationPage(MasterPage):
    def __init__(self,page):
        self.page = page
        self.createprofilesubmit_btn = ElevatedButton(text="Submit", on_click=self.create_profile_submit)
        self.createProfileConfirmation = AlertDialog(
        modal=True,
        title=Text("Confirm Selection?"),
        content= [],
        actions=[
            TextButton("Yes", on_click=self.create_profile),
            TextButton("No", on_click=self.close_dlg)
            ]
        )
        super().__init__()
    
    def build(self):
        return Column(controls=[Row(controls=[profileNameInput]),
                    Container(content=Column(controls=[Row(controls=[modeText,]),Row(controls=[mode_dropdown,modeQ])])),
                    Column(controls=[Row(controls=[speedText]),Row(controls=[speed_dropdown,speedQ])]),
                    Column(controls=[Row(controls=[lapsText]),Row(controls=[laps_dropdown,lapsQ])]),
                    self.createprofilesubmit_btn])
     
    def create_profile(self,e):
        write_profile_to_DB()
        self.close_dlg(e)
        self.page.views.pop()
        self.page.snack_bar = SnackBar(Text("Your Profile has been Saved"))
        self.page.snack_bar.open = True
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.running = False

    def create_profile_submit(self,e):
        existingProfiles = fetch_profiles_from_DB()
        nameInput = profileNameInput
        userInputs = [mode_dropdown,speed_dropdown,laps_dropdown,profileNameInput]
        if self.verify_inputs(userInputs) == True and self.verify_create_name(existingProfiles,nameInput) == True:
            self.createProfileConfirmation.content = Column(
                controls=[
                Text(profileNameInput.value),
                Row(controls=[
                Text(mode_dropdown.value),
                Text(speed_dropdown.value),
                Text(laps_dropdown.value)
                ],
                alignment="spaceAround")],height=80,horizontal_alignment="center",alignment="spaceEvenly"
                )
            self.open_dlg(self.createProfileConfirmation) 
            self.update()
            self.page.update()
        else:
            self.update()
            self.page.update()
        