
class List():
	def __init__(self, length: int) -> None:
		self.lst = [None for i in range(length)]
		self.maxLength = length
		self.frontPointer = 0
		self.rearPointer = -1
	
	def isEmpty(self) -> bool:
		return True if len(set(self.lst)) - 1 == 0 else False
	
	# Don't know if this is required, not in the specification in the textbook.
	def isFull(self) -> bool:
		return True if self.lst.count(None) == 0 else False
	
	def append(self, item) -> None:
		if item is None:
			print('NoneType as item not supported.')
		
		if self.isFull() is not True:
			self.rearPointer += 1
			self.lst[self.rearPointer] = item
		else:
			print(f'Unable to append item \'{item}\' as list is full')

	def pop(self, pos=None):
		pos = self.rearPointer if pos is None else pos
		poppedItem = self.lst[self.rearPointer]
		self.lst[self.rearPointer] = None

		for j in range(pos, len(self.lst)):
			if j+1 < len(self.lst):
				self.lst[j] = self.lst[j+1]
			else:
				self.lst[j] = None
		
		self.rearPointer -= 1

		return poppedItem

	def remove(self, item):
		for i, item2 in enumerate(self.lst):
			if item == item2:
				for j in range(i, len(self.lst)):
					if j+1 < len(self.lst):
						self.lst[j] = self.lst[j+1]
					else:
						self.lst[j] = None
				
				self.rearPointer -= 1

				return
	
	def search(self, item):
		return item in self.lst[self.frontPointer, self.rearPointer+1]
	
	def insert(self, pos, item) -> None:
		if lst.isFull is True:
			print(f"Unable to insert item '{item}' as list is full")
		
		for i in range(len(self.lst)-1, pos-1, -1):
			if i-1 >= 0:
				self.lst[i] = self.lst[i-1]
			else:
				self.lst[i] = None
		
		self.rearPointer += 1

		self.lst[pos] = item
	
	def length(self):
		return len(set(self.lst)) - 1
	
	def __str__(self) -> str:
		return str(self.lst)

def logList(lst: List) -> None:
	print(lst.length(), lst.isEmpty(), lst.isFull(), lst)

lst = List(4)
logList(lst)


lst.append(1)

lst.append(3)


lst.insert(1, 2)


logList(lst)

