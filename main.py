
from enum import Enum

import enchant



from htmlResourceParser import *

STARTING_PAGE = 'https://opinie.wp.pl/kampania-samorzadowa-wchodzi-w-krytyczna-faze-jaroslaw-kaczynski-ma-przeblyski-szczerosci-6311166497413249a'
DICTIONARY = enchant.Dict("pl")
#print(DICTIONARY.check("dobrej"))

tree = PageResource(STARTING_PAGE)
print("PARAGRAPHS === Liczba elementow (PARAGRAPHS) {}".format(len(tree.data[PageResource.PARAGRAPHS])))
print(tree.data[PageResource.PARAGRAPHS])
print("\n")

print("HEADERS === Liczba elementow (HEADERS) {}".format(len(tree.data[PageResource.HEADERS])))
print(tree.data[PageResource.HEADERS])
print("\n")

print("LINKS === Liczba elementow (LINKS) {}".format(len(tree.data[PageResource.LINKS])))
print(tree.data[PageResource.LINKS])
print("\n")

print("DIVS === Liczba elementow (DIVS) {}".format(len(tree.data[PageResource.DIVS])))
print(tree.data[PageResource.DIVS])
print("\n")





#print(stringList)