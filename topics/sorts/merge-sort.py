
from lists import lst1 as lst

def merge_sort(lst: list) -> list:
	if len(lst) > 1:
		left = lst[:len(lst)//2]
		right = lst[len(lst)//2:]

		sortedLeft = merge_sort(left)
		sortedRight = merge_sort(right)

		newList = []
		while len(sortedLeft) > 0 and len(sortedRight) > 0:
			if sortedLeft[0] < sortedRight[0]:
				newList.append(sortedLeft.pop(0))
			else:
				newList.append(sortedRight.pop(0))
		
		newList += sortedLeft if len(sortedLeft) > 0 else sortedRight
		return newList
	else:
		return lst

print(merge_sort(lst))
