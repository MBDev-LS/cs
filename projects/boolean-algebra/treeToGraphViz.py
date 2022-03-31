
import testing_main
import graphviz
dot = graphviz.Digraph(comment='Boolean Expression')

expression = '(A+B).(C+D)'
expression = 'A.B.C+A.C+A.C.D+A.C.D'

nameDict = {
    '~': {'name': 'not', 'nextCount': 1},
    '.': {'name': 'and', 'nextCount': 1},
    '+': {'name': 'or', 'nextCount': 1},
}

variables = [char for char in expression if char not in list(nameDict.keys()) + ['(', ')']]

for var in variables:
    nameDict[var] = {'name': var.lower(), 'nextCount': 1}

tree = testing_main.expressionToTree(expression)

def drawTree(baseNode, nameDict: dict, graphText: str=None) -> str:
    graphText = graphText if graphText is not None else ''

    print("Dealing with node:")
    baseNode.printDescendants()

    if baseNode.graphId == '':
        baseNode.setGraphId(f'{nameDict[baseNode.value]["name"]}{nameDict[baseNode.value]["nextCount"]}')
        
        nameDict[baseNode.value]["nextCount"] += 1
    
    graphText += f'{baseNode.graphId} [shape=circle, label="{baseNode.value}"]\n'
    print(f'Added "{baseNode.graphId} [shape=circle, label="{baseNode.value}"]\\n" as main addition')
    
    if baseNode.leftChild is not None:
        if baseNode.leftChild.graphId == '':
            baseNode.leftChild.setGraphId(f'{nameDict[baseNode.leftChild.value]["name"]}{nameDict[baseNode.leftChild.value]["nextCount"]}')
            nameDict[baseNode.leftChild.value]["nextCount"] += 1
            
        
        graphText += f'{baseNode.graphId} -- {baseNode.leftChild.graphId}\n'
        print(f'Added "{baseNode.graphId} -- {baseNode.leftChild.graphId}\\n" as sub addition on the left')
        graphText = drawTree(baseNode.leftChild, nameDict, graphText)

    if baseNode.rightChild is not None:
        if baseNode.rightChild.graphId == '':
            baseNode.rightChild.setGraphId(f'{nameDict[baseNode.rightChild.value]["name"]}{nameDict[baseNode.rightChild.value]["nextCount"]}')
            nameDict[baseNode.rightChild.value]["nextCount"] += 1
            
        
        graphText += f'{baseNode.graphId} -- {baseNode.rightChild.graphId}\n'
        print(f'Added "{baseNode.graphId} -- {baseNode.rightChild.graphId}\\n" as sub addition on the right')
        graphText = drawTree(baseNode.rightChild, nameDict, graphText)
    
    return graphText

print(drawTree(tree, nameDict))
