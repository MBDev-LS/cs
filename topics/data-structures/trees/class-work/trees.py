
import tabulate

class BinaryNode():
	def __init__(self, value, lChild=None, rChild=None) -> None:
		self.value = value
		self.lChild = lChild
		self.rChild = rChild
	
	def __str__(self) -> str:
		return str(self.value)

class BinaryTree():
	def __init__(self, rootNode: BinaryNode=None) -> None:
		self.rootNode = rootNode
	
	def addNode(self, nodeValue: int, baseNode: BinaryNode=None):
		if self.rootNode is None:
			self.rootNode = BinaryNode(nodeValue)
			return
		
		baseNode = baseNode if baseNode is not None else self.rootNode
		if nodeValue < baseNode.value:
			if baseNode.lChild is None:
				baseNode.lChild = BinaryNode(nodeValue)
				return
			
			self.addNode(nodeValue, baseNode.lChild)
		elif nodeValue > baseNode.value:
			if baseNode.rChild is None:
				baseNode.rChild = BinaryNode(nodeValue)
				return
			
			self.addNode(nodeValue, baseNode.rChild)
		else:
			return

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

	def getNodeList(self, baseNode: BinaryNode, nodeList: list=None):
		baseNode = baseNode if baseNode is not None else self.rootNode
		nodeList = [baseNode]

		if baseNode.lChild is not None:
			nodeList += self.getNodeList(baseNode.lChild)
		

		if baseNode.rChild is not None:
			nodeList += self.getNodeList(baseNode.rChild)
	
		return nodeList


	def displayAdjacencyTable(self, baseNode: BinaryNode=None):
		baseNode = baseNode if baseNode is not None else self.rootNode

		tableList = []

		for node in self.getNodeList(baseNode):
			lValue = str(node.lChild.value) if node.lChild is not None else ''
			rValue = str(node.rChild.value) if node.rChild is not None else ''
			tableList.append([str(node.value), lValue, rValue])
		
		print(tabulate.tabulate(tableList, headers=['Node', 'Left Child', 'Right Child'], tablefmt='fancy_grid'))


tree = BinaryTree()
tree.addNode(4)
tree.addNode(2)
print(tree.getDepth())

tree.displayAdjacencyTable()

