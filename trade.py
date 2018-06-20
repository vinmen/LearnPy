from ib_insync import *
import logging
import time
import keyboard

ib = IB()
#ib.connect('127.0.0.1', 4002, clientId=10)
util.logToConsole(logging.INFO)
i = 0
clientID = 205
last_price = 0.0
previous_price = 0.0
up_vote = 0
down_vote = 0

while(True or i < 4000):
    try:
        if not ib.isConnected():
            ib.connect('127.0.0.1', 7496, clientId=11, timeout=10) 
            time.sleep(1) 
        else:
            contract = Future('ES', '20180921', 'GLOBEX')  
            #contract = Future('NIFTY50', '20180628', 'NSE', )               
            ib.reqMktData(contract, '', False, False)
            ticker = ib.ticker(contract)
            ib.sleep(1)

            last_price = ticker.dict().get('last')               

            if previous_price > last_price:                
                print(str(last_price) + " down") 
            elif previous_price < last_price:                
                print(str(last_price) + " up")  

            previous_price = last_price            
            i = i + 1  
            ib.sleep(1)                      
    except:
        ib.disconnect()   
        break     
    #if keyboard.is_pressed('q'):
        #break
        
ib.disconnect()