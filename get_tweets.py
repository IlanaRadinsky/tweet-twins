from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pprint

ckey = '9iYEHY0pfWIGQ8YFduNGbedQv'
csecret = 'u9btwE95BSaqobp88lmPYDup2fwFIByqAGEOTbRcBQoRzed4Ym'

atoken = '978265942668054528-3OVrymkyZPXMMUVnEDOIpnA6KUBU92T'
asecret = 'qO3OmfXJK61bBZStpUw5F3ZbPKhK1gZ3Zlim4OO2DaGJ5'

class listener(StreamListener):
    def on_data(self, data):
        pp = pprint.PrettyPrinter(indent=4)

        data = data.strip()
        d = json.loads(data)
        if d['lang'] == 'en':
            #pp.pprint(d)
            print(d['text'], d['user']['id'], d['user']['screen_name'])
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())

twitterStream.filter(track=["torah", "hashem", "yeshiva", "kosher"])
