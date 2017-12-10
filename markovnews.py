import requests, sys, tweepy, re, time, markovify

config = open('config.ini','r')
tokens = config.readlines()
config.close()

CONSUMER_KEY = tokens[0].rstrip()
CONSUMER_SECRET = tokens[1].rstrip()
ACCESS_KEY = tokens[2].rstrip()
ACCESS_SECRET = tokens[3].rstrip()
NEWSAPI_CLIENT_KEY = tokens[4].strip()

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

def query_api(endpoint, query_params, api_params):
    # We're trusting the params are valid.
    # Convert the query_params and api_params dict into a query.
    query = "?" + "&".join(map("=".join, list(query_params.items()) + list(api_params.items())))
    return requests.get(endpoint + query)

# https://newsapi.org/docs
def query_newsapi_headlines(query_params):
    # Make the request and return body in JSON format.
    return query_api("https://newsapi.org/v2/top-headlines", query_params, {'apiKey': NEWSAPI_CLIENT_KEY}).json()

# https://newsapi.org/docs
def query_newsapi_everything(query_params):
    # Make the request and return body in JSON format.
    return query_api("https://newsapi.org/v2/everything", query_params, {'apiKey': NEWSAPI_CLIENT_KEY}).json()

def get_news_headlines(news_sources):
    # sources: A comma-seperated string of identifiers (maximum 20) ...
    news_sources = news_sources if isinstance(news_sources, list) else list(news_sources)
    return query_newsapi_headlines({'sources': ",".join(news_sources)});

def url_from_article(article):
    return article['url']

def headline_from_article(article):
    return ' '.join((article['title'], article['description']));


#article = map(get_news(url_list[0])
sources = ['bbc-news','fox-news','nbc-news','associated-press']
articles = get_news_headlines(sources)['articles']
headlines = map(headline_from_article, articles)
model = markovify.Text(' '.join(headlines))

for x in range(10):
    print(model.make_sentence())