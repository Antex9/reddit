from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_about = "https://oauth.reddit.com/api/v1/user/420BLAZE_N_FAZE_CLAN/about"

class User(object):

    def __init__(self, reddit_id):
        self.id = reddit_id


    def me (self):

        pprint(reddit.client.request(url_me))



