
from Configuration import *
from htmlResourceParser import *

#TODO links = [STARTING_PAGE]

#TODO: for nextLink in links
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
#TODO: links.append(tree.links)

#TODO: DODAC ZABEZPIECZENIE PRZED POBIERANIEM DANYCH Z TEJ SAMEJ STRONY (NP. plik w którym bedzie lista u¿ytych stron)
#TODO: STWORZYC LISTE Z LINKAMI - dodawac do niej caly czas nowe linki wraz z wchodzeniem "glebiej" w inne podstrony
#TODO: STWORZYC PETLE KTORA BEDZIE WYKONWYAC TO SAMO CO POWYZEJ AZ DO OSIAGNIECIA PEWNEJ LICZBY PLIKOW | ALTERNATYWNIE: JAKIS WATEK SPRAWDZAJACY CZAS



#print(stringList)