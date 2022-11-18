import flet
from theme import *
from flet import (AppBar, Dropdown, ElevatedButton, Icon, Page, Row, Text,
                  TextField, View, colors, dropdown, icons,Column)

modeText = Text(value="Choose a Mode", size=16, expand=True)
lapsText = Text(value="Choose How Many Laps",size=16,expand = True)
speedText = Text(value="Choose a Speed",size=16,expand=True)

modeQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="describe modes")
lapsQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="sdescribe slaps")
speedQ = Icon(name=icons.INFO_OUTLINE_ROUNDED, tooltip="dexfirpbe speed")

profileNameInput = TextField(label="Name", hint_text="My Cleaning Profile", expand=True, autofocus=True)

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

createCleaningProfileContents = [AppBar(title=Text("Create Profile"),center_title=True),Column(controls=[
    Row(controls=[profileNameInput]),
    Row(controls=[modeText,modeQ]),
    mode_dropdown,
    Row(controls=[speedText,speedQ]),
    speed_dropdown,
    Row(controls=[lapsText,lapsQ]),
    laps_dropdown],alignment = "spaceAround")
    ]
        