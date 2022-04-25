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
from mongo_factory import getMongo, getAuthorIDs 
from tweet_puller import pull_from_file 

config = dotenv_values()

def auth():
    return config["BEARER_TOKEN"]

def create_headers(bearer_token):
    return {"Authorization" : "Bearer {}".format(bearer_token), "User-Agent" : "v2RecentSearchPython"}

def create_url(id):
    
    tweet_fields = "tweet.fields=public_metrics,author_id"
    url = "https://api.twitter.com/2/tweets?ids={}&{}".format(id, tweet_fields)

    return url


def connect_to_endpoint(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()


async def main():
    mongoDB = await getMongo()
    ids = pull_from_file()
    bearer_token = auth()
    headers = create_headers(bearer_token=bearer_token)
    
    for id in ids:
        url = create_url(id)
        json_response = connect_to_endpoint(url, headers)
        if json_response.get('data') is not None:
            data = json_response['data']
            for datum in data:
                tweet_id = datum['id']
                if not datum['text'].startswith('RT'):
                    print(f'UPSERTING TWEET WITH ID {tweet_id}')
                    mongoDB.update_one({'id' : tweet_id},{'$set' : datum}, upsert=True)
                else:
                    print(f'DID NOT UPSERT TWEET WITH ID {tweet_id}')
                    
asyncio.run(main())

