import time
import configparser
from twitter_api import createApi
from brawl_api import createBrawlApi

#==================fatal===========================
client=createBrawlApi()
api=createApi()
message=""
#====================command functions=======================
def commands(com,player_id):
    if com=="!stats":
        return stats(player_id)    
    elif com=="!lastmatch":
        return lastMatch(player_id)
    elif com=="!clubstats":
        return clubStats(player_id)
    elif com=="!help":
        return com_help(player_id)



#=====================primary commands=========================
def stats(player_id):
    try:
        player=client.get_player(player_id)
        message=("👽Player Tag: {0}📛Player Name: {1}💪Club Name: {2}#️⃣Club Tag: {3}🏆Trophies: {4}🎖Highest Trophies: {5}🎌3 vs 3 Victories: {6}🏁Solo Victories: {7}🏴‍☠Duo Victories: {8}").format(player.tag+"\n",player.name+"\n",player.club.name+"\n",player.club.tag+"\n\n",str(player.trophies)+"\n",str(player.highestTrophies)+"\n\n",str(player.x3vs3_victories)+"\n",str(player.soloVictories)+"\n",str(player.duoVictories)+"\n")
    except:
        message="¯\_( ͡❛ ͜ʖ ͡❛)_/¯ Invalid Player Tag"
    return message
#=======================================================================
#print(commands("!stats","#2GJG2CJKLO"))
#username="LudacrisSlay"
#print(com_help(username))
#=======================================================================
def lastMatch(player_id):
    try:
        log=client.get_battle_logs(player_id)
        message=log
    except:
        message="¯\_( ͡❛ ͜ʖ ͡❛)_/¯ Invalid Player Tag"
    return str(message)
print(lastMatch("#Y2GPG22OP"))
def com_help(username):
    message="How to use Brawl Genie:\n1. Stats - <Mention_me> !stats <player_tag>\n2. Club Stats - <Mention_me> !stats <player_tag>"
    try:
        profile_id=api.get_user(screen_name=username)
        api.send_direct_message(username,text=message)
        return "Check your DMs."
    except:
        return message

def clubStats(club_tag):
    try:
        club=client.get_club(club_tag)
        message=("👽Club Tag: {0}\n💪Club Name: {1}\n✉Description: {2}\n\n🎯Type: {3}\n🎖Required Trophies: {4}\n🏆Total Trophies: {5}").format(club.tag,club.name,club.description,club.type,str(club.requiredTrophhies),str(club.trophies))
    except:
        message="¯\_( ͡❛ ͜ʖ ͡❛)_/¯ Invalid Player Tag"
    return message
