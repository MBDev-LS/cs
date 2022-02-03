# Skeleton Program for the AQA A1 Summer 2017 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

from mimetypes import init
from random import *

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'

SNAKEBODY = '='
SNAKEHEAD = '>'
DEADSNAKEHEAD = '✖'

FIELDLENGTH = 20 
FIELDWIDTH = 35 

def GetHowLongToRun():
	print('Welcome to the Plant Growing Simulation')
	print()
	print('You can step through the simulation a year at a time')
	print('or run the simulation for 0 to 5 years')
	print('How many years do you want the simulation to run?')
	Years = int(input('Enter a number between 0 and 5, or -1 for stepping mode: '))
	return Years

def CreateNewField(): 
	Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
	Row = FIELDLENGTH // 2
	Column = FIELDWIDTH // 2
	Field[Row][Column] = SEED
	return Field

def ReadFile():   
	FileName = input('Enter file name: ')
	Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
	try:
		FileHandle = open(FileName, 'r')
		for Row in range(FIELDLENGTH):
			FieldRow = FileHandle.readline()
			for Column in range(FIELDWIDTH):
				Field[Row][Column] = FieldRow[Column]
		FileHandle.close()
	except:
		Field = CreateNewField()
	return Field

def InitialiseField(): 
	Response = input('Do you want to load a file with seed positions? (Y/N): ')
	if Response == 'Y':
		Field = ReadFile()
	else:
		Field = CreateNewField()
	return Field

def Display(Field, Season, Year):
	print('Season: ', Season, '  Year number: ', Year)
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			print(Field[Row][Column], end='')
		print('|{0:>3}'.format(Row))
	print()

def CountPlants(Field):
	NumberOfPlants = 0
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			if Field[Row][Column] == PLANT:
				NumberOfPlants += 1
	if NumberOfPlants == 1:
		print('There is 1 plant growing')
	else:  
		print('There are', NumberOfPlants, 'plants growing')

def SimulateSpring(Field):
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			if Field[Row][Column] == SEED:  
				Field[Row][Column] = PLANT
	CountPlants(Field)
	if randint(0, 1) == 1:
		Frost = True
	else:
		Frost = False
	if Frost:    
		PlantCount = 0
		for Row in range(FIELDLENGTH):
			for Column in range(FIELDWIDTH):
				if Field[Row][Column] == PLANT:
					PlantCount += 1
					if PlantCount % 3 == 0:
						Field[Row][Column] = SOIL
		print('There has been a frost')
		CountPlants(Field)
	return Field

def SimulateSummer(Field): 
	RainFall = randint(0, 2)
	if RainFall == 0:
		PlantCount = 0
		for Row in range(FIELDLENGTH):
			for Column in range(FIELDWIDTH):
				if Field[Row][Column] == PLANT:
					PlantCount += 1
					if PlantCount % 2 == 0:
						Field[Row][Column] = SOIL
		print('There has been a severe drought')
		CountPlants(Field)
	return Field

def SeedLands(Field, Row, Column): 
	if Row >= 0 and Row < FIELDLENGTH and Column >= 0 and Column < FIELDWIDTH: 
		if Field[Row][Column] == SOIL:
			Field[Row][Column] = SEED
	return Field

def SimulateAutumn(Field): 
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			if Field[Row][Column] == PLANT:
				Field = SeedLands(Field, Row - 1, Column - 1)
				Field = SeedLands(Field, Row - 1, Column)
				Field = SeedLands(Field, Row - 1, Column + 1)
				Field = SeedLands(Field, Row, Column - 1)
				Field = SeedLands(Field, Row, Column + 1)
				Field = SeedLands(Field, Row + 1, Column - 1)
				Field = SeedLands(Field, Row + 1, Column)
				Field = SeedLands(Field, Row + 1, Column + 1)
	return Field

def SimulateWinter(Field):
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			if Field[Row][Column] == PLANT:
				Field[Row][Column] = SOIL
	return Field

def SimulateOneYear(Field, Year):
	Field = SimulateSpring(Field)
	Display(Field, 'spring', Year)
	Field = SimulateSummer(Field)
	Display(Field, 'summer', Year)
	Field = SimulateAutumn(Field)
	Display(Field, 'autumn', Year)
	Field = SimulateWinter(Field)
	Display(Field, 'winter', Year)

class Snake():
	MOVEMENTMODS = {
		'W': (0, -1),
		'A': (-1, 0),
		'S': (0, 1),
		'D': (1, 0),
	}
	
	def __init__(self, field, startingPos) -> None:
		self.field = field
		self.body = [(startingPos[0]-3, startingPos[1]), (startingPos[0]-2, startingPos[1]), (startingPos[0]-1, startingPos[1]), startingPos]
		self.backCache = (startingPos[0]-4, startingPos[1])
		self.alive = True

		self.field[self.body[0][1]][self.body[0][0]] = SNAKEBODY
		self.field[self.body[1][1]][self.body[1][0]] = SNAKEBODY
		self.field[self.body[2][1]][self.body[2][0]] = SNAKEBODY
		self.field[self.body[3][1]][self.body[3][0]] = SNAKEHEAD

	
	def moveSnake(self, move):
		if move.upper() not in Snake.MOVEMENTMODS:
			return

		newHeadPos = (self.body[-1][0] + Snake.MOVEMENTMODS[move.upper()][0], self.body[-1][1] + Snake.MOVEMENTMODS[move.upper()][1])
		# Check to see that new coords are in bounds
		newHeadSquare = self.field[newHeadPos[1]][newHeadPos[1]]
		if newHeadSquare == SOIL:
			self.field[self.body[0][1]][self.body[0][0]] = SOIL
			self.field[self.body[-1][1]][self.body[-1][0]] = SNAKEBODY
			# print(self.field[self.body[-1][1]][self.body[-1][0]])

			self.backCache = self.body[0]
			self.body.pop(0)

			self.body.append(newHeadPos)

			self.field[newHeadPos[1]][newHeadPos[0]] = SNAKEHEAD
		elif newHeadSquare == SEED:
			# self.body.insert(0, self.backCache)
			# self.field[self.backCache[1]][self.backCache[0]] = SNAKEBODY

			self.field[self.body[-1][1]][self.body[-1][0]] = SNAKEBODY

			self.body.append(newHeadPos)

			self.field[newHeadPos[1]][newHeadPos[0]] = SNAKEHEAD
		else:
			self.field[newHeadPos[1]][newHeadPos[0]] = DEADSNAKEHEAD
			self.alive = False

def Simulation():
	YearsToRun = GetHowLongToRun()
	if YearsToRun != 0:
		Field = InitialiseField()
		snake = Snake(Field, (4, FIELDLENGTH-1))
		if YearsToRun >= 1:
			for Year in range(1, YearsToRun + 1):
				SimulateOneYear(Field, Year)
		else:
			Continuing = True                     
			Year = 0
			while Continuing:
				Year += 1
				SimulateOneYear(Field, Year)

				if snake.alive is True:
					snakeMove = input('Move snake (WASD): ')
					while snakeMove.upper() not in ['W', 'A', 'S', 'D']:
						snakeMove = input('Move snake (WASD): ')
					
					snake.moveSnake(snakeMove)
				
				Response = '' # input('Press Enter to run simulation for another Year, Input X to stop: ')
				if Response == 'x' or Response == 'X':
					Continuing = False
		print('End of Simulation')
	input()

if __name__ == "__main__":
	Simulation()      
