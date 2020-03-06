
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import time
import threading

key = input(str("Password to START?"))


if key == 'g':
    def stock():
        
        threading.Timer(4.7, stock).start()
        
        vxx = yf.Ticker("VXX")
        
        print('Latest Bid:', vxx.info['bid'])
        print('Size:', vxx.info['bidSize'])
        
        print('Latest Ask:', vxx.info['ask'])
        print('Size:', vxx.info['askSize'])
        
        price = (float(vxx.info['bid']) + float(vxx.info['ask']))/2
        
        print('Current Price:', (round(price,2)))
        
        
    stock()
    
    key_2 = input(str("Enter 's' to STOP"))
                
    if key_2 == 's':
        threading.Timer(4.7, stock).cancel()
            
    
        
    
else:
    (print('WRONG PASSWORD'))


    
