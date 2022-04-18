
class Node():
	def __init__(self, data, pointingTo=None) -> None:
		self.data = data
		self.next = pointingTo

class List():
	def __init__(self, head: Node=None) -> None:
		self.head = head
	
	def isEmpty(self) -> bool:
		return True if self.head is None else False
	
	def append(self, item) -> None:
		currentNode = self.head

		if currentNode is None:
			self.head = Node(item)
			return

		while currentNode.next != None:
			currentNode = currentNode.next
		
		currentNode.next = Node(item)

	def pop(self, pos=None):
		currentNode = self.head

		if pos is None:
			if currentNode is None:
				raise IndexError('pop from empty list')
			elif currentNode.next is None:
				returningData = currentNode.data
				self.head = None
				return returningData
			

			while currentNode.next != None:
				if currentNode.next.next is None:
					break

				currentNode = currentNode.next
			
			returningData = currentNode.next.data
			currentNode.next = None

			return returningData

		if currentNode is None:
			raise IndexError('pop from empty list')
		elif pos == 0:
			returningData = self.head.data
			self.head = currentNode.next
			return returningData

		
		for i in range(pos-1):
			if currentNode.next is None:
				raise IndexError('pop index out of range')
			
			currentNode = currentNode.next
		
		currentNode.next = currentNode.next.next

	def remove(self, item):
		currentNode = self.head
		index = 0
		while currentNode != None:
			if currentNode.data == item:
				self.pop(index)
				return

			currentNode = currentNode.next
			index += 1
	
	def search(self, item):
		currentNode = self.head
		while currentNode != None:
			if currentNode.data == item:
				return True

			currentNode = currentNode.next
		
		return False

	def search(self, item):
		currentNode = self.head
		index = 0
		while currentNode != None:
			if currentNode.data == item:
				return index

			currentNode = currentNode.next
			index += 1
		
		raise ValueError(f'{item} not in list')
	
	def insert(self, pos, item) -> None:
		currentNode = self.head

		if currentNode is None:
			self.head = Node(item)
			return

		for i in range(pos-1):
			if currentNode.next is None:
				break
			currentNode = currentNode.next
		
		newNode = Node(item, currentNode.next)
		currentNode.next = newNode
	
	def __str__(self) -> str:
		currentNode = self.head
		outputStr = '['

		while currentNode is not None:
			outputStr += str(currentNode.data)
			outputStr += ', ' if currentNode.next is not None else ''
			currentNode = currentNode.next
		
		outputStr += ']'


		return outputStr

def length(lst: List) -> int:
	lstLength = 0
	currentNode = lst.head

	while currentNode != None:
		currentNode = currentNode.next
		lstLength += 1
	
	return lstLength


baseNode = Node(1)
lst = List(baseNode)


print('\n'+'Test 1'.center(24, '='))

print(length(lst), lst)
lst.append(2)
print(length(lst), lst)
print(lst.pop())
print(length(lst), lst)
print(lst.pop())
print(length(lst), lst)



print('\n'+'Test 2'.center(24, '='))

print(length(lst), lst)
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(length(lst), lst)
lst.pop(1)
print(length(lst), lst)
lst.pop(0)
print(length(lst), lst)
lst.pop(2)
print(length(lst), lst)
lst.pop()
lst.pop()
print(length(lst), lst)



print('\n'+'Test 3'.center(24, '='))
print(length(lst), lst)
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(length(lst), lst)
lst.remove(1)
print(length(lst), lst)
lst.remove(4)
print(length(lst), lst)
lst.remove(5)
print(length(lst), lst)



print('\n'+'Test 4'.center(24, '='))
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(length(lst), lst)

try:
	print(lst.search('01189998819991197253'))
except ValueError as e:
	print('Caught Error:')
	print(f'ValueError: {e}')

try:
	print(lst.search(7))
except ValueError as e:
	print('Caught Error:')
	print(f'ValueError: {e}')

print(lst.search(1))
print(lst.search(3))
print(lst.search(5))



print('\n'+'Test 5'.center(24, '='))
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(length(lst), lst)
lst.insert(0, 7)
print(length(lst), lst)
lst.pop(1)
print(length(lst), lst)
lst.insert(2, 7)
print(length(lst), lst)
lst.pop(2)
print(length(lst), lst)
lst.insert(5, 7)
print(length(lst), lst)


