import tweepy
import configparser
import pandas as pd


#read config

config=configparser.ConfigParser()
config.read('brawlconfig.ini')

api_key= config['twitter']['api_key']
api_key_secret=config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

bearer_key='AAAAAAAAAAAAAAAAAAAAAHqPfwEAAAAAkA9rZxkhyE%2FMPu5u5rjT5eUOUs8%3DvW9WBj1sSxICVHvPoECtRwWnwGAbkK5C5yqYTntmz9rks7hzgR'
client = tweepy.Client(bearer_key,api_key,api_key_secret,access_token,access_token_secret)

auth =tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)


def createApi():
    api = tweepy.API(auth)
    return api;

def createClient():
    return client;



# public_tweets =api.home_timeline()

# #public_tweets[0].user.screen_name    -------->author

# print(public_tweets[0].text) #----------->tweet

# mentions = api.mentions_timeline()

# for people in mentions:
#     mentionData.append([people.text])


# #saving in cvs file

# columns = ['Time','User','Tweet'] #----------> columns for cvs
# data=[] #------> empty list to append data

# #-------------------scrapping the data from json------------
# for tweet in public_tweets:
#     data.append([tweet.created_at,tweet.user.screen_name,tweet.text])

# df =pd.DataFrame(data,columns=columns)  #formatting it in rows and columns

# df.to_csv('tweets.csv', mode='a', index=False, header=False)  #--------->put in csv file
