import sqlite3
from widgets import *


def fetch_schedules_from_DB():
    return parse_schedules(read_schedules_from_DB())


def read_schedules_from_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    schedules = cur.execute("SELECT * FROM schedules")
    s = schedules.fetchall()
    con.close()
    return s


def parse_schedules(schedules):
    scheduleDict = {}
    for schedule in schedules:
        schedule_ID = schedule[0]
        schedule_Name = schedule[1]
        schedule_Day = schedule[2]
        schedule_Time = schedule[3]
        schedule_Repetition = schedule[4]
        schedule_Profile = schedule[5]
        schedule_Mode = schedule[6]
        schedule_Speed = schedule[7]
        schedule_Laps = schedule[8]
        scheduleDict[schedule_ID] = {
            "Name": schedule_Name,
            "Day": schedule_Day,
            "Time": schedule_Time,
            "Repetition": schedule_Repetition,
            "Profile": schedule_Profile,
            "Mode": schedule_Mode,
            "Speed": schedule_Speed,
            "Laps": schedule_Laps
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
    data = [name, day, time, repetition, profile, mode, speed, laps]
    cur.execute(
        """INSERT into schedules(name,day,time,repetition,profile,mode,speed,laps)
            VALUES (?,?,?,?,?,?,?,?)""", data
    )
    con.commit()
    con.close()
    clear_schedule_values()


def remove_schedule_from_DB(scheduleIndex):
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("DELETE FROM schedules WHERE schedule_id = ?",
                (scheduleIndex,))
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
    data = [name, day, time, repetition, profile, mode, speed, laps, index]
    cur.execute(
        """UPDATE schedules
        SET name = ?, day = ?, time = ?, repetition = ?, profile =?, mode=?, speed=? ,laps = ?
        WHERE schedule_id = ?;""", data)
    con.commit()
    con.close()
    clear_schedule_values()

def remove_profile_from_schedule(scheduleIndex):
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    index = scheduleIndex
    profile = "Default"
    data = [profile, index]
    cur.execute(
        """UPDATE schedules
        SET profile =?
        WHERE schedule_id = ?;""", data)
    con.commit()
    con.close()

def update_profile_selection_dropdown():
    profileSelection_dropdown.options = []
    profileSelection_dropdown.options.append(dropdown.Option("Default"))
    profileSelection_dropdown.options.append(dropdown.Option("Custom"))
    profiles = fetch_profiles_from_DB()
    for profile in profiles:
        profiles = fetch_profiles_from_DB()
        name = profiles[profile]["Name"]
        profileSelection_dropdown.options.append(dropdown.Option(name))


def fetch_profiles_from_DB():
    return parse_profiles(read_profiles_from_DB())


def fetch_default_profile_from_DB():
    return parse_default_profile(read_default_profile_from_DB())


def read_profiles_from_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    profiles = cur.execute("SELECT * FROM profiles")
    p = profiles.fetchall()
    con.close()
    return p


def read_default_profile_from_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    profiles = cur.execute("SELECT * FROM defaultprofile")
    p = profiles.fetchone()
    print(p)
    con.close()
    return p


def parse_profiles(profiles):
    profileDict = {}
    for profile in profiles:
        profile_ID = profile[0]
        profile_Name = profile[1]
        profile_Mode = profile[2]
        profile_Speed = profile[3]
        profile_Laps = profile[4]
        profileDict[profile_ID] = {
            "Name": profile_Name,
            "Mode": profile_Mode,
            "Speed": profile_Speed,
            "Laps": profile_Laps
        }
    return profileDict


def parse_default_profile(profile):
    defaultProfile = {}
    profile_Mode = profile[1]
    profile_Speed = profile[2]
    profile_Laps = profile[3]
    defaultProfile = {
        "Mode": profile_Mode,
        "Speed": profile_Speed,
        "Laps": profile_Laps
    }
    return defaultProfile


def write_profile_to_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    name = profileNameInput.value
    mode = mode_dropdown.value
    speed = speed_dropdown.value
    laps = laps_dropdown.value
    data = [name, mode, speed, laps]
    cur.execute(
        """INSERT into profiles(name,mode,speed,laps)
             VALUES (?,?,?,?)""", data
    )
    con.commit()
    con.close()
    clear_profile_values()


def remove_profile_from_DB(profileIndex):
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    profile = cur.execute("SELECT * FROM profiles WHERE profile_id = ?""", (profileIndex,))
    profile = profile.fetchall()
    profileName = profile[0][1]
    schedules = fetch_schedules_from_DB()
    for schedule in schedules:
        cleaningProfile = schedules[schedule]["Profile"]
        if cleaningProfile == profileName:
            remove_profile_from_schedule(schedule)
    cur.execute("DELETE FROM profiles WHERE profile_id = ?", (profileIndex,))
    con.commit()
    con.close()


def write_updated_profile_to_DB(profileIndex):
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    index = profileIndex
    name = profileNameInput.value
    mode = mode_dropdown.value
    speed = speed_dropdown.value
    laps = laps_dropdown.value
    data = [name, mode, speed, laps, index]
    cur.execute(
        """UPDATE profiles
        SET name = ?, mode = ?,speed = ?,laps = ?
        WHERE profile_id = ?;""", data
    )
    con.commit()
    con.close()
    clear_profile_values()


def write_updated_default_profile_to_DB():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    mode = mode_dropdown.value
    speed = speed_dropdown.value
    laps = laps_dropdown.value
    data = [mode, speed, laps]
    cur.execute(
        """UPDATE defaultprofile
        SET mode = ?,speed = ?,laps = ?;""", data
    )
    con.commit()
    con.close()
    clear_profile_values()
