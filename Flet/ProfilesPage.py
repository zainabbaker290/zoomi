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

class ProfilesPage(MasterPage):
    def __init__(self,page):
        self.isCustomFlag = False
        self.page = page
        self.profileEditorMenu=  AlertDialog(
            modal=True,
            title=Text("Edit Profile"),
            content=[],
            actions=[
                TextButton("Save", on_click=self.edit_profile),
                TextButton("Exit", on_click=self.deny_editProfile)
                ]
            )   
        self.defaultProfileEditorMenu = AlertDialog(
            modal=True,
            title=Text("Edit Default Profile"),
            content=[],
            actions=[
                TextButton("Save", on_click=self.edit_default_profile),
                TextButton("Exit", on_click=self.deny_editProfile)
                ]
            )  
        super().__init__()

    def build(self):
        parsedProfile= fetch_profiles_from_DB()
        profilesDisplay = self.display_profiles(parsedProfile)
        return profilesDisplay
  

    def display_profiles(self,profileDict):
        profilesDisplay = Column(controls = [])
        defaultProfile = fetch_default_profile_from_DB()
        defaultCard = Container(content=Row(controls=[
                    Container(content=Card(content=Column(controls=[
                        Container(content=Row(controls =[
                            Text(value = "Default",style="titleMedium",color=onP)
                            ],
                            alignment="center"),bgcolor=p,padding=5, border_radius=border_radius.only(topLeft=10,topRight=10)),
                            Container(content=Row(controls=[
                                    Text(value = defaultProfile["Mode"],style="titleSmall"),
                                    Text(value = defaultProfile["Speed"],style="titleSmall"),
                                    Text(value = defaultProfile["Laps"],style="titleSmall")
                                    ],alignment="spaceEvenly"
                                ),padding=padding.all(11))
                            ],
                            expand=True
                        ),expand=True),expand=True, on_hover=self.card_on_hover),
                        Card(content=Container(content=Column(controls=[
                            IconButton(icon=icons.EDIT_OUTLINED,icon_color=onPC, icon_size=20, height=40,width=40, on_click = self.open_default_profile_editor)
                            ],
                            horizontal_alignment="center"),
                            
                            bgcolor=pC,border_radius=10
                        ))
                    ],spacing=0
                ),           
            )
        profilesDisplay.controls.append(defaultCard)
        if profileDict:
            for object in profileDict:
                profileIndex = object
                profileCard = Row(controls=[
                        Container(content=Card(content=Column(controls=[
                            Container(content=Row(controls =[
                                Text(value = profileDict[object]["Name"],style="titleMedium",color=onT)
                            ],
                            alignment="center"),bgcolor=t,padding=5,border_radius=border_radius.only(topLeft=10,topRight=10)),
                            Container(content=Row(controls=[
                                    Text(value = profileDict[object]["Mode"],style="titleSmall"),
                                    Text(value = profileDict[object]["Speed"],style="titleSmall"),
                                    Text(value = profileDict[object]["Laps"],style="titleSmall"), 
                                    ],alignment="spaceEvenly"
                                ),padding=padding.all(11))
                                ],
                            ),expand=True),expand=True,on_hover=self.card_on_hover),
                        Container(content=Card(content=Container(content=Column(controls=[
                                IconButton(icon=icons.EDIT_OUTLINED,icon_color= onTC,icon_size=20, height=40,width=40, data=profileIndex, on_click = self.open_profile_editor),
                                IconButton(icon=icons.DELETE_OUTLINED,icon_color= onTC,icon_size=20, height=40,width=40, data=profileIndex, on_click = self.delete_profile)],
                                spacing=0
                                ),
                                bgcolor=tC,
                                border_radius=border_radius.all(10)
                                
                                
                            )))
                        ],spacing=0)
                    
                
                profilesDisplay.controls.append(profileCard)
        else:
            profilesDisplay.controls.append(Card(content=Container(content=Row(controls=[Text(value="You have no custom profiles. Make one below!")],
            alignment="center"),padding=padding.all(25))))
        return profilesDisplay

    def open_default_profile_editor(self,e):
        defaultProfile = fetch_default_profile_from_DB()
        mode_dropdown.value = defaultProfile["Mode"]
        speed_dropdown.value = defaultProfile["Speed"]
        laps_dropdown.value = defaultProfile["Laps"]
        self.defaultProfileEditorMenu.content = Column(controls=(
        Row(controls=[mode_dropdown,modeQ]),
        Row(controls=[speed_dropdown,speedQ]),
        Row(controls=[laps_dropdown,lapsQ])),height=220,width=350)
        self.open_dlg(self.defaultProfileEditorMenu)

    def open_profile_editor(self,e):
        profileIndex=e.control.data
        profilesDict = fetch_profiles_from_DB()
        object = profilesDict[profileIndex]
        profileNameInput.value =object["Name"]
        mode_dropdown.value = object["Mode"]
        speed_dropdown.value = object["Speed"]
        laps_dropdown.value = object["Laps"]
        self.profileEditorMenu.content = Column(controls=(Row(controls=[profileNameInput]),
        Row(controls=[mode_dropdown,modeQ]),
        Row(controls=[speed_dropdown,speedQ]),
        Row(controls=[laps_dropdown,lapsQ])),height=280,width=350)
        self.profileEditorMenu.data = profileIndex
        self.open_dlg(self.profileEditorMenu)

    def edit_profile(self,e):
        existingProfiles = fetch_profiles_from_DB()
        profileIndex = self.profileEditorMenu.data
        nameInput = profileNameInput
        if self.verify_edit_name(existingProfiles,profileIndex,nameInput):
            profileNameInput.error_text = None
            self.close_dlg(e)
            write_updated_profile_to_DB(profileIndex)
            self._build()
            self.update()
            self.page.update()
            self.page.snack_bar = SnackBar(Text("Your Profile has been Updated"))
            self.page.snack_bar.open = True
            self.page.update()

    def deny_editProfile(self,e):
        clear_profile_values()
        self.close_dlg(e)

    def card_on_hover(self,e):
        e.control.content.elevation = 3 if e.data == "true" else 1
        self.update()
        self.page.update()

    
    def delete_profile(self,e):
        profileIndex=e.control.data
        remove_profile_from_DB(profileIndex)
        self._build()
        self.update()
        self.page.snack_bar = SnackBar(Text("Your Profile Has Been Deleted"))
        self.page.snack_bar.open = True
        self.page.update()

   
    def edit_default_profile(self,e):
        self.close_dlg(e)
        write_updated_default_profile_to_DB()
        self._build()
        self.update()
        self.page.snack_bar = SnackBar(Text("Your Default Profile has been Updated"))
        self.page.snack_bar.open = True
        self.page.update()

