
class Variable():
	def __init__(self, identifier: str) -> None:
		self.identifier = identifier

class Operator():
	def __init__(self, identifier: str, operatorDict: dict=None, precedence: int=None, associativity: str=None, operandNum: int=None) -> None:
		self.identifier = identifier

		
		if operatorDict is not None:
			self.attrFromDict(operatorDict)
		else:
			self.setPrecedence(precedence)
			self.setAssociativity(associativity)
			self.setOperandNum(operandNum)

	def setPrecedence(self, newPrecedence):
		self.precedence = newPrecedence
	
	def setAssociativity(self, newAssociativity):
		self.associativity = newAssociativity

	def setOperandNum(self, newOperandNum):
		self.operandNum = newOperandNum
	
	def attrFromDict(self, operatorDict: dict) -> None:
		expectedDictFuncs = {
			'precedence' : self.setPrecedence,
			'associativity' : self.setAssociativity,
			'operandNum' : self.setOperandNum
		}
		

		for key in expectedDictFuncs:
			if key in operatorDict:
				expectedDictFuncs[key](operatorDict[key])
			else:
				expectedDictFuncs[key](None)

class TreeNode():
	def __init__(self) -> None:
		pass


class OperatorTreeNode(TreeNode):
	"""
	A class which represents an operator in
	a tree representing a boolean expression.
	"""

	def __init__(self, operator: Operator) -> None:
		super().__init__()

		self.operator = operator


class OneOperandTreeNode(OperatorTreeNode):
	def __init__(self, operator: Operator, child: TreeNode) -> None:
		super().__init__(operator)

		self.child = child
	
	def setChild(self, newChild: TreeNode):
		self.child = newChild
	
	def removeChild(self):
		self.child = None


class TwoOperandTreeNode(OperatorTreeNode):
	def __init__(self, operator: Operator, lChild: TreeNode, rChild: TreeNode) -> None:
		super().__init__(operator)

		self.lChild = lChild
		self.rChild = rChild
	

	def setLeftChild(self, newLeftChild: TreeNode):
		self.lChild = newLeftChild
	

	def setRightChild(self, newRightChild: TreeNode):
		self.rChild = newRightChild
	

	def removeChildren(self):
		self.lChild = None
		self.rChild = None


class VariableTreeNode(TreeNode):
	def __init__(self, variableName: str) -> None:
		super().__init__()

		variableName = variableName




