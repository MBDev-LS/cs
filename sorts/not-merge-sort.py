import copy
import random

lst = [1, 7, 3, 1]
lst = [1, 7, 3, 1, 7, 4, 9, 100, 6, 2, 8, 1]
lst = [random.randint(1, 1000) for i in range(1001)]
print(lst)

sortingList = [[item] for item in lst]
newSortingList = copy.deepcopy(sortingList)

while len(sortingList) > 1:
	# print("Started new loop.")
	sortingList = copy.deepcopy(newSortingList)

	if len(sortingList) == 1:
		break

	for i in range(0, len(sortingList)):
		if i >= len(newSortingList)-1:
			continue

		# print('LOOK HERE:', len(sortingList))
		# print("Started step")
		listA = newSortingList.pop(i)
		taken = False
		if len(newSortingList)-1 < i:
			if len(newSortingList[-1]) == 1:
				listB = newSortingList.pop()
				taken = True
			else:
				continue
		if not taken is True:
			listB = newSortingList.pop(i)
		newList = []

		while len(listA) > 0 and len(listB) > 0:
			# print("Ran mini sort")
			if listA[0] < listB[0]:
				newList.append(listA.pop(0))
			else:
				newList.append(listB.pop(0))
		
		newList += listA if len(listA) > 0 else listB
		


		newSortingList.insert(i, newList)


lst.sort()
print(lst)
print(sortingList[0])
print(lst == sortingList[0])
