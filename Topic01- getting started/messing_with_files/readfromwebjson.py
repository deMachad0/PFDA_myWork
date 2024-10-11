# reading from web url
# Author: Andre 

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)

print(data['bpi']['EUR']['rate_float'])

price_euro = data['bpi']['EUR']['rate_float']

formatted_price = f"{price_euro:,.4f}" # formatting price to euros

print ("Bitcoin price in Euros: ", formatted_price)