
import json
from pathlib import Path

from tabulate import tabulate
import copy
from math import inf


class Node():
	def __init__(self, name: str, edges: dict=None, start: bool=False, end: bool=False) -> None:
		self.name = name
		self.edges = edges if edges is not None else {}
		self.cost = inf
		self.previousNode = None
		self.start = start
		self.end = end
		self.shortestPath = []
	
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

	def bfs(self, startNode: Node=None) -> list:
		startNode = startNode if startNode is not None else self.startNode
		queue = [startNode]
		traversalOrder = [startNode]

		while len(queue) > 0:
			currentNode = queue.pop(0)
			print(f'Branching from {currentNode.name}')

			for edgeNode in currentNode.edges:
				if currentNode.cost + currentNode.edges[edgeNode] < edgeNode.cost:
					if edgeNode not in traversalOrder:
						print(f'From {currentNode} found {edgeNode.name}')
						traversalOrder.append(edgeNode)
					
					
					edgeNode.shortestPath = currentNode.shortestPath + [currentNode]
					edgeNode.cost = currentNode.cost + currentNode.edges[edgeNode]
					edgeNode.previousNode = currentNode

					queue.append(edgeNode)
	
		return traversalOrder

	def setStartNode(self, newStartNode) -> None:
		self.startNode = newStartNode
		self.startNode.cost = 0

	def setEndNode(self, newEndNode) -> None:
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
				self.bfs()

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

	def export(self, filename) -> None:
		BASE_DIR = Path(__file__).resolve().parent
		SAVES_DIR = BASE_DIR / 'saves'
		FILE_DIR = SAVES_DIR / filename
		nodesDict = {}
		for node in self.nodes:
			nodeDict = {}
			for connectedNode in node.edges:
				nodeDict[connectedNode.name] = node.edges[connectedNode]

			nodesDict[node.name] = nodeDict

		with open(FILE_DIR, 'w+') as f:
			f.write(json.dumps(nodesDict))
	
	def jsonExport(self, filename) -> None:
		filenameWithExt = filename + '.json'
		BASE_DIR = Path(__file__).resolve().parent
		SAVES_DIR = BASE_DIR / 'saves'
		FILE_DIR = SAVES_DIR / filenameWithExt
		nodesDict = {}
		for node in self.nodes:
			nodeDict = {}
			for connectedNode in node.edges:
				nodeDict[connectedNode.name] = node.edges[connectedNode]

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

def intInput(prompt: str):
	userInput = input(prompt)

	while not userInput.isdigit():
		userInput = input(prompt)
	
	return int(userInput)

def menu(optionList: list, prompt=None):
	optionText = 'Options\n'
	optionText += '\n'.join([f'{i+1} - {str(item)}' for i, item in enumerate(optionList)])
	optionText += '\nPlease select an option: ' if prompt is None else '\n' + prompt

	userChoice = discreteInput(optionText, [str(i+1) for i in range(len(optionList))])
	
	return optionList[int(userChoice)-1]

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
		
		newNode = Node(nodeName)
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
			weight = intInput('Enter edge weight: ')
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
	BASE_DIR = Path(__file__).resolve().parent
	SAVES_DIR = BASE_DIR / 'saves'
	FILE_DIR = SAVES_DIR / filename

	try:
		with open(FILE_DIR, 'rt') as f:
			graphDict = json.loads(f.read())
	except FileNotFoundError as e:
		print(f'File cannot be loaded: {e}')
		return
	
	loadedGraph = Graph()

	for nodeName in graphDict:
		newNode = Node(nodeName)
		loadedGraph.addNode(newNode)
	
	print(loadedGraph)

	for nodeName in graphDict:
		for edgeNode in graphDict[nodeName]:
			loadedGraph.getNodeByName(nodeName).addEdge(loadedGraph.getNodeByName(edgeNode), graphDict[nodeName][edgeNode])
	
	return loadedGraph


def main():
	filename = 'testing'
	filenameJson = filename + '.json'
	
	testingOption = input('Would you like to create a new graph (1) or load a saved one (2): ')
	while testingOption not in ['1', '2']:
		testingOption = input('Would you like to create a new graph (1) or load a saved one (2): ')
	
	if testingOption == '1':
		graph = createGraph()
	else:
		graph = loadGraph(filenameJson)
	
	graph.print()

	print(f'Is weighted: {graph.isWeighted()}, Is directed: {graph.isDirected()}')

	graph.setStartNode(graph.nodes[0])
	graph.setEndNode(graph.nodes[-1])
	traversalOrder = graph.bfs()
	print('----')
	print(' '.join([node.name for node in traversalOrder]))

	graph.export(f'{filename}.txt')
	graph.jsonExport(filename)
	graph.printAdjacencyList(True)
	graph.printAdjacencyMatrix()

	graph.exportAdjacencyMatrix()

if __name__ == '__main__':
	main()
