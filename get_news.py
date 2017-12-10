from bs4 import BeautifulSoup
import requests
import re

source_settings = {
    'bbc-news': {
        'article_tag': 'div.story-body__inner',
        'dirty_tags': ["script", "img", "figure", "aside"]
    }
}

def article_from_html(html, settings):
    soup = BeautifulSoup(html, "html.parser")
    try:
        article = soup.select(settings['article_tag'])[0]
        for tag in settings['dirty_tags']:
            for element in soup.select(tag):
                element.decompose()
        text = article.get_text()
        text = re.sub(r'[^a-zA-Z0-9,. ]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text
    except:
        return ""

def article_text(site, source):
    return article_from_html(requests.get(site).text, source_settings[source])

#print(article_text('http://www.bbc.com/news/technology-10757263', 'bbc-news'))
