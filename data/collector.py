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
config = dotenv_values()
import sys
import datetime
sys.path.append(config['DB_PATH'])
from mongo_factory import getMongo, getAuthorIDs, get_tweet_ids
from find_date import get_time_from_tweet
from tweet_puller import file_collector 
import time


def auth():
    return config["BEARER_TOKEN"]

def create_headers(bearer_token):
    return {"Authorization" : "Bearer {}".format(bearer_token), "User-Agent" : "v2RecentSearchPython"}

def create_url(ids):
    
    tweet_fields = "tweet.fields=public_metrics,author_id"
    url = "https://api.twitter.com/2/tweets?ids={}&{}".format(ids, tweet_fields)

    return url


def connect_to_endpoint(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()

def chunk(lst, n):
    ''' 
    partition evenly sized n-sized chunks
    '''
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



async def main():
    mongoDB = await getMongo()
    ids = file_collector()
    bearer_token = auth()
    headers = create_headers(bearer_token=bearer_token)
    chunked_ids = chunk(ids, 100)

    count = 1
    start = time.time()
    for id_partition in chunked_ids:
        ids_stringified = ','.join(id_partition)
        url = create_url(ids_stringified)
        print(f'\n\n\n\n\nREQUEST #{count} MADE\n\n\n\n')
        time.sleep(1)
        json_response = connect_to_endpoint(url, headers)
        if json_response.get('data') is not None:
            data = json_response['data']
            for datum in data:
                tweet_id = datum['id']
                created_at = get_time_from_tweet(tweet_id)
                datum['created_at'] = created_at
                if not datum['text'].startswith('RT'):
                    print(f'UPSERTING TWEET WITH ID {tweet_id}')
                    mongoDB.update_one({'id' : tweet_id},{'$set' : datum}, upsert=True)
                else:
                    print(f'DID NOT UPSERT TWEET WITH ID {tweet_id}')
        count += 1
    
    end = time.time()
    print(f'total time elapsed: {str(end - start)}')


                    
async def refactor(): 
    await get_tweet_ids()

asyncio.run(main())

