
from math import inf
from graphs import initial_testing_graph as node_dict_list
import time


class Node:
	def __init__(self, name: str, links: list = None, start: bool = False, end: bool = False):
		self.active = True
		if start is True:
			self.cost = 0
		else:
			self.cost = inf
		self.name = name
		self.links = [] if links is None else links
		self.start = start
		self.end = end
		self.previous_node = None

	def __str__(self):
		return f'<Node {self.name} [{", ".join([link.node1.name + ": " + str(link.weight) for link in self.links])}] ({self.cost})>'

	def __repr__(self):
		return f'Node(name={self.name}, links={self.links}, start={self.start}, end={self.end})'


class Link:
	def __init__(self, node0: Node, node1: Node, weight: int):
		self.node0 = node0
		self.node1 = node1
		self.weight = weight

	def __str__(self):
		return f'<link n0={self.node0.name} n1={self.node1.name} weight={self.weight}>'

	def __repr__(self):
		return f'Link(node0={self.node0}, node1={self.node1}, weight={self.weight})'


def get_node_index_by_name(name: Node, node_list: list):
	for i, node in enumerate(node_list):
		if node.name == name:
			return i
	return -1


def sort_node_list(node_list: list):
	return sorted(node_list, key=lambda n: n.cost, reverse=True)


t0 = time.perf_counter()

node_list = []

for node in node_dict_list:
	if node['pos'] == 'start':
		node_list.append(Node(node['name'], start=True))
	elif node['pos'] == 'end':
		node_list.append(Node(node['name'], end=True))
	else:
		node_list.append(Node(node['name']))

for node in node_dict_list:
	for linked_node in node['links']:
		node0 = get_node_index_by_name(node['name'], node_list)
		node1 = get_node_index_by_name(linked_node['node'], node_list)
		if node0 == -1 or node1 == -1:
			raise('node_dict_list not valid')

		node_list[node0].links.append(
			Link(node_list[node0], node_list[node1], linked_node['weight']))

working_stack = sort_node_list(node_list)
finished_list = []

working_stack.append(node_list.pop())
finished = False

while finished is not True:
	working_stack = sort_node_list(working_stack)
	print('Working Stack: [', ', '.join([str(node)
										for node in working_stack]) + ' ]')
	print('Finished List: [', ', '.join([str(node)
										for node in finished_list]) + ' ]')

	print('\n'+'LINKS'.center(20, '='))
	for link in working_stack[-1].links:
		print(link)
		if link.node1 in working_stack:
			if working_stack[-1].cost + link.weight < link.node1.cost:
				print(
					f'\n{working_stack[-1].cost + link.weight} is less than {link.node1.cost} so new route is faster\n')
				link.node1.cost = working_stack[-1].cost + link.weight
				link.node1.previous_node = working_stack[-1]
			else:
				print(
					f'\n{working_stack[-1].cost + link.weight} is more than or equal {link.node1.cost} so new route is slower or the same\n')
		else:
			print(
				f'\nNot checking link, {link.node1.name} is not in the working stack\n')

	if working_stack[-1].end is not True:  # May not be necessary, not sure
		finished_list.append(working_stack.pop(-1))
	else:
		finished = True

finished_list.append(working_stack.pop())

final_path = []
final_path.append(finished_list[-1])

while final_path[-1].start is not True:
	final_path.append(finished_list.pop(
		finished_list.index(final_path[-1].previous_node)))

final_path.reverse()

t1 = time.perf_counter()

print('Result'.center(40, '='))

print('Shortest Path:', ' -> '.join([node.name for node in final_path]))
print('Path Length:', final_path[-1].cost)
print(f'Time Taken (seconds): {t1-t0}')
