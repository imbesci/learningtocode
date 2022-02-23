
!pip3 install pandas==1.1.5 numpy==1.19.4 scipy==1.5.4
!pip3 install alpaca-trade-api
!pip3 install pymongo
!pip3 install dnspython

coin = "ETH"


import sys
import dns

####################TWEETS######################
import tweepy
import os
import pandas as pd
import time

#Authenticate Twitter API
consumer_key = "zfSUJduOLq0MOX0xtFMUyTott"
consumer_secret = "M2oiB5bNekdUYDnDOQcIQ5Jz2VRiSjZxTEW55h376cMfbA3fjo"
access_token = "881877178572566528-7NPh026TleuetNPnAyf0Na9yduxfdQX"
access_token_secret = "FbpTXnD89Y9oBSKHSWnr6HAzgdmaHIQn22CfA2NugHd1M"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Get tweets
username = 'WhaleTrades'
count = 500
try:     
  # Creation of query method using parameters
  tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
  
  # Pulling information from tweets iterable object
  tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
  
  # Creation of dataframe from tweets list
  # Add or remove columns as you remove tweet information
  tweets_df = pd.DataFrame(tweets_list)

except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)

prints = []
for i in tweets_list:
  if f"${coin}" in i[2]:
    value = int(i[2].splitlines()[0].split()[0][3:].replace(',',''))
    side = i[2].splitlines()[0].split()[2]
    price = float(i[2].splitlines()[0].split()[3].replace('@','').replace('$',''))
    when = i[0]
    prints.append((when,value,side,price))
longs = []
shorts = []
for x in prints:
  if x[2] == 'LONGED':
    longs.append(x)
  else:
    shorts.append(x)

ldf = pd.DataFrame(longs, columns=['Date','Size','Side','Price'])
sdf = pd.DataFrame(shorts, columns=['Date','Size','Side','Price'])

import hmac
import requests
from requests import Request
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

ts = int(time.time() * 1000)
request = Request('GET', 'https://ftx.com/api/markets')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('uF0WFrnYCD7QSdBfbcOzFkPZioLCvi9qDAIFrLmR'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = 'g1b4Eo1hhJmzWV9xMBCz4fUmPpCcDv5FiNXBt3rR'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)
#Authentication end

#Request
historical = requests.get(f'https://ftx.com/api/markets/{coin}/USD/candles?resolution=60').json()
historical = pd.DataFrame(historical['result'])
historical.drop(['startTime'], axis = 1, inplace=True)
historical.head()
historical['time'] = pd.to_datetime(historical['time'], unit='ms')
historical.set_index('time', inplace=True)

from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.update_layout(xaxis2= {'anchor': 'y', 'overlaying': 'x', 'side': 'top'},
                  yaxis_domain=[0, 1]);

# Add traces
fig.add_trace(
    go.Candlestick(x=historical.index, open = historical.open, high= historical.high, low = historical.low, close=historical.close, name="yaxis data"),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(mode='markers', x=ldf.Date, y=ldf.Price, marker = dict(size=ldf.Size/100000, color = 'Green'))
)
fig.add_trace(
    go.Scatter(mode='markers', x=sdf.Date, y=sdf.Price, marker = dict(size=sdf.Size/100000, color = 'Red'))
)
# Add figure title
fig.update_layout(
    title_text="Whale Trades"
)

# Set x-axis title
fig.update_xaxes(title_text="Price")

# Set y-axes titles
fig.update_yaxes(title_text="Price", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)


fig.update_layout(width=1700, height=900)

fig.show()