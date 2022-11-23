import urllib.request
from bs4 import BeautifulSoup as bs
from difflib import get_close_matches

word = input()

url = "https://www.vocabulary.com/dictionary/" + word +""
htmlfile = urllib.request.urlopen(url)
soup = bs(htmlfile, 'lxml')

soup1 = soup.find(class_="short")

try:
    soup1 = soup1.get_text()
except AttributeError:
    print('Cannot find such word! Please check spelling')
    exit()

#print short meaning
print("SHORT MEANING: \n\n",soup1)
print("\n")
#print long meaning
soup2 = soup.find(class_="long")
soup2 = soup2.get_text()
print("LONG MEANING: \n\n",soup2)
print("\n")

#print instances like synonyms, antonyms etc.

soup3 = soup.find(class_="instances")
txt = soup3.get_text()
txt1 = txt.rstrip()

print(' '.join(txt1.split()))