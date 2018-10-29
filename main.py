from slugify import slugify, Slugify, UniqueSlugify, slugify_unicode
from slugify import slugify_ru


import enchant

from htmlResourceParser import *

STARTING_PAGE = 'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
DICTIONARY = enchant.Dict("pl")

tree = getHtmlContent(STARTING_PAGE)

print(DICTIONARY.check("dobrej"))

print(enchant.list_languages())
paragraphs = getParagraphs(tree)
links = getLinks(tree)

print(slugify('one two ##### three',separator=' '))


'''
slugify_unicode - usuwa wszystkie znaki specjalne. Tryb unicode nie usuwa znaków charakterystycznych dla języka (po prostu polskich znaków)
separator=' '   - normalnie usuwane są tez spacje, separator pozwala na oddzielenie wyrazow
[0].split()         - dzieli zdanie/stringa/text na pojedyncze slowa
'''
stringList = [slugify_unicode(paragraphs[0], separator=' ')][0].split()


print(stringList)