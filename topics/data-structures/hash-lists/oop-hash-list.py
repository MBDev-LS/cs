
class HashList():
	def __init__(self, maxLength: int, rehashValue: int=1) -> None:
		self.maxLength = maxLength
		self.hashList = [None for i in range(int(maxLength*10))]
		self.modValue = int(maxLength*10)
		self.rehashValue = rehashValue
		self.size = 0
	
	def getIndex(self, item) -> int:
		if type(item) == str:
			itemTotal = 0
			for char in item:
				itemTotal += ord(char)
			
			return itemTotal % self.modValue
		return item % self.modValue


	def isFull(self) -> bool:
		return self.size == self.maxLength

	def isEmpty(self) -> bool:
		return self.size == 0
	
	def insertItem(self, item) -> bool:
		if self.isFull() is True:
			print(f'Unable to add item {item} to hash list as hash list is full.')
			return False

		indexToInsert = self.getIndex(item)

		if self.hashList[indexToInsert] is None:
			self.hashList[indexToInsert] = item
			
			self.size += 1
			return True
		
		rehashedIndex = (indexToInsert + self.rehashValue) % self.modValue

		while rehashedIndex != indexToInsert:
			if self.hashList[rehashedIndex] is None:
				self.hashList[rehashedIndex] = item
				
				self.size += 1
				return True
			
			rehashedIndex = (rehashedIndex + 1) % self.modValue
		
		print(f'Unable to add item {item} to hash list as hash list is full.')
		return False

	def removeItem(self, item) -> bool:
		if self.isEmpty() is True:
			print('Unable to remove item as from hash list as hash list is empty.')
			return False
		
		indexToRemove = self.getIndex(item)

		if self.hashList[indexToRemove] == item:
			self.hashList[indexToRemove] = None
			
			self.size -= 1
			return True

		rehashedIndex = (indexToRemove + self.rehashValue) % self.modValue
		
		while rehashedIndex != indexToRemove and self.hashList[rehashedIndex] is not None:
			if self.hashList[rehashedIndex] == item:
				self.hashList[rehashedIndex] = None
				
				self.size -= 1
				return True
			
			rehashedIndex = (rehashedIndex + 1) % self.modValue
		
		print('Unable to remove item as from hash list as hash list .')
		return False
	
	def checkForItem(self, item) -> bool:
		indexToRemove = self.getIndex(item, self.modValue)

		if self.hashList[indexToRemove] == item:
			return True

		rehashedIndex = (indexToRemove + self.rehashValue) % self.modValue
		
		while rehashedIndex != indexToRemove and self.hashList[rehashedIndex] is not None:
			if self.hashList[rehashedIndex] == item:
				return True
			
			rehashedIndex = (rehashedIndex + 1) % self.modValue
		
		return False
	
	def __str__(self) -> str:
		return str(self.hashList)

lst = HashList(4)
print(lst.isEmpty(), lst.isFull(), lst)
lst.insertItem(7)
print(lst.isEmpty(), lst.isFull(), lst)
lst.insertItem(142)
lst.insertItem(789)
lst.insertItem(76723)
print(lst.isEmpty(), lst.isFull(), lst)
lst.insertItem(212)
print(lst.isEmpty(), lst.isFull(), lst)
lst.removeItem(7)
lst.removeItem(142)
lst.removeItem(789)
lst.removeItem(76723)
lst.removeItem(212)
lst.removeItem(1111)
print(lst.isEmpty(), lst.isFull(), lst)
