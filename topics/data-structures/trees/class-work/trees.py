
import tabulate

class BinaryNode():
	def __init__(self, value, lChild=None, rChild=None) -> None:
		self.value = value
		self.lChild = lChild
		self.rChild = rChild
	
	def numberOfChildren(self):
		if self.lChild is None and self.rChild is None:
			return 0
		elif self.lChild is None or self.rChild is None:
			return 1
		else:
			return 2

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

	def search(self, searchValue: int, baseNode: BinaryNode=None):
		baseNode = baseNode if baseNode is not None else self.rootNode

		if baseNode is None:
			return None
		elif baseNode.value == searchValue:
			return self.rootNode

		if searchValue < baseNode.value:
			if baseNode.lChild is None:
				return None
			elif searchValue == baseNode.lChild.value:
				return baseNode.lChild
			
			return self.search(searchValue, baseNode.lChild)

		elif searchValue > baseNode.value:
			if baseNode.rChild is None:
				baseNode.rChild = BinaryNode(searchValue)
				return None
			elif searchValue == baseNode.rChild.value:
				return baseNode.lChild
			
			return self.search(searchValue, baseNode.rChild)
		else:
			return

	def findParentOfNode(self, searchValue: int, baseNode: BinaryNode=None):
		baseNode = baseNode if baseNode is not None else self.rootNode

		if baseNode is None:
			return None
		elif baseNode.value == searchValue:
			return self.rootNode
		
		

		if searchValue < baseNode.value:
			if baseNode.lChild is None:
				return None
			elif searchValue == baseNode.lChild.value:
				return baseNode
			
			return self.search(searchValue, baseNode.lChild)

		elif searchValue > baseNode.value:
			if baseNode.rChild is None:
				baseNode.rChild = BinaryNode(searchValue)
				return None
			elif searchValue == baseNode.rChild.value:
				return baseNode
			
			return self.search(searchValue, baseNode.rChild)
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

	def search(self, searchValue: int, baseNode: BinaryNode=None):
		baseNode = baseNode if baseNode is not None else self.rootNode

		if baseNode is None:
			return None
		elif baseNode.value == searchValue:
			return self.rootNode

		if searchValue < baseNode.value:
			if baseNode.lChild is None:
				return None
			elif searchValue == baseNode.lChild.value:
				return baseNode.lChild
			
			return self.search(searchValue, baseNode.lChild)

		elif searchValue > baseNode.value:
			if baseNode.rChild is None:
				baseNode.rChild = BinaryNode(searchValue)
				return None
			elif searchValue == baseNode.rChild.value:
				return baseNode.lChild
			
			return self.search(searchValue, baseNode.rChild)
		else:
			return


	def delete(self, value: int, baseNode: BinaryNode=None):
		nodeToDelete = self.search(value)

		if nodeToDelete is None:
			return
		
		nodeToDeletesParent = self.findParentOfNode(nodeToDelete.value)

		if nodeToDelete.numberOfChildren() == 0:
			if nodeToDelete.value < nodeToDeletesParent.value:
				nodeToDeletesParent.lChild = None
			elif nodeToDelete.value > nodeToDeletesParent.value:
					nodeToDeletesParent.rChild = None
		elif nodeToDelete.numberOfChildren() == 1:
			childValue = nodeToDelete.lChild.value if nodeToDelete.lChild.value is not None else nodeToDelete.rChild.value

			nodeToDelete.value = childValue
			nodeToDelete.lChild, nodeToDelete.rChild = None, None
		elif nodeToDelete.numberOfChildren() == 2:
			rightSubTreeMin = self.search(min(self.getNodeList(nodeToDelete.rChild)))
			
			nodeToDelete.value = rightSubTreeMin
			self.delete(rightSubTreeMin)



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
tree.addNode(1)

print(tree.getDepth())

tree.displayAdjacencyTable()

searchedNode4 = tree.search(4)
searchedNode2 = tree.search(2)

searchedNoneNode = tree.search(1)

print(searchedNode4, searchedNode2, searchedNoneNode)

tree.delete(1)

searchedNoneNode = tree.search(1)

print(searchedNode4, searchedNode2, searchedNoneNode)

