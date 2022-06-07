
operatorList = { # That's a dict you idiot, change this when you have time
	'~': {'precedence': 4, 'associativity': 'right'},
	'.': {'precedence': 3, 'associativity': 'left'},
	'+': {'precedence': 2, 'associativity': 'left'},
}

inputString = '(A+B).(C+D)'

# inputString = 'A.B+C.D'
# inputString = 'A+B.C+D'
inputString = '~(A+B).(C+D)'

variables = [char for char in inputString if char not in list(operatorList.keys()) + ['(', ')']]

intQueue = []
resultQueue = []

for i, char in enumerate(inputString):
	if char in variables:
		intQueue.append(char)
	else:
		fullNum = intQueue
		intQueue = []

		if len(fullNum) > 0:
			resultQueue.append(''.join(fullNum))
		
		resultQueue.append(char)

if len(intQueue) > 0:
	resultQueue.append(''.join(intQueue))

inputString = resultQueue
outputQueue = []
operatorStack = []

for i, char in enumerate(inputString):
	if char in variables:
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


"A+B*C+D"