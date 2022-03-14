
# Import(s)

from pprint import pprint

#	General Utility Functions

def raiseUserError(errorMessage: str):
	print(f'ERROR: {errorMessage}')
	exit()


def getInitialState(machine: dict) -> str:
	for stateKey in machine:
		if machine[stateKey]['meta_data']['initial_state'] is True:
			return stateKey


def getAcceptState(machine: dict, include_all=False) -> str:
	stateList = []

	for stateKey in machine:
		if machine[stateKey]['meta_data']['accept_state'] is True:
			if include_all is False:
				return stateKey
			stateList.append(stateKey)
	
	if len(stateList) == 0:
		return None
	
	return stateList


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

def getBracketClosePosition(charIndex, regexString, scDict) -> int: # Fails on second bracket level, due to malformed regexString which is too short (including only the first and second characters)
	closingBracket = scDict['brackets'][regexString[charIndex]]['close_bracket']
	closePosition = None
	bracketCount = 0

	for n in range(charIndex, len(regexString)):
		if regexString[n] == regexString[charIndex]:
			bracketCount += 1
		if regexString[n] == closingBracket:
			bracketCount -= 1
			if bracketCount == 0:
				closePosition = n
				break

	if closePosition is None:
		raiseUserError(f'Bracket \'{regexString[charIndex]}\' at position {charIndex+1} not closed.')

	return closePosition

def splitRegexIntoOptions(regexWithinOrBrackets, charIndex):
	"a|(z|(x|y|m)))"

	bracketStart = None
	bracketCount = 0
	resultList = []

	for i, char in enumerate(regexWithinOrBrackets):
		if char == '(':
			bracketStart = i if bracketStart is None else bracketStart
			bracketCount += 1
		elif char == ')':
			bracketCount -= 1
			if bracketStart is not None and bracketCount == 0:
				draftOption = ''.join([regexWithinOrBrackets[j] for j in range(bracketStart, i+1)])
				resultList.append(draftOption)
				bracketStart = None
		else:
			if bracketStart is None:
				resultList.append(char)

	if bracketCount != 0:
		raiseUserError(f'Bracket \'{regexString[charIndex]}\' at position {charIndex+1} not closed.')

	while '|' in resultList:
		resultList.remove('|')

	return resultList

def orHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
	print('Handling or.')
	# print(charIndex, currentState, stateCount, machine, scDict)
	BracketClosePosition = getBracketClosePosition(charIndex, regexString, scDict)

	bracketsInRegexString = False
	bracketCount = 1 # Introduce a mult-bracket system for finding the outer most bracket
	if BracketClosePosition+1 < len(regexString):
		if regexString[BracketClosePosition+1] in scDict['aftOperators']:
			bracketsInRegexString = True

	withinBrackets = regexString[charIndex+1:BracketClosePosition]
	orList = splitRegexIntoOptions(withinBrackets, charIndex)
	# orList = withinBrackets.split('|')
	for i, option in enumerate(orList):
		# Minus one is to deal with the fact we take the first one out later.
		option, stateCount = regexToFsm(option, scDict, stateCount-1) # Issue with brackets can be traced back to the argument passed here
		stateCount += 1
		print('OPTION PRINT')
		print(option)

		skipModifier = 0
		if bracketsInRegexString is True:
			option = scDict['brackets'][regexString[charIndex]]['quantifier_funcs'][regexString[BracketClosePosition+1]](option) # Need to standardise parameters
			skipModifier = 1

		# print(option[getInitialState(option)])

		for transition in option[getInitialState(option)]['transitions']:
			# print('ONE:\n'+transition)
			machine[currentState]['transitions'][transition] = option[getInitialState(option)]['transitions'][transition]

		print('IMP0:', machine)

		for resState in option:
			if resState == getInitialState(option):
				continue

			machine[resState] = option[resState]
		
		print('IMP0.5:', machine)

	print('IMP: ',machine)

	reverseListOfEndTransitions = [endState for endState in getAcceptState(machine, include_all=True)] # Neet to get the ones that go to it
	reverseListOfEndTransitions.reverse()
	if bracketsInRegexString is True: # Just take the first letter of the original text orList option strings
		for endState in getAcceptState(machine, include_all=True):
			pprint(getAcceptState(machine, include_all=True))
			machine[endState]['transitions'][orList[i][0]] = '<start of or>'

	return machine, len(withinBrackets)+1+skipModifier, len(machine)-1


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

	return machine, stateCount


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

regexString = r'ab+(sasboy|no)+' # Removed '+' from the end # adding '(l|p)+' causes an issue with merging with other or statements, also does not work with the +
# regexString = r'ab+(a|(z|(x|(y|m))))'
# regexString = r'ab+(a|(z|(x|(y))))'
# regexString = r'ab+(z|x)'

# regexString = r'ab+(sasboy|no)'

regexString = r'(z(a|b|c))' # Works
regexString = r'(z(y|(a|b|c)))'

stateCount = 1

finalMachine, stateCount = regexToFsm(regexString, scDict, stateCount)

print('Final Machine'.center(50))
pprint(finalMachine)
