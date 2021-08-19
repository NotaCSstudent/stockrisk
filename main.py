from datetime import time
import dotenv as env
from dotenv import load_dotenv
import os
import matplotlib
import matplotlib.pyplot as plt



load_dotenv(dotenv_path='./stuff.env')




import requests
import pandas as pd
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
import numpy as np

token = os.getenv('TOKEN');
class Ticker:
    def __init__(self,ticker:str):
        
        self.ticker = ticker;
        self.daily = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ self.ticker + '&apikey={token}').json();
        self.intraday = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ self.ticker +'&interval=5min&apikey={token}').json();
        self.monthly = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+ self.ticker +'&apikey={token}').json();
        self.daily_data = {'date' : [],'open' : [], 'close' : [],'high' : [], 'low' : [] , 'volume' : []}
    def dailydata(self):
        daydata  = self.daily['Time Series (Daily)']
        for keys in daydata:
            self.daily_data['date'].append(keys);
            self.daily_data['open'].append(float(daydata[keys]['1. open']))
            self.daily_data['high'].append(float(daydata[keys]['2. high']))
            self.daily_data['low'].append(float(daydata[keys]['3. low']))
            self.daily_data['close'].append(float(daydata[keys]['4. close']))
            self.daily_data['volume'].append(int(daydata[keys]['5. volume']))
        
        return self.daily_data


        
        


        
        

apple = Ticker('AAPL')
tesla = Ticker('TSLA')
microsoft = Ticker('MSFT')
nvdia = Ticker('NVDA')
ford = Ticker('F')

tickers = [apple,tesla,microsoft,nvdia,ford]





