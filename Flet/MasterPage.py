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

class MasterPage(UserControl):
    def __init__(self):
        self.page = None
        super().__init__()
        return
    def build(self):
        return
    def close_dlg(self,e):
        self.page.dialog.open = False
        self.page.update()

    def open_dlg(self,dlg):
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
   
        return

    def verify_inputs(self,userInputs):
        fail = False
        for input in userInputs:
                if not input.value:
                    input.error_text = f"Please Choose {input.label}"
                    self.page.snack_bar = SnackBar(Text("Please Fill in all Inputs"))
                    self.page.snack_bar.open = True
                    fail = True
                else:
                    input.error_text = None
                self.page.update()
        if fail:
            return False
        else:
            return True
            
    def card_on_hover(self,e):
        e.control.content.elevation = 3 if e.data == "true" else 1
        self.page.update()
    def verify_create_name(self,existingObjects,input):
        for object in existingObjects:
            print(existingObjects[object]["Name"])
            if existingObjects[object]["Name"] == input.value:
                input.error_text = "This name has already been used."
                self.page.update()
                return False
        else: 
            input.error_text = None
            return True

    def verify_edit_name(self,existingObjects,index,input):
        fail = False
        if not input.value:
            input.error_text = "Please Enter Name."
            self.page.update()
            return False
        print(existingObjects)
        for profileIndex in existingObjects:
            print(existingObjects[profileIndex]["Name"])
            print("index",profileIndex)
            print("editor index",input)
            if existingObjects[profileIndex]["Name"] == input.value and profileIndex != index:
                input.error_text = "This name has already been used."
                self.page.update()
                fail = True
        if fail:
            return False
        else:
            input.error_text = None
            self.page.update()
            return True
            
    def card_on_hover(self,e):
        e.control.content.elevation = 3 if e.data == "true" else 1
        self.update()
        self.page.update()