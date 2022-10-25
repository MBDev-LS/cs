
from infix_to_postfix import infix_to_rpn
from classes import Operator, Variable, TreeNode, OneOperandTreeNode, TwoOperandTreeNode, VariableTreeNode

def postfix_to_tree(postfixList: list) -> TreeNode:
	treeStack = []

	for token in postfixList:
		if isinstance(token, Variable):
			treeStack.append(VariableTreeNode(token.identifier))
		elif isinstance(token, Operator):
			if token.operandNum == 1:
				newOperatorNode = OneOperandTreeNode(token, treeStack.pop())

			elif token.operandNum == 2:
				rightChild = treeStack.pop()
				leftChild = treeStack.pop()
				newOperatorNode = TwoOperandTreeNode(token, leftChild, rightChild)

			treeStack.append(newOperatorNode)
	
	return treeStack.pop()


if __name__ == '__main__':
	oopPostfix = infix_to_rpn('((M+N).(Z.C)).~~(D+A)')
	booleanExprTree = postfix_to_tree(oopPostfix)

	print(booleanExprTree)

