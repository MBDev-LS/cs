# Skeleton Program for the AQA A1 Summer 2017 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

from random import *

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'
SNAIL = 'A'


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

class Snail():
	def __init__(self, position: tuple, sex: str, field: str) -> None:
		self.position = position
		self.sex = sex
		self.field = field
	
	def move(self, newPosition: tuple):
		self.field[self.position[1]][self.position[0]] = SOIL
		self.field[newPosition[1]][newPosition[0]] = SOIL
		self.position = newPosition

	# def layEggs(self):
	# 	pass

	# def attemptsToMate(self):
	# 	if self.sex == 'f':
	# 		self.layEggs()


def spawnSnails(field):
	snail1 = Snail((randint(1, FIELDWIDTH-1), randint(1, FIELDLENGTH-1)), 'f', field)

	maxSnailBoundryXRight = min([snail1.position[0] + 5, FIELDWIDTH - 1])
	maxSnailBoundryXLeft = max([snail1.position[0] - 5, 0])
	print(maxSnailBoundryXLeft, maxSnailBoundryXRight)

	maxSnailBoundryYBottom = min([snail1.position[1] + 5, FIELDLENGTH - 1])
	maxSnailBoundryYTop = max([snail1.position[1] - 5, 0])
	print(maxSnailBoundryYBottom, maxSnailBoundryYTop)

	snail2X = choice([i for i in range(maxSnailBoundryXLeft, maxSnailBoundryXRight) if i not in [0]]) # Needs to be modified so snail cannot spawn in the centre (on the first plant)
	snail2Y = choice([i for i in range(maxSnailBoundryYTop, maxSnailBoundryYBottom) if i not in [0]]) # Needs to be modified so snail cannot spawn in the centre (on the first plant)
	print(snail2X, snail2Y)
	snail2 = Snail((snail2X, snail2Y), 'm', field)
	
	field[snail1.position[1]][snail1.position[0]] = SNAIL
	field[snail2.position[1]][snail2.position[0]] = SNAIL

	return field


def CreateNewField(): 
	Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
	Row = FIELDLENGTH // 2
	Column = FIELDWIDTH // 2
	Field[Row][Column] = SEED
	
	Field = spawnSnails(Field)
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

def Simulation():
	YearsToRun = GetHowLongToRun()
	if YearsToRun != 0:
		Field = InitialiseField()
		if YearsToRun >= 1:
			for Year in range(1, YearsToRun + 1):
				SimulateOneYear(Field, Year)
		else:
			Continuing = True                     
			Year = 0
			while Continuing:
				Year += 1
				SimulateOneYear(Field, Year)
				Response = input('Press Enter to run simulation for another Year, Input X to stop: ')
				if Response == 'x' or Response == 'X':
					Continuing = False
		print('End of Simulation')
	input()

if __name__ == "__main__":
	Simulation()      
