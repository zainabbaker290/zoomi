from theme import *

from flet import (AppBar, Column, Container, Dropdown, Icon,
                  NavigationBar, NavigationDestination, Row, Text, TextField, dropdown, icons, padding)

navBar = NavigationBar(
    destinations=[
        NavigationDestination(icon=icons.CLEANING_SERVICES, label="Profiles"),
        NavigationDestination(icon=icons.HOME_ROUNDED, label="Home"),
        NavigationDestination(
            icon=icons.CALENDAR_MONTH_ROUNDED, label="Schedules")
    ])

appBar = AppBar(title=Text("Home"), center_title=True)

modeText = Text(value="Choose a Mode", size=16, expand=True)

lapsText = Text(value="Choose How Many Laps", size=16, expand=True)

speedText = Text(value="Choose a Speed", size=16, expand=True)

dayText = Text(value="Choose a Day", size=16, expand=True)

timeText = Text(value="Choose a Time", size=16, expand=True)

reccuranceText = Text(value="Choose the Repititon", size=16, expand=True)

profileSelectionText = Text(
    value="Choose a Cleaning Profile", size=16, expand=True)

modeQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
             tooltip="placeholder for tooltip - to be added later")

lapsQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
             tooltip="splaceholder for tooltip - to be added later")

speedQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
              tooltip="dplaceholder for tooltip - to be added later")

dayQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
            tooltip="placeholder for tooltip - to be added later")

timeQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
             tooltip="placeholder for tooltip - to be added later")

reccuranceQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
                   tooltip="placeholder for tooltip - to be added later")

profileSelectionQ = Icon(name=icons.INFO_OUTLINE_ROUNDED,
                         tooltip="placeholder for tooltip - to be added later")

scheduleNameInput = TextField(
    label="Name", hint_text="My Scheduled Clean", expand=True)

profileNameInput = TextField(
    label="Name", hint_text="My Cleaning Profile", expand=True, autofocus=True)

mode_dropdown = Dropdown(
    expand=True,
    label="Mode",
    hint_text="Choose your Cleaning Mode",
    options=[
        dropdown.Option("Automatic"),
        dropdown.Option("Turbo"),
        dropdown.Option("Green"),
    ],
)
speed_dropdown = Dropdown(
    expand=True,
    label="Speed",
    hint_text="Choose your Speed",
    options=[
        dropdown.Option("Default"),
        dropdown.Option("Quick Clean"),
        dropdown.Option("Deep Clean"),
    ],
)
laps_dropdown = Dropdown(
    expand=True,
    label="Laps",
    hint_text="Choose your Number of Laps",
    options=[
        dropdown.Option("One Lap"),
        dropdown.Option("Two Laps"),
        dropdown.Option("Three Laps"),
    ],
)

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

createScheduledCleanContents = [AppBar(title=Text("Create a Scheduled Clean"), center_title=True), Column(controls=[
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

noCustomEditMenu = Container(content=Column(controls=(
    Container(content=Row(
        controls=[scheduleNameInput]), padding=padding.only(top=10)),
    Row(controls=[day_dropdown, dayQ]),
    Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown, timeQ]),
    Row(controls=[repetition_dropdown, reccuranceQ]),
    Row(controls=[profileSelection_dropdown, profileSelectionQ])), width=350, height=280, scroll="auto", auto_scroll=True), padding=padding.all(5))

withCustomEditMenu = Container(content=Column(controls=(
    Container(content=Row(
        controls=[scheduleNameInput]), padding=padding.only(top=10)),
    Row(controls=[day_dropdown, dayQ]),
    Row(controls=[hours_dropdown, minutes_dropdown, amPm_dropdown, timeQ]),
    Row(controls=[repetition_dropdown, reccuranceQ]),
    Row(controls=[profileSelection_dropdown, profileSelectionQ]),
    Row(controls=[mode_dropdown, laps_dropdown, speed_dropdown])), width=350, height=280, scroll="auto", auto_scroll=True))

configureCleaningProfileContents = [
    Row(controls=[mode_dropdown, laps_dropdown, speed_dropdown])]

noCustomStartMenu = Column(controls=[
    Row(controls=[Text(value="Select a Cleaning Profile")]),
    Row(controls=[profileSelection_dropdown])], height=100, width=350)

withCustomStartMenu = Column(controls=[
    Row(controls=[profileSelection_dropdown]),
    Row(controls=[mode_dropdown, modeQ]),
    Row(controls=[speed_dropdown, speedQ]),
    Row(controls=[laps_dropdown, lapsQ])], height=330, width=350, alignment="spaceEvenly")

createCleaningProfileContents = [AppBar(title=Text("Create Profile"), center_title=True), Column(controls=[
    Row(controls=[profileNameInput]),
    Row(controls=[modeText, modeQ]),
    mode_dropdown,
    Row(controls=[speedText, speedQ]),
    speed_dropdown,
    Row(controls=[lapsText, lapsQ]),
    laps_dropdown], alignment="spaceAround")
]


def clear_schedule_values():
    scheduleNameInput.error_text = None
    day_dropdown.error_text = None
    hours_dropdown.error_text = None
    minutes_dropdown.error_text = None
    amPm_dropdown.error_text = None
    repetition_dropdown.error_text = None
    profileSelection_dropdown.error_text = None
    mode_dropdown.error_text = None
    speed_dropdown.error_text = None
    laps_dropdown.error_text = None
    scheduleNameInput.value = None
    day_dropdown.value = None
    hours_dropdown.value = None
    minutes_dropdown.value = None
    amPm_dropdown.value = None
    repetition_dropdown.value = None
    profileSelection_dropdown.value = None
    mode_dropdown.value = None
    speed_dropdown.value = None
    laps_dropdown.value = None


def clear_profile_values():
    profileNameInput.error_text = None
    mode_dropdown.error_text = None
    speed_dropdown.error_text = None
    laps_dropdown.error_text = None
    profileNameInput.value = None
    mode_dropdown.value = None
    speed_dropdown.value = None
    laps_dropdown.value = None
