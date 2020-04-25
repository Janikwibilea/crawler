#!/usr/bin/env python
# coding: utf-8

# ## Aufgabe: Crawler
# 
# **Aufgabe:**
# 
# - Passe den ArticleFetcher so an, dass er die Informationen aus allen Seiten extrahiert
# 
# Hier nochmal die URL: http://python.beispiel.programmierenlernen.io/index.php
# 
# **Tipps:**
# 
# - Schau dir zuerst an, wie du den Button "Zur nächsten Seite" ansteuern kannst.
# - Wie greifst du von Python aus auf das "href" - Attribut dieses Buttons zu?
# - (Optional): Probier ggf. zuerst, nur die Infos der ersten 2 Seiten zu holen. Kannst du darauf aufbauend das Programm verallgemeinern, so dass es alle Seiten einliest?
# - Du kannst dich daran orientieren, ob es einen "Zur nächsten Seite"-Button gibt, oder nicht. Wenn es diesen Button nicht mehr gibt, bist du auf der letzten Seite angelangt. Welcher Schleifentyp bietet sich hier an, wenn du die Schleife erst dann stoppen willst, wenn es den Button nicht mehr gibt?

# In[8]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import time


# In[3]:


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


# In[4]:


fetcher = ArticleFetcher()
fetcher.fetch()


# In[ ]:




