
# Explanation of the algorithm: https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Explanation of precedence & associativity: https://youtu.be/SKj-s6chzkM

# At the splitting stage, oop the variables and operators

from classes import Operator, Variable, Bracket
from utilities import printLog

OPERATOR_DICT = {
	'~': {
		'precedence': 3,
		'associativity': 'right',
		'operandNum': 1
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

def checkForBracket(bracketTextToCheckFor: str, obj: Bracket) -> bool:
	if isinstance(obj, Bracket):
		return (bracketTextToCheckFor == '(' and obj.bracketType == 'opening') or (bracketTextToCheckFor == ')' and obj.bracketType == 'closing')
	else:
		return False

def split_into_components(inputStr: str) -> list:
	inputStr = inputStr.replace(' ', '')
	holdingList = []
	outputList = []

	for char in inputStr:
		if char in OPERATOR_DICT or char in ['(', ')']:
			if len(holdingList) > 0:
				outputList.append(Variable(''.join(holdingList)))
			holdingList = []

			if char in OPERATOR_DICT: 
				newObj = Operator(char)
				newObj.attrFromDict(OPERATOR_DICT[char])
			else:
				newObj = Bracket('opening' if char == '(' else 'closing')
			
			outputList.append(newObj)
		else:
			holdingList.append(char)
	
	if len(holdingList) > 0:
		outputList.append(Variable(''.join(holdingList)))
	
	return outputList

def infix_to_rpn(inputStr: str) -> str:
	inputList = split_into_components(inputStr)
	outputList = []
	operatorStack = []

	for token in inputList:
		print(f'''
input: {" ".join([str(item) for item in inputList])}

Current Char: {token}
outputList: {[str(item) for item in outputList]}
operatorStack: {[str(item) for item in operatorStack]}
''')

		if isinstance(token, Variable):
			outputList.append(token)
		elif isinstance(token, Operator):
			if len(operatorStack) > 0:
				while not checkForBracket('(', operatorStack[-1]) and (operatorStack[-1].precedence > token.precedence
				or (operatorStack[-1].precedence == token.precedence and token.associativity == 'left')):
					outputList.append(operatorStack.pop())

					if len(operatorStack) == 0:
						break
			
			operatorStack.append(token)
		elif checkForBracket('(', token):
			operatorStack.append(token)
		elif checkForBracket(')', token):
			if len(operatorStack) > 0:
				while not checkForBracket('(', operatorStack[-1]):
					outputList.append(operatorStack.pop())

				if checkForBracket('(', operatorStack[-1]):
					operatorStack.pop()
	
	while len(operatorStack) > 0:
		if operatorStack[-1] == '(':
			printLog('error', 'Mismatched brackets', True)
		
		outputList.append(operatorStack.pop())
	
	return outputList

if __name__ == '__main__':
	result = infix_to_rpn('A + B')

	print(result)
	print(' '.join([str(item) for item in result]))

