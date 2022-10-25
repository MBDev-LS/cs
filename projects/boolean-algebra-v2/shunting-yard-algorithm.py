
# Explanation of the algorithm: https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Explanation of precedence & associativity: https://youtu.be/SKj-s6chzkM


OPERATOR_DICT = {
	'~': {
		'precedence': 3,
		'associativity': 'right',
		'operandNum': 2
	},
	'.': {
		'precedence': 2,
		'associativity': 'left',
		'operandNum': 2
	},
	'+': {
		'precedence': 1,
		'associativity': 'left',
		'operandNum': 2
	}
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
	outputList = []
	operatorStack = []

	for chars in inputList:
		print(f'''
input: {" ".join(inputList)}

Current Char: {chars}
outputList: {outputList}
operatorStack: {operatorStack}
''')

		if chars not in OPERATOR_DICT and chars not in ['(', ')']:
			outputList.append(chars)
		elif chars in OPERATOR_DICT:
			if len(operatorStack) > 0:
				while operatorStack[-1]	!= '(' and (OPERATOR_DICT[operatorStack[-1]]['precedence'] > OPERATOR_DICT[chars]['precedence']
				or (OPERATOR_DICT[operatorStack[-1]]['precedence'] == OPERATOR_DICT[chars]['precedence'] and OPERATOR_DICT[chars]['associativity'] == 'left')):
					outputList.append(operatorStack.pop())

					if len(operatorStack) == 0:
						break
			
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

print(infix_to_rpn('~ (~A + B.C)'))