

  
 #This example uses Python 2.7 and the python-request library.

from os import close
import  os
from requests import Request, Session
import json
import requests
import pprint
from tkinter import  Button, Label, Tk,PhotoImage
from PIL import Image
from dotenv import load_dotenv
import os
import sys

load_dotenv()

#enviroment variables
from requests.sessions import session
#Use an appy of coinmarketcap
url = os.getenv("url")
#price of btc fuction
def priceBTC(url):
    API_KEY=os.getenv("API_KEY") 
    parameters = {
    'slug':'bitcoin',
    'convert':'USD'
    }
    headers={
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':f'{API_KEY}'
    }
    session=Session()
    session.headers.update(headers)

    response=session.get(url,params=parameters)
    #pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    BTC_price=str(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    return BTC_price
#price of ethereum fuction
def priceETH(url):
    API_KEY=os.getenv("API_KEY") 
    parameters = {
    'slug':'ethereum',
    'convert':'USD'
    }
    headers={
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':f'{API_KEY}'
    }
    session=Session()
    session.headers.update(headers)

    response=session.get(url,params=parameters)
    #pprint.pprint(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
    ETH_price=str(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
    return ETH_price



def reset():
   os.execl(sys.executable, sys.executable, * sys.argv)
   
   
   
    
ETH_price=priceETH(url)
BTC_price=priceBTC(url)
    #root class
class main:

    root=Tk()
    root.iconbitmap('Cjdowner-Cryptocurrency-Flat-Bitcoin-BTC.ico')
    root.title("Lector de precio de crypto")
    root.geometry("500x700")
    root.resizable(0,0)
    

    root.configure(bg='white')
    imageneth = PhotoImage(file="giphy.gif")
    imagenbtc = PhotoImage(file="btc2.gif")


 
#ethereum price label

    precioeth=Label(root,text=f"El precio de ETH es " + "$" + ETH_price)
    precioeth.config(fg="black",bg="cyan",font=("Verdana",12))
    precioeth.pack()

    Label(root, image=imageneth, bd=1).pack(side="top")
#btc price label
    preciobtc=Label(root,text="El precio de BITCOIN BTC es "+ "$" + BTC_price )
    preciobtc.config(fg="black",bg="gold",font=("Verdana",12))
    preciobtc.pack()
    Label(root, image=imagenbtc, bd=1).pack(side="top")
#exit and reset buttons
    Button(text="EXIT",command=quit).pack()
    Button(text="RESET",command=reset).pack()



    root.mainloop()

w=main()
