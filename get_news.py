from bs4 import BeautifulSoup
import requests
import re

def article_from_html(text, article="div.story-body__inner"):
    soup = BeautifulSoup(text, "html.parser")
    article = soup.select(article)[0]
    for script_tag in soup.select('script'):
        script_tag.decompose()
    for script_tag in soup.select('img'):
        script_tag.decompose()
    for script_tag in soup.select('figure'):
        script_tag.decompose()
    text = article.get_text()
    text = re.sub(r'[^a-zA-Z0-9,. ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def get_news(site):
    return article_from_html(requests.get(site).text)

#print(get_news('http://www.bbc.com/news/technology-10757263'))
