import datetime
from Bot_Module.webCrawler.MinecraftWikiCrawler import MinecraftWikiCrawler

class WebCrawlerCore():

    def __init__(self):
        try:
            self.MinecraftWikiCrawler = MinecraftWikiCrawler()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
