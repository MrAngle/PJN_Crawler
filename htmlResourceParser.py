from slugify import slugify, Slugify, UniqueSlugify, slugify_unicode

import requests
from lxml import html
from Configuration import *
import os

from bs4 import BeautifulSoup


class PageResource:
    # HEADERS = 0
    # PARAGRAPHS = 1
    # DIVS = 2
    # SPANS = 3

    # okresla czy artykuł ma być parsowany, czy wyciągany "surowy"
    RAW_MODE = True;

    # okresla czy ma się pojawic plik "incorrect"
    SAVE_INCORRECT_WORD_TO_FILE = False;

    def __init__(self, pageName, dictionaryType):
        self.rawPageName = pageName
        self.contentIsOk = True
        self.fileExist = False
        self.links = []
        try:
            self.setHtmlContent(pageName)
            self.links = list(set(self.getLinks()))
        except:
            print("cos nie tak w wyciaganiu kontentu")
            self.contentIsOk = False

        if self.contentIsOk:
            try:
                self.DICTIONARY = dictionaryType
                #self.setHtmlContent(pageName)
                # do weryfikowania działania slownika
                self.fileIncorrectWords = None
                self.fileCorrectWords = None
                self.fileLink = None
                self.fileExist = self.prepareFilesAndDir(slugify(pageName, separator='_'))
                #self.fileExist = self.prepareFilesAndDir(pageName)
                #self.links = list(set(self.getLinks()))

                if not self.fileExist:
                    headers = self.getHeaders()
                    paragraphs = self.getParagraphs()
                    divs = self.getTextInDivs()
                    spans = self.getTextInSpans()

                    #self.data = [headers, paragraphs, divs, spans]
                    self.data = [paragraphs]
            except:
                print("COS NIE TAK W FUNKCJI __INIT__ ==========================================================")
                self.links = True



    def prepareFilesAndDir(self, pageName):
        try:
            file_path = "{}\\{}\\".format(PATH_FOR_FILES,pageName)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                # print("dziala")
                os.makedirs(directory)

                #TODO: w pozniejszym etapie usunac "WRITE", bo bedziemy wyciagac slowa z plikow
                if self.SAVE_INCORRECT_WORD_TO_FILE:
                    self.fileIncorrectWords = open("{}\\{}\\incorrectWords.txt".format(PATH_FOR_FILES,pageName), "w")
                    # self.fileIncorrectWords.write(
                    #     "++++++++++++++++++ SLOWA KTORE NIE ZOSTALY ZNALEZIONE W SLOWNIKU ++++++++++++++++++ "
                    #     "\nLINK DO STRONY : {}\n\n\n".format(pageName))

                self.fileCorrectWords = open("{}\\{}\\correctWords.txt".format(PATH_FOR_FILES,pageName), "w")
                # self.fileCorrectWords.write(
                #     "++++++++++++++++++ SLOWA KTORE ZOSTALY ZNALEZIONE W SLOWNIKU ++++++++++++++++++ "
                #     "\nLINK DO STRONY : {}\n\n\n".format(pageName))

                self.fileLink = open("{}\\{}\\link.txt".format(PATH_FOR_FILES,pageName), "w")
                return False

        except:
            print("COS NIE TAK W FUNKCJI prepareFilesAndDir ==========================================================")
        return True

    def setHtmlContent(self, pageName):
        self.htmlContent = self.getHtmlContent(pageName)

    # zwraca "brudny" kod html
    def getHtmlContent(self, pageName):
        # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')

        page = requests.get(pageName)
        #x = HtmlXPathSelector(page)
        return html.fromstring(page.content)

    # zwraca linki
    def getLinks(self):
        links = self.htmlContent.xpath('//@href')
        return [x for x in links if x.startswith('http')] # zwraca linki tylko te ktore zaczynają sie od http


    # zwraca paragrafy
    def getParagraphs(self):
        print(self.htmlContent.xpath('//p/text()/text()'))
        if not self.RAW_MODE:
            return self.splitTextToWords(self.htmlContent.xpath('//p/text()>text()'))
        else:
            return self.htmlContent.xpath('//p/text()')

    # zwraca headery
    def getHeaders(self):
        return self.splitTextToWords(self.htmlContent.xpath("//h1/text()"))

    # zwraca divy
    def getTextInDivs(self):
        return self.splitTextToWords(self.htmlContent.xpath('//div/text()'))

    # zwraca spany
    def getTextInSpans(self):
        return self.splitTextToWords(self.htmlContent.xpath('//span/text()'))

    '''
        slugify_unicode                                 - usuwa wszystkie znaki specjalne. Tryb unicode nie usuwa znaków charakterystycznych dla języka (po prostu polskich znaków)
        separator=' '                                   - normalnie usuwane są tez spacje, separator pozwala na oddzielenie wyrazow
        [0].split()                                     - dzieli zdanie/stringa/text na pojedyncze slowa
        ''.join([i for i in text if not i.isdigit()])   - usuwa wszystkie liczby
    '''
    def splitTextToWords(self, list):


        stringList = []
        try:
            for text in list:
                text = ''.join([i for i in text if not i.isdigit()])
                for word in [slugify_unicode(text, separator=' ')][0].split():
                    # jesli slowo znajduje sie w slowniku zostaje dodane do listy
                    if self.checkWordInDict(word):
                        stringList.append(word)
        except:
            print("COS NIE TAK W FUNKCJI splitTextToWords ============================================================")
            self.contentIsOk = False

        return stringList

    def checkWordInDict(self, word):
        # wszystkie slowa ktore teoretycznie nie znajduja sie w slowniku zostaja zapisane w pliku incorrectWords"
        if not self.DICTIONARY.check(word):
            if self.SAVE_INCORRECT_WORD_TO_FILE:
                self.fileIncorrectWords.write("{}\n".format(word))
            return False
        return True

    def saveWordsToFile(self):
        try:
            for text in self.data:
                for word in text:
                    self.fileCorrectWords.write("{}\n".format(word))

            self.fileLink.write("{}\n".format(self.rawPageName))
        except:
            print("COS NIE TAK W FUNKCJI saveWordsToFile ============================================================")
            self.contentIsOk = False
            return


    def __del__(self):
        #print("kasuje sie")
        try:
            if self.SAVE_INCORRECT_WORD_TO_FILE:
                self.fileIncorrectWords.close()
            self.fileCorrectWords.close()
            self.fileLink.close()
        except:
            print("problem przy zamykaniu pliku")
