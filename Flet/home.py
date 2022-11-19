from flet import NavigationBar,NavigationDestination,icons,Text
from profileWidgets import *
from scheduleWidgets import *

navBar = NavigationBar(
    destinations=[
    NavigationDestination(icon=icons.CLEANING_SERVICES, label="Profiles"),
    NavigationDestination(icon=icons.HOME_ROUNDED, label="Home"),
    NavigationDestination(icon=icons.CALENDAR_MONTH_ROUNDED, label="Schedules")
])

appBar =AppBar(title=Text("Home"),center_title=True)

noCustomStartMenu = Column(controls=[
    Row(controls=[Text(value="Select a Cleaning Profile")]),
    Row(controls=[profileSelection_dropdown])],height=100,width=350)

withCustomStartMenu =Column(controls=[
    Row(controls=[profileSelection_dropdown]),
    Row(controls=[mode_dropdown,modeQ]),
    Row(controls=[speed_dropdown,speedQ]),
    Row(controls=[laps_dropdown,lapsQ])],height=330,width=350,alignment="spaceEvenly")