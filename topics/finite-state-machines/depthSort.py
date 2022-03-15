

def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['initial_state'] is True:
			return stateKey

def floodFsm(state: str, machine: dict, visitedTransitionsList: list=None, depth: int=None) -> list:
	visitedTransitionsList = visitedTransitionsList or []
	depth = depth or 1
	
	resList = [{'depth': depth, 'state': state}]
	for transition in machine[state]['transitions']:
		if (state, machine[state]['transitions'][transition]) in visitedTransitionsList:
			continue
		visitedTransitionsList.append((state, machine[state]['transitions'][transition]))
		resList.extend(floodFsm(machine[state]['transitions'][transition], machine, visitedTransitionsList, depth+1))

	resList = sorted(resList, key=lambda d: d['depth'])

	return resList

def fsmDepthSort(machine: dict) -> list:
	resList = floodFsm(getInitialState(machine), testMachine)

	newResList = []

	for stateDict in resList:
		if stateDict['state'] in newResList:
			continue

		newResList.append(stateDict['state'])
	
	return newResList


testMachine = {
    "S1": {
        "meta_data": {"accept_state": False, "initial_state": True},
        "transitions": {"a": "S2", "c": "S4"},
    },
    "S2": {
        "meta_data": {"accept_state": False, "initial_state": False},
        "transitions": {"b": "S3"},
    },
    "S3": {
        "meta_data": {"accept_state": True, "initial_state": False},
        "transitions": {"a": "S2", "c": "S4"},
    },
    "S4": {
        "meta_data": {"accept_state": False, "initial_state": False},
        "transitions": {"d": "S3"},
    },
}

print(fsmDepthSort(testMachine))