import pymongo
from dotenv import dotenv_values
from pandas import json_normalize
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd


AGGREGATE_OFFSET = '1D'

def retrieve_data(db = 'comp578',coll="Tweets"):
    """Retrieve data from the db
        db:     name of target database\
        coll:   name of target collection"""
    client = pymongo.MongoClient(dotenv_values()["RUS_DB_URL"])
    db = client[db]
    twitter_data = db[coll]
    return twitter_data.find().limit(10)

sia = SentimentIntensityAnalyzer()

data_flat = json_normalize(retrieve_data())

def analyze(text):
    scores = sia.polarity_scores(text)
    return scores['compound']

#clean up the data
data_flat['text']= data_flat['text'].apply(analyze)
data_flat.drop(labels=['_id','author_id'],axis=1,inplace=True)

col_dict = {
    'id' : 'id',
    'text' : 'text',
    'created_at' : 'created_at',
    'public_metrics.retweet_count' : 'retweet_count',
    'public_metrics.reply_count' : 'reply_count',
    'public_metrics.like_count' : 'like_count',
    'public_metrics.quote_count' : 'quote_count'
}

data_flat.columns=[col_dict[x] for x in data_flat.columns]

print(data_flat)

#set datetime index
date_time = pd.to_datetime(data_flat['created_at']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
datetime_index = pd.DatetimeIndex(date_time)
data_flat.set_index(keys=datetime_index,drop=True,inplace=True)

print(data_flat)

#aggregate based on day
text_sent = data_flat['text'].resample(AGGREGATE_OFFSET).mean()
text_sent.name = 'sentiment'
reply_count = data_flat['reply_count'].resample(AGGREGATE_OFFSET).sum()
retweet_count = data_flat['retweet_count'].resample(AGGREGATE_OFFSET).sum()
like_count = data_flat['like_count'].resample(AGGREGATE_OFFSET).sum()
quote_count = data_flat['quote_count'].resample(AGGREGATE_OFFSET).sum()
tweet_count = data_flat['text'].resample(AGGREGATE_OFFSET).count()
tweet_count.name='tweet_count'

#merge columns
data_agg = pd.merge(text_sent,reply_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,retweet_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,like_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,quote_count, right_index=True,left_index=True)
data_agg = pd.merge(data_agg,tweet_count, right_index=True,left_index=True)
#print(data_agg)

#write to file
data_agg.to_csv(path_or_buf='data.csv', sep=',', index=True)
