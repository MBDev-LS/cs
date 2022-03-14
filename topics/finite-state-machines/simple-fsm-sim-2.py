
def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['initial_state']:
			return stateKey


machine = {
    "S1": {
        "meta_data": {"accept_state": False, "initial_state": True},
        "transitions": {"a": "S3", "b": "S4", "c": "S5", "z": "S2"},
    },
    "S2": {
        "meta_data": {"accept_state": True, "initial_state": False},
        "transitions": {"a": "S3", "b": "S4", "c": "S5", "z": "S2"},
    },
    "S3": {
        "meta_data": {"accept_state": True, "initial_state": False},
        "transitions": {"a": "S3", "b": "S4", "c": "S5", "z": "S2"},
    },
    "S4": {
        "meta_data": {"accept_state": True, "initial_state": False},
        "transitions": {"a": "S3", "b": "S4", "c": "S5", "z": "S2"},
    },
    "S5": {
        "meta_data": {"accept_state": True, "initial_state": False},
        "transitions": {"a": "S3", "b": "S4", "c": "S5", "z": "S2"},
    },
}


inputStr = 'az'

currentStateKey = getInitialState(machine)
print(f'Started at state {currentStateKey}')

for char in inputStr:
	if char in machine[currentStateKey]['transitions']:
		currentStateKey = machine[currentStateKey]['transitions'][char]
		print(f'NEW STATE: {currentStateKey}')

print('Accepted' if machine[currentStateKey]['meta_data']['accept_state'] is True else 'Rejected')
