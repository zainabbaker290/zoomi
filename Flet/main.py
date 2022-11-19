import flet
import sqlite3
from math import pi
from flet.transform import Scale
from flet import (AppBar, Dropdown, theme, ElevatedButton, Image,Icon, Page, Row, Text, FilledTonalButton , IconButton, FloatingActionButton, border_radius,
                  TextField, View, colors, dropdown, icons,AlertDialog,Card, filled_tonal_button,margin,padding, Container, TextButton, Column, alignment, SnackBar, NavigationBar, NavigationDestination)
from scheduleWidgets import *
from profileWidgets import *
from profiles import *
from schedules import *
from home import *
from theme import *

zoomiBatteryPercentage = 100
zoomiState= "deactivated"
zoomiBagPercentage = 0
zoomiFlipped= False

def main(page: Page):
    page.window_resizable=False
    page.window_width= 500
    page.window_height = 780
    output_text = Text()   
    #BatteryIcon = Icon(icon=icons.BATTERY_FULL)
    #runs when start cycle button pressed.
    def start_cycle(e):
        if profileSelection_dropdown.value=="Custom":
            userInputs=[mode_dropdown,laps_dropdown,speed_dropdown]
            if not verify_inputs(userInputs):
                return 
        page.snack_bar=SnackBar(Text("Your Cleaning Cycle Has Started!"))
        page.snack_bar.open = True
        close_dlg(e)
        page.update()
    
    def check_for_custom(e):
        if profileSelection_dropdown.data == "edit":
            if profileSelection_dropdown.value == "Custom":
                    scheduleEditorMenu.content = withCustomEditMenu
                    page.update()
            else:
                    scheduleEditorMenu.content = noCustomEditMenu
                    page.update()
        elif profileSelection_dropdown.data == "start":
            if profileSelection_dropdown.value == "Custom":
                    startCycleMenu.content = withCustomStartMenu
                    page.update()
            else:
                startCycleMenu.content = noCustomStartMenu
                page.update()
        else:
            if profileSelection_dropdown.value == "Custom":
                refresh_schedule_creation_custom()
            else:
                refresh_schedule_creation_no_custom()

    def navbar_change(e):
        if navBar.selected_index == 0:
            open_profiles(e)
        if navBar.selected_index == 1:
            open_home(e)
        if navBar.selected_index == 2:
            open_schedules(e)

    navBar.on_change = navbar_change
    profileSelection_dropdown.on_change = check_for_custom
    def card_on_hover(e):
        e.control.content.elevation = 3 if e.data == "true" else 1
        page.update()
    def open_dlg(dlg):
        page.dialog = dlg
        dlg.open = True
        page.update()
   
        return
    def close_dlg(e):
        page.dialog.open = False
        page.update()

    def display_profiles(profileDict):
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
                        ),expand=True),expand=True, on_hover=card_on_hover),
                        Card(content=Container(content=Column(controls=[
                            IconButton(icon=icons.EDIT_OUTLINED,icon_color=onPC, icon_size=20, height=40,width=40, on_click = open_default_profile_editor)
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
                            ),expand=True),expand=True,on_hover=card_on_hover),
                        Container(content=Card(content=Container(content=Column(controls=[
                                IconButton(icon=icons.EDIT_OUTLINED,icon_color= onTC,icon_size=20, height=40,width=40, data=profileIndex, on_click = open_profile_editor),
                                IconButton(icon=icons.DELETE_OUTLINED,icon_color= onTC,icon_size=20, height=40,width=40, data=profileIndex, on_click = delete_profile)],
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

    def display_schedules(scheduleDict):
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
                            ),expand=True)),expand=True,on_hover=card_on_hover),
                        Card(content=Container(content=Column(controls=[
                                IconButton(icon=icons.EDIT_OUTLINED,icon_color=onTC, icon_size=20,height=40,width=40, data=scheduleIndex, on_click = open_schedule_editor),
                                IconButton(icon=icons.DELETE_OUTLINED, icon_color=onTC,icon_size=20, height=40,width=40, data=scheduleIndex, on_click = delete_schedule)],
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
                            ),expand=True),expand=True,on_hover=card_on_hover),
                        Card(content=Container(content=Column(controls=[
                                IconButton(icon=icons.EDIT_OUTLINED,icon_color=onTC, icon_size=20, height=40,width=40, data=scheduleIndex, on_click = open_schedule_editor),
                                IconButton(icon=icons.DELETE_OUTLINED, icon_color=onTC, icon_size=20, height=40,width=40, data=scheduleIndex, on_click = delete_schedule)],
                                spacing=0
                                ),
                                bgcolor=tC,
                                border_radius=border_radius.all(10)
                        
                                
                            ))
                        ],spacing=0)
                    schedulesDisplay.controls.append(scheduleCard)
        else:
            schedulesDisplay.controls.append(Text(value="You haven't created any Scheduled Cleans. Try one out below!"))
        schedulesDisplay.spacing=0
        return schedulesDisplay

    def delete_schedule(e):
        scheduleIndex=e.control.data
        remove_schedule_from_DB(scheduleIndex)
        refresh_schedules()
        page.snack_bar = SnackBar(Text("Your Schedule Has Been Deleted"))
        page.snack_bar.open = True
        page.update()

    def delete_profile(e):
        profileIndex=e.control.data
        remove_profile_from_DB(profileIndex)
        refresh_profiles()
        page.snack_bar = SnackBar(Text("Your Profile Has Been Deleted"))
        page.snack_bar.open = True
        page.update()

    def open_start_cycle_menu(e):
        update_profile_selection_dropdown()
        profileSelection_dropdown.value = "Default"
        startCycleMenu.content=noCustomStartMenu
        profileSelection_dropdown.data = "start"
        open_dlg(startCycleMenu)

    def open_default_profile_editor(e):
        defaultProfile = fetch_default_profile_from_DB()
        mode_dropdown.value = defaultProfile["Mode"]
        speed_dropdown.value = defaultProfile["Speed"]
        laps_dropdown.value = defaultProfile["Laps"]
        defaultProfileEditorMenu.content = Column(controls=(
        Row(controls=[mode_dropdown,modeQ]),
        Row(controls=[speed_dropdown,speedQ]),
        Row(controls=[laps_dropdown,lapsQ])),height=220,width=350)
        open_dlg(defaultProfileEditorMenu)

    def open_profile_editor(e):
        profileIndex=e.control.data
        profilesDict = fetch_profiles_from_DB()
        object = profilesDict[profileIndex]
        profileNameInput.value =object["Name"]
        mode_dropdown.value = object["Mode"]
        speed_dropdown.value = object["Speed"]
        laps_dropdown.value = object["Laps"]
        profileEditorMenu.content = Column(controls=(Row(controls=[profileNameInput]),
        Row(controls=[mode_dropdown,modeQ]),
        Row(controls=[speed_dropdown,speedQ]),
        Row(controls=[laps_dropdown,lapsQ])),height=280,width=350)
        profileEditorMenu.data = profileIndex
        open_dlg(profileEditorMenu)

    def open_schedule_editor(e):
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
            scheduleEditorMenu.content = withCustomEditMenu
            
        else:
            scheduleEditorMenu.content = noCustomEditMenu
        scheduleEditorMenu.data = scheduleIndex
        open_dlg(scheduleEditorMenu)

    def create_schedule(e):
        write_schedule_to_DB()
        close_dlg(e)
        view_pop_noe()
        page.snack_bar = SnackBar(Text("Your Schedule has been Saved"))
        page.snack_bar.open = True
        page.update()
        
    def create_profile(e):
        write_profile_to_DB()
        close_dlg(e)
        view_pop_noe()
        page.snack_bar = SnackBar(Text("Your Profile has been Saved"))
        page.snack_bar.open = True
        page.update()  
    
    def edit_profile(e):
        existingProfiles = fetch_profiles_from_DB()
        profileIndex = profileEditorMenu.data
        nameInput = profileNameInput
        if verify_edit_name(existingProfiles,profileIndex,nameInput):
            profileNameInput.error_text = None
            close_dlg(e)
            write_updated_profile_to_DB(profileIndex)
            refresh_profiles()
            page.snack_bar = SnackBar(Text("Your Profile has been Updated"))
            page.snack_bar.open = True
            page.update()

    def edit_default_profile(e):
        close_dlg(e)
        write_updated_default_profile_to_DB()
        refresh_profiles()
        page.snack_bar = SnackBar(Text("Your Default Profile has been Updated"))
        page.snack_bar.open = True
        page.update()

    def edit_schedule(e):
        existingSchedules = fetch_schedules_from_DB()
        scheduleIndex = scheduleEditorMenu.data
        nameInput = scheduleNameInput
        userInputs = [scheduleNameInput, day_dropdown,hours_dropdown,
        minutes_dropdown, amPm_dropdown,
        repetition_dropdown, profileSelection_dropdown]
        if profileSelection_dropdown.value == "Custom":
            userInputs.append(mode_dropdown)
            userInputs.append(speed_dropdown)
            userInputs.append(laps_dropdown)
        if verify_edit_name(existingSchedules,scheduleIndex,nameInput) and verify_inputs(userInputs) == True:
            scheduleNameInput.error_text = None
            close_dlg(e)
            write_updated_schedule_to_DB(scheduleIndex)
            refresh_schedules()
            page.snack_bar = SnackBar(Text("Your Schedule has been Updated"))
            page.snack_bar.open = True
            page.update()
        return

    def deny_editSchedule(e):
        clear_schedule_values()
        close_dlg(e)

    def deny_editProfile(e):
        clear_profile_values()
        close_dlg(e)

    startCycleMenu = AlertDialog(
        modal=True,
        title=Text("Start Cleaning Cycle?"),
        content=[],
        actions=[
            TextButton("Begin", on_click=start_cycle),
            TextButton("Cancel", on_click=close_dlg)
            ]
        )   
    profileEditorMenu = AlertDialog(
        modal=True,
        title=Text("Edit Profile"),
        content=[],
        actions=[
            TextButton("Save", on_click=edit_profile),
            TextButton("Exit", on_click=deny_editProfile)
            ]
        )   
    defaultProfileEditorMenu = AlertDialog(
        modal=True,
        title=Text("Edit Default Profile"),
        content=[],
        actions=[
            TextButton("Save", on_click=edit_default_profile),
            TextButton("Exit", on_click=deny_editProfile)
            ]
        )   
    scheduleEditorMenu = AlertDialog(
        modal=True,
        title=Text("Edit Schedule"),
        content=[],
        actions=[
            TextButton("Save", on_click=edit_schedule),
            TextButton("Exit", on_click=deny_editSchedule)
            ]
        )   
    createScheduleConfirmation = AlertDialog(
        modal=True,
        title=Text("Confirm Selection?"),
        content=[],
        actions=[
            TextButton("Yes", on_click=create_schedule
    ),
            TextButton("No", on_click=close_dlg)
            ]
        )   

    createProfileConfirmation = AlertDialog(
        modal=True,
        title=Text("Confirm Selection?"),
        content= [],
        actions=[
            TextButton("Yes", on_click=create_profile),
            TextButton("No", on_click=close_dlg)
            ]
        ,
        actions_alignment="spaceAround")
    
    def verify_inputs(userInputs):
        fail = False
        for input in userInputs:
                if not input.value:
                    input.error_text = f"Please Choose {input.label}"
                    page.snack_bar = SnackBar(Text("Please Fill in all Inputs"))
                    page.snack_bar.open = True
                    fail = True
                else:
                    input.error_text = None
                page.update()
        if fail:
            return False
        else:
            return True


    def verify_create_name(existingObjects,input):
        for object in existingObjects:
            print(existingObjects[object]["Name"])
            if existingObjects[object]["Name"] == input.value:
                input.error_text = "This name has already been used."
                page.update()
                return False
        else: 
            input.error_text = None
            return True

    def verify_edit_name(existingObjects,index,input):
        fail = False
        if not input.value:
            input.error_text = "Please Enter Name."
            page.update()
            return False
        print(existingObjects)
        for profileIndex in existingObjects:
            print(existingObjects[profileIndex]["Name"])
            print("index",profileIndex)
            print("editor index",input)
            if existingObjects[profileIndex]["Name"] == input.value and profileIndex != index:
                input.error_text = "This name has already been used."
                page.update()
                fail = True
        if fail:
            return False
        else:
            input.error_text = None
            page.update()
            return True
        

    
    def create_profile_submit(e):
        existingProfiles = fetch_profiles_from_DB()
        nameInput = profileNameInput
        userInputs = [mode_dropdown,speed_dropdown,laps_dropdown,profileNameInput]
        if verify_inputs(userInputs) == True and verify_create_name(existingProfiles,nameInput) == True:
            createProfileConfirmation.content = Column(
                controls=[
                Text(profileNameInput.value),
                Row(controls=[
                Text(mode_dropdown.value),
                Text(speed_dropdown.value),
                Text(laps_dropdown.value)
                ],
                alignment="spaceAround")],height=80,horizontal_alignment="center",alignment="spaceEvenly"
                )
            open_dlg(createProfileConfirmation) 
            page.update()
    
    def create_schedule_submit(e):
        existingSchedules = fetch_schedules_from_DB()
        nameInput = scheduleNameInput
        userInputs = [scheduleNameInput, day_dropdown,hours_dropdown,
        minutes_dropdown, amPm_dropdown,
        repetition_dropdown, profileSelection_dropdown]
        if profileSelection_dropdown.value == "Custom":
            userInputs.append(mode_dropdown)
            userInputs.append(speed_dropdown)
            userInputs.append(laps_dropdown)
        if verify_inputs(userInputs) == True and verify_create_name(existingSchedules,nameInput) == True:
                createScheduleConfirmation.content = Column(controls=[
                    Text(scheduleNameInput.value),
                    Text(day_dropdown.value),
                    Text(hours_dropdown.value),
                    Text(minutes_dropdown.value), 
                    Text(amPm_dropdown.value),
                    Text(repetition_dropdown.value),
                    Text(profileSelection_dropdown.value)],
                    height = 200
                    )
                open_dlg(createScheduleConfirmation)
                page.update()
    
    def determineBatteryIcon():
        if zoomiBatteryPercentage == 100:
            return Icon(name=icons.BATTERY_FULL,color=colors.GREEN,rotate=pi/2)
        else:
            return Icon(name=icons.BATTERY_UNKNOWN)

    def determineCapacityIcon():
        if zoomiBagPercentage <100:
            return Icon(name=icons.CHECK, color=colors.GREEN)
        else:
            return Icon(name=icons.WARNING, color=colors.RED)

    def determineStatusIcon():
        if zoomiState == "active":
            return Icon(name=icons.CIRCLE, color=colors.GREEN)
        if zoomiState == "deactivated":
            return Icon(name=icons.CIRCLE, color=colors.ORANGE)
        if zoomiState == "sleep":
            return Icon(name=icons.PAUSE_CIRCLE)

    createprofilesubmit_btn = ElevatedButton(text="Submit", on_click=create_profile_submit)
    createschedulesubmit_btn = ElevatedButton(text="Submit", on_click=create_schedule_submit)

    
    def route_change(e):
        page.views.clear()
        appBar.title=(Text("Home"))
        status = "Standby"
        batteryIcon = determineBatteryIcon()
        capacityIcon = determineCapacityIcon()
        statusIcon = determineStatusIcon()
        page.views.append(
            View(
                "/",
                [
                    appBar,
                    Column(
                        controls=[
                            # Row(controls=[
                            #     Text(value="My Zoomi Robot", style="titleLarge"),
                            #     statusIcon
                            #     ]
                            # ),
                            Card(content=
                                    Column(
                                        controls=[
                                        Row(controls=[
                                            Text(value="Welcome Home",style="titleLarge"),
                                        ]
                                        ),
                                        Image(src=f"roomba.png",width=200,height=200),
                                        Row(controls=[
                                            Text(value=status,style="titleMedium"),
                                            statusIcon
                                        ]
                                        ),
                                        Row(
                                            controls=[
                                                Row(controls=[
                                                    Text(value="Battery"),
                                                    batteryIcon]),
                                                Row(controls=[
                                                    Text(value="Capacity"),
                                                    capacityIcon])
                                            ]
                                        ),
                                        
                                        
                                        ]
                                    )           
                                )
                        ],
                        horizontal_alignment="center"
                        
                    ),
                    ElevatedButton("Start Cycle", on_click=open_start_cycle_menu),
                    navBar
                    
                ],
                horizontal_alignment="center"
                )
            )
        page.theme_mode="light"
        page.theme=theme.Theme(color_scheme_seed="#006781",use_material3=True)
        navBar.selected_index=1

        if page.route == "/schedules" or page.route == "/schedules/createschedule":
            appBar.title=Text(value="Scheduled Cleans")
            s = fetch_schedules_from_DB()
            d = display_schedules(s)
            page.views.append(
                View(
                    "/schedules",
                    
                    [appBar,
                    d,
                    FloatingActionButton(icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createschedule),
                    navBar],
                    scroll="auto"
                )
            )
            navBar.selected_index=2

        if page.route == "/profiles" or page.route == "/profiles/createprofile":
            print(read_profiles_from_DB())
            appBar.title=Text(value="Cleaning Profiles")
            parsedProfile= parse_profiles(read_profiles_from_DB())
            profilesDisplay = display_profiles(parsedProfile)
            page.views.append(
                View(
                    "/profiles",
                    
                    [appBar,
                    profilesDisplay,
                    FloatingActionButton(icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createprofile),
                    navBar],
                    scroll="auto")
                )
            navBar.selected_index=0

        

        if page.route == "/schedules/createschedule":
            appBar.title=Text(value="Create a Scheduled Clean")
            contents = []
            update_profile_selection_dropdown()
            profileSelection_dropdown.data = "create"

            for widget in createScheduledCleanContents:
                contents.append(widget)

            contents.append(createschedulesubmit_btn)
            contents.append(output_text)
            page.views.append(
                View(
                    "/schedules/createschedule", 
                    [contents],scroll="auto"
                    
                )
            )

        elif page.route == "/profiles/createprofile":
            appBar.title=Text("Create a Cleaning Profile")
            contents = createCleaningProfileContents
            contents.append(createprofilesubmit_btn)
            contents.append(output_text)
            page.vertical_alignment="spaceAround"
            page.views.append(
                View(
                    "/profiles/createprofile", 
                    [appBar,
                    Row(controls=[profileNameInput]),
                    Container(content=Column(controls=[Row(controls=[modeText,]),Row(controls=[mode_dropdown,modeQ])])),
                    Column(controls=[Row(controls=[speedText]),Row(controls=[speed_dropdown,speedQ])]),
                    Column(controls=[Row(controls=[lapsText]),Row(controls=[laps_dropdown,lapsQ])]),
                    createprofilesubmit_btn
                    ],
                    horizontal_alignment="center"
                        
                )
            )

        page.update()
    
    def refresh_schedule_creation_no_custom():
        page.views.pop()
        contents = []
        for widget in createScheduledCleanContents:
            contents.append(widget)
        contents.append(createschedulesubmit_btn)
        contents.append(output_text)
        page.views.append(
            View(
                "/schedules/createschedule", 
                contents, scroll="auto"
                
            )
        )
        page.update()

    def refresh_schedule_creation_custom():
        page.views.pop()
        contents = []
        for widget in createScheduledCleanContents:
            contents.append(widget)
        for widget in configureCleaningProfileContents:
            contents.append(widget)
        contents.append(createschedulesubmit_btn)
        contents.append(output_text)
        page.views.append(
            View(
                "/schedules/createschedule", 
                contents, scroll="auto"
                
            )
        )
        page.update()

    def refresh_profiles():
        p= parse_profiles(read_profiles_from_DB())
        d = display_profiles(p)
        page.views.pop()
        page.views.append(
            View(
                "/profiles",
                 [appBar,d,
                 FloatingActionButton(icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createprofile)
                ,
                navBar]))
        page.update()

    def refresh_schedules():
        s = fetch_schedules_from_DB()
        d = display_schedules(s)
        page.views.pop()
        page.views.append(
            View(
                "/schedules",
                
                [appBar,d,
                FloatingActionButton(icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createschedule),
                navBar],scroll="auto",horizontal_alignment="center"
            )
        )
    
    # def page_resize(e):
    #     pw.value = f"{page.width} by {page.height}px"
    #     pw.update()

    # page.on_resize = page_resize

    # pw = Text(bottom=50, right=50, style="displaySmall")
    # page.overlay.append(pw)

    def view_pop_noe():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_home(e):
        page.go("/")

    def open_createprofile(e):
        page.go("/profiles/createprofile")

    def open_profiles(e):
        page.go("/profiles")
    
    def open_schedules(e):
        page.go("/schedules")

    def open_createschedule(e):
        page.go("/schedules/createschedule")

    page.go(page.route)


flet.app(target=main,assets_dir="assets")
