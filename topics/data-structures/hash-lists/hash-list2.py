
maxLength = 10
listmaxLength = int(maxLength*10)
hashList = [None for i in range(int(maxLength*10))]
modValue = int(maxLength*10)
rehashValue = 1
size = 0

def getIndex(item: int, modValue: int) -> int:#
	if type(item) == str:
		itemTotal = 0
		for char in item:
			itemTotal += ord(char)
		
		return itemTotal % modValue
	return item % modValue

def isFull(size: int, maxLength: int) -> bool:
	return size == maxLength

def isEmpty(size: list) -> bool:
	return size == 0

def insertItem(item: int, rehashValue: int, hashList: list, listmaxLength: int, size: int, modValue) -> list:
	if isFull(size, maxLength) is True:
		print(f'Unable to add item {item} to hash list as hash list is full.')
		return hashList, size

	indexToInsert = getIndex(item, modValue)

	if hashList[indexToInsert] is None:
		hashList[indexToInsert] = item
		
		return hashList, size + 1
	
	rehashedIndex = (indexToInsert + rehashValue) % listmaxLength

	while rehashedIndex != indexToInsert:
		if hashList[rehashedIndex] is None:
			hashList[rehashedIndex] = item
			
			return hashList, size + 1
		
		rehashedIndex = (rehashedIndex + 1) % listmaxLength
	
	print(f'Unable to add item {item} to hash list as hash list is full.')
	return hashList, size

def removeItem(item, hashList, listmaxLength, modValue, rehashValue, size):
	if isEmpty(size) is True:
		print('Unable to remove item as from hash list as hash list is empty.')
		return hashList, False, size
	
	indexToRemove = getIndex(item, modValue)

	if hashList[indexToRemove] == item:
		hashList[indexToRemove] = None
		
		return hashList, True, size - 1

	rehashedIndex = (indexToRemove + rehashValue) % listmaxLength
	
	while rehashedIndex != indexToRemove and hashList[rehashedIndex] is not None:
		if hashList[rehashedIndex] == item:
			hashList[rehashedIndex] = None
			
			return hashList, True, size - 1
		
		rehashedIndex = (rehashedIndex + 1) % listmaxLength
	
	print('Unable to remove item as from hash list as hash list .')
	return hashList, False, size



def logHashList(hashList: list, maxLength: int, size) -> None:
	print(size, isFull(size, maxLength), isEmpty(size), hashList)

logHashList(hashList, maxLength, size)
hashList, size = insertItem("One", rehashValue, hashList, listmaxLength, size, modValue)
logHashList(hashList, maxLength, size)
hashList, size = insertItem("Not One", rehashValue, hashList, listmaxLength, size, modValue)
logHashList(hashList, maxLength, size)
hashList, removed, size = removeItem("One", hashList, listmaxLength, modValue, rehashValue, size)
logHashList(hashList, maxLength, size)
hashList, removed, size = removeItem(21, hashList, listmaxLength, modValue, rehashValue, size)
hashList, removed, size = removeItem(1, hashList, listmaxLength, modValue, rehashValue, size)