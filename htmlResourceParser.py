import requests
from lxml import html
from enum import Enum

'''
Przykladowe strony 
'http://riad.pk.edu.pl/~bialas/'
'http://econpy.pythonanywhere.com/ex/001.html'
'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
'''


class PageResource:
    class DataType(Enum):
        HEADERS = 0
        PARAGRAPHS = 1
        LINKS = 2

    def __init__(self, pageName):
        self.setHtmlContent(pageName)
        headers = self.getHeaders()
        paragraphs = self.getParagraphs()
        links = self.getLinks()

        self.data = [headers, paragraphs, links]

    def setHtmlContent(self, pageName):
        self.htmlContent = self.getHtmlContent(pageName)

    # zwraca "brudny" kod html
    def getHtmlContent(self, pageName):
        # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        page = requests.get(pageName)
        return html.fromstring(page.content)

    # zwraca linki
    def getLinks(self):
        return self.htmlContent.xpath('//@href')

    # zwraca paragrafy
    def getParagraphs(self):
        return self.htmlContent.xpath('//p/text()')

    # zwraca headery
    def getHeaders(self):
        return self.htmlContent.xpath('//p/text()')

    # zwraca divy
    def getTextInDivs(self):
        return self.htmlContent.xpath('//div/text()')
