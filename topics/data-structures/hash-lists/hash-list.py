

length = 10
listLength = int(length*1.25)
hashList = [None for i in range(int(length*1.5))]
modValue = int(length*1.25)
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