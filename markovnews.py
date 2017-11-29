import requests, sys, tweepy, re, time, markovify
from get_news import get_news

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

def get_news_object(news_source):
        url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + news_source + '&'
       'apiKey=' + NEWS_API_KEY)
        response = requests.get(url)
        return response

       

def get_news_urls(response):
    url_list = []
    for article in response.json()['articles']:
        url_list.append(article['url'])
    return url_list

def get_news_headlines(response):
    headlines = []
    for article in response.json()['articles']:
        headlines.append(article['title'] + " " + article["description"])
    return headlines


def markov_the_news(text):
    model = markovify.Text(text)
    return model.make_sentence()

# while True:
#     api.update_status(markov_the_news(text))

# get_news_urls()

# for x in response.json()['articles']:
#     print(x['urlToImage'])


bbc_response = get_news_object('bbc-news')
nbc_response = get_news_object('engadget')
msnbc_response = get_news_object('nbc-news')
# url_list = get_news_urls(response)
bbc_headlines = get_news_headlines(bbc_response)
nbc_headlines = get_news_headlines(nbc_response)
msnbc_headlines = get_news_headlines(msnbc_response)

# article = get_news(url_list[0])

for x in range(10):
    print(markov_the_news(' '.join(bbc_headlines + nbc_headlines + msnbc_headlines)))