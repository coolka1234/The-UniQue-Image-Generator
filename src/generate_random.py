import requests
import json
from dotenv import load_dotenv
import os

raw_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers", #ints
    "params": {
        "apiKey": os.getenv('RANDOM_API_KEY'),
        "n": 6, # number of random integers
        "min": 1, # minimum value
        "max": 6, # maximum value
        "replacement": True # allow duplicates
    },
    'id':1
}

headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}
data=json.dumps(raw_data)

response = requests.post(
    url='https://api.random.org/json-rpc/2/invoke',
    data=data,
    headers=headers
    )

print(response.text)