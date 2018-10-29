from slugify import slugify, Slugify, UniqueSlugify, slugify_unicode


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
    HEADERS = 0
    PARAGRAPHS = 1
    LINKS = 2
    DIVS = 3

    def __init__(self, pageName):
        self.setHtmlContent(pageName)
        headers = self.getHeaders()
        paragraphs = self.getParagraphs()
        links = self.getLinks()
        divs = self.getTextInDivs()

        self.data = [headers, paragraphs, links, divs]

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

        return self.splitTextToWords(self.htmlContent.xpath('//p/text()'))

    # zwraca headery
    def getHeaders(self):
        return self.splitTextToWords(self.htmlContent.xpath('//h1/text()'))

    # zwraca divy
    def getTextInDivs(self):
        return self.splitTextToWords(self.htmlContent.xpath('//div/text()'))

    '''
        slugify_unicode - usuwa wszystkie znaki specjalne. Tryb unicode nie usuwa znaków charakterystycznych dla języka (po prostu polskich znaków)
        separator=' '   - normalnie usuwane są tez spacje, separator pozwala na oddzielenie wyrazow
        [0].split()         - dzieli zdanie/stringa/text na pojedyncze slowa
        '''
    def splitTextToWords(self, list):
        stringList = []
        try:
            for text in list:
                for word in [slugify_unicode(text, separator=' ')][0].split():
                    stringList.append(word)
        except:
            print("COS NIE TAK W FUNKCJI splitTextToWords ============================================================")

        return stringList

