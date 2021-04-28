import requests 

from datetime import datetime

import json
from util.auth_cookies import load_cookies

 #Step1 go to mycroft database to run the following two delete scripts
 #delete from device.geography where account_id='d214b11c-cf7a-4c5f-8b53-f8cc3b4e31fb'
 #delete from device.device where account_id='d214b11c-cf7a-4c5f-8b53-f8cc3b4e31fb' 


def remove_device():
    cookies = load_cookies()
    print('Loaded cookies info is:')
    print(json.dumps(cookies))
    
    response = requests.delete("http://42.60.37.128:5001/api/devices/07f33943-8dd3-47df-8ab5-8cd6a6de613d",cookies=cookies,headers = {'Content-Type':'application/json'}) 
    
    print('status code for calling API is: {0}'.format(response.status_code))
    


    
def main():
    remove_device()
  
 

if __name__ == "__main__":
    main()



  
