import enchant


'''
Przykladowe strony 
'http://riad.pk.edu.pl/~bialas/'
'http://econpy.pythonanywhere.com/ex/001.html'
'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
https://stackoverflow.com/questions/12851791/removing-numbers-from-string
'''

#STRONA Z KTOREJ SA POBIERANE SLOWA
STARTING_PAGE = 'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'

#UZYWANY SLOWNIK
DICTIONARY = enchant.Dict("pl")

'''
Powinny sie tworzyc foldery o nazwie strony z ktorej pobierane sa slowa
w srodku powinny byc 2 pliki - correct i incorrect 
'''

#MIEJSCE GDZIE BEDZIESZ SOBIE ZAPISYWAL PLIKI
#USTAW SOBIE SWOJA SCIEZKE - przy zmianie na swoja zakomentuj moja prosze :)
''' PIOTREK '''
PATH_FOR_FILES = "C:\\Users\\lipin\\PycharmProjects\\PJN_FILES_LAB3"

#MIEJSCE NA TWOJA SCIEZKE
''' PAWEL '''
#PATH_FOR_FILES = "C:\Users\lipin\PycharmProjects\PJN_FILES_LAB3"