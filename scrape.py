from bs4 import BeautifulSoup as bs
import urllib

# storing some information here
# looks like the menu is divided by day like this: menuid-#-day

url="https://menus.sodexomyway.com/BiteMenu/Menu?menuId=337&locationId=10380001&whereami=http://northwestern.sodexomyway.com/dining-near-me/sargent"

soup = bs(urllib.urlopen(url), 'html.parser')
# for link in soup.findAll('a'):
#         print link.string
# for food in soup.find_all("div", class_="bite-menu-item"):
#     print food.

categories = []
for item in soup.select("#menuid-2-day .accordion-copy"):
    categories.append(item.string)

food = []
#for item in soup.select(".bite-menu-item button"):
for item in soup.select(".get-nutrition"):
    if item.string == None:
        # item.string returns None because these specific menu entries have images with them
        print item.contents[0]
    else:
        print item.string
    #food.append(item.string)

#print food

