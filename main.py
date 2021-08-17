import dotenv as env
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='./stuff.env')

token = os.getenv('TOKEN')


import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey={token}'
r = requests.get(url)
data = r.json()
print(type(data))
#print(data)