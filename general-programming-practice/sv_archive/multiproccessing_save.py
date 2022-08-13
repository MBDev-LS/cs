
from datetime import datetime
import json
import time

from waybackpy import WaybackMachineSaveAPI

import concurrent.futures

from config import DOMAIN


BASELINK = f'http://{DOMAIN}/people/'
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"

with open('/Users/louisstevens/Documents/cs/general-programming-practice/sv_archive/people_combined.json', 'r') as f:
	dictList = json.loads(f.read())


def savePersonDict(personDict: dict) -> None:

	print(f'[STARTING PAGE SAVE] Starting save of page for {personDict["name"]} (params: {personDict["params"]}) at {datetime.now().strftime(f"%m/%d/%Y %H:%M:%S")}')

	save_api = WaybackMachineSaveAPI(
		BASELINK + personDict['params'], USER_AGENT)
	
	save_api.save()

	try: 
		pass
		# save_api.save()
	except:
		print(f'[PAGE SAVE FAILED] Failed to save page for {personDict["name"]} (params: {personDict["params"]}) at {datetime.now().strftime(f"%m/%d/%Y %H:%M:%S")}')
	else:
		print(f'[SAVED PAGE] Saved page for {personDict["name"]} (params: {personDict["params"]}) at {datetime.now().strftime(f"%m/%d/%Y %H:%M:%S")}')

# if __name__ == '__main__':
# 	listOfLists = []

# 	for i in range(0, len(dictList), 2):

# 		subList = dictList[i: min(i+2, len(dictList))]

# 		with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
# 			futures = executor.map(savePersonDict, subList)

startTime = time.perf_counter()

for pageDict in dictList:
	savePersonDict(pageDict)

	time.sleep(10)

endTime = time.perf_counter()

print(f'Saving finished after {round(endTime - startTime, 2)}.')
