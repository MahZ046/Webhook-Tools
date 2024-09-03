import requests
import os
import time
from urllib.parse import urlparse

def logo():
    print("""
  __  __       _     ______
 |  \/  |     | |   |___  /
 | \  / | __ _| |__    / / 
 | |\/| |/ _` | '_ \  / /  
 | |  | | (_| | | | |/ /__ 
 |_|  |_|\__,_|_| |_/_____|
                           
   Discord webhook sender V 1.0                        

                    """)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def sender():
    os.system("clear")
    logo()
    url = input("Enter Webhook: ").strip()
    
    if not is_valid_url(url):
        print("Invalid URL")
        time.sleep(2)
        menu()
        return

    msg = input("Enter Message: ").strip()
    data = {
        "avatar_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.explicit.bing.net%2Fth%3Fid%3DOIP.cCK2NXaqBP581P1hs_SbQQHaHa%26pid%3DApi&f=1&ipt=7c19a914f10db0eaca8828cc926d729c3ff2a4c1a18bf29d8cebc40f0d0cd6c5&ipo=images",
        "username": "sans",
        "content": msg,
    }
    r = requests.post(url, json=data)
    print(f"Status Code: {r.status_code}")
    time.sleep(1)
    menu()

def spammer():
    print("Webhook Spammer function not implemented yet.")
    time.sleep(1)
    menu()

def Info():
    print("Webhook Info function not implemented yet.")
    time.sleep(1)
    menu()

def menu():
    os.system("clear")
    logo()
    while True:
        print("[1] Webhook Sender")
        print("[2] Webhook Spammer")
        print("[3] Webhook Info")
        print("[4] Exit")
        
        choice = input("Choice: ").strip()
        
        if choice == '1':
            sender()
        elif choice == '2':
            spammer()
        elif choice == '3':
            Info()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please select a valid option.")

def main():
    os.system("clear")
    logo()
    menu()

if __name__ == "__main__":
    main()
