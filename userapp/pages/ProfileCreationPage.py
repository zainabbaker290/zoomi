
from database import *
from pages.MasterPage import MasterPage
from theme import *
from widgets import *

from flet import (AlertDialog, Column, Container,
                  ElevatedButton, Row, SnackBar, Text, TextButton)


class ProfileCreationPage(MasterPage):
    def __init__(self, page):
        self.page = page
        self.createProfileSubmitButton = ElevatedButton(
            text="Submit", on_click=self.create_profile_submit)
        self.createProfileConfirmation = AlertDialog(
            modal=True,
            title=Text("Confirm Selection?"),
            content=[],
            actions=[
                TextButton("Yes", on_click=self.create_profile),
                TextButton("No", on_click=self.close_dlg)
            ]
        )
        super().__init__()

    def build(self):
        return Column(controls=[Row(controls=[profileNameInput]),
                                Container(content=Column(
                                    controls=[Row(controls=[modeText, ]), Row(controls=[mode_dropdown, modeQ])])),
                                Column(controls=[Row(controls=[speedText]),
                                                 Row(controls=[speed_dropdown, speedQ])]),
                                Column(controls=[Row(controls=[lapsText]),
                                                 Row(controls=[laps_dropdown, lapsQ])]),
                                self.createProfileSubmitButton])

    def create_profile(self, e):
        write_profile_to_DB()
        self.close_dlg(e)
        self.page.views.pop()
        self.page.snack_bar = SnackBar(Text("Your Profile has been Saved"))
        self.page.snack_bar.open = True
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.running = False

    def create_profile_submit(self, e):
        existingProfiles = fetch_profiles_from_DB()
        nameInput = profileNameInput
        userInputs = [mode_dropdown, speed_dropdown,
                      laps_dropdown, profileNameInput]
        if self.verify_inputs(userInputs) == True and self.verify_create_name(existingProfiles, nameInput) == True:
            self.createProfileConfirmation.content = Column(
                controls=[
                    Text(profileNameInput.value),
                    Row(controls=[
                        Text(mode_dropdown.value),
                        Text(speed_dropdown.value),
                        Text(laps_dropdown.value)
                    ],
                        alignment="spaceAround")], height=80, horizontal_alignment="center", alignment="spaceEvenly"
            )
            self.open_dlg(self.createProfileConfirmation)
            self.update()
            self.page.update()
        else:
            self.update()
            self.page.update()
