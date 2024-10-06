import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


# json_response = response.json()
# python_response = json_response['result']['random']['data']
# print(python_response)

def generate_random(number_of_random_integers, minimum_value, maximum_value, duplicates_allowed):
    raw_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers", #ints
    "params": {
        "apiKey": os.getenv('RANDOM_API_KEY'),
        "n": number_of_random_integers, # number of random integers
        "min": minimum_value, # minimum value
        "max": maximum_value, # maximum value
        "replacement": duplicates_allowed # allow duplicates
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
    json_response = response.json()
    python_response = json_response['result']['random']['data']
    return python_response