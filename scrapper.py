import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def main():
    raw_site = requests.get("https://codoholicconfessions.wordpress.com/2017/05/21/strangest-sorting-algorithms/")
    soup = BeautifulSoup(raw_site.text, 'html.parser')
    lista = soup.find_all("strong")
    main_site = open("index.md", "w")
    main_site.write("# Esoteric sorting algorithms\n")
    main_site.write("Esoteric sorting algorithm is the one, which has no actual use other than entertain with its absurdity. Here is the list of ten algorithms, that I found somewhere on the internet:\n")
    for esoteric in lista:
        main_site.write(esoteric.text + "\n")
        clear_text = esoteric.text.strip("1234567890 ")
        clear_text = re.sub(r"\s+", '_', clear_text)
        main_site.write("[Click for more informations](" + clear_text + ".md)\n")
        bonus_site = open(clear_text + ".md", "w")
        bonus_site.write("# " + clear_text)
        bonus_site.close()
        #print("Here are top searches related to each of the list elements:")
        #for url in search(clear_text, stop=2):
            #print(url)
        #print()
    main_site.write("This was the whole list I found. Have fun!\n")
    main_site.write("![Smile](smile.jpg)")
    main_site.close()
main()