
def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['initial_state']:
			return stateKey

machine = {
	'S1': {
		'accept_state': False,
		'initial_state': True,
		'0': 'S2',
	},
	'S2': {
		'accept_state': True,
		'initial_state': False,
		'1': 'S2',
		'0': 'S1'
	},
}

inputStr = '0101'

currentStateKey = getInitialState(machine)
print(f'Started at state {currentStateKey}')

for char in inputStr:
	if char in machine[currentStateKey]:
		currentStateKey = machine[currentStateKey][char]
		print(f'NEW STATE: {currentStateKey}')

print('Accepted' if machine[currentStateKey]['accept_state'] is True else 'Rejected')