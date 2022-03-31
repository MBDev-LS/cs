
import testing_main
import graphviz
dot = graphviz.Graph(comment='Boolean Expression')

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

def drawTree(baseNode, nameDict: dict, dot) -> str:

    print("Dealing with node:")
    baseNode.printDescendants()

    if baseNode.graphId == '':
        baseNode.setGraphId(f'{nameDict[baseNode.value]["name"]}{nameDict[baseNode.value]["nextCount"]}')
        
        nameDict[baseNode.value]["nextCount"] += 1
    
    
    dot.node(baseNode.graphId, baseNode.value, shape='circle')
    print(f'Added "{baseNode.graphId} [shape=circle, label="{baseNode.value}"]\\n" as main addition')
    
    if baseNode.leftChild is not None:
        if baseNode.leftChild.graphId == '':
            baseNode.leftChild.setGraphId(f'{nameDict[baseNode.leftChild.value]["name"]}{nameDict[baseNode.leftChild.value]["nextCount"]}')
            nameDict[baseNode.leftChild.value]["nextCount"] += 1
            
        
        dot.edge(baseNode.graphId, baseNode.leftChild.graphId)
        print(f'Added "{baseNode.graphId} -- {baseNode.leftChild.graphId}\\n" as sub addition on the left')
        dot = drawTree(baseNode.leftChild, nameDict, dot)

    if baseNode.rightChild is not None:
        if baseNode.rightChild.graphId == '':
            baseNode.rightChild.setGraphId(f'{nameDict[baseNode.rightChild.value]["name"]}{nameDict[baseNode.rightChild.value]["nextCount"]}')
            nameDict[baseNode.rightChild.value]["nextCount"] += 1
            
        
        dot.edge(baseNode.graphId, baseNode.rightChild.graphId)
        print(f'Added "{baseNode.graphId} -- {baseNode.rightChild.graphId}\\n" as sub addition on the right')
        dot = drawTree(baseNode.rightChild, nameDict, dot)
    
    return dot

drawTree(tree, nameDict, dot).render('projects/boolean-algebra/doctest-output/test.gv').replace('\\', '/')
