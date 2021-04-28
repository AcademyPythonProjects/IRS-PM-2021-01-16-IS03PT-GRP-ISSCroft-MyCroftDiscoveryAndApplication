import requests 
from datetime import datetime

from binascii import b2a_base64
import json


new_account_request= dict(
        termsOfUse=True,
        privacyPolicy=True,
        
        login=dict(
            federatedPlatform=None,
            federatedToken=None,
            email=b2a_base64(b"test@outlook.com").decode(),
            password=b2a_base64(b"nustest").decode(),
        ),
    )

data=json.dumps(new_account_request)
print(data)
response = requests.post('http://42.60.37.128:5002/api/account',data=json.dumps(new_account_request),headers = {'Content-Type':'application/json'})

print(response.content)

  
