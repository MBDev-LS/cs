
import copy

from sqlalchemy import true

xDimension = 40
yDimension = 30

boardList = [[0 for x in range(xDimension)] for y in range(yDimension)]

# boardList = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# boardList = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(boardList)

cycles = 100

def updateCell(cellCoordX: int, cellCoordY: int, board: list) -> int:
	surroundingCells = []

	for xMod in range(-1, 2):
		for yMod in range(-1, 2):
			if xMod == 0 and yMod == 0:
				continue
			elif cellCoordY + yMod >= len(board):
				continue
			elif cellCoordX + xMod >= len(board[cellCoordY]):
				continue
			elif cellCoordY + yMod <= 0:
				continue
			elif cellCoordX + xMod <= 0:
				continue

			surroundingCells.append(board[cellCoordY + yMod][cellCoordX + xMod])
	
	aliveCount = surroundingCells.count(1)
	# deadCount = surroundinxgCells.count(0)

	currentState = board[cellCoordY][cellCoordX]

	if currentState == 0:
		if aliveCount == 3:
			return 1
		else:
			return 0
	
	elif currentState == 1:
		if aliveCount < 2:
			return 0
		elif aliveCount >= 2 and aliveCount <= 3:
			return 1
		elif aliveCount >= 4:
			return 0

	return 0

def displayBoard(board):

	maxLength = len(str(len(board[0])))
	lstOfLines = [[] for i in range(maxLength)]


	for i, lst in enumerate(lstOfLines):
		for y in range(len(board)):
			if len(str(y)) > i:
				lst.append(str(y)[i])
			else:
				lst.append(' ')
	
	for lst in lstOfLines:
		print(' '*5+' '.join(lst))


	# print('     '+''.join([str(i) + ' ' for i in range(len(board[0]))]))
	print('    ' + '_'*int(2+2*len(board[0])))

	
	for y in range(len(board)):

		print(f'{y:>3} |' + ''.join(["⬛️" if item == 1 else "⬜️" for item in board[y]] ) + '|')
		# print('|' + ''.join(["■" if item == 1 else "□" for item in board[y]] ) + '|')
	
	print('    '+'‾'*int(2+2*len(board[0])))

def intInput(prompt: str) -> int:
	userInput = input(prompt)
	while userInput.isdigit() is not True:
		if userInput == 'e':
			return -1
		
		print('Enter an integer.')
		userInput = input(prompt)

	
	return int(userInput)


displayBoard(boardList)

while True:
	xToEdit = intInput('Enter X coord to edit (enter \'e\' to abandon editing): ')
	if xToEdit == -1:
		print('Editing stopped.')
		break
	elif xToEdit >= xDimension:
		print('That coordiate is out of the valid range.')
		continue
	

	yToEdit = intInput('Enter Y coord to edit (enter \'e\' to abandon editing): ')
	if yToEdit == -1:
		print('Editing stopped.')
		break
	elif yToEdit >= yDimension:
		print('That coordiate is out of the valid range.')
		continue

	value = input('Set this coord to alive (1) or dead (0): ')
	while value not in ['alive', '0', 'dead', '1']:
		if value == -1:
			print('Editing stopped.')
			break

		print('Invalid response.')
		value = input('Set this coord to alive (1) or dead (0): ')
	
	boardList[yToEdit][xToEdit] = 1 if value in ['alive', '1'] else 0

	display = input('Display board (y/n): ').lower()
	while display not in ['y', 'n']:
		display = input('Display board (y/n): ').lower()
	
	if display == 'y':
		displayBoard(boardList)

for cycleCount in range(cycles):
	newBoard = [[0 for x in range(xDimension)] for y in range(yDimension)]
	
	for x in range(xDimension):
		for y in range(yDimension):
			newBoard[y][x] = updateCell(x, y, boardList)

	boardList = copy.deepcopy(newBoard)

	flat = []

	for y in range(yDimension):
		for x in range(xDimension):
			flat.append(boardList[y][x])

	displayBoard(boardList)

	input()

	if len(set(flat)) == 1 and boardList[0][0] == 0:
		print('Everything is dead.')
		exit()

