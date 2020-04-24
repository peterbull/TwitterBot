import tweepy
import config
import time

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
            break
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Smapdi':
        follower.follow()
        break
