from database import *
from pages.HomePage import HomePage
from pages.ProfileCreationPage import ProfileCreationPage
from pages.ProfilesPage import ProfilesPage
from pages.ScheduleCreationPage import ScheduleCreationPage
from pages.SchedulesPage import SchedulesPage
from theme import *
from widgets import *

import flet
from flet import FloatingActionButton, Page, Text, View, icons, theme


def fletmain(page: Page):
    page.session.set
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 780
    print("d")
    def navbar_change(e):
        if navBar.selected_index == 0:
            open_profiles(e)
        if navBar.selected_index == 1:
            open_home(e)
        if navBar.selected_index == 2:
            open_schedules(e)

    navBar.on_change = navbar_change

    

    def route_change(e):
        page.views.clear()
        page.theme_mode = "light"
        page.theme = theme.Theme(
            color_scheme_seed="#006781", use_material3=True)
        appBar.title = (Text("Home"))
        homePage = HomePage(page)
        page.views.append(
            View(
                "/",
                [appBar, homePage, navBar]
            )
        )
        navBar.selected_index = 1

        if page.route == "/schedules" or page.route == "/schedules/createschedule":
            appBar.title = Text(value="Scheduled Cleans")
            schedulesDisplay = SchedulesPage(page)
            page.views.append(
                View(
                    "/schedules",

                    [appBar,
                     schedulesDisplay,
                     FloatingActionButton(
                         icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createschedule),
                     navBar],
                    scroll="auto"
                )
            )
            navBar.selected_index = 2

        if page.route == "/profiles" or page.route == "/profiles/createprofile":
            appBar.title = Text(value="Cleaning Profiles")
            profilesDisplay = ProfilesPage(page)
            page.views.append(
                View(
                    "/profiles",

                    [appBar,
                     profilesDisplay,
                     FloatingActionButton(
                         icon=icons.ADD_CIRCLE_OUTLINED, on_click=open_createprofile),
                     navBar],

                    scroll="auto"
                )

            )
            navBar.selected_index = 0

        if page.route == "/schedules/createschedule":
            appBar.title = Text(value="Create a Scheduled Clean")
            createSchedulePage = ScheduleCreationPage(page)
            page.views.append(
                View(
                    "/schedules/createschedule",
                    [appBar, createSchedulePage],
                    scroll="auto"
                )
            )

        elif page.route == "/profiles/createprofile":
            appBar.title = Text("Create a Cleaning Profile")
            page.vertical_alignment = "spaceAround"
            createProfilePage = ProfileCreationPage(page)
            page.views.append(
                View(
                    "/profiles/createprofile",
                    [appBar,
                     createProfilePage],
                    horizontal_alignment="center"
                )
            )

        page.update()

    def view_pop(e):
        clear_profile_values()
        clear_schedule_values()
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


flet.app(target=fletmain, assets_dir="assets")
