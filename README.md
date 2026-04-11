### RPC Buster

```
            ,.  ,.           ______  ______ _______    ______                               
            ||  ||          (_____ \(_____ (_______)  (____  \              _               
           ,''--''.          _____) )_____) )          ____)  )_   _  ___ _| |_ _____  ____ 
          : (.)(.) :        |  __  /|  ____/ |        |  __  (| | | |/___|_   _) ___ |/ ___)
         ,'        `.       | |  \ \| |    | |_____   | |__)  ) |_| |___ | | |_| ____| |    
         :          :       |_|   |_|_|     \______)  |______/|____/(___/   \__)_____)_|    
         :          :       By Belly
         `._m____m_,' 
```

**Disclaimer** : This depos shows how this brute force method. It has been developed for educational purposes only. I am not responsible for what you do with.


### Installation
```
git clone https://github.com/tryagainbelly/rpcbuster
cd rpcbuster
pip install requests
```

RPC Buster is a tool for exploiting the ‘xmlrpc.php’ file using a brute-force attack.
This file is present on WordPress sites, but depending on the site's configuration, we may not necessarily have access to it.

### Fichier xmlrpc.php
This is an API used for remotely managing certain features, such as user management, creating posts, and so on. What makes this file vulnerable is the fact that it handles authentication.
Specifically, why is this of interest to an attacker? By default, on a WordPress site, the XML-RPC file is enabled and sends login credentials (username and password) in API requests without any protection.
So, every time a request is made for certain methods, the system verifies the username and password directly within the request. And very often, this endpoint has no rate limits or lockout mechanisms, unlike the standard WordPress login page, which allows an attacker to perform a brute-force attack.

Some interesting methods include, for example, ‘metaWeblog.getUsersBlogs’ and ‘wp.getUsersBlogs’

The advantage for an attacker is that they can brute-force this endpoint without giving it much thought, since plugins often focus on the login page ‘wp-login.php’.

### Methodology
1. Recon: You can check if the endpoint is available by going to https://test.com/xmlrpc.php and seeing if you receive the message “The XML-RPC server only accepts POST requests.” Alternatively, you can run vulnerability scans using various tools that can identify this endpoint.
2. Automation: You can now use RPC Buster to automate brute-force attacks.
The script automatically detects whether you are using a single value or a wordlist.
Example of a configuration using a wordlist:
```
{
    "url": "https://test.com/xmlrpc.php",
    "methodName":"metaWeblog.getUsersBlogs",
    "user":"toto",
    "password":"",
    "wordlist_password":"/wordlist/rockyou.txt"
}
```

3. Usage: Run ‘rpcbuster.py’. If successful, the valid credentials are saved to hit.txt

If an attacker manages to obtain valid credentials, they will have legitimate access to the site and will be able to distribute malware, spam, etc.

### License 

MIT (For authorized security research only)