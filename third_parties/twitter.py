import os
from dotenv import load_dotenv
import requests

load_dotenv()


def scrape_user_tweets(username, num_tweets=5):
    tweet_list = []
    eden_twitter_gist = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
    tweets = requests.get(eden_twitter_gist, timeout=5).json()
    for tweet in tweets:
        tweet_dic = {
            "text": tweet["text"],
            "url": f"https://twitter.com/{username}/status/{tweet['id']}",
        }
        tweet_list.append(tweet_dic)
    return tweet_list


if __name__ == "__main__":
    tweets = scrape_user_tweets("EdenEmarco177")
    print(tweets)
