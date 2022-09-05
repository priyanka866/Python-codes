# -*- coding: utf-8 -*-
#Status code information-
# https://www.webfx.com/web-development/glossary/http-status-codes/

#basic request 

import requests

url = 'http://api.open-notify.org/iss-now.json'

resp = requests.get(url=url)
#print(resp)
if resp.status_code == 200:
    print("Status code is",resp.status_code)
else:
    print("Status code is",resp.status_code) 
    
resp.raise_for_status()    
    
data = resp.json() 
print(data['timestamp'])