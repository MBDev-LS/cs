
operatorList = {
	'^': {'precedence': 4, 'associativity': 'right'},
	'*': {'precedence': 3, 'associativity': 'left'},
	'÷': {'precedence': 3, 'associativity': 'left'},
	'+': {'precedence': 2, 'associativity': 'left'},
	'-': {'precedence': 2, 'associativity': 'left'},
}

inputString = '1*2^4+24+(1-48)+100'

intStack = []
resultQueue = []

for i, char in enumerate(inputString):
	if char.isdigit() is True:
		intStack.append(char)
	else:
		fullNum = intStack
		intStack = []

		if len(fullNum) > 0:
			resultQueue.append(''.join(fullNum))
		
		resultQueue.append(char)

resultQueue.append(''.join(intStack))

inputString = resultQueue
outputQueue = []
operatorStack = []

for i, char in enumerate(inputString):
	if char.isdigit() is True:
		outputQueue.append(char)
	elif char in operatorList:
		if len(operatorStack) != 0:
			while operatorStack[-1] != '(' and (operatorList[operatorStack[-1]]['precedence'] > operatorList[char]['precedence'] or (operatorList[operatorStack[-1]]['precedence'] == operatorList[char]['precedence'] and operatorList[char]['associativity'] == 'left')):
				outputQueue.append(operatorStack.pop())

				if len(operatorStack) == 0:
					break
		
		operatorStack.append(char)
	elif char == '(':
		operatorStack.append(char)
	elif char == ')':
		while operatorStack[-1] != '(':
			if len(operatorStack) == 0:
				print(f'Failed: Character {i} is a missmatched closing bracket.')
				exit()
			
			outputQueue.append(operatorStack.pop())
		
		operatorStack.pop()

while len(operatorStack) > 0:
	if operatorStack[-1] == '(':
		print(f'Failed: Missmatched opening bracket.')
		exit()
	
	outputQueue.append(operatorStack.pop())

print(' '.join(outputQueue))
