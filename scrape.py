from bs4 import BeautifulSoup as bs
from bs4 import NavigableString
import urllib
import time
import datetime

# Sargent
url="https://menus.sodexomyway.com/BiteMenu/Menu?menuId=337&locationId=10380001&whereami=http://northwestern.sodexomyway.com/dining-near-me/sargent"

today = "#menuid-"

if datetime.date.today().strftime("%d")[0:1] is not "0":
    today = today + datetime.date.today().strftime("%d") + "-day"
else:
    today = today + datetime.date.today().strftime("%d")[1:2] + "-day"

soup = bs(urllib.urlopen(url), 'html.parser')

food = {}
mealtime = ""
specific_meal = ""

currentDay = soup.select(today)

for item in currentDay[0].select(".get-nutrition"):
    for parent in item.parents:
        if 'class' in parent.attrs and parent.attrs['class'][0] == 'accordion-block':
            currentMT = parent.find('div', class_='accordion-title').find('span', class_="accordion-copy").string
            if mealtime != currentMT:
                mealtime = currentMT
        if 'class' in parent.attrs and parent.attrs['class'][0] == 'bite-menu-item':
            for sibling in parent.previous_siblings:
                if not isinstance(sibling, NavigableString) and 'class' in sibling.attrs and sibling.attrs['class'][0] == 'bite-menu-course':
                    currentSM = sibling.find('span').string
                    if specific_meal != currentSM:
                        specific_meal = currentSM
                        print specific_meal
                    break
    if currentMT not in food:
        food[currentMT] = []
    if item.string == None:
        # item.string returns None because these specific menu entries have images with them
        food[currentMT].append(item.contents[0].strip())
    else:
        food[currentMT].append(item.string.strip())
    #food.append(item.string)


