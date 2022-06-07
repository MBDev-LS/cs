
from lists import lst1 as lst

def isSorted(lst: list) -> bool:
	for i in range(1, len(lst)):
		if lst[i] < lst[i-1]:
			return False
	
	return True

def getIntLen(num: int) -> int:
	pass

buckets = [[] for i in range(10)]
counter = 0
results = []

while isSorted(lst) is not True:
	print(counter)
	for item in lst:

		buckets[(item // 10**counter)%10].append(item)
	
	lst = []
	for bucket in buckets:
		lst.extend(bucket)
	
	counter += 1

print(lst)