from twitter_api import createApi,createClient
import pandas as pd
import logger
import tweepy
import time
from brawl_info import commands
from brawlgenie import following_check

api=createApi()
client=createClient()

player_tag=""
message=""

tweet_ids=[]
client_id=client.get_me().data.id

followers=client.get_users_followers(client_id)
#print(followers)

start_id=1564841906672369664

while True:
    response = client.get_users_mentions(client_id,since_id=start_id)
    #print(response)
    if response.data !=None:
        for tweet in response.data:
            try:
                text_split=tweet.text.split(" ")
                if "!stats" ==text_split[1]:
                    message=commands("!stats",text_split[2])
                elif "!help"==text_split[1]:
                    message=commands("!help",0)
                elif "!clubstats"==text_split[1]:
                    message=commands("!clubstats",text_split[2])
                else:
                    message="Invalid Command"
                client.create_tweet(in_reply_to_tweet_id=tweet.id,text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)
    time.sleep(3)

