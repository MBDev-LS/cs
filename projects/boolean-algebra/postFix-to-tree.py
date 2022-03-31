
class Node():
	def __init__(self, value: str, branches: list=None) -> None:
		self.branches = branches if branches is not None else []
		self.value = value
		self.leaf = False if branches is not None else True
	
	def addBranch(self, newChild: str) -> int:
		self.branches.append(newChild)
		self.leaf = False
	
	def addBranches(self, newChildren: list) -> int:
		self.branches += newChildren
		self.leaf = False

	def setValue(self, newValue: str) -> int:
		self.value = newValue


operatorsDict = {
	'~': {'precedence': 4, 'operandCount': 1},
	'.': {'precedence': 3, 'operandCount': 2},
	'+': {'precedence': 2, 'operandCount': 2},
}

postFixInputString = 'A B + ~ C D + .'

postFixInputList = postFixInputString.split(' ')
postFixInputList.reverse()

variables = [char for char in postFixInputList if char not in list(operatorsDict.keys()) + ['(', ')']]

foundOperator = False
currentParent = Node('START PLACEHOLDER')

for i, char in enumerate(postFixInputList):
	if char not in operatorsDict:
		currentParent.addBranch(Node(char))
	else:
		if foundOperator is False:
			currentParent.setValue(char)
			continue
		
		newNode = Node(char)
		currentParent.addBranch(newNode)
		currentParent = newNode

def getOperands(postFixListReversed: list, operandCount: int, operatorsDict: dict,  variables: list):
	resList = []
	operandAddedCount = 0
	skipCount = 0
	for i, char in enumerate(postFixListReversed):
		if skipCount > 0:
			skipCount -= 1
			continue
		
		if char in variables:
			resList.append(char)
		else:
			extentionList = getOperands(postFixListReversed[i+1:], operatorsDict[char]['operandCount'], operatorsDict, variables)
			skipCount = len(extentionList)
			resList += extentionList
		
		operandAddedCount += 1
		if operandAddedCount == operandCount:
			break
	
	return resList

def findTreeForPostFixString(postFixInputList, operatorsDict: dict, variables: list, currentParent: Node=None):
	currentParent = currentParent if currentParent is not None else Node('START PLACEHOLDER')
	baseNode = currentParent

	for i, char in enumerate(postFixInputList):
		if char not in operatorsDict:
			currentParent.addBranch(Node(char))
		else:
			if currentParent.value == 'START PLACEHOLDER':
				currentParent.setValue(char)
			else:
				newNode = Node(char)
				currentParent.addBranch(newNode)

			currentParent = findTreeForPostFixString(getOperands(postFixInputList[i:], operatorsDict[char]['operandCount'], operatorsDict,  variables), operatorsDict,  variables, currentParent)

	return baseNode

result = findTreeForPostFixString(postFixInputList, operatorsDict, variables)

# This approach is stupid, use the reverse bit and ditch the rest. Then use a recursive approach to create trees with the correct number of operands after operators 

print()