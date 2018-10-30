import enchant


'''
Przykladowe strony 
'http://riad.pk.edu.pl/~bialas/'
'http://econpy.pythonanywhere.com/ex/001.html'
'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
https://stackoverflow.com/questions/12851791/removing-numbers-from-string
'''

STARTING_PAGE = 'https://stackoverflow.com/questions/12851791/removing-numbers-from-string'
DICTIONARY = enchant.Dict("pl")

'''
    Powinny sie tworzyc foldery o nazwie strony z ktorej pobierane sa slowa
    w srodku powinny byc 2 pliki - correct i incorrect 
    
    Incorrect jest g³ownie przeznaczone do sprawdzania dzia³ania s³ownika (i zeby sobie popatrzec 
    ile s³ow jest odrzucanych :))
'''

#USTAW SOBIE SWOJA SCIEZKE - przy zmianie na swoja zakomentuj moja prosze :)
PATH_FOR_FILES = "C:\\Users\\lipin\\PycharmProjects\\PJN_FILES_LAB3"

#MIEJSCE NA TWOJA SCIEZKE
#PATH_FOR_FILES = "C:\Users\lipin\PycharmProjects\PJN_FILES_LAB3"