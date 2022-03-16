
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

def getHighestState(machine: dict) -> str:
	sortedStateList = [int(stateName[1:]) for stateName in list(machine)]
	sortedStateList.sort()

	return f'S{sortedStateList[-1]}'


#							Extending Functions
#	Quantifier Functions

def addRegularState(char, currentState, stateCount, machine, acceptState=False, initialState=False):
	machine[currentState]['transitions'][char] = f'S{stateCount}'

	machine[f'S{stateCount}'] = {
		'meta_data': {
			'accept_state': acceptState,
			'initial_state': initialState,
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

def orOneOrMoreHandler(machine: dict, cachedStateCount: int) -> dict:

	acceptStates = getAcceptState(machine, include_all=True)
	baseState = f'S{cachedStateCount-1}'
	for acceptState in acceptStates:
		for transition in machine[baseState]['transitions']:
			if int(machine[baseState]['transitions'][transition][1:]) > int(baseState[1:]):
				machine[acceptState]['transitions'][transition] = machine[baseState]['transitions'][transition]

	return machine

def zeroOneOrMoreHandler(machine: dict, cachedStateCount: int) -> dict:

	acceptStates = getAcceptState(machine, include_all=True)
	baseState = f'S{cachedStateCount-1}'
	for acceptState in acceptStates:
		for transition in machine[baseState]['transitions']:
			if int(machine[baseState]['transitions'][transition][1:]) > int(baseState[1:]):
				machine[acceptState]['transitions'][transition] = acceptState

	return machine


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

def listSplitter(l, chopper):
	bits = [[]]
	for item in l:
		if item is chopper:
			bits.append([])
		else:
			bits[-1].append(item)
	results = []
	for item in bits:
		if len(item):
			results.append(item)
	return results

def splitRegexIntoOptions(regexWithinOrBrackets, regexString, charIndex, scDict):
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
				draftOption += regexWithinOrBrackets[i+1] if regexWithinOrBrackets[i+1] in scDict['aftOperators'] else ''
				resultList.append(draftOption)
				bracketStart = None
		else:
			if bracketStart is None and char not in scDict['aftOperators']:
				resultList.append(char)

	if bracketCount != 0:
		raiseUserError(f'Bracket \'{regexString[charIndex]}\' at position {charIndex+1} not closed.')

	
	splitList = listSplitter(resultList, '|')
	resultList = [''.join(lst) for lst in splitList]

	return resultList


#	Depth Sorting

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
	resList = floodFsm(getInitialState(machine), machine)

	newResList = []

	for stateDict in resList:
		if stateDict['state'] in newResList:
			continue

		newResList.append(stateDict['state'])
	
	return newResList


def fixStates(machine: dict) -> dict:
	sortedStateList = [int(stateName[1:]) for stateName in list(machine)]

	sortedStateNameList = fsmDepthSort(machine)
	startingOffset = sortedStateList[0]

	keysDict = {}
	for i, stateName in enumerate(sortedStateNameList):
		keysDict[stateName] = f'S{i+startingOffset}'
	
	newMachine = {}
	for stateName in machine:
		newMachine[keysDict[stateName]] = machine[stateName]
		for transition in machine[stateName]['transitions']:
			machine[stateName]['transitions'][transition] = keysDict[machine[stateName]['transitions'][transition]]
	
	print(newMachine)
	return newMachine

def removeAcceptStates(machine: dict) -> dict:
	for state in machine:
		machine[state]['meta_data']['accept_state'] = False
	
	return machine


def orHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
	print('Handling or.')
	cachedStateCount = stateCount
	# print(charIndex, currentState, stateCount, machine, scDict)
	BracketClosePosition = getBracketClosePosition(charIndex, regexString, scDict)

	quantifierInRegexString = False
	if BracketClosePosition+1 < len(regexString):
		if regexString[BracketClosePosition+1] in scDict['aftOperators']:
			quantifierInRegexString = True

	withinBrackets = regexString[charIndex+1:BracketClosePosition]
	orList = splitRegexIntoOptions(withinBrackets, regexString, charIndex, scDict)
	# orList = withinBrackets.split('|')
	for i, option in enumerate(orList):
		# Minus one is to deal with the fact we take the first one out later.
		option, stateCount = regexToFsm(option, scDict, stateCount-1)
		stateCount += 1
		print('OPTION PRINT')
		print(option)

		skipModifier = 0

		for transition in option[getInitialState(option)]['transitions']:

			if option[getInitialState(option)]['transitions'][transition] in getAcceptState(option, include_all=True):
				if getAcceptState(machine) is None:
					newAcceptStateCount = len(option)-len(getAcceptState(option, include_all=True))+(stateCount-1)
					print(newAcceptStateCount)

					machine[f'S{newAcceptStateCount}'] = {
						'meta_data': {
							'accept_state': True,
							'initial_state': False,
						},
						'transitions': {}
					}
					machine[currentState]['transitions'][transition] = getAcceptState(machine)
				else:
					machine[currentState]['transitions'][transition] = getAcceptState(machine)
			else:
				machine[currentState]['transitions'][transition] = option[getInitialState(option)]['transitions'][transition]


		print('IMP0:', machine)

		for resState in option:
			if resState == getInitialState(option) or resState in getAcceptState(option, include_all=True):
				continue

			machine[resState] = option[resState]
			
			for transition in option[resState]['transitions']:
				if option[resState]['transitions'][transition] in getAcceptState(option, include_all=True):
					if getAcceptState(machine, include_all=True) is None: # removing include_all=True here may save time
						newAcceptStateCount = len(option)-len(getAcceptState(option, include_all=True))+(stateCount-1)
						machine[f'S{newAcceptStateCount}'] = {
						'meta_data': {
							'accept_state': True,
							'initial_state': False,
						},
						'transitions': {}
						}
						machine[resState]['transitions'][transition] = getAcceptState(machine)
					else:
						machine[resState]['transitions'][transition] = getAcceptState(machine)
		
		print('IMP0.5:', machine)
		machine = fixStates(machine)

	print('IMP: ',machine)

	if quantifierInRegexString is True:
		scDict['brackets'][regexString[charIndex]]['quantifier_funcs'][regexString[BracketClosePosition+1]](machine, cachedStateCount)
		skipModifier += 1

	print(machine)
	machine = removeAcceptStates(machine)

	return machine, len(withinBrackets)+1+skipModifier, len(machine) # Not working. Machine wrong.

# Was trying to fix the issue of multiple or statements one after another by combining the accept states produced by an or statement. This is not working.


#	Range Function

def setHandler(charIndex, currentState, stateCount, regexString, machine, scDict):
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
			print('stateCount:', stateCount)
			stateCreated = True

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

	# machine[f'S{stateCount}']['meta_data']['accept_state'] = True
	machine[getHighestState(machine)]['meta_data']['accept_state'] = True

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
				'+': orOneOrMoreHandler,
				'*': zeroOneOrMoreHandler,
			}
		},
		'[': {
			'func': setHandler,
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

# regexString = r'(z(a|b|c))' # Works
# regexString = r'(z(y|(a|b|c)))'

# regexString = r'(a|b)+' # Works
# regexString = r'(z|(a|b|c)+)+'
#regexString = r'(a|b)(c|d)'
#regexString = r'(a|b)'
#regexString = r'(a|b)(c|d)'

regexString = r'(ab|cd)e'
regexString = r'(ab|cd)+(ef|gh)+'
regexString = r'(ab|cd)*(ef|gh)*'

stateCount = 1

finalMachine, stateCount = regexToFsm(regexString, scDict, stateCount)

print('Final Machine'.center(50))
pprint(finalMachine)
