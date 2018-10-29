import requests
from lxml import html

'''
Przykladowe strony 
'http://riad.pk.edu.pl/~bialas/'
'http://econpy.pythonanywhere.com/ex/001.html'
'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
'''


# zwraca "brudny" kod html
def getHtmlContent(pageName):
    # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    page = requests.get(pageName)
    return html.fromstring(page.content)


# zwraca linki
def getLinks(htmlContent):
    return htmlContent.xpath('//@href')


# zwraca paragrafy
def getParagraphs(htmlContent):
    return htmlContent.xpath('//p/text()')


# zwraca headery
def getHeaders(htmlContent):
    return htmlContent.xpath('//p/text()')


# zwraca divy
def getTextInDivs(htmlContent):
    return htmlContent.xpath('//div/text()')
