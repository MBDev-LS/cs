
import json
from pathlib import Path

from tabulate import tabulate
import copy


class Node():
	def __init__(self, name: str, edges: dict=None) -> None:
		self.name = name
		self.edges = edges if edges is not None else {}
	
	def addEdge(self, node, weight: int):
		self.edges[node] = weight
	
	def __str__(self) -> str:
		return f'{str(self.name)} -> {", ".join([node.name for node in self.edges])}'

class Graph():
	def __init__(self, nodes: list=None) -> None:
		self.nodes = nodes if nodes is not None else []

	def getNodeByName(self, nameToSearch: str):
		for node in self.nodes:
			if nameToSearch == node.name:
				return node
		
		return None
	
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
	

	def printAdjacencyList(self) -> None:
		tableData = []

		for node in self.nodes:
			nodeDict = {}
			for connectedNode in node.edges:
				nodeDict[connectedNode.name] = node.edges[connectedNode]

			tableData.append([node.name, str(nodeDict)])
		
		print(tabulate(tableData, headers=['Node', 'Edges'], tablefmt="fancy_grid"))

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
			f.write(json.dumps(nodeDict))
	
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
		connectionFrom = discreteInput(f'Nodes: {", ".join(nodeNamesList)}\n' + 'Enter node to connect (\'-exit\' to exit): ', [node.name for node in newGraph.nodes] + ['-exit']) # possible issue regarding the use of node dict
		if connectionFrom == '-exit':
			break
		nodeNamesList.remove(connectionFrom)
		connectionTo = discreteInput(f'Nodes: {", ".join(nodeNamesList)}\n' + f'Enter node to connect {connectionFrom} to (\'-exit\' to exit): ', nodeNamesList + ['-exit']) # possible issue regarding the use of node dict
		if connectionTo == '-exit':
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
	
	graph = createGraph()
	# graph = loadGraph(filenameJson)
	graph.print()

	graph.export(f'{filename}.txt')
	graph.jsonExport(filename)
	graph.printAdjacencyList()
	graph.printAdjacencyMatrix()

if __name__ == '__main__':
	main()