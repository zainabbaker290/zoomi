import sqlite3
from profileWidgets import *
def fetch_profiles_from_DB():
        return parse_profiles(read_profiles_from_DB())

def fetch_default_profile_from_DB():
        return parse_default_profile(read_default_profile_from_DB())

def read_profiles_from_DB():
        con = sqlite3.connect("app.db")
        cur =con.cursor()
        profiles = cur.execute("SELECT * FROM profiles")
        p = profiles.fetchall()
        con.close()
        return p

def read_default_profile_from_DB():
        con = sqlite3.connect("app.db")
        cur =con.cursor()
        profiles = cur.execute("SELECT * FROM defaultprofile")
        p = profiles.fetchone()
        print(p)
        con.close()
        return p

def parse_profiles(profiles):
        profileDict= {}
        for profile in profiles:
            profile_ID = profile[0]
            profile_Name = profile[1]
            profile_Mode= profile[2]
            profile_Speed = profile[3]
            profile_Laps = profile[4]
            profileDict[profile_ID] = {
            "Name": profile_Name, 
            "Mode":profile_Mode, 
            "Speed":profile_Speed,
            "Laps":profile_Laps
            }
        return profileDict

def parse_default_profile(profile):
        defaultProfile={}
        profile_Mode= profile[1]
        profile_Speed = profile[2]
        profile_Laps = profile[3]
        defaultProfile = {
        "Mode":profile_Mode, 
        "Speed":profile_Speed,
        "Laps":profile_Laps
        }
        return defaultProfile

def write_profile_to_DB():
        con = sqlite3.connect("app.db")
        cur = con.cursor()
        name = profileNameInput.value
        mode = mode_dropdown.value
        speed = speed_dropdown.value
        laps = laps_dropdown.value
        data = [name,mode,speed,laps]
        cur.execute(
            """INSERT into profiles(name,mode,speed,laps)
             VALUES (?,?,?,?)"""
            ,data
            )
        con.commit()
        con.close()
        clear_profile_values()

def remove_profile_from_DB(profileIndex):
            con = sqlite3.connect("app.db")
            cur =con.cursor()
            cur.execute("DELETE FROM profiles WHERE profile_id = ?",(profileIndex,))
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
    data = [name,mode,speed,laps,index]
    cur.execute(
        """UPDATE profiles
        SET name = ?, mode = ?,speed = ?,laps = ?
        WHERE profile_id = ?;"""
        ,data
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
    data = [mode,speed,laps]
    cur.execute(
        """UPDATE defaultprofile
        SET mode = ?,speed = ?,laps = ?;"""
        ,data
        )
    con.commit()
    con.close()
    clear_profile_values()

def clear_profile_values():
        profileNameInput.value = None
        mode_dropdown.value = None
        speed_dropdown.value = None
        laps_dropdown.value = None