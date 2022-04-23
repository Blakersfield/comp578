import asyncio
from sqlite3 import connect
import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import time
from dotenv import dotenv_values 
import sys
import datetime
sys.path.append('/Users/giovanniflores/Development/comp578/db')
from mongo_factory import getMongo, getAuthorIDs, insertTweets

config = dotenv_values()

def auth():
    return config["BEARER_TOKEN"]

def create_headers(bearer_token):
    return {"Authorization" : "Bearer {}".format(bearer_token), "User-Agent" : "v2RecentSearchPython"}

def create_url(keyword, start_date, end_date, max_results=10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all"

    query_params = {
        'query' : keyword,
        'start_time' : start_date, 
        'end_time' : end_date,
        'max_results' : max_results,
        'expansions' : 'author_id,geo.place_id',
        'tweet.fields' : 'public_metrics',
    }


    return (search_url, query_params);


def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token'] = next_token
    response = requests.get(url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()



bearer_token = auth()
headers = create_headers(bearer_token=bearer_token)
keyword = "#elon lang:en"
# start_time = "2021-03-01T00:00:00:00.000Z"
start_time = datetime.datetime(2022, 3, 1).astimezone().isoformat()
end_time = datetime.datetime(2022, 3, 31).astimezone().isoformat()
# end_time = "2021-03-31T00:00:00.000Z"
max_results = 10 
url = create_url(keyword, start_time, end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])
data = json_response['data']
print(data)




# async def main():
#     await insertTweets(data)
    # docs = await getAuthorIDs()
    # for doc in docs:
    #     author_id = doc['author_id']
    #     print(author_id)

    
# asyncio.run(main())

