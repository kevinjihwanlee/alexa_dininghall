from bs4 import BeautifulSoup as bs
import urllib

url="https://menus.sodexomyway.com/BiteMenu/Menu?menuId=1164&locationId=10380002&whereami=http://northwestern.sodexomyway.com/dining-near-me/foster-walker-west"

soup = bs(urllib.urlopen(url), 'html.parser')
# for link in soup.findAll('a'):
#         print link.string
# for food in soup.find_all("div", class_="bite-menu-item"):
#     print food.

for item in soup.select(".bite-menu-item button"):
    if item != None or item.string != "":
        print item.string
