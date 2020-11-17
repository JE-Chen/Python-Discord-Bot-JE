import requests
from bs4 import BeautifulSoup


class MinecraftWikiCrawler:

    def __init__(self):
        self.Prefix = 'https://minecraft-zh.gamepedia.com/'

    def Search(self, Tag):
        format_string = ''
        url = self.Prefix + Tag
        res = requests.get(url)
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')
        Total = ''
        for index, data in enumerate(soup.select('#pageWrapper #bodyContent div.mw-parser-output p')):
            format_string += str(data.text)
            if data.has_attr('href'):
                format_string += str(data['href'])
        Total += format_string
        return Total
