
from lists import lst1 as lst

swapped = True
index = 1

while swapped:
	bouncer = False
	for i, item in enumerate(lst):
		j = len(lst)-i if bouncer is True else i
		jmod = -1 if bouncer is True else 1
		if j > len(lst) - 1:
			continue
		if (lst[j] > lst[j+jmod] and bouncer is not True) or (lst[j] < lst[j+jmod] and bouncer is True):
			lst[j], lst[j+jmod] = lst[j+jmod], lst[j]
			swapped = True
		else:
			swapped = False
		bouncer = not bouncer

print(lst)