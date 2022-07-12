
import json
from pathlib import Path


from tabulate import tabulate
import copy
from math import inf, sqrt

BASE_DIR = Path(__file__).resolve().parent
SAVES_DIR = BASE_DIR / 'saves' / 'a_star'



class Node():
	def __init__(self, name: str, x_coord: int, y_coord: int, edges: dict=None, start: bool=False, end: bool=False) -> None:
		self.name = name
		self.edges = edges if edges is not None else {}
		self.cost = inf

		self.previousNode = None
		self.start = start
		self.end = end
		self.shortestPath = []

		self.x_coord = x_coord
		self.y_coord = y_coord

		self.heuristic = -1
	
	def generateHeuristic(self, endNode) -> int:
		return sqrt((endNode.x_coord - self.x_coord)**2 + (endNode.y_coord - self.y_coord)**2)
	
	def setHeuristic(self, endNode):
		self.heuristic = self.generateHeuristic(endNode)

	def addEdge(self, node, weight: int):
		self.edges[node] = weight
	
	def __str__(self) -> str:
		return f'{str(self.name)} -> {", ".join([node.name for node in self.edges])}'

class Graph():
	def __init__(self, nodes: list=None, startNode: Node=None, endNode: Node=None) -> None:
		self.nodes = nodes if nodes is not None else []
		self.startNode = startNode
		if startNode is not None:
			self.startNode.cost = 0
		
		self.endNode = endNode

	def a_star(self, startNode: Node, endNode: Node):
		self.setStartNode(startNode)
		self.setEndNode(endNode)

		for node in self.nodes:
			node.setHeuristic(self.startNode)

		possibilities = sorted([node for node in self.nodes], key=lambda n: (n.cost + n.heuristic, n.name))
		visited = []

		while len(possibilities) > 0:
			possibilities = sorted(possibilities, key=lambda n: (n.cost + n.heuristic, n.name))
			currentNode = possibilities.pop(0)
			visited.append(currentNode)

			for edgeNode in currentNode.edges:
				newDistance = currentNode.cost + currentNode.edges[edgeNode]
				if newDistance < edgeNode.cost:
					edgeNode.cost = newDistance
					edgeNode.previousNode = currentNode
		
		for node in self.nodes:
			print(f'{node.name}: {node.cost}')
		
		return

	def setStartNode(self, newStartNode) -> None:
		self.startNode = newStartNode
		self.startNode.start = True
		self.startNode.cost = 0

	def setEndNode(self, newEndNode) -> None:
		self.startNode.end = True
		self.endNode = newEndNode

	def getNodeByName(self, nameToSearch: str):
		for node in self.nodes:
			if nameToSearch == node.name:
				return node
		
		return None
	
	def isWeighted(self) -> bool:
		weightList = []

		for node in self.nodes:
			for edgeNode in node.edges:
				weightList.append(node.edges[edgeNode])
		
		if len(weightList) == 0:
			return False
		
		return not (len(set(weightList)) == 1 and weightList[0] == 1)

	def isDirected(self) -> bool:
		for node in self.nodes:
			for edgeNode in node.edges:
				for secondLayerEdgeNode in edgeNode.edges:
					if node.edges[edgeNode] == edgeNode.edges[secondLayerEdgeNode] and secondLayerEdgeNode == node:
						return False
		
		return True
	
	def addNode(self, node: Node) -> bool:
		if node.name in [existingNode.name for existingNode in self.nodes]:
			return False
		
		self.nodes.append(node)
		return True
	

	def printAdjacencyMatrix(self) -> None:
		tableData = []

		nodeHeaders = [node for node in self.nodes]

		for node in self.nodes:
			rowList = [node.name]
			for nodeHeader in nodeHeaders:
				if nodeHeader in node.edges:
					rowList.append(node.edges[nodeHeader])
				else:
					rowList.append('')
			
			tableData.append(rowList)

		headers = [''] + [node.name for node in self.nodes]
		
		print(tabulate(tableData, headers=headers, tablefmt="fancy_grid"))
	

	def printAdjacencyList(self, includeShortestPath=False) -> None:
		if includeShortestPath is True:
			if self.startNode is None:
				print('Unable to include shortest path, as not start not is set.')
				includeShortestPath = False
			else:
				self.a_star(self.nodes[0], self.nodes[-1])

		tableData = []

		for node in self.nodes:
			nodeDict = {}
			for connectedNode in node.edges:
				nodeDict[connectedNode.name] = node.edges[connectedNode]

			if includeShortestPath is True:
				if self.startNode == node:
					tableData.append([node.name, str(nodeDict), f'{node.name}'])
				else:
					tableData.append([node.name, str(nodeDict), ' -> '.join([pathNode.name for pathNode in node.shortestPath]) + f' -> {node.name}'])
			else:
				tableData.append([node.name, str(nodeDict)])
		
		headers = ['Node', 'Edges', f'Shortest path from {self.startNode.name}'] if includeShortestPath is True else ['Node', 'Edges']

		print(tabulate(tableData, headers=headers, tablefmt="fancy_grid"))

	def exportAdjacencyMatrix(self) -> None:
		tableData = []

		nodeHeaders = [node for node in self.nodes]

		outputString = ''

		for node in self.nodes:
			rowList = []
			for nodeHeader in nodeHeaders:
				if nodeHeader in node.edges:
					rowList.append(node.edges[nodeHeader])
				else:
					rowList.append(0)
			
			tableData.append(rowList)
			outputString += ', '.join([str(item) for item in rowList]) + '\n'
		
		print(outputString)


	def export(self, filename) -> None:
		FILE_DIR = SAVES_DIR / filename
		nodesDict = {}
		for node in self.nodes:
			nodeDict = {
					'meta': {
						'x_coord': node.x_coord,
						'y_coord': node.y_coord,
					},
					'edges': {}
				}
			for connectedNode in node.edges:
				nodeDict['edges'][connectedNode.name] = node.edges[connectedNode]

			nodesDict[node.name] = nodeDict

		with open(FILE_DIR, 'w+') as f:
			f.write(json.dumps(nodesDict))
	
	def jsonExport(self, filename) -> None:
		filenameWithExt = filename + '.json'
		FILE_DIR = SAVES_DIR / filenameWithExt
		nodesDict = {}
		for node in self.nodes:
			nodeDict = {
					'meta': {
						'x_coord': node.x_coord,
						'y_coord': node.y_coord,
					},
					'edges': {}
				}
			for connectedNode in node.edges:
				nodeDict['edges'][connectedNode.name] = node.edges[connectedNode]

			nodesDict[node.name] = nodeDict

		with open(FILE_DIR, 'w+') as f:
			f.write(json.dumps(nodesDict))

	def print(self) -> None:
		outputString = '\n'.join([str(node) for node in self.nodes])
		print(outputString)
	
	def __str__(self) -> str:
		return '\n'.join([str(node) for node in self.nodes])


