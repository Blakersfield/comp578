from datetime import datetime

def get_time_from_tweet(tweet_id):
    # tweet_id = 1497831781046784007
    tweet_id = int(tweet_id)
    shifted = tweet_id >> 22
    timestamp = shifted + 1288834975657 
    time_created = datetime.fromtimestamp(timestamp/1000)
    return time_created.isoformat()