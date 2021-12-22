initial_testing_graph = [
    {'name': 'A', 'pos': 'start', 'links': [
        {'node': 'B', 'weight': 1},
        {'node': 'C', 'weight': 5},
        {'node': 'G', 'weight': 2}
    ]},
    {'name': 'B', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 1},
        {'node': 'C', 'weight': 4},
        {'node': 'D', 'weight': 1},
    ]},
    {'name': 'C', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 5},
        {'node': 'G', 'weight': 2},
        {'node': 'H', 'weight': 7},
        {'node': 'E', 'weight': 10},
        {'node': 'D', 'weight': 5},
        {'node': 'B', 'weight': 4},
    ]},
    {'name': 'D', 'pos': 'middle', 'links': [
        {'node': 'B', 'weight': 1},
        {'node': 'C', 'weight': 5},
        {'node': 'E', 'weight': 8},
    ]},
    {'name': 'E', 'pos': 'middle', 'links': [
        {'node': 'D', 'weight': 8},
        {'node': 'C', 'weight': 10},
        {'node': 'H', 'weight': 7},
        {'node': 'F', 'weight': 4},
    ]},
    {'name': 'F', 'pos': 'end', 'links': [
        {'node': 'E', 'weight': 4},
        {'node': 'H', 'weight': 2},
    ]},
    {'name': 'G', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 2},
        {'node': 'C', 'weight': 2},
        {'node': 'H', 'weight': 20},
    ]},
    {'name': 'H', 'pos': 'middle', 'links': [
        {'node': 'G', 'weight': 20},
        {'node': 'C', 'weight': 7},
        {'node': 'E', 'weight': 7},
        {'node': 'F', 'weight': 2},
    ]},
]

testing_graph_2 = [
    {'name': 'A', 'pos': 'start', 'links': [
        {'node': 'B', 'weight': 1},
        {'node': 'C', 'weight': 14},
        {'node': 'D', 'weight': 8},
    ]},
    {'name': 'B', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 1},
        {'node': 'C', 'weight': 9},
        {'node': 'E', 'weight': 8},
    ]},
    {'name': 'C', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 14},
        {'node': 'B', 'weight': 9},
        {'node': 'D', 'weight': 7},
        {'node': 'E', 'weight': 1},
    ]},
    {'name': 'D', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 8},
        {'node': 'C', 'weight': 7},
        {'node': 'E', 'weight': 2},
        {'node': 'F', 'weight': 10},
    ]},
    {'name': 'E', 'pos': 'middle', 'links': [
        {'node': 'B', 'weight': 8},
        {'node': 'C', 'weight': 1},
        {'node': 'D', 'weight': 2},
        {'node': 'F', 'weight': 4},
    ]},
    {'name': 'F', 'pos': 'end', 'links': [
        {'node': 'D', 'weight': 10},
        {'node': 'E', 'weight': 4},
    ]},
]

testing_graph_3 = [
    {'name': 'A', 'pos': 'start', 'links': [
        {'node': 'D', 'weight': 1},
        {'node': 'B', 'weight': 2},
    ]},
    {'name': 'B', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 2},
        {'node': 'C', 'weight': 5},
    ]},
    {'name': 'C', 'pos': 'end', 'links': [
        {'node': 'B', 'weight': 5},
    ]},
    {'name': 'D', 'pos': 'middle', 'links': [
        {'node': 'A', 'weight': 1},
    ]},
]