def discreteInput(prompt: str, possibleInputs: list, caseSensitive: bool=True):
	userInput = input(prompt)

	while (userInput not in possibleInputs and caseSensitive) or (userInput.lower() not in [possibleInput.lower() for possibleInput in possibleInputs]):
		userInput = input(prompt)
	
	return userInput

def intInput(prompt: str, allow_decimals: bool=False):
	userInput = input(prompt)

	if allow_decimals is True:
		valid = False
		while valid is not True:
			try:
				userInput = input(prompt)
				float(userInput)
				valid = True
			except:
				print('Please enter a valid input (float): ')
	else:
		while not userInput.isdigit():
			userInput = input(prompt)
	
	return float(userInput)

def menu(optionList: list, prompt=None):
	optionText = 'Options\n'
	optionText += '\n'.join([f'{i+1} - {str(item)}' for i, item in enumerate(optionList)])
	optionText += '\nPlease select an option: ' if prompt is None else '\n' + prompt

	userChoice = discreteInput(optionText, optionList)
	
	return userChoice

def createGraph() -> Graph:
	newGraph = Graph()
	graphWeighted = discreteInput('Is graph weighted (y/n): ', ['y', 'n'], False)
	graphDirected = discreteInput('Is graph directed (y/n): ', ['y', 'n'], False)

	while True:
		nodeName = input('Enter new node\'s name (\'-exit\' to exit): ')
		if nodeName == '-exit':
			break
		while nodeName in [node.name for node in newGraph.nodes]:
			print('Name of node must be unique.')
			nodeName = input('Enter new node\'s name: ')

		xCoord = intInput('Enter the note\'s x-coordinate: ')
		yCoord = intInput('Enter the note\'s y-coordinate: ')
		
		newNode = Node(nodeName, xCoord, yCoord)
		newGraph.addNode(newNode)

	while True:
		if len(newGraph.nodes) == 0:
			print('No other nodes to connect to.')
			break
		
		nodeNamesList = [node.name for node in newGraph.nodes]
		connectionFrom = menu(nodeNamesList + ['exit'], 'Enter node to connect: ') # possible issue regarding the use of node dict
		if connectionFrom == 'exit':
			break
		nodeNamesList.remove(connectionFrom)
		connectionTo = menu(nodeNamesList + ['exit'], f'Enter node to connect {connectionFrom} to: ')
		if connectionTo == 'exit':
			break

		

		if graphWeighted == 'y':
			weight = intInput('Enter edge weight: ', True)
		else:
			weight = 1

		newGraph.getNodeByName(connectionFrom).addEdge(newGraph.getNodeByName(connectionTo), weight)

	if graphDirected.lower() == 'y':
		return newGraph
	
	copiedGraph = copy.deepcopy(newGraph)

	for node in newGraph.nodes:
		for edge in node.edges:
			copiedGraph.getNodeByName(edge.name).addEdge(copiedGraph.getNodeByName(node.name), node.edges[edge])
	
	return copiedGraph


