import random
from Configuration import *
from htmlResourceParser import *

from lxml import etree


# TODO links = [STARTING_PAGE]

# TODO: for nextLink in links


# a = [0, 2, 22]
# b = [0, 1, 33]
# c = [0, 1, 44]
# c.extend(a)
# print(c)
# c = list(set(c))
# d = ["aa", "aak", "maki", "aa"]
# b.pop(0)
# d.remove("aa")
# print(c)
# #b = list(set(b))
# print(b)
# # print(b)
#
# del b[3:len(b)]
# print(b)


def keepMaxNumberOfLinks(linksM):
    listCount = len(linksM)

    if listCount > MAX_NUMBER_OF_LINKS:
        toDelete = MAX_NUMBER_OF_LINKS - listCount
        del linksM[0:toDelete]

    return linksM


def main():
    links = [STARTING_PAGE]
    print(len(links))

    # random.randint(0,len(links))

    for x in range(0, MAX_NUMBER_OF_PAGES):

        randomNumber = random.randint(0, len(links)-1)
        try:
            print("RANDOM: {},  {}. zaczynam od {}".format(randomNumber, x, links[randomNumber]))
        except:
            print("Dziwny znak przy stronki")

        tree = PageResource(links[randomNumber], DICTIONARY)  # losowa wartosc zeby nie szlo zawsze ta sama sciezka

        if not tree.fileExist and tree.contentIsOk == True:
            # print("PARAGRAPHS === Liczba elementow (PARAGRAPHS) {}".format(len(tree.data[PageResource.PARAGRAPHS])))
            # print(tree.data[PageResource.PARAGRAPHS])
            # print("\n")
            #
            # print("HEADERS === Liczba elementow (HEADERS) {}".format(len(tree.data[PageResource.HEADERS])))
            # print(tree.data[PageResource.HEADERS])
            # print("\n")
            #
            # print("LINKS === Liczba elementow (LINKS) {}".format(len(tree.links)))
            # print(tree.links)
            # print("\n")
            #
            # print("DIVS === Liczba elementow (DIVS) {}".format(len(tree.data[PageResource.DIVS])))
            # print(tree.data[PageResource.DIVS])
            # print("\n")
            #
            # print("SPANS === Liczba elementow (SPANS) {}".format(len(tree.data[PageResource.SPANS])))
            # print(tree.data[PageResource.SPANS])
            # print("\n")
            try:
                tree.saveWordsToFile()  # save results in files
            except:
                print("nie udalo sie zapisac do pliku")

        else:
            try:
                print(slugify(links[randomNumber], separator='_') + " juz istnieje")
            except:
                print("Dziwny znak przy stronki")


        if tree.links and tree.contentIsOk == True:
            links.extend(tree.links)  # add new links to list
        links = list(set(links))  # remove duplicate from list

        links.remove(links[randomNumber])
        links = keepMaxNumberOfLinks(links)  # keep maximum number of links in list





main()

# node = etree.fromstring("""<content>
# Text outside tag <div>Text <em>inside</em> tag</div>
# </content>""")
# stringify_children(node)

# TODO: DODAC ZABEZPIECZENIE PRZED POBIERANIEM DANYCH Z TEJ SAMEJ STRONY (NP. plik w ktorym bedzie lista uzytych stron)

# TODO: Fajnie by bylo dodac pare watkow


# print(stringList)
