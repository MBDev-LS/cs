
class Node():
    def __init__(self, value: str, branches: list=None) -> None:
        self.branches = branches if branches is not None else []
        self.operator = value
        self.leaf = False if branches is not None else True
    
    def addBranch(self, newChild: str) -> int:
        self.branches.append(newChild)
        self.leaf = False

    def setOperator(self, newValue: str) -> int:
        self.value = newValue


operatorsDict = {
	'~': {'precedence': 4, 'operandCount': 1},
	'.': {'precedence': 3, 'operandCount': 2},
	'+': {'precedence': 2, 'operandCount': 2},
}

postFixInputString = 'A B + ~ C D + .'
postFixInputList = postFixInputString.split(' ')
postFixInputList.reverse()

foundOperator = False
currentParent = Node('START PLACEHOLDER')

for i, char in enumerate(postFixInputList):
    if char not in operatorsDict:
        currentParent.addBranch(Node(char))
    else:
        if foundOperator is False:
            currentParent.setOperator(char)
            continue
        
        newNode = Node(char)
        currentParent.addBranch(newNode)
        currentParent = newNode

# This approach is stupid, use the reverse bit and ditch the rest. Then use a recursive approach to create trees with the correct number of operands after operators 
