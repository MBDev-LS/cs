
def floodFSM(state, machine, visitedList=None, depth=None):
	visitedList = visitedList or []
	depth = depth or 1
	if state in visitedList:
		return []
	
	visitedList.append(state)
	resList = [{'depth': depth, 'state': state}]
	for transition in machine[state]['transitions']:
		resList.extend(floodFSM(machine[state]['transitions'][transition], machine, visitedList, depth+1))
	
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