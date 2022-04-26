

length = 10
listLength = int(length*10)
hashList = [None for i in range(int(length*10))]
modValue = int(length*10)
rehashValue = 1

def getIndex(item: int, modValue: int) -> int:
	return item % modValue

def insertItem(item: int, rehashValue: int, hashList: list, listLength: int, modValue) -> hashList:
	indexToInsert = getIndex(item, modValue)

	if hashList[indexToInsert] is None:
		hashList[indexToInsert] = item
		
		return hashList
	
	rehashedIndex = (indexToInsert + rehashValue) % listLength

	while rehashedIndex != indexToInsert:
		if hashList[rehashedIndex] is None:
			hashList[rehashedIndex] = item
			
			return hashList
		
		rehashedIndex = (rehashedIndex + 1) % listLength
	
	print(f'Unable to add item {item} to hash list as hash list is full.')
	return hashList

def removeItem(item, hashList, listLength, modValue, rehashValue):
	indexToRemove = getIndex(item, modValue)

	if hashList[indexToRemove] == item:
		hashList[indexToRemove] = None
		
		return hashList, True

	rehashedIndex = (indexToRemove + rehashValue) % listLength
	
	while rehashedIndex != indexToRemove and hashList[rehashedIndex] is not None:
		if hashList[rehashedIndex] == item:
			hashList[rehashedIndex] = None
			
			return hashList, True
		
		rehashedIndex = (rehashedIndex + 1) % listLength
	
	return hashList, False

def isFull(hashList: list, length: int) -> bool:
	return len(set(hashList))-1 == length

def isEmpty(hashList: list) -> bool:
	return len(set(hashList))-1 == 1

def logHashList(hashList: list, length: int) -> None:
	print(isFull(hashList, length), isEmpty(hashList), hashList)

logHashList(hashList, length)

insertItem(51, rehashValue, hashList, length, modValue)

logHashList(hashList, length)

insertItem(62, rehashValue, hashList, listLength, modValue)
logHashList(hashList, length)
insertItem(73, rehashValue, hashList, listLength, modValue)
logHashList(hashList, length)
insertItem(84, rehashValue, hashList, listLength, modValue)
logHashList(hashList, length)
insertItem(95, rehashValue, hashList, listLength, modValue)
logHashList(hashList, length)
insertItem(106, rehashValue, hashList, listLength, modValue)
logHashList(hashList, length)
insertItem(42, rehashValue, hashList, listLength, modValue)
insertItem(72, rehashValue, hashList, listLength, modValue)
insertItem(90, rehashValue, hashList, listLength, modValue)
insertItem(90, rehashValue, hashList, listLength, modValue)

logHashList(hashList, length)

hashList, removed = removeItem(90, hashList, listLength, modValue, rehashValue)
print(hashList, removed)
hashList, removed = removeItem(4, hashList, listLength, modValue, rehashValue)
print(hashList, removed)