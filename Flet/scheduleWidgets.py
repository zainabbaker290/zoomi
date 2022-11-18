import flet
from flet import AppBar, Container,ElevatedButton, Page, Text, View, Column, padding,colors,margin,Row,Dropdown,ResponsiveRow, Icon, colors, icons, ElevatedButton, Page, Text, dropdown, TextField
from profiles import fetch_profiles_from_DB
from profileWidgets import *
from theme import *
dayText = Text(value="Choose a Day",size=16, expand=True)
timeText = Text(value="Choose a Time",size=16, expand=True)
reccuranceText = Text(value="Choose the Repititon",size=16, expand=True)
profileSelectionText = Text(value="Choose a Cleaning Profile",size=16, expand=True)

dayQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="describe modes")
timeQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="describe modes")
reccuranceQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="describe modes")
profileSelectionQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="describe modes")

scheduleNameInput = TextField(label="Name", hint_text="My Scheduled Clean",expand=True)
day_dropdown = Dropdown(
        expand=True,
        label="Day",
        hint_text="Choose a Day",
        options=[
            dropdown.Option("Monday"),
            dropdown.Option("Tuesday"),
            dropdown.Option("Wedensday"),
            dropdown.Option("Thursday"),
            dropdown.Option("Friday"),
            dropdown.Option("Saturday"),
            dropdown.Option("Sunday"),
        ],
    )
hours_dropdown = Dropdown(
    expand=True,
    label="Hours",
    hint_text="Choose an Hour",
    options=[
            dropdown.Option("1"),
            dropdown.Option("2"),
            dropdown.Option("3"),
            dropdown.Option("4"),
            dropdown.Option("5"),
            dropdown.Option("6"),
            dropdown.Option("7"),
            dropdown.Option("8"),
            dropdown.Option("9"),
            dropdown.Option("10"),
            dropdown.Option("11"),
            dropdown.Option("12")
        ],
    )
minutes_dropdown = Dropdown(
    expand=True,
    autofocus=True,
    label="Minutes",
    hint_text="Choose your Minute",
    options=[
            dropdown.Option("00"),
            dropdown.Option("05"),
            dropdown.Option("10"),
            dropdown.Option("15"),
            dropdown.Option("20"),
            dropdown.Option("25"),
            dropdown.Option("30"),
            dropdown.Option("35"),
            dropdown.Option("40"),
            dropdown.Option("45"),
            dropdown.Option("50"),
            dropdown.Option("55"),
        ],
    )
amPm_dropdown = Dropdown(
    expand=True,
    label="Time",
    hint_text="Choose your Time of Day",
    options=[
            dropdown.Option("AM"),
            dropdown.Option("PM"),
        ],
    )
repetition_dropdown = Dropdown(
        expand=True,
        label="Repetitions",
        hint_text="Choose how often you'd like your Cycle to Repeat",
        options=[
            dropdown.Option("Daily"),
            dropdown.Option("Every Three Days"),
            dropdown.Option("Weekly"),
            dropdown.Option("Every Two Weeks")
        ],
    )

profileSelection_dropdown = Dropdown(
    expand=True,
        label="Profile Selection",
        hint_text="Which Cleaning Profile would you like to Use?",
        options=[
            dropdown.Option("Default"),
            dropdown.Option("Custom"),
        ],
        
    )



createScheduledCleanContents =[AppBar(title=Text("Create a Scheduled Clean"),center_title=True),Column(controls=[
    Row(controls=[scheduleNameInput]),
    Row(controls=[dayText]),
    Row(controls=[day_dropdown, dayQ]),
    Row(controls=[timeText]),
    Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown, timeQ]),
    Row(controls=[reccuranceText]),
    Row(controls=[repetition_dropdown, reccuranceQ]),
    Row(controls=[profileSelectionText]),
    Row(controls=[profileSelection_dropdown, profileSelectionQ])])
    ]
noCustomEditMenu=Container(content=Column(controls=(
            Container(content=Row(controls=[scheduleNameInput]),padding=padding.only(top=10)),
            Row(controls=[day_dropdown, dayQ]),
            Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown,timeQ]),
            Row(controls=[repetition_dropdown,reccuranceQ]),
            Row(controls=[profileSelection_dropdown,profileSelectionQ])),width=350,height=280,scroll="auto",auto_scroll=True),padding=padding.all(5))

withCustomEditMenu = Container(content=Column(controls=(
            Container(content=Row(controls=[scheduleNameInput]),padding=padding.only(top=10)),
            Row(controls=[day_dropdown, dayQ]),
            Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown,timeQ]),
            Row(controls=[repetition_dropdown,reccuranceQ]),
            Row(controls=[profileSelection_dropdown,profileSelectionQ]),
            Row(controls=[mode_dropdown,laps_dropdown, speed_dropdown])),width=350,height=280,scroll="auto",auto_scroll=True))

configureCleaningProfileContents = [Row(controls=[mode_dropdown,laps_dropdown, speed_dropdown])]