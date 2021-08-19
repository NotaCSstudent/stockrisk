from datetime import time
import dotenv as env
from dotenv import load_dotenv
import os
import matplotlib
import matplotlib.pyplot as plt



load_dotenv(dotenv_path='./stuff.env')

token = os.getenv('TOKEN')


import requests
import pandas as pd
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey={token}'
r = requests.get(url)
data = r.json()

#print(data)
TSLA = pd.DataFrame(data)
#print(TSLA)

TSLAmin = data['Time Series (5min)']

more = pd.DataFrame(TSLAmin)
#print(more)

price = []
timeperiod = []
for keys in TSLAmin:
    price.append(TSLAmin[keys]['1. open'])
    timeperiod.append(keys)

#print(timeperiod)

import numpy as np


y = np.array(price)
x = timeperiod


plt.plot(x,y)


