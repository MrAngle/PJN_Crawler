import random
from Configuration import *
from htmlResourceParser import *

#TODO links = [STARTING_PAGE]

#TODO: for nextLink in links

links = [STARTING_PAGE]

# a = [0, 2, 22]
# b = [0, 1, 33]
# c = [0, 1, 44]
# b.extend(a)
# b = list(set(b))
# print(b)
#
# del b[3:len(b)]
# print(b)

def keepMaxNumberOfLinks(links):
    listCount = len(links)
    if listCount > MAX_NUMBER_OF_LINKS:
        del links[MAX_NUMBER_OF_LINKS:listCount]




for x in range(0, MAX_NUMBER_OF_PAGES):

    tree = PageResource(links[random.randint(0,len(links))], DICTIONARY) # losowa wartosc zeby nie szlo zawsze ta sama sciezka
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

    print("SPANS === Liczba elementow (SPANS) {}".format(len(tree.data[PageResource.SPANS])))
    print(tree.data[PageResource.SPANS])
    print("\n")

    tree.saveWordsToFile()      # save results in files

    links.extend(tree.links)    # add new links to list
    links = list(set(links))    # remove duplicate from list
    links.pop(0)
    keepMaxNumberOfLinks(links) # keep maximum number of links in list

#TODO: DODAC ZABEZPIECZENIE PRZED POBIERANIEM DANYCH Z TEJ SAMEJ STRONY (NP. plik w ktorym bedzie lista uzytych stron)

#TODO: Fajnie by bylo dodac pare watkow



#print(stringList)