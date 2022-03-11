
# Import(s)

from ast import operator
from pprint import pprint

from pytest import skip

#	General Utility Functions

def raiseUserError(errorMessage: str):
	print(f'ERROR: {errorMessage}')
	exit()


def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['initial_state']:
			return stateKey


def getAcceptState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['accept_state']:
			return stateKey


def getStateCount(machine):
	return len(machine) + 1

def reverseCloseBracketSearch(closingBracket: str, scDict) -> str:
	for bracket in scDict['brackets']:
		if scDict['brackets'][bracket]['close_bracket'] == closingBracket:
			return bracket
	
	return None


#							Extending Functions
#	Quantifier Functions

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

#	Special Quantifier Functions

def oneOrMoreOfOr(subMachine: dict):
	secondStateKey = list(subMachine[getInitialState(subMachine)]['transitions'].keys())[0]
	secondStateInOr = subMachine[getInitialState(subMachine)]['transitions'][secondStateKey]
	subMachine[getAcceptState(subMachine)]['transitions'][secondStateKey] = secondStateInOr
	
	return subMachine


#	OR Function (and utility function(s))

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


	withinBrackets = regexString[charIndex+1:BracketClosePosition]
	orList = withinBrackets.split('|')
	for option in orList:
		# Minus one is to deal with the fact we take the first one out later.
		option = regexToFsm(option, scDict, stateCount-1)
		print('OPTION PRINT')
		print(option)

		skipModifier = 0
		if regexString[BracketClosePosition+1] in scDict['aftOperators']: # This could be hardcoded for optimisation
			option = scDict['brackets'][regexString[charIndex]]['quantifier_funcs'][regexString[BracketClosePosition+1]](option) # Need to standardise parameters
			skipModifier = 1

		# print(option[getInitialState(option)])

		for transition in option[getInitialState(option)]['transitions']:
			# print('ONE:\n'+transition)
			machine[currentState]['transitions'][transition] = option[getInitialState(option)]['transitions'][transition]

		# print(machine)

		for resState in option:
			if resState == getInitialState(option):
				continue

			option[resState]['meta_data']['initial_state'] == False
			if option[resState]['meta_data']['accept_state'] is True:
				if resState in machine:
					continue

			if resState not in machine:
				machine[resState] = option[resState]
			else:
				for transition in option[resState]['transitions']:
					machine[resState]['transitions'][transition] = option[resState]['transitions'][transition]

	return machine, BracketClosePosition-charIndex-1+skipModifier, len(machine)-1


#	Range Function

def rangeHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
	pass


#	Main Function

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
	skipFor = 0

	for i, char in enumerate(regexString):
		stateCreated = False
		if skipFor > 0:
			skipFor -= 1
			continue
		if char == '+':
			print('CHECK')

		
		if char in scDict['aftOperators']:
			continue

		elif char in scDict['brackets']:
			print('BRACKETS')
			machine, skipFor, stateCount = scDict['brackets'][char]['func'](i, currentState, stateCount, regexString, machine, scDict)
			print('f', stateCount)

		elif i == len(regexString)-1:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

			continue

		elif regexString[i+1] in scDict['aftOperators']:

			machine = scDict['aftOperators'][regexString[i+1]]['func'](char, machine, stateCount)
			stateCreated = scDict['aftOperators'][regexString[i+1]]['stateCreated']
		else:
			machine = addRegularState(char, currentState, stateCount, machine)
			stateCreated = True

		currentState = f'S{stateCount}'
		stateCount += 1 if stateCreated is True else 0
		print(stateCount, getStateCount(machine))

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
			'close_bracket': ')',
			'quantifier_funcs': {
				'+': oneOrMoreOfOr,
				'*': None,
			}
		},
		'[': {
			'func': rangeHandler,
			'stateCreated': True,
			'close_bracket': ']',
			'quantifier_funcs': {
				'+': None,
				'*': None,
			}
		},
	}
}

regexString = r'ab+(sasboy|no)+' # adding (l|p)+ causes an issue with merging with other or statements, also does not work with the +

stateCount = 1

finalMachine = regexToFsm(regexString, scDict, stateCount)

print('Final Machine'.center(50))
pprint(finalMachine)
