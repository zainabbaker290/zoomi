import sqlite3
from scheduleWidgets import *
from profileWidgets import *
def fetch_schedules_from_DB():
    return parse_schedules(read_schedules_from_DB())
    
def read_schedules_from_DB():
    con = sqlite3.connect("app.db")
    cur =con.cursor()
    schedules = cur.execute("SELECT * FROM schedules")
    s = schedules.fetchall()
    con.close()
    return s

def parse_schedules(schedules):
    scheduleDict= {}
    for schedule in schedules:
        schedule_ID = schedule[0]
        schedule_Name = schedule[1]
        schedule_Day = schedule[2]
        schedule_Time= schedule[3]
        schedule_Repetition = schedule[4]
        schedule_Profile = schedule[5]
        schedule_Mode= schedule[6]
        schedule_Speed= schedule[7]
        schedule_Laps = schedule[8]
        scheduleDict[schedule_ID] = {
        "Name": schedule_Name, 
        "Day" : schedule_Day,
        "Time" : schedule_Time,
        "Repetition" : schedule_Repetition,
        "Profile": schedule_Profile,
        "Mode":schedule_Mode, 
        "Speed":schedule_Speed,
        "Laps":schedule_Laps
        }
    return scheduleDict

def write_schedule_to_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    name = scheduleNameInput.value
    day = day_dropdown.value
    time = hours_dropdown.value + ":" + minutes_dropdown.value + amPm_dropdown.value
    repetition = repetition_dropdown.value
    profile = profileSelection_dropdown.value
    mode = mode_dropdown.value
    speed = speed_dropdown.value
    laps = laps_dropdown.value
    data = [name,day,time,repetition,profile,mode,speed,laps]
    cur.execute(
        """INSERT into schedules(name,day,time,repetition,profile,mode,speed,laps)
            VALUES (?,?,?,?,?,?,?,?)"""
        ,data
        )
    con.commit()
    con.close()
    clear_schedule_values()

def remove_schedule_from_DB(scheduleIndex):
            con = sqlite3.connect("app.db")
            cur =con.cursor()
            cur.execute("DELETE FROM schedules WHERE schedule_id = ?",(scheduleIndex,))
            con.commit()
            con.close()

def write_updated_schedule_to_DB(scheduleIndex):
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    index = scheduleIndex
    name = scheduleNameInput.value
    day = day_dropdown.value
    time = hours_dropdown.value + ":" + minutes_dropdown.value + amPm_dropdown.value
    repetition = repetition_dropdown.value
    profile = profileSelection_dropdown.value
    mode = mode_dropdown.value
    speed = speed_dropdown.value
    laps = laps_dropdown.value
    data = [name,day,time,repetition,profile,mode,speed,laps,index]
    cur.execute(
        """UPDATE schedules
        SET name = ?, day = ?, time = ?, repetition = ?, profile =?, mode=?, speed=? ,laps = ?
        WHERE schedule_id = ?;"""
        ,data)
    con.commit()
    con.close()
    clear_schedule_values()
    
def update_profile_selection_dropdown():
    profileSelection_dropdown.options = []
    profileSelection_dropdown.options.append(dropdown.Option("Default"))
    profileSelection_dropdown.options.append(dropdown.Option("Custom"))
    profiles = fetch_profiles_from_DB()
    for profile in profiles:
        profiles = fetch_profiles_from_DB()
        name = profiles[profile]["Name"] 
        profileSelection_dropdown.options.append(dropdown.Option(name))

def clear_schedule_values():
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