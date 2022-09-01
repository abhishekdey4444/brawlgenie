#player tag ---------->show stats
#player tag----------->rankings
#club tag------------>show stats
#club tag----------->rankings


#--------------libraries------------------
from twitter_api import createApi
import pandas as pd


#--------------api object-----------------
api = createApi();
followers_list=api.get_followers()
#-------------constants---------------------
bot_id="brawlgenie"


#--------------functions----------------------
for i in range(len(followers_list)):
    followers_userid=followers_list[i].screen_name

#-------------use function------------------
def following_check(user):
    if user in followers_userid:
        return True
    else:
        return False

#------------------main function---------------

print(following_check("kraken_head"))
    
