
from pprint import pprint

def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['initial_state']:
			return stateKey



def zeroOrMore(char, machine, stateCount):
	machine[f'S{stateCount-1}']['transitions'][char] = f'S{stateCount-1}'

	return machine

def OneOrMore(char, machine, stateCount):
	machine[f'S{stateCount-1}']['transitions'][char] = f'S{stateCount}'

	machine[f'S{stateCount}'] = {
		'meta_data': {
			'accept_state': False,
			'initial_state': False,
		},
		'transitions': {}
	}

	machine[f'S{stateCount}']['transitions'][char] = f'S{stateCount}'

	return machine

def addRegularState(char, currentState, stateCount, machine):
	machine[currentState]['transitions'][char] = f'S{stateCount}'
		
	machine[f'S{stateCount}'] = {
		'meta_data': {
			'accept_state': False,
			'initial_state': False,
		},
		'transitions': {}
	}

	return machine

def regexToFsm(regexString, operators):
	machine = {
	'S1': {
		'meta_data': {
			'accept_state': False,
			'initial_state': True,
		},
		'transitions': {}
	}
}

	currentState = getInitialState(machine)
	stateCount = 2

	for i, char in enumerate(regexString):
		stateCreated = False
		if char in operators:
			continue

		if i == len(regexString)-1:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

			continue

		if regexString[i+1] in operators:
			machine = operators[regexString[i+1]]['func'](char, machine, stateCount)
			stateCreated = operators[regexString[i+1]]['stateCreated']
		else:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

		currentState = f'S{stateCount}'
		stateCount += 1 if stateCreated is True else 0

	machine[f'S{stateCount-1}']['meta_data']['accept_state'] = True

	return machine

operators = {
	'*': {
			'func': zeroOrMore,
			'stateCreated': False
		},
	'+': {
			'func': OneOrMore,
			'stateCreated': True
		},

}

regexString = r'ab+'

finalMachine = regexToFsm(regexString, operators)

pprint(finalMachine)