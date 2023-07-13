
# Explanation of the algorithm: https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Explanation of precedence & associativity: https://youtu.be/SKj-s6chzkM


OPERATOR_DICT = {
	'^': {
		'precedence': 4,
		'associativity': 'r',
		'operandNum': 2
	},
	'*': {
		'precedence': 3,
		'associativity': 'l',
		'operandNum': 2
	},
	'/': {
		'precedence': 3,
		'associativity': 'l',
		'operandNum': 2
	},
	'+': {
		'precedence': 2,
		'associativity': 'l',
		'operandNum': 2
	},
	'-': {
		'precedence': 2,
		'associativity': 'l',
		'operandNum': 2
	},
	'~': {
		'precedence': 2,
		'associativity': 'r',
		'operandNum': 2
	}
	# This does not yet work. Speak to sir about it.
}

def split_into_components(inputStr: str) -> list:
	inputStr = inputStr.replace(' ', '')
	holdingList = []
	outputList = []

	for char in inputStr:
		if char in OPERATOR_DICT or char in ['(', ')']:
			if len(holdingList) > 0:
				outputList.append(''.join(holdingList))
			
			holdingList = []
			outputList.append(char)
		else:
			holdingList.append(char)
	
	if len(holdingList) > 0:
		outputList.append(''.join(holdingList))
	
	return outputList

def infix_to_rpn(inputStr: str) -> str:
	inputList = split_into_components(inputStr)
	print('H(IIIIIII', inputList)
	outputList = []
	operatorStack = []

	for chars in inputList:
		print(f'''
input: {" ".join(inputList)}

Current Char: {chars}
outputList: {outputList}
operatorStack: {operatorStack}
''')

		if chars.isdigit() is True:
			outputList.append(chars)
		elif chars in OPERATOR_DICT:
			if len(operatorStack) > 0:
				while operatorStack[-1]	!= '(' and (OPERATOR_DICT[operatorStack[-1]]['precedence'] > OPERATOR_DICT[chars]['precedence']
				or (OPERATOR_DICT[operatorStack[-1]]['precedence'] == OPERATOR_DICT[chars]['precedence'] and OPERATOR_DICT[chars]['associativity'] == 'l')):
					outputList.append(operatorStack.pop())
			
			operatorStack.append(chars)
		elif chars == '(':
			operatorStack.append(chars)
		elif chars == ')':
			if len(operatorStack) > 0:
				while operatorStack[-1]	!= '(':
					outputList.append(operatorStack.pop())

				if operatorStack[-1] == '(':
					operatorStack.pop()
	
	while len(operatorStack) > 0:
		if operatorStack[-1] == '(':
			print('Error: mismatched brackets')
		
		outputList.append(operatorStack.pop())
	
	return ' '.join(outputList)

print(infix_to_rpn('9 ~ c d - e / +'))