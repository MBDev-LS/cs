
import copy
from lists import lst1 as lst

sortedList = [lst.pop(0)]

for i, item in enumerate(lst):
	wasSorted = False

	sortedListStatic = copy.deepcopy(sortedList)
	for j, sortedItem in enumerate(sortedListStatic):
		if item < sortedItem:
			sortedList.insert(j, lst[i])
			wasSorted = True
			break
	
	if wasSorted is not True:
		sortedList.append(lst[i])

print(sortedList)
