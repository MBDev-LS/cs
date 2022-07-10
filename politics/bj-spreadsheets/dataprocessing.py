
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'

with open(DATA_DIR / 'torymps.json', 'r') as f:
	toryMpsJson = json.loads(f.read())

# print(toryMpsJson)

payrollVote = []

for tmp in toryMpsJson:
	if 'office' in tmp:
		isPayroll = False
		for office in tmp['office']:
			if 'Commission' not in office['dept'] and 'Committee' not in office['dept'] and 'speaker' not in office['dept'].lower() and office['dept'] != 'Panel of Chairs': 
				isPayroll = True
				break
		
		if isPayroll is True:
			payrollVote.append(tmp)

print(len(payrollVote))

with open(DATA_DIR / 'payroll-vote.json', 'w+') as f:
	toryMpsJson = f.write(json.dumps(payrollVote))