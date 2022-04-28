import pymongo
from dotenv import dotenv_values
from find_date import get_time_from_tweet

config = dotenv_values()


async def get_server_info():
    conn_str = config["RUS_DB_URL"]
    return conn_str


async def getMongo():
    conn_str = await get_server_info()
    myclient = pymongo.MongoClient(conn_str)
    comp578 = myclient["comp578"]
    twitter_data = comp578["Tweets"]
    return twitter_data


async def getAuthorIDs():
    mongoDB = await getMongo()
    docs = mongoDB.find({
    }, {"_id": 0, "author_id": 1})
    return docs


async def get_tweet_ids():
    mongoDB = await getMongo()
    tweet_docs = mongoDB.find(
        {},
        {"_id" : 0, "id":  1},
    ).sort("id" , pymongo.ASCENDING)
    for tweet_doc in tweet_docs:
       tweet_id = tweet_doc['id']
       created_at = get_time_from_tweet(tweet_id)
       print(f'UPSERTING TWEET WITH ID: {tweet_id}, CREATED AT: {created_at}')
       mongoDB.update_one({"id" : tweet_id}, {'$set' : {'created_at' : created_at}})



