from pages.MasterPage import MasterPage
from database import *
from theme import *
from widgets import *

from flet import (AlertDialog, Column, ElevatedButton, Row, SnackBar, Text, TextButton)


class ScheduleCreationPage(MasterPage):
    def __init__(self,page):
        self.dead = False
        self.page = page
        self.createScheduleConfirmation = AlertDialog(
        modal=True,
        title=Text("Confirm Selection?"),
        content=[],
        actions=[
            TextButton("Yes", on_click=self.create_schedule
    ),
            TextButton("No", on_click=self.close_dlg)
            ]
        )   
        self.customFlag = False
        self.createschedulesubmit_btn = ElevatedButton(text="Submit", on_click=self.create_schedule_submit
        )
        super().__init__()
    
    def build(self):
        profileSelection_dropdown.on_change = self.check_for_custom
        d = Column(controls=[
            Row(controls=[scheduleNameInput]),
            Row(controls=[dayText]),
            Row(controls=[day_dropdown, dayQ]),
            Row(controls=[timeText]),
            Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown, timeQ]),
            Row(controls=[reccuranceText]),
            Row(controls=[repetition_dropdown, reccuranceQ]),
            Row(controls=[profileSelectionText]),
            Row(controls=[profileSelection_dropdown, profileSelectionQ]),
            self.createschedulesubmit_btn])

        if self.customFlag == True:
            d = Column(controls=[
            Row(controls=[scheduleNameInput]),
            Row(controls=[dayText]),
            Row(controls=[day_dropdown, dayQ]),
            Row(controls=[timeText]),
            Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown, timeQ]),
            Row(controls=[reccuranceText]),
            Row(controls=[repetition_dropdown, reccuranceQ]),
            Row(controls=[profileSelectionText]),
            Row(controls=[profileSelection_dropdown, profileSelectionQ]),
            Row(controls=[mode_dropdown,laps_dropdown, speed_dropdown]),
            self.createschedulesubmit_btn])
        return d
    
    def create_schedule(self,e):
        write_schedule_to_DB()
        self.close_dlg(e)
        self.page.views.pop()
        self.page.snack_bar = SnackBar(Text("Your Schedule has been Saved"))
        self.page.snack_bar.open = True
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.running = False

    def check_for_custom(self,e):
        if profileSelection_dropdown.value == "Custom":
            self.customFlag=True
            self._build()
            self.update()
            self.page.update()
        else:
            self.customFlag=False
            self._build()
            self.update()
            self.page.update()

    def create_schedule_submit(self,e):
        existingSchedules = fetch_schedules_from_DB()
        nameInput = scheduleNameInput
        userInputs = [scheduleNameInput, day_dropdown,hours_dropdown,
        minutes_dropdown, amPm_dropdown,
        repetition_dropdown, profileSelection_dropdown]
        if profileSelection_dropdown.value == "Custom":
            userInputs.append(mode_dropdown)
            userInputs.append(speed_dropdown)
            userInputs.append(laps_dropdown)
        if self.verify_inputs(userInputs) == True and self.verify_create_name(existingSchedules,nameInput) == True:
                self.createScheduleConfirmation.content = Column(controls=[
                    Text(scheduleNameInput.value),
                    Text(day_dropdown.value),
                    Text(hours_dropdown.value),
                    Text(minutes_dropdown.value), 
                    Text(amPm_dropdown.value),
                    Text(repetition_dropdown.value),
                    Text(profileSelection_dropdown.value)],
                    height = 200
                    )
                self.open_dlg(self.createScheduleConfirmation)
                self.update()
                self.page.update()
        else:
            self.update()
            self.page.update()
