import copy

lst = [1, 7, 3, 1]

sortingList = [[item] for item in lst]
newSortingList = copy.deepcopy(sortingList)

while len(sortingList) > 1:
	print("Started new loop.")
	sortingList = copy.deepcopy(newSortingList)
	if len(sortingList) == 1:
		break

	for i in range(0, len(sortingList), 2):
		print("Started step")
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
			print("Ran mini sort")
			if listA[0] < listB[0]:
				newList.append(listA.pop(0))
			else:
				newList.append(listB.pop(0))
		
		newList += listA if len(listA) > 0 else listB
		


		newSortingList.insert(i, newList)

print(sortingList)

