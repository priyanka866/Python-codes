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

# #kanye quote app

from tkinter import *
import requests

def get_quote():
    url= 'https://api.kanye.rest'
    resp=requests.get(url)
    data = resp.json()
    return data['quote']
   
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="D:/Python-codes/kanye_api_rqst/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="D:/Python-codes/kanye_api_rqst/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()