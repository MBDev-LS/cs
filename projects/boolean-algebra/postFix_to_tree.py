
class Node():
	def __init__(self, value: str, leftChild=None, rightChild=None) -> None:
		self.value = value

		self.leftChild = leftChild
		self.rightChild = rightChild
		self.leaf = False if leftChild is None and rightChild is None else True
		self.graphId = ''
	
	def setLeftChild(self, newLeftChild: list) -> int:
		self.leftChild = newLeftChild
		self.leaf = False
	
	def setRightChild(self, newRightChild: list) -> int:
		self.rightChild = newRightChild
		self.leaf = False

	def setValue(self, newValue: str) -> int:
		self.value = newValue
	
	def checkIfLeaf(self) -> bool:
		self.leaf = True if self.leftChild is None and self.rightChild is None else False
		return self.leaf

	def printDescendants(self):
		print(f'{self.value}'.center(50))
		print(f'/ \\'.center(50))
		print(f'{self.leftChild}    {self.rightChild}'.center(50))

	def setGraphId(self, graphId: str):
		self.graphId = graphId
	
	def __str__(self) -> str:
		return self.value



operatorsDict = {
	'~': {'precedence': 4, 'operandCount': 1},
	'.': {'precedence': 3, 'operandCount': 2},
	'+': {'precedence': 2, 'operandCount': 2},
}

postFixInputString = 'A B + C D + .'
postFixInputString = 'A B + ~ C D + .'

postFixInputList = postFixInputString.split(' ')
postFixInputList.reverse()


variables = [char for char in postFixInputList if char not in list(operatorsDict.keys()) + ['(', ')']]

foundOperator = False
currentParent = Node('START PLACEHOLDER')

def getOperands(postFixListReversed: list, operandCount: int, operatorsDict: dict,  variables: list, topLevel=True) -> list:
	resList = []
	operandAddedCount = 0
	skipCount = 0
	for i, char in enumerate(postFixListReversed):
		if skipCount > 0:
			skipCount -= 1
			continue
		
		if char in variables:
			resList.append([char] if topLevel is True else char)
		else:
			extentionList = getOperands(postFixListReversed[i+1:], operatorsDict[char]['operandCount'], operatorsDict, variables, False)
			skipCount = len(extentionList)
			extentionList.insert(0, char)
			if topLevel is True:
				resList.append(extentionList)
			else:
				resList += extentionList
		
		operandAddedCount += 1
		if operandAddedCount == operandCount:
			break

	newResList = []
	for lst in resList:
		if len(lst) == 1:
			newResList.append(lst[0])
		else:
			newResList.append(lst)

	resList = [sublist for sublist in resList ]
	
	return newResList

def addTwoChildren(baseNode: Node, lChild: str, rChild: str, operatorsDict: dict, variables: list):
	if lChild is not None:
		if lChild not in variables:
			operands = getOperands(lChild[1:], operatorsDict[lChild[0]]['operandCount'], operatorsDict,  variables)
			leftLeft = operands[0]
			leftRight = operands[1] if len(operands) > 1 else None
			lNode = Node(lChild[0])
			lNode = addTwoChildren(lNode, leftLeft, leftRight, operatorsDict, variables)
			
		else:
			lNode = Node(lChild)
		
		baseNode.setLeftChild(lNode)

	if rChild is not None:
		if rChild not in variables:
			operands = getOperands(rChild[1:], operatorsDict[rChild[0]]['operandCount'], operatorsDict,  variables)
			
			rightLeft = operands[0]
			rightRight = operands[1] if len(operands) > 1 else None
			rNode = Node(rChild[0])
			rNode = addTwoChildren(rNode, rightLeft, rightRight, operatorsDict, variables)
			
		else:
			rNode = Node(rChild)

		
		baseNode.setRightChild(rNode)

	return baseNode

def findTreeForPostFixString(postFixInputList, operatorsDict: dict, variables: list, currentParent: Node=None):
	currentParent = currentParent if currentParent is not None else Node('START PLACEHOLDER')
	baseNode = currentParent

	if currentParent.value == 'START PLACEHOLDER':
		currentParent.setValue(postFixInputList[0])

	left = getOperands(postFixInputList[1:], operatorsDict[postFixInputList[0]]['operandCount'], operatorsDict,  variables)[0]
	right = getOperands(postFixInputList[1:], operatorsDict[postFixInputList[0]]['operandCount'], operatorsDict,  variables)[1]
	currentParent = addTwoChildren(currentParent, left, right, operatorsDict, variables)


	return baseNode

def checkTreeLeaves(topNode: Node):
	topNode.checkIfLeaf()
	topNode.leftChild = checkTreeLeaves(topNode.leftChild) if topNode.leftChild is not None else None
	topNode.rightChild = checkTreeLeaves(topNode.rightChild) if topNode.rightChild is not None else None

	return topNode

def postfixToTree(postFixInputString):
	postFixInputList = postFixInputString.split(' ')
	postFixInputList.reverse()


	variables = [char for char in postFixInputList if char not in list(operatorsDict.keys()) + ['(', ')']]

	result = findTreeForPostFixString(postFixInputList, operatorsDict, variables)

	result = checkTreeLeaves(result)
	# displayTree(result, 1)
	# tempDisplayTree(result)

	return result

def tempDisplayTree(topNode: Node):
	topNode.printDescendants()

	if topNode.leftChild is not None:
		tempDisplayTree(topNode.leftChild)
	if topNode.rightChild is not None:
		tempDisplayTree(topNode.rightChild)

	return topNode

# def displayTree(topNode: Node, depth: int, side: str=None):
# 	if depth == 1:
# 		print(f'{topNode.value}'.center(50))
# 	else:
# 		print(f'{(depth+1)*" " if side == "r" else ""}{topNode.value}{(depth+1)*" " if side == "l" else ""}'.center(50))
	
# 	isLeft = True if topNode.leftChild is not None else False
# 	isRight = True if topNode.rightChild is not None else False
# 	print('{} {}'.format("/" if isLeft is True else " ", "\\" if isRight is True else " ").center(50))

# 	if isLeft is True:
# 		displayTree(topNode.leftChild, depth+1, 'l')
	
# 	if isRight is True:
# 		displayTree(topNode.rightChild, depth+1, 'r')


postfixToTree('A B + ~ C D + .')