
import tabulate
import tableslib

# Output is the ladt output

INPUTS = ['0', '1']

machine = { # This is an XOR gate
	'S0': {
		'startState': True,
		'transitions': {
			'0': {
				'nextState': 'S1',
				'output': '0'
			},
			'1': {
				'nextState': 'S2',
				'output': '0'
			},
		}
	},
	'S1': {
		'startState': False,
		'transitions': {
			'0': {
				'nextState': 'S1',
				'output': '0'
			},
			'1': {
				'nextState': 'S2',
				'output': '1'
			},
		}
	},
	'S2': {
		'startState': False,
		'transitions': {
			'0': {
				'nextState': 'S1',
				'output': '1'
			},
			'1': {
				'nextState': 'S2',
				'output': '0'
			},
		}
	}
}

def print_state_transition_table(machine: dict) -> None:
	tableList = []

	for state in machine:
		for transition in machine[state]['transitions']:
			tableList.append([state, transition, machine[state]['transitions'][transition]['nextState'], machine[state]['transitions'][transition]['output']])

	print(tabulate.tabulate(tableList, headers=["Current state","Input", "Next State", "Output"], tablefmt='fancy_grid'))

def get_possible_inputs(machine: dict) -> None:
	inputList = []

	for state in machine:
		inputList += machine[state]['transitions'].keys()
	
	return list(set(inputList))


def checkInputString(machine: dict, inputString: str) -> bool:
	possibleInputs = get_possible_inputs(machine)
	
	result = inputString

	for input in possibleInputs: # Getting difference
		result = result.replace(input, '')
	
	return len(result) == 0


def getStartState(machine: dict) -> str:
	for state in machine:
		if machine[state]['startState'] is True:
			return state


def print_state_sequence_table(machine: dict, inputString: str) -> None:
	if checkInputString(machine, inputString) is False:
		print('Invalid input string, halting.')
	
	currentState = getStartState(machine)

	sequenceTable = [[char] + [None for i in range(2)] for i, char in enumerate(inputString)]

	for i, char in enumerate(inputString):
		if char not in machine[currentState]['transitions']:
			print(f'No transition found for input \'{char}\' at state \'{currentState}\', machine is invalid (continuing).')
			exit()

		sequenceTable[i][1] = currentState
		sequenceTable[i][2] = machine[currentState]['transitions'][char]['output']

		print('')

		currentState = machine[currentState]['transitions'][char]['nextState']

	# print(tabulate.tabulate(sequenceTable, tablefmt='fancy_grid'))
	outputString = tableslib.lists_to_table(sequenceTable)
	return sequenceTable


print_state_transition_table(machine)
print(print_state_sequence_table(machine, '110010'))
