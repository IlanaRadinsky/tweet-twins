from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pprint
import subprocess
import re


ckey = '9iYEHY0pfWIGQ8YFduNGbedQv'
csecret = 'u9btwE95BSaqobp88lmPYDup2fwFIByqAGEOTbRcBQoRzed4Ym'

atoken = '978265942668054528-3OVrymkyZPXMMUVnEDOIpnA6KUBU92T'
asecret = 'qO3OmfXJK61bBZStpUw5F3ZbPKhK1gZ3Zlim4OO2DaGJ5'

global results
results = {}

class listener(StreamListener):
    def __init__(self, api=None):
        super(listener, self).__init__()
        self.__numTweets = 0
        self.results = {}
       
    #def on_data(self, data):
    def ignore():
        pp = pprint.PrettyPrinter(indent=4)

        data = data.strip()
        d = json.loads(data)
        if d['lang'] == 'en':
            #pp.pprint(d)
            text = d['text']
            user_id = d['user']['id']
            screen_name = d['user']['screen_name']
            print(text, user_id, screen_name)    
        return True

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        global results
        text = status.text
        screen_name = status.user.screen_name
        hashtags = self.parse_hashtag(text)
        
        if screen_name in results:
                results[screen_name].append((text,hashtags))
        else:
                results[screen_name] = [(text, hashtags)]
        self.__numTweets += 1
        return self.__numTweets < 10

    def parse_hashtag(self, string):
        regex = re.compile(r'#\S*')
        found = re.findall(regex, string)
        return found
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())

twitterStream.filter(track=["#"])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)
