
from ast import operator
from pprint import pprint



regexString = r'ab+'

def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['initial_state']:
			return stateKey

machine = {
	'S1': {
		'accept_state': False,
		'initial_state': True,
	}
}

currentState = getInitialState(machine)
stateCount = 2

def zeroOrMore(char, machine, stateCount):
	machine[f'S{stateCount-1}'][char] = f'S{stateCount-1}'

	return machine

def OneOrMore(char, machine, stateCount):
	machine[f'S{stateCount-1}'][char] = f'S{stateCount}'

	machine[f'S{stateCount}'] = {
		'accept_state': False,
		'initial_state': False,
	}

	machine[f'S{stateCount}'][char] = f'S{stateCount}'

	return machine

def addRegularState(char, currentState, stateCount, machine):
	machine[currentState][char] = f'S{stateCount}'
		
	machine[f'S{stateCount}'] = {
		'accept_state': False,
		'initial_state': False,
	}

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

machine[f'S{stateCount-1}']['accept_state'] = True

pprint(machine)