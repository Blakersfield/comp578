import pymongo
from dotenv import dotenv_values 


config = dotenv_values()


async def get_server_info():
   conn_str = config["RUS_DB_URL"]
   return conn_str

async def getMongo():
   conn_str  = await get_server_info()
   myclient = pymongo.MongoClient(conn_str);
   comp578 = myclient["comp578"]
   twitter_data = comp578["Tweets"]
   return twitter_data 

# async def insertTweet(mongoDB, data):
#       mongoDB.insert_one(tweet)

   

async def getAuthorIDs():
   mongoDB = await getMongo()
   docs = mongoDB.find({
   }, {"_id": 0, "author_id": 1})
   return docs







