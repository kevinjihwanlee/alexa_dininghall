from bs4 import BeautifulSoup as bs, NavigableString
import urllib, time, datetime

# the URL that contains the menus of the week for the dining hall
# currently set to Sargent SEE TODO
url="https://menus.sodexomyway.com/BiteMenu/Menu?menuId=337&locationId=10380001&whereami=http://northwestern.sodexomyway.com/dining-near-me/sargent"

soup = bs(urllib.urlopen(url), 'html.parser')

# grabs the date and adjusts the link accordingly to get the correct menu
today = "#menuid-"
if datetime.date.today().strftime("%d")[0:1] is not "0":
    today = today + datetime.date.today().strftime("%d") + "-day"
else:
    today = today + datetime.date.today().strftime("%d")[1:2] + "-day"

food = {}
mealtime = ""
specific_meal = ""

# pulls the specific menu block
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
                    break # this break is important because we want to find the FIRST title
    if currentMT not in food:
        food[currentMT] = {}
    if currentSM not in food[currentMT]:
        food[currentMT][currentSM] = []
    if item.string == None:  # item.string returns None because these specific menu entries have images with them
        food[currentMT][currentSM].append(item.contents[0].strip())
    else:
        food[currentMT][currentSM].append(item.string.strip())

# testing functionality 
print food['DINNER']['Daily Dish']


