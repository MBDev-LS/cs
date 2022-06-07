
import random

lst = [random.randint(1, 10) for i in range(0, 10)]

def isSorted(lst: list) -> bool:
	for i in range(1, len(lst)):
		if lst[i] < lst[i-1]:
			return False
	
	return True


while isSorted(lst) is not True:
	random.shuffle(lst)

print(lst)