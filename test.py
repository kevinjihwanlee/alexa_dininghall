from bs4 import BeautifulSoup as bs, NavigableString
import urllib2, time, datetime, json

# actually shouldn't need BeautifulSoup anymore

# this should be Sargent
# need to collect the location IDs for each dining hall
url = "https://www.dineoncampus.com/v1/location/menu.json?date=2018-7-7&location_id=5b33ae291178e909d807593e&platform=0&site_id=5acea5d8f3eeb60b08c5a50d"

# read all data
page = urllib2.urlopen(url).read()

# convert json text to python dictionary
data = json.loads(page)

print data

