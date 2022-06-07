
hexDict = {
	0: '0',
	1: '1',
	2: '2',
	3: '3',
	4: '4',
	5: '5',
	6: '6',
	7: '7',
	8: '8',
	9: '9',
	10: 'A',
	11: 'B',
	12: 'C',
	13: 'D',
	14: 'E',
	15: 'F'
}

while True:
	currentNum = input('Enter: ')
	if currentNum.isdigit():
		currentNum = int(currentNum)
	else:
		print("Invalid number.")
		exit()

	resList = []

	while True:
		
		print(f'Res: {currentNum//16}     Rem: {currentNum%16}')
		resList.append(currentNum%16)
		currentNum = currentNum//16
		

		if currentNum == 0:
			break

	resList.reverse()

	print(f'In binary: {"".join(hexDict[num] for num in resList)}')