def loadGraph(filename: str):
	FILE_DIR = SAVES_DIR / filename

	try:
		with open(FILE_DIR, 'rt') as f:
			graphDict = json.loads(f.read())
	except FileNotFoundError as e:
		print(f'File cannot be loaded: {e}')
		return
	
	loadedGraph = Graph()

	for nodeName in graphDict:
		newNode = Node(nodeName, graphDict[nodeName]['meta']['x_coord'], graphDict[nodeName]['meta']['y_coord'])
		loadedGraph.addNode(newNode)
	
	print(loadedGraph)

	for nodeName in graphDict:
		for edgeNode in graphDict[nodeName]['edges']:
			loadedGraph.getNodeByName(nodeName).addEdge(loadedGraph.getNodeByName(edgeNode), graphDict[nodeName]['edges'][edgeNode])
	
	return loadedGraph


def main():
	
	
	testingOption = input('Would you like to create a new graph (1) or load a saved one (2): ')
	while testingOption not in ['1', '2']:
		testingOption = input('Would you like to create a new graph (1) or load a saved one (2): ')
	
	if testingOption == '1':
		graph = createGraph()
	else:
		filename = input('Enter filename (no ext.): ')
		filename = filename if filename != '' else 'testing1'
		filenameJson = filename + '.json'

		graph = loadGraph(filenameJson)
	
	graph.print()

	print(f'Is weighted: {graph.isWeighted()}, Is directed: {graph.isDirected()}')

	print('-'*50)
	print('A*'.center(50))
	graph.a_star(graph.nodes[0], graph.getNodeByName('d'))
	print('-'*50)
	# print(' -> '.join([node.name for node in graph.dijkstra(graph.nodes[0], graph.getNodeByName('d'))]))


	graph.export(f'{filename}.txt')
	graph.jsonExport(filename)
	graph.printAdjacencyList(True)
	graph.printAdjacencyMatrix()

	graph.exportAdjacencyMatrix()

if __name__ == '__main__':
	main()
