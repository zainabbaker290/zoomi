from flet import *
from flet import padding, border,border_radius
def main(page):
    page.title = "ListTile Examples"
    page.add(
        Card(
            content=Container(
                width=500,
                content=Column(
                    [
                        ListTile(
                            title=Text("One-line list tile"),
                        ),
                        ListTile(title=Container(content=Row(controls =[
                                Text(value = "scdlksflfdldskfskkldf",style="titleMedium",color=colors.AMBER)
                            ],
                            alignment="center"),bgcolor=colors.AMBER_100,padding=5,),subtitle=
                            Container(content=Row(controls=[
                                    Text(value = "ddcxc",style="titleSmall"),
                                    Text(value = "xcvxc",style="titleSmall"),
                                    Text(value = "dscvc",style="titleSmall"),
                                    ],alignment="spaceEvenly"
                                )
                                ,padding=padding.only(top=11)
                                ), trailing= Card(content=Container(content=Column(controls=[
                                IconButton(icon=icons.EDIT_OUTLINED, icon_size=20,height=40,width=40),
                                IconButton(icon=icons.DELETE_OUTLINED,icon_size=20, height=40,width=40) ],
                                spacing=0
                                ),
                                bgcolor=colors.BLUE,
                                border_radius=border_radius.all(10)
                        
                                
                            )), dense=True),
                        ListTile(
                            leading=Icon(icons.SETTINGS),
                            title=Text("One-line selected list tile"),
                            selected=True,
                        ),
                        ListTile(
                            leading=Image(src="/icons/icon-192.png", fit="contain"),
                            title=Text("One-line with leading control"),
                        ),
                        ListTile(
                            title=Text("One-line with trailing control"),
                            trailing=PopupMenuButton(
                                icon=icons.MORE_VERT,
                                items=[
                                    PopupMenuItem(text="Item 1"),
                                    PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                        ListTile(
                            leading=Icon(icons.ALBUM),
                            title=Text("One-line with leading and trailing controls"),
                            trailing=PopupMenuButton(
                                icon=icons.MORE_VERT,
                                items=[
                                    PopupMenuItem(text="Item 1"),
                                    PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                        ListTile(
                            leading=Icon(icons.SNOOZE),
                            title=Text("Two-line with leading and trailing controls"),
                            subtitle=Text("Here is a second title."),
                            trailing=PopupMenuButton(
                                icon=icons.MORE_VERT,
                                items=[
                                    PopupMenuItem(text="Item 1"),
                                    PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                    ],
                    spacing=0,
                ),
                padding=padding.symmetric(vertical=10),
            )
        )
    )

app(target=main)