import json
import time
import os

from util.filesystem import FileSystemAccess

 
 
def save_cookies(cookies):
     with FileSystemAccess('identity').open('cookies.json', 'w') as f:
        json.dump(cookies, f)
        f.flush()
        os.fsync(f.fileno())

def load_cookies() -> dict:
     cookies=dict()
     with FileSystemAccess('identity').open('cookies.json', 'r') as f:
        cookies=json.load(f)  
     return cookies  

#def main(): 
    #cookies=dict(
      #seleneAccess='accesstoken111',
      #seleneRefresh='refreshtoken222'
    #)
    #save_cookies(cookies)
    #test=load_cookies()
    #print(test.items())

#if __name__ == "__main__":
    #main()



