
while True:
	currentNum = input('Enter: ')
	if currentNum.isdigit():
		currentNum = int(currentNum)
	else:
		print("Invalid number.")
		exit()

	resList = []

	while True:
		
		print(f'Res: {currentNum//2}     Rem: {currentNum%2}')
		resList.append(currentNum%2)
		currentNum = currentNum//2
		

		if currentNum == 0:
			break

	resList.reverse()

	print(f'In binary: {"".join(str(num) for num in resList)}')
	