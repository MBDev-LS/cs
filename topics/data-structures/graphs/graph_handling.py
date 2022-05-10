
import json

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

	def export(self, filename) -> None:
		nodeDict = {}
		for node in self.nodes:
			nodeDict[node.name] = [connectedNode.name for connectedNode in node.edges]
		
		with open(filename, 'w+') as f:
			f.write(json.dumps(nodeDict))
	
	def jsonExport(self, filename) -> None:
		nodeDict = {}
		for node in self.nodes:
			nodeDict[node.name] = [connectedNode.name for connectedNode in node.edges]
		
		with open(filename + '.json', 'wt') as f:
			f.write(json.dumps(nodeDict))

	def print(self) -> None:
		outputString = '\n'.join([str(node) for node in self.nodes])
		print(outputString)

def discreteInput(prompt: str, possibleInputs: list, caseSensitive: bool=True):
	userInput = input(prompt)

	while (userInput not in possibleInputs and caseSensitive) or (userInput.lower() not in [possibleInput.lower() for possibleInput in possibleInputs]):
		userInput = input(prompt)

	
	return userInput

def intInput(prompt: str):
	userInput = input(prompt)

	while not userInput.isdigit():
		userInput = input(prompt)
	
	return userInput



def createGraph() -> Graph:
	newGraph = Graph()
	graphWeighted = discreteInput('Is graph weighted (y/n): ', ['y', 'n'], False)

	while True:
		addNodeBool = discreteInput('Add node (y/n): ', ['y', 'n'], False)
		if addNodeBool == 'n':
			break

		nodeName = input('Enter new node\'s name: ')
		newNode = Node(nodeName)

		while True:
			addEdgeBool = discreteInput('Add edge (y/n): ', ['y', 'n'], False)
			if addEdgeBool == 'n':
				break
			elif len(newGraph.nodes) == 0:
				print('No other nodes to connect to.')
				break
			
			connectionTo = discreteInput(f'Nodes: {", ".join([node.name for node in newGraph.nodes])}\n' + 'Enter to connect new node to: ', [node.name for node in newGraph.nodes]) # possible issue regarding the use of node dict
			if graphWeighted == 'y':
				weight = intInput('Enter edge weight: ')
			else:
				weight = 1
			newNode.addEdge(newGraph.getNodeByName(connectionTo), weight)

		newGraph.addNode(newNode)

	return newGraph

def main():
	graph = createGraph()
	graph.print()

	graph.export('test1.txt')
	graph.jsonExport('test1')

if __name__ == '__main__':
	main()