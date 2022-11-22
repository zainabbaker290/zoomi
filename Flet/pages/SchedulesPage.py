from database import *
from pages.MasterPage import MasterPage
from theme import *
from widgets import *

from flet import (AlertDialog, Card, Column, Container, IconButton, Row,
                  SnackBar, Text, TextButton, border_radius, icons, margin,
                  padding)


class SchedulesPage(MasterPage):
    def __init__(self,page):
        self.page = page
        super().__init__()
        self.scheduleEditorMenu = AlertDialog(
        modal=True,
        title=Text("Edit Schedule"),
        content=[],
        actions=[
            TextButton("Save", on_click=self.edit_schedule),
            TextButton("Exit", on_click=self.deny_editSchedule)
            ]
        ) 

    def build(self):
        profileSelection_dropdown.on_change = self.check_for_custom
        parsedSchedules = fetch_schedules_from_DB()
        schedulesDisplay = self.display_schedules(parsedSchedules)
        return schedulesDisplay

    def delete_schedule(self,e):
        scheduleIndex=e.control.data
        remove_schedule_from_DB(scheduleIndex)
        self._build()
        self.update()
        self.page.snack_bar = SnackBar(Text("Your Schedule Has Been Deleted"))
        self.page.snack_bar.open = True
        self.page.update()

    def deny_editSchedule(self,e):
        clear_schedule_values()
        self.close_dlg(e)

    def edit_schedule(self,e):
        existingSchedules = fetch_schedules_from_DB()
        scheduleIndex = self.scheduleEditorMenu.data
        nameInput = scheduleNameInput
        userInputs = [scheduleNameInput, day_dropdown,hours_dropdown,
        minutes_dropdown, amPm_dropdown,
        repetition_dropdown, profileSelection_dropdown]
        if profileSelection_dropdown.value == "Custom":
            userInputs.append(mode_dropdown)
            userInputs.append(speed_dropdown)
            userInputs.append(laps_dropdown)
        if self.verify_edit_name(existingSchedules,scheduleIndex,nameInput) and self.verify_inputs(userInputs) == True:
            scheduleNameInput.error_text = None
            self.close_dlg(e)
            write_updated_schedule_to_DB(scheduleIndex)
            self._build()
            self.page.update()
            self.page.snack_bar = SnackBar(Text("Your Schedule has been Updated"))
            self.page.snack_bar.open = True
            self.page.update()
        return

    def open_schedule_editor(self,e):
        update_profile_selection_dropdown()
        profileSelection_dropdown.data = "edit"
        scheduleIndex=e.control.data
        schedulesDict = fetch_schedules_from_DB()
        object = schedulesDict[scheduleIndex]
        timeString = object["Time"]
        hours = timeString.split(":")[0]
        minutes = (timeString.split(":")[1])[:2]
        amPm = timeString[-2:]
        scheduleNameInput.value = object["Name"]
        day_dropdown.value = object["Day"]
        hours_dropdown.value = hours
        minutes_dropdown.value = minutes
        amPm_dropdown.value = amPm
        repetition_dropdown.value = object["Repetition"]
        profileSelection_dropdown.value = object["Profile"]
        mode_dropdown.value = object["Mode"]
        speed_dropdown.value = object["Speed"]
        laps_dropdown.value = object["Laps"]
        if profileSelection_dropdown.value == "Custom":
            self.scheduleEditorMenu.content = withCustomEditMenu
            
        else:
            self.scheduleEditorMenu.content = noCustomEditMenu
        self.scheduleEditorMenu.data = scheduleIndex
        self.open_dlg(self.scheduleEditorMenu)
    
    
    def display_schedules(self,scheduleDict):
            schedulesDisplay = Column(controls = [],scroll="auto")
            if scheduleDict:
                for schedule in scheduleDict:
                    scheduleIndex = schedule
                    if scheduleDict[schedule]["Profile"] == "Custom":
                        object = schedule
                        scheduleCard = Row(controls=[
                            Container(content=(Card(content=Column(controls=[
                                Container(content=Row(controls =[
                                    Text(value = scheduleDict[object]["Name"],style="titleMedium",color=onT)
                                ],
                                alignment="center"),bgcolor=t,padding=5,border_radius=border_radius.only(topLeft=10,topRight=10)),
                                Container(content=Row(controls=[
                                        Text(value = scheduleDict[object]["Day"],style="titleSmall"),
                                        Text(value = scheduleDict[object]["Time"],style="titleSmall"),
                                        Text(value = scheduleDict[object]["Repetition"],style="titleSmall"),
                                        ],alignment="spaceEvenly"
                                    )
                                    ,padding=padding.only(top=11)
                                    ),
                                Container(content=Column(controls=[
                                
                                Container(content=Row(controls=[
                                        Text(value = scheduleDict[object]["Mode"],style="labelMedium"),
                                        Text(value = scheduleDict[object]["Speed"],style="labelMedium"),
                                        Text(value = scheduleDict[object]["Laps"],style="labelMedium")
                                        ],alignment="spaceEvenly"
                                )
                                )
                                ]
                                ),margin=margin.only(left=30,right=30,top=5,bottom=5),padding=padding.only(left=40,right=30,top=3,bottom=3)
                                )
                                    ],spacing=0
                                ),expand=True)),expand=True,on_hover=self.card_on_hover),
                            Card(content=Container(content=Column(controls=[
                                    IconButton(icon=icons.EDIT_OUTLINED,icon_color=onTC, icon_size=20,height=40,width=40, data=scheduleIndex, on_click = self.open_schedule_editor),
                                    IconButton(icon=icons.DELETE_OUTLINED, icon_color=onTC,icon_size=20, height=40,width=40, data=scheduleIndex, on_click = self.delete_schedule)],
                                    spacing=0
                                    ),
                                    bgcolor=tC,
                                    border_radius=border_radius.all(10)
                            
                                    
                                ))
                            ],spacing=0)
                        schedulesDisplay.controls.append(scheduleCard)
                    else:
                        object = schedule
                        scheduleCard = Row(controls=[
                            Container(content=Card(content=Column(controls=[
                                Container(content=Row(controls =[
                                    Text(value = scheduleDict[object]["Name"],style="titleMedium",color=onT)
                                ],
                                alignment="center"),bgcolor=t,padding=5,border_radius=border_radius.only(topLeft=10,topRight=10)),
                                Container(content=Row(controls=[
                                        Text(value = scheduleDict[object]["Day"],style="titleSmall"),
                                        Text(value = scheduleDict[object]["Time"],style="titleSmall"),
                                        Text(value = scheduleDict[object]["Repetition"],style="titleSmall"), 
                                        Text(value = scheduleDict[object]["Profile"],style="titleSmall"),
                                        ],alignment="spaceEvenly"
                                    ),padding=padding.all(11)),
                                    
                                    ],
                                ),expand=True),expand=True,on_hover=self.card_on_hover),
                            Card(content=Container(content=Column(controls=[
                                    IconButton(icon=icons.EDIT_OUTLINED,icon_color=onTC, icon_size=20, height=40,width=40, data=scheduleIndex, on_click = self.open_schedule_editor),
                                    IconButton(icon=icons.DELETE_OUTLINED, icon_color=onTC, icon_size=20, height=40,width=40, data=scheduleIndex, on_click = self.delete_schedule)],
                                    spacing=0
                                    ),
                                    bgcolor=tC,
                                    border_radius=border_radius.all(10)
                            
                                    
                                ))
                            ],spacing=0)
                        schedulesDisplay.controls.append(scheduleCard)
            else:
                schedulesDisplay.controls.append(Card(content=Container(content=Row(controls=[Text(value="You have no Schedules. Make one below!")],
            alignment="center"),padding=padding.all(25))))
            schedulesDisplay.spacing=0
            return schedulesDisplay

    def check_for_custom(self,e):
        if profileSelection_dropdown.value == "Custom":
                self.scheduleEditorMenu.content = withCustomEditMenu
                self.update()
                self.page.update()
        else:
                self.scheduleEditorMenu.content = noCustomEditMenu
                self.update()
                self.page.update()

    