import urllib2, time, datetime, ujson
import constants

today = datetime.date.today().strftime('%Y-%m-%d').replace('-0', '-')

url = constants.beginning_url + '&location_id=' + constants.locations['sargent'] + '&date=' + today

current = time.localtime()

# TO-DO: look up the breakfast, lunch, dinner times

# TO-DO: cache menu when calling the same query within the same mealtime

# read all data
page = urllib2.urlopen(url).read()

# convert json text to python dictionary
data = ujson.loads(page)

print 'three'
# setting constants to Dinner for now (index 2)

mealtime = 2

print data['menu']['periods'][mealtime]['name']

with open('data.json', 'w') as outfile:
    ujson.dump(data, outfile)

