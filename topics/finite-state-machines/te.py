
def floodFSM(state, machine, visitedTransitionsList=None, depth=None):
	visitedTransitionsList = visitedTransitionsList or []
	depth = depth or 1
	
	resList = [{'depth': depth, 'state': state}]
	for transition in machine[state]['transitions']:
		if (state, machine[state]['transitions'][transition]) in visitedTransitionsList:
			continue
		visitedTransitionsList.append((state, machine[state]['transitions'][transition]))
		resList.extend(floodFSM(machine[state]['transitions'][transition], machine, visitedTransitionsList, depth+1))

	return resList

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


print(floodFSM('S1', testMachine))