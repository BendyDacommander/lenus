import colorama
from colorama import Fore, Style
import requests
import time
import random
import string
import os

Color_1 = Fore.RED
Color_3 = Fore.YELLOW

NitroGenLogo = f"""
{Color_1}                       ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
{Color_1}                       ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
{Color_1}                       ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
{Color_1}                       ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
{Color_1}                       ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
{Color_1}                       ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                        Please note that this is luck based
                                      and may not generate a valid nitro link
                                    if you get lucky you will find the valid links
                                                   in Nitro.txt
"""

def nitrogen():
    os.system('cls')
    print(NitroGenLogo)
    time.sleep(2)

def generate_nitro_codes(num):
    with open("Nitro.txt", "w", encoding='utf-8') as file:
        input(f'{Fore.YELLOW}[!] {Fore.WHITE}Press enter to continue... ')
        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k=16
            ))

            file.write(f"https://discord.gift/{code}\n")

def check_nitro_codes():
    with open("Nitro.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(f"{Fore.GREEN}[!] {Fore.WHITE}Valid | {nitro} ")
                break
            else:
                print(f"{Color_3}[!] {Fore.WHITE}Invalid  {nitro} ")


def main():
    nitrogen()
    generate_nitro_codes(1000)
    check_nitro_codes()

if __name__ == "__main__":
    main()
