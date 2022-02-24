import copy
import random

from lists import lst1 as lst

print(f'Before: {lst}')

sortingList = [[item] for item in lst]
newSortingList = copy.deepcopy(sortingList)

while len(sortingList) > 1:
	sortingList = copy.deepcopy(newSortingList)

	if len(sortingList) == 1:
		break

	for i in range(0, len(sortingList)):
		if i >= len(newSortingList)-1:
			continue

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
			if listA[0] < listB[0]:
				newList.append(listA.pop(0))
			else:
				newList.append(listB.pop(0))
		
		newList += listA if len(listA) > 0 else listB

		newSortingList.insert(i, newList)


lst.sort()
print(f'Python\'s sort function: {lst}')
print(f'After: {sortingList[0]}')
print(f'Match: {lst == sortingList[0]}')
