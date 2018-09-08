from pushbullet import Pushbullet
from tinydb import TinyDB, Query
from datetime import datetime
import subprocess
import json

def push_the_link(object):
	url = 'https://marknad.sgsstudentbostader.se/pgObjectInformation.aspx?company=1&obj=' + str(object['ObjectNo'])
	title = 'NEW in ' + str(object['MarketPlaceDescription']) + ' at ' + str(object['Street']) + \
	' with ' + str(object['CountInterest']) + ' applications ' + str(object['ObjectTypeDescription']) + \
	' and rent ' + str(object['RentPerMonth'])

	pb.push_link(title, url)

directory = '/home/pi/repos/sgs_bot/'

db = TinyDB(directory + 'sgs_db.json')
api_filename = directory + 'api.key'
time_format = '%Y-%m-%dT%H:%M:%S'

with open(api_filename, 'r') as f:
	api_key = f.read()

api_key = api_key.split('\n')
api_key = api_key[0]

pb = Pushbullet(api_key)

requests_filename = '/home/pi/repos/sgs_bot/requests.curl'

with open(requests_filename, 'r') as f:
	requests = f.read()

requests = requests.split('\n')

responses = []
for request in requests:
	process = subprocess.Popen(request, stdout=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	responses.append(output.decode('utf-8'))

responses = list(filter(None, responses))

for i in range(len(responses)):
	responses[i] = json.loads(responses[i])

house = Query()
for response in responses:
	for object in response['Result']:
		occurences = 0
		results = db.search(house.ObjectNo == object['ObjectNo'])
		for result in results:
			if (datetime.strptime(result['PublishingDate'], time_format) <= datetime.strptime(object['PublishingDate'], time_format)):
				occurences += 1

		if (occurences == 0):
			db.insert(object)
			push_the_link(object)
#		else:
#			print('Object ' + str(object['Street']) + ' already exists.')
