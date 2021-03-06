# Skeleton Program for the AQA A1 Summer 2017 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# This addition favour plants that are further apart from each other,
# if a plant is withing one square of another it's seeds are less likely to drop.

from random import *
import copy

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'

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

def SeedLands(Field, Row, Column, probability):
	if not randint(1, 100) <= 100 * probability:
		return Field
	if Row >= 0 and Row < FIELDLENGTH and Column >= 0 and Column < FIELDWIDTH: 
		if Field[Row][Column] == SOIL:
			Field[Row][Column] = SEED
	return Field

def checkDisplay(Field, sx, sy, cx, cy):
	Field[sy][sx] = 'X'
	Field[cy][cx] = '#'
	
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			print(Field[Row][Column], end='')
		print('|{0:>3}'.format(Row))
	print()

def checkSurroundingArea(field, columStartingPoint, rowStartingPoint, areaSize, checkCharacter) -> bool:
	for RowAdd in range(-areaSize, areaSize+1):
		
		for ColumnAdd in range(-areaSize, areaSize+1):
			if ColumnAdd == 0 and RowAdd == 0:
				continue
			elif rowStartingPoint + RowAdd >= FIELDLENGTH or columStartingPoint + ColumnAdd >= FIELDWIDTH:
				continue
			elif rowStartingPoint + RowAdd < 0 or columStartingPoint + ColumnAdd < 0 :
				continue

			# print(rowStartingPoint + RowAdd, columStartingPoint + ColumnAdd)

			if field[rowStartingPoint + RowAdd][columStartingPoint + ColumnAdd] == checkCharacter:
				
				return True

			# checkDisplay(copy.deepcopy(field), columStartingPoint, rowStartingPoint, columStartingPoint + ColumnAdd, rowStartingPoint + RowAdd)
	
	return False

def SimulateAutumn(Field):
	for Row in range(FIELDLENGTH): 
		for Column in range(FIELDWIDTH):
			# print(checkSurroundingArea(Field, Column, Row, 1, 'P'))
			# print(checkSurroundingArea(Field, Column, Row, 1, '.'))
			
			if Field[Row][Column] == PLANT:
				seedChance = 0.7
				if checkSurroundingArea(Field, Column, Row, 1, 'S') is True:
					seedChance = 0.4
				Field = SeedLands(Field, Row - 1, Column - 1, seedChance)
				Field = SeedLands(Field, Row - 1, Column, seedChance)
				Field = SeedLands(Field, Row - 1, Column + 1, seedChance)
				Field = SeedLands(Field, Row, Column - 1, seedChance)
				Field = SeedLands(Field, Row, Column + 1, seedChance)
				Field = SeedLands(Field, Row + 1, Column - 1, seedChance)
				Field = SeedLands(Field, Row + 1, Column, seedChance)
				Field = SeedLands(Field, Row + 1, Column + 1, seedChance)
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
