import pymongo
from dotenv import dotenv_values
from pandas import json_normalize
from nltk.sentiment import SentimentIntensityAnalyzer

def retrieve_data(db = 'comp578',coll="Tweets"):
    """Retrieve data from the db
        db:     name of target database\
        coll:   name of target collection"""
    client = pymongo.MongoClient(dotenv_values()["RUS_DB_URL"])
    db = client[db]
    twitter_data = db[coll]
    return twitter_data.find()

sia = SentimentIntensityAnalyzer()

data_flat = json_normalize(retrieve_data())

def analyze(text):
    scores = sia.polarity_scores(text)
    return max(scores,key=scores.get)

data_flat['text']= data_flat['text'].apply(analyze)
print(data_flat['text'])

data_flat.to_csv(path_or_buf='data.csv', sep='|', index=False)
