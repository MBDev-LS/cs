# Skeleton Program for the AQA A1 Summer 2017 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

from random import *
from math import inf
from uuid import getnode
from xml.dom.minicompat import NodeList

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'
ANIMAL = 'A'

FIELDLENGTH = 20 
FIELDWIDTH = 35

class FieldNode():
	def __init__(self, coords, links=None, start=False, end=False) -> None:
		self.coords = coords
		self.links = [] if links is None else links
		self.start = start
		self.end = end

		if start is True:
			self.cost = 0
		else:
			self.cost = inf
		
		self.previous_node = None

	def addLink(self, link):
		self.links.append(link)
	
	def __str__(self) -> str:
		return f'<Node {self.coords} [{", ".join([str(link.node1.coords) + ": " + str(link.weight) for link in self.links])}] ({self.cost})>'
	
	def __repr__(self) -> str:
		return f'Node(coord={self.coords}, links={self.links}, start={self.start}, end={self.end})'

class Link():
	def __init__(self, node0: FieldNode, node1: FieldNode) -> None:
		self.node0 = node0
		self.node1 = node1
		self.weight = 1

	def __str__(self):
			return f'<link n0={self.node0.name} n1={self.node1.name} weight={self.weight}>'

	def __repr__(self):
		return f'Link(node0={self.node0}, node1={self.node1}, weight={self.weight})'

def getNodeFromCoords(nodeList: list, searchCoords) -> FieldNode:
	for node in nodeList:
		if node.coords == searchCoords:
			return node
	
	return None


def FieldToGraph(field: list, startCoords: tuple, endCoords: tuple) -> list:
	nodeList = []

	for x in range(FIELDWIDTH):
		for y in range(FIELDLENGTH):
			
			if (x, y) == startCoords:
				nodeList.append(FieldNode((x, y), start=True))
			elif (x, y) == endCoords:
				nodeList.append(FieldNode((x, y), end=True))
			elif field[y][x] == SOIL:
				nodeList.append(FieldNode((x, y)))

	for node in nodeList:
		print('NEW START POINT:', (node.coords))
		for xAdd in range(-1, 2):
			print(f'xAdd: {xAdd}')
			for yAdd in range(-1, 2):
				print(f'yAdd: {yAdd}')
				if xAdd == 0 and yAdd == 0:
					print('SKIPPED')
					continue

				print((node.coords[0]+xAdd, node.coords[1]+yAdd))
				
				searchResult = getNodeFromCoords(nodeList, (node.coords[0]+xAdd, node.coords[1]+yAdd))

				if searchResult == None:
					continue

				node.addLink(Link(node, searchResult))


	return nodeList


def GetHowLongToRun():
	print('Welcome to the Plant Growing Simulation')
	print()
	print('You can step through the simulation a year at a time')
	print('or run the simulation for 0 to 5 years')
	print('How many years do you want the simulation to run?')
	Years = int(input('Enter a number between 0 and 5, or -1 for stepping mode: '))
	return Years

class Animal():
	def __init__(self, position: tuple, sex: str, field: str) -> None:
		self.position = position
		self.sex = sex
		self.field = field
	
	def move(self, newPosition: tuple):
		self.field[self.position[1]][self.position[0]] = SOIL
		self.field[newPosition[1]][newPosition[0]] = ANIMAL
		self.position = newPosition
	
	def randMove(self):
		print('randMove Running')
		maxAnimalBoundryXRight = min([self.position[0] + 5, FIELDWIDTH - 1])
		maxAnimalBoundryXLeft = max([self.position[0] - 5, 0])
		print(maxAnimalBoundryXLeft, maxAnimalBoundryXRight)

		maxAnimalBoundryYBottom = min([self.position[1] + 5, FIELDLENGTH - 1])
		maxAnimalBoundryYTop = max([self.position[1] - 5, 0])
		print(maxAnimalBoundryYTop, maxAnimalBoundryYBottom)

		movementOptions = []
		for x in range(maxAnimalBoundryXLeft, maxAnimalBoundryXRight):
			for y in range(maxAnimalBoundryYTop, maxAnimalBoundryYBottom):
				if self.field[y][x] == SOIL:
					movementOptions.append((x, y))

		print(movementOptions)
		
		if len(movementOptions) == 0:
			return
		
		self.move(choice(movementOptions))


def spawnAnimals(field):
	animal1 = Animal((randint(1, FIELDWIDTH-1), randint(1, FIELDLENGTH-1)), 'f', field)
	field[animal1.position[1]][animal1.position[0]] = ANIMAL

	return field, animal1


def CreateNewField(): 
	Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
	Row = FIELDLENGTH // 2
	Column = FIELDWIDTH // 2
	Field[Row][Column] = SEED
	
	field, animal1 = spawnAnimals(Field)
	return field, animal1

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
		Field, animal1 = InitialiseField()
		FieldToGraph(Field, startCoords=(0, 0), endCoords=(1, 0))
		with open('djikstra2.txt', 'w') as f:
			f.write(str(FieldToGraph(Field, startCoords=(0, 0), endCoords=(1, 0))))
		if YearsToRun >= 1:
			for Year in range(1, YearsToRun + 1):
				SimulateOneYear(Field, Year)
		else:
			Continuing = True                     
			Year = 0
			while Continuing:
				Year += 1
				SimulateOneYear(Field, Year)
				animal1.randMove()
				Response = input('Press Enter to run simulation for another Year, Input X to stop: ')
				if Response == 'x' or Response == 'X':
					Continuing = False
		print('End of Simulation')
	input()

if __name__ == "__main__":
	Simulation()
