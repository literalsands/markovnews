import requests, sys, tweepy, re, time, markovify

config = open('config.ini','r')
tokens = config.readlines()
config.close()

CONSUMER_KEY = tokens[0].rstrip()
CONSUMER_SECRET = tokens[1].rstrip()
ACCESS_KEY = tokens[2].rstrip()
ACCESS_SECRET = tokens[3].rstrip()
NEWS_API_KEY = tokens[4].strip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# api.update_status("test")

def get_news_urls():
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=' + NEWS_API_KEY)
    response = requests.get(url)
    url_list = []
    for article in response.json()['articles']:
        url_list.append(article['url'])
    return url_list


def markov_the_news(text):
    model = markovify.NewlineText(text)
    return model.make_sentence()

# while True:
#     api.update_status(markov_the_news(text))

# get_news_urls()

# for x in response.json()['articles']:
#     print(x['urlToImage'])