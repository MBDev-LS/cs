
class BinaryNode():
	def __init__(self, value, lChild=None, rChild=None) -> None:
		self.value = value
		self.lChild = lChild
		self.rChild = rChild

	def __str__(self) -> str:
		return str(self.value)

class BinaryTree():
	def __init__(self, rootNode: BinaryNode) -> None:
		self.rootNode = rootNode
	
	def getDepth(self, node=None, depth=0):
		depth += 1
		node = node if node is not None else self.rootNode

		if node.lChild is not None:
			lRes = self.getDepth(node.lChild, depth)
		
		if node.rChild is not None:
			rRes = self.getDepth(node.rChild, depth)
		
		if node.lChild is None and node.rChild is None:
			return depth

		if node.lChild is None:
			return rRes
		if node.rChild is None:
			return lRes
		else:
			return max(lRes, rRes)

	def print(self) -> None:
		pass

rootNode = BinaryNode()
tree = BinaryTree()

