
from lists import lst3 as lst

swapped = True
index = 1
while swapped:
	swapped = False
	for i, item in enumerate(lst):
		if i >= len(lst) - 1:
			continue
		if item > lst[i+1]:
			lst[i], lst[i+1] = lst[i+1], lst[i]
			swapped = True
	for j in range(len(lst)-1, 0, -1):
		if lst[j] < lst[j-1]:
			lst[j], lst[j-1] = lst[j-1], lst[j]
			swapped = True

print(lst)