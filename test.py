import urllib2, time, datetime, json
import constants

today = datetime.date.today().strftime('%Y-%m-%d').replace('-0', '-')

url = constants.beginning_url + today + '&location_id=' + constants.locations['sargent'] + constants.end_url

# read all data
page = urllib2.urlopen(url).read()

# convert json text to python dictionary
data = json.loads(page)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

