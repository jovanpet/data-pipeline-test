import tweepy
import pandas as pd

import tweepy

ACCESS_TOKEN=""
ACCESS_SECRET=""
API_KEY=""
API_SECRET=""

def run_etl():
    api=tweepy.Client(None, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    user = api.get_me()
    users={
        "ID":user.data["id"],
        "Name": user.data["name"],
        "Username": user.data["username"]
    }
    print(users)

    df=pd.Series(list(user.items()))
    
    df.to_csv('refined_tweets.csv')
    
run_etl()
