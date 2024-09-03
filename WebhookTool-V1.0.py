import requests 
import os
import time
from urllib.parse import urlparse

def main():
    os.system("cls")
    print("""\

  __  __       _     ______
 |  \/  |     | |   |___  /
 | \  / | __ _| |__    / / 
 | |\/| |/ _` | '_ \  / /  
 | |  | | (_| | | | |/ /__ 
 |_|  |_|\__,_|_| |_/_____|
                           
   Discord webhook sender V 1.0                        

                    """)
    url = input("Enter Webhook:" + " ")
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    if is_valid_url(url) == False:
        print("Invalid URL")
        time.sleep(2)
        main()
    else:
        
        msg = input("Enter Message:" + " ")
        data = {
        "avatar_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.explicit.bing.net%2Fth%3Fid%3DOIP.cCK2NXaqBP581P1hs_SbQQHaHa%26pid%3DApi&f=1&ipt=7c19a914f10db0eaca8828cc926d729c3ff2a4c1a18bf29d8cebc40f0d0cd6c5&ipo=images",
        "username": "sans",
        "content": msg,
        }
        r = requests.post(url , json=data)
        print(r)
        time.sleep(1)
        main()
main()