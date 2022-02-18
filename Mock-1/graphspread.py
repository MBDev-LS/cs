graphs = []
path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (1, 18), (1, 17), (1, 16), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (1, 19), (2, 19), (3, 18), (3, 17), (3, 16), (3, 15), (3, 14), (3, 13), (3, 12), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (3, 19), (4, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14), (5, 13), (5, 12), (5, 11), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16), (6, 17), (6, 18), (5, 19), (6, 19), (7, 18), (7, 17), (7, 16), (7, 15), (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (7, 19), (8, 19), (9, 18), (9, 17), (9, 16), (9, 15), (9, 14), (9, 13), (9, 12), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (9, 19), (10, 19), (11, 18), (11, 17), (11, 16), (11, 15), (11, 14), (11, 13), (11, 12), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (11, 5), (11, 4), (11, 3), (11, 2), (11, 1), (11, 0), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (12, 18), (11, 19), (12, 19), (13, 18), (13, 17), (13, 16), (13, 15), (13, 14), (13, 13), (13, 12), (13, 11), (13, 10), (13, 9), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (13, 3), (13, 2), (13, 1), (13, 0), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (13, 19), (14, 19), (15, 18), (15, 17), (15, 16), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (15, 9), (15, 8), (15, 7), (15, 6), (15, 5), (15, 4), (15, 3), (15, 2), (15, 1), (15, 0), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (17, 7), (17, 6), (17, 5), (17, 4), (17, 3), (17, 2), (17, 1), (17, 0), (18, 0), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (17, 8), (18, 8), (19, 7), (19, 6), (19, 5), (19, 4), (19, 3), (19, 2), (19, 1), (19, 0), (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (19, 8), (19, 9), (19, 10), (19, 11), (18, 12), (17, 12), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17), (16, 18), (15, 19), (16, 19), (17, 18), (17, 17), (17, 16), (17, 15), (17, 14), (17, 13), (18, 13), (18, 14), (18, 15), (18, 16), (18, 17), (18, 18), (17, 19), (18, 19), (19, 18), (19, 17), (19, 16), (19, 15), (19, 14), (19, 13), (19, 12), (20, 11), (20, 10), (20, 9), (20, 8), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (21, 2), (21, 1), (21, 0), (22, 0), (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (21, 8), (21, 9), (21, 10), (21, 11), (20, 12), (20, 13), (20, 14), (20, 15), (20, 16), (20, 17), (20, 18), (19, 19), (20, 19), (21, 18), (21, 17), (21, 16), (21, 15), (21, 14), (21, 13), (21, 12), (22, 11), (22, 10), (22, 9), (22, 8), (23, 7), (23, 6), (23, 5), (23, 4), (23, 3), (23, 2), (23, 1), (23, 0), (24, 0), (24, 1), (24, 2), (24, 3), (24, 4), (24, 5), (24, 6), (24, 7), (23, 8), (23, 9), (23, 10), (23, 11), (22, 12), (22, 13), (22, 14), (22, 15), (22, 16), (22, 17), (22, 18), (21, 19), (22, 19), (23, 18), (23, 17), (23, 16), (23, 15), (23, 14), (23, 13), (23, 12), (24, 11), (24, 10), (24, 9), (24, 8), (25, 7), (25, 6), (25, 5), (25, 4), (25, 3), (25, 2), (25, 1), (25, 0), (26, 0), (26, 1), (26, 2), (26, 3), (26, 4), (26, 5), (26, 6), (26, 7), (25, 8), (25, 9), (25, 10), (25, 11), (24, 12), (24, 13), (24, 14), (24, 15), (24, 16), (24, 17), (24, 18), (23, 19), (24, 19), (25, 18), (25, 17), (25, 16), (25, 15), (25, 14), (25, 13), (25, 12), (26, 11), (26, 10), (26, 9), (26, 8), (27, 7), (27, 6), (27, 5), (27, 4), (27, 3), (27, 2), (27, 1), (27, 0), (28, 0), (28, 1), (28, 2), (28, 3), (28, 4), (28, 5), (28, 6), (28, 7), (27, 8), (27, 9), (27, 10), (27, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16), (26, 17), (26, 18), (25, 19), (26, 19), (27, 18), (27, 17), (27, 16), (27, 15), (27, 14), (27, 13), (27, 12), (28, 11), (28, 10), (28, 9), (28, 8), (29, 7), (29, 6), (29, 5), (29, 4), (30, 3), (29, 2), (29, 1), (29, 0), (30, 0), (30, 1), (30, 2), (31, 1), (31, 0), (32, 0), (32, 1), (31, 2), (31, 3), (30, 4), (30, 5), (30, 6), (30, 7), (29, 8), (29, 9), (29, 10), (29, 11), (28, 12), (28, 13), (28, 14), (28, 15), (28, 16), (28, 17), (28, 18), (27, 19), (28, 19), (29, 18), (29, 17), (29, 16), (29, 15), (29, 14), (29, 13), (29, 12), (30, 11), (30, 10), (30, 9), (30, 8), (31, 7), (31, 6), (31, 5), (31, 4), (32, 3), (32, 2), (33, 1), (33, 0), (34, 0), (34, 1), (33, 2), (33, 3), (32, 4), (32, 5), (32, 6), (32, 7), (31, 8), (31, 9), (31, 10), (31, 11), (30, 12), (30, 13), (30, 14), (30, 15), (30, 16), (30, 17), (30, 18), (29, 19), (30, 19), (31, 18), (31, 17), (31, 16), (31, 15), (31, 14), (31, 13), (31, 12), (32, 11), (32, 10), (32, 9), (32, 8), (33, 7), (33, 6), (33, 5), (33, 4), (34, 3), (34, 2), (34, 4), (34, 5), (34, 6), (34, 7), (33, 8), (33, 9), (33, 10), (33, 11), (32, 12), (32, 13), (32, 14), (32, 15), (32, 16), (32, 17), (32, 18), (31, 19), (32, 19), (33, 18), (33, 17), (33, 16), (33, 15), (33, 14), (33, 13), (33, 12), (34, 11), (34, 10), (34, 9), (34, 8), (34, 12), (34, 13), (34, 14), (34, 15), (34, 16), (34, 17), (34, 18), (33, 19), (34, 19)]

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'

FIELDLENGTH = 20 
FIELDWIDTH = 35
from copy import deepcopy

import time

def CreateNewField(): 
	Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
	Row = FIELDLENGTH // 2
	Column = FIELDWIDTH // 2
	Field[Row][Column] = SEED

	return Field

def Display(Field):
	for Row in range(FIELDLENGTH):
		for Column in range(FIELDWIDTH):
			print(Field[Row][Column], end='')
		print('|{0:>3}'.format(Row))
	print()

baseField = CreateNewField()
graphs.append(deepcopy(baseField))

for coords in path:
    newGraph = deepcopy(graphs[-1])

    newGraph[coords[1]][coords[0]] = '%'

    graphs.append(newGraph)

for graph in graphs:
    Display(graph)
    time.sleep(0.05)

