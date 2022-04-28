
import copy

xDimension = 10
yDimension = 20

boardList = [[0 for x in range(xDimension)] for y in range(yDimension)]

# boardList = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]


cycles = 10

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
	print('_'*(2+len(board[0])))

	for y in range(len(board)):
		# print('|' + ''.join(["⬛️" if item == 1 else "⬜️" for item in board[y]] ) + '|')
		print('|' + ''.join(["■" if item == 1 else "□" for item in board[y]] ) + '|')
	
	print('‾'*(2+len(board[0])))

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

	if len(set(flat)) == 1 and boardList[0][0] == 0:
		print('Everything is dead.')
		exit()

