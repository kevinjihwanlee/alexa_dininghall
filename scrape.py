from bs4 import BeautifulSoup as bs
import urllib

# storing some information here
# looks like the menu is divided by day like this: menuid-#-day

url="https://menus.sodexomyway.com/BiteMenu/Menu?menuId=337&locationId=10380001&whereami=http://northwestern.sodexomyway.com/dining-near-me/sargent"

soup = bs(urllib.urlopen(url), 'html.parser')

# categories = []
# for item in soup.select("#menuid-2-day .accordion-copy"):
#     categories.append(item.string)
# print categories
food = {}
#for item in soup.select(".bite-menu-item button"):
# meal_container = soup.find('div', class_='accordion-block')

# for item in meal_container.descendants:

mealtime = ""

currentDay = soup.select("#menuid-2-day")

#for item in soup.select(".get-nutrition"):
for item in currentDay[0].select(".get-nutrition"):
    for parent in item.parents:
        if 'class' in parent.attrs and parent.attrs['class'][0] == 'accordion-block':
                currentMT = parent.find('div', class_='accordion-title').find('span', class_="accordion-copy").string
                if mealtime != currentMT:
                    mealtime = currentMT
            #print parent.attrs
    if currentMT not in food:
        food[currentMT] = []
    if item.string == None:
        # item.string returns None because these specific menu entries have images with them
        food[currentMT].append(item.contents[0].strip())
    else:
        food[currentMT].append(item.string.strip())
    #food.append(item.string)

# print food

