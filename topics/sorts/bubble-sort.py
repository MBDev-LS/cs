
from lists import lst1 as lst

swapped = True
index = 1
while swapped:
	for i, item in enumerate(lst):
		if i >= len(lst) - 1:
			continue
		if item > lst[i+1]:
			lst[i], lst[i+1] = lst[i+1], lst[i]
			swapped = True
		else:
			swapped = False

print(lst)