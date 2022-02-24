
def getInt(prompt):
	userInput = input(prompt)
	while not userInput.isdigit():
		print('Please enter a valid integer.')
		userInput = input(prompt)
	
	return int(userInput)

def getMostFrequentInList(lst: list) -> list:
	listSet = set(lst)

	mostFrequentInfo = {'item': None, 'frequency': 0}
	frequentList = []

	for item in listSet:
		if lst.count(item) > mostFrequentInfo['frequency']:
			mostFrequentInfo['item'] = item
			mostFrequentInfo['frequency'] = lst.count(item)
		elif lst.count(item) == mostFrequentInfo['frequency']:
			frequentList.append(mostFrequentInfo)
			frequentList.append({'item': item, 'frequency': lst.count(item)})

	return [mostFrequentInfo] if frequentList == [] else frequentList

numberOfInts = getInt('How many integers will you enter: ')
listOfInts = []

for i in range(numberOfInts):
	listOfInts.append(getInt('Enter an integer: '))

mostFrequentInfo = getMostFrequentInList(listOfInts)

print(f'{", ".join([str(item["item"]) for item in mostFrequentInfo])} {"is most frequent" if len(mostFrequentInfo) == 1 else "are the most frequent"} with {mostFrequentInfo[0]["frequency"]} occurrence{"s" if mostFrequentInfo[0]["frequency"] > 1 else ""}{"" if len(mostFrequentInfo) == 1 else " each"}.')
