import requests 
#import os
from datetime import datetime
import json
from util.auth_cookies import load_cookies
 


def add_device():
    cookies = load_cookies()
    print('Loaded cookies info is:')
    print(json.dumps(cookies))
    device = dict(
        city="Singapore",
        country="Singapore",
        name="Selene Test Device 2",
        pairingCode="AL3EKL",
        placement="YY House",
        region="Singapore",
        timezone="Asia/Singapore",
        wakeWord="hey mycroft",
        voice="American Male"
        )
        
    response = requests.post("http://42.60.37.128:5001/api/devices", data=json.dumps(device),cookies=cookies, headers = {'Content-Type':'application/json'}) 
    print('status code for calling API is: {0}'.format(response.status_code))
    
4

    
def main():
    add_device()
  
 

if __name__ == "__main__":
    main()



  
