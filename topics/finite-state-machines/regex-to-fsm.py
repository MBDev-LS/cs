
from pprint import pprint

def raiseUserError(errorMessage: str):
	print(f'ERROR: {errorMessage}')
	exit()

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

def getBracketClosePosition(charIndex, regexString, scDict) -> int:
	closingBracket = scDict['brackets'][regexString[charIndex]]['close_bracket']
	closePosition = None
	
	for n in range(charIndex+1, len(regexString)):
		if regexString[n] == closingBracket:
			closePosition = n
			break

	if closePosition is None:
		raiseUserError(f'Bracket \'{regexString[charIndex]}\' at position {charIndex+1} not closed.')
	
	return closePosition


def orHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
	print('Handling or.')
	# print(charIndex, currentState, stateCount, machine, scDict)
	BracketClosePosition = getBracketClosePosition(charIndex, regexString, scDict)
	# Need to split on '|'
	withinBrackets = regexString[charIndex+1:BracketClosePosition]
	orList = withinBrackets.split('|')
	for option in orList:
		option = regexToFsm(option, scDict, stateCount-1) # Minus one is to deal with the fact we take the first one out later.
		print(option[getInitialState(option)])

		for transition in option[getInitialState(option)]['transitions']:
			print('ONE:\n'+transition)
			machine[currentState]['transitions'][transition] = option[getInitialState(option)]['transitions'][transition]
		
		print(machine)

		for resState in option:
			if resState == getInitialState(option):
				continue

			option[resState]['meta_data']['initial_state'] == False
			machine[resState] = option[resState]

		print(f'LOOK HERE: {machine}')

	# print(machine)


def rangeHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
	pass


def regexToFsm(regexString, scDict, stateCount):
	machine = {
		f'S{stateCount}': {
			'meta_data': {
				'accept_state': False,
				'initial_state': True,
			},
			'transitions': {}
		}
	}

	stateCount += 1
	currentState = getInitialState(machine)

	for i, char in enumerate(regexString):
		stateCreated = False
		if char in scDict['aftOperators']:
			continue

		if char in scDict['brackets']:
			scDict['brackets'][char]['func'](i, currentState, stateCount, regexString, machine, scDict)

		if i == len(regexString)-1:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

			continue

		if regexString[i+1] in scDict['aftOperators']:
			machine = scDict['aftOperators'][regexString[i+1]]['func'](char, machine, stateCount)
			stateCreated = scDict['aftOperators'][regexString[i+1]]['stateCreated']
		else:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

		currentState = f'S{stateCount}'
		stateCount += 1 if stateCreated is True else 0

	machine[f'S{stateCount}']['meta_data']['accept_state'] = True

	return machine


scDict = {
	'aftOperators': {
		'*': {
			'func': zeroOrMore,
			'stateCreated': False
		},
		'+': {
			'func': OneOrMore,
			'stateCreated': True
		},
	},
	'brackets': {
		'(': {
			'func': orHandler,
			'stateCreated': True,
			'close_bracket': ')'
		},
		'[': {
			'func': rangeHandler,
			'stateCreated': True,
			'close_bracket': ']'
		},
	}
}

regexString = r'ab+(sasboy|no)'

stateCount = 1

finalMachine = regexToFsm(regexString, scDict, stateCount)

print('Final Machine'.center(50))
pprint(finalMachine)
