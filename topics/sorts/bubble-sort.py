
from lists import lst1 as lst

swapped = True
index = 0
while swapped:
	swapped = False
	for i, item in enumerate(lst):
		print(f'Current Number is {item} in position {i}/{len(lst)-1}')
		if i >= len(lst) - (index+1):
			print(f'{item} is more than or equal to the index limit')
			continue
		
		print(f'Comparing {item} to {lst[i+1]}')
		if item > lst[i+1]:
			print(f'Swapping {item} and {lst[i+1]}')
			lst[i], lst[i+1] = lst[i+1], lst[i]
			swapped = True
	
	index += 1
	print(f'Index incremented by 1, now {index}')

print(lst)