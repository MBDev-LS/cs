class Node():
	def __init__(self, value, index) -> None:
		self.value = value
		self.index = index
		self.nextNode = None

class Queue:
	def __init__(self):
		self.__startNode = None

	def addValue(self, value):
		if self.startNode == None:
			newNode = Node(value, 0)
		else:
			currentNode = self.__startNode
			while not currentNode.nextNode == None:
				currentNode = currentNode.nextNode
			newNode = Node(value, currentNode.index + 1)
			currentNode.nextNode = newNode

	def displayQueue(self):
		currentNode = self.startNode
		while currentNode != None:
			print("Node: " + str(currentNode.index + 1) + ":")
			print("Value: " + str(currentNode.value))
			print("Index: " + str(currentNode.index))
			print()
			current = current.nextNode


queue = Queue()
queue.addValue(1)
queue.addValue(4)
queue.addValue(2)
queue.addValue(8)
queue.addValue(7)
queue.displayQueue
input()