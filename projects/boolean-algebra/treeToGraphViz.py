
from pprint import pprint
import testing_main

import graphviz
import dot2tex

import re

dot = graphviz.Graph(comment='Boolean Expression')
dot.attr(rankdir='RL')  

expression = '(A+B).(C+D)'
expression = 'A.B.C+A.C+A.C.D+A.C.D'.upper()

nameDict = {
    '~': {'name': 'not', 'nextCount': 1, 'placeholderShape': 'square', 'actualShape': 'not port'},
    '.': {'name': 'and', 'nextCount': 1, 'placeholderShape': 'ellipse', 'actualShape': 'and port'},
    '+': {'name': 'or', 'nextCount': 1, 'placeholderShape': 'diamond', 'actualShape': 'or port'},
}

variables = [char for char in expression if char not in list(nameDict.keys()) + ['(', ')']]

for var in variables:
    nameDict[var] = {'name': var.lower(), 'nextCount': 1, 'placeholderShape': 'circle', 'actualShape': 'circle'}

tree = testing_main.expressionToTree(expression)

def drawTree(baseNode, nameDict: dict, dot) -> str:

    print("Dealing with node:")
    baseNode.printDescendants()

    if baseNode.graphId == '':
        baseNode.setGraphId(f'{nameDict[baseNode.value]["name"]}{nameDict[baseNode.value]["nextCount"]}')
        
        nameDict[baseNode.value]["nextCount"] += 1
    
    
    dot.node(baseNode.graphId, baseNode.value, shape=nameDict[baseNode.value]["placeholderShape"])
    print(f'Added "{baseNode.graphId} [shape={nameDict[baseNode.value]["placeholderShape"]}, label="{baseNode.value}"]\\n" as main addition')
    
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

dot = drawTree(tree, nameDict, dot)
dot.render('projects/boolean-algebra/doctest-output/test.gv').replace('\\', '/')

print('-------\n\n\n\n')
print(dot.source)
texSource = dot2tex.dot2tex(dot.source, format='tikz', crop=True)

sourceList = texSource.split(';')
newTexGraphInner = ' \draw\n'

for line in sourceList:
    formattedLine = line.replace('\n', '').strip()
    reMatch = re.match(r"\\node \((and\d+|or\d+|not\d+|[a-z]\d+)\) at \((\d+\.\d+bp,\d+\.\dbp)\) \[draw,(diamond|ellipse|square|circle)\] \{([A-Z]|[+.~])\}", formattedLine)
    if reMatch is not None:
        pprint(formattedLine)
        lineId = reMatch.group(1)
        coordsNoBrackets = reMatch.group(2)
        shapeType = reMatch.group(3)
        value = reMatch.group(4)

        print(lineId, coordsNoBrackets, shapeType, value)
        
        if shapeType == 'circle':
            newTexGraphInner += f'circle [radius = 10pt]node[circle,fill=white,minimum size=10pt]' + '{' + value + '}\n'
        else:
            newTexGraphInner += f'({coordsNoBrackets}) node[{nameDict[value]["actualShape"]}] ({lineId}) ' + '{}\n'


print(newTexGraphInner)