import brawlstats
import configparser

config=configparser.ConfigParser()
config.read('config.ini')

token= config['brawlstars']['token']


client =brawlstats.Client(token=token,timeout=5)
player=client.get_player("#2GJG2C800")


def createBrawlApi():
    return client
