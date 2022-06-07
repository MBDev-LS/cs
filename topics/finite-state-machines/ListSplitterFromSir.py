def listSplitter(l, chopper):
	bits = [[]]
	for item in l:
		if item is chopper:
			bits.append([])
		else:
			bits[-1].append(item)
	results = []
	for item in bits:
		if len(item):
			results.append(item)
	return results


stuff = [1, 2, 3, 4, 3, 3, 5]

print(listSplitter(stuff, 3))
