import pymongo
from dotenv import dotenv_values
from pandas import json_normalize
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

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
data_flat.drop(labels=['_id','author_id'],axis=1,inplace=True)
data_flat.columns=[
'id',
'text',
'created_at',
'retweet_count',
'reply_count',
'like_count',
'quote_count']
date_time = pd.to_datetime(data_flat['created_at']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
#print(date_time)
datetime_index = pd.DatetimeIndex(date_time)
#print(datetime_index)
data_flat.set_index(keys=datetime_index,drop=True,inplace=True)


#print(type(data_flat['created_at'][1]))
#print(data_flat)
reply_count = data_flat['reply_count'].resample('1D').sum()
retweet_count = data_flat['retweet_count'].resample('1D').sum()
like_count = data_flat['like_count'].resample('1D').sum()
quote_count = data_flat['quote_count'].resample('1D').sum()
tweet_count = data_flat['text'].resample('1D').count()
tweet_count.name='tweet_count'
print(tweet_count)
#neu_count = data_flat['text'].resample('1D').count('neu')
data_agg = pd.merge(reply_count,retweet_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,like_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,quote_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,tweet_count, right_index=True,left_index=True)
#print(data_agg)

data_agg.to_csv(path_or_buf='data.csv', sep=',', index=False)
