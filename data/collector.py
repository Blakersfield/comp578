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
sys.path.append('/Users/giovanniflores/Development/comp578/db')
from mongo_factory import getMongo

config = dotenv_values()

def auth():
    return config["BEARER_TOKEN"]

def create_headers(bearer_token):
    return {"Authorization" : "Bearer {}".format(bearer_token), "User-Agent" : "v2RecentSearchPython"}

def create_url(keyword, start_date, end_date, max_results=10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent"

    # query_params = {
    #     'query' : keyword,
    #     'start_time' : start_date,
    #     'end_time' : end_date,
    #     'max_results' : max_results,
    #     'expansions' : 'author_id, in_reply_to_user_id, geo.place_id',
    #     'tweet.fields' : 'id, text, author_id, in_replly_to_user_id, geo, conversation_id, created_at, lang, public_metrics, referenced_tweets, reply_settings, source',
    #     'user.fields' : 'id, name, username, created_at, description, public_metrics, verified',
    #     'place.fields' : 'full_name, id, country, country_code, geo, name, place_type',
    #     'next_token' : {}}

    query_params = {'query' : '(from:faggot -is:retweet) OR #russiantank', 'tweet.fields': 'author_id'}

    return (search_url, query_params);


def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token'] = next_token
    # response = requests.request('GET', url, headers=headers, params=params)
    response = requests.get(url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()



bearer_token = auth()
headers = create_headers(bearer_token=bearer_token)
keyword = "gay lang:en"
start_time = "2021-03-01T00:00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 10


url = create_url(keyword, start_time, end_time, max_results)
print(str(url[0]))

print(headers)

print(str(url[1]))


json_response = connect_to_endpoint(url[0], headers, url[1])
data = json_response['data']

async def main():
    mongoDB = await getMongo()
    for tweet in data:
        mongoDB.insert_one(tweet)

asyncio.run(main())#     # sotre



# mybigload = json.loads(json_response);
# print(json.dumps(mybigload, indent=4, sort_key=True))