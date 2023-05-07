
from pprint import pprint
import requests
import json


headers = {
	'Accept': 'application/json',
	'Authorization': 'LOW sXtLFFKKnepJRKkD:MKN2XXYuYLKk7GFf',
	'Content-Type': 'application/x-www-form-urlencoded',
}

# linksToArchiveList = [
# 	'https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php',
# 	'https://docs.scipy.org/doc/scipy-1.10.1/reference/generated/scipy.stats.pearsonr.html',
# 	'https://tex.stackexchange.com/a/352969',
# 	'https://johncanning.net/wp/?p=1202'

# ]

# for link in linksToArchiveList:
# 	data = {
# 		'url': link
# 	}

# 	response = requests.post('https://web.archive.org/save', headers=headers, data=data)

# 	pprint(response.text)



statusDicts = [
	'{"url":"https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php","job_id":"spn2-74643ed016a90175180abd678d1d93dcc0f071e5"}',
	'{"url":"https://docs.scipy.org/doc/scipy-1.10.1/reference/generated/scipy.stats.pearsonr.html","job_id":"spn2-bea1273059ed2ef321eb8f63a0f8a2600b1d8dcc"}',
	'{"url":"https://tex.stackexchange.com/a/352969","job_id":"spn2-4b3926712caee6f9f9bd7696f445ec18adb73f83"}',
	'{"url":"https://johncanning.net/wp/?p=1202","job_id":"spn2-1f578b33c25f1fb630745ea58cd89d165dec1c50"}'
]

for urlDict in statusDicts:
	urlDictProper = json.loads(urlDict)

	response = requests.get(f'https://web.archive.org/save/status/{urlDictProper["job_id"]}', headers=headers)

	pprint(response.json())