import pymongo
from dotenv import dotenv_values
from pandas.io.json import json_normalize
#import pandas as pd

def retrieve_data(db = 'comp578',coll="Tweets"):
    """Retrieve data from the db
        db:     name of target database\
        coll:   name of target collection"""
    client = pymongo.MongoClient(dotenv_values()["RUS_DB_URL"])
    db = client[db]
    twitter_data = db[coll]
    return twitter_data.find()

data_flat = json_normalize(retrieve_data())
data_flat.to_csv(path_or_buf='data.csv', sep='|', index=False)
#print(data_flat.columns)


#print(x)
#for d in x:
#    print('\r\r')
#    for i in d:
#        print(i,d[i])
#        
#    print(d["id"])
#
#print(x[1])