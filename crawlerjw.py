import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import time



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import time


class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        while url != "":
            time.sleep(1)
            print(url)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            articles = []
            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)   
            naechste_seite = doc.select_one(".btn")
            print(naechste_seite)
        
        return articles    


fetcher = ArticleFetcher()
fetcher.fetch()





