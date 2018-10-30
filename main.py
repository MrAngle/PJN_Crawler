
from Configuration import *
from htmlResourceParser import *




tree = PageResource(STARTING_PAGE, DICTIONARY)
print("PARAGRAPHS === Liczba elementow (PARAGRAPHS) {}".format(len(tree.data[PageResource.PARAGRAPHS])))
print(tree.data[PageResource.PARAGRAPHS])
print("\n")

print("HEADERS === Liczba elementow (HEADERS) {}".format(len(tree.data[PageResource.HEADERS])))
print(tree.data[PageResource.HEADERS])
print("\n")

print("LINKS === Liczba elementow (LINKS) {}".format(len(tree.links)))
print(tree.links)
print("\n")

print("DIVS === Liczba elementow (DIVS) {}".format(len(tree.data[PageResource.DIVS])))
print(tree.data[PageResource.DIVS])
print("\n")

tree.saveWordsToFile()



#print(stringList)