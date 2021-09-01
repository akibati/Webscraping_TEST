import urllib.parse
import urllib.request
import os

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        

        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        atriles = sp.select(".xrnccd")
        news = list()
        for i, tag in enumerate(atriles, 1):
            title = tag.find("h3").text
            #print(title)
            news.append(title)
        
        st = open(os.path.join("googlescraping.txt"), "w", encoding="utf-8")
        st.write("\n".join(news))
        st.close()

        
s = "ストリートダンス"
s_quote = urllib.parse.quote(s)
news = "https://news.google.com/search?q=" + s_quote + "&hl=ja&gl=JP&ceid=JP%3Aja"
Scraper(news).scrape()
print("end")


