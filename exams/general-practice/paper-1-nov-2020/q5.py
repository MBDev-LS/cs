
def getNChars(n) -> list:
	charList = []

	for i in range(n):
		charList.append(input('Enter a character: '))
	
	return charList


def getCharCountFromList(lst) -> int:
	charSet = set(lst)
	charCountList = []

	for char in charSet:
		charCountList.append({'char': char, 'count': lst.count(char)})
	
	return charCountList


def intInput(promt: str) -> int:
	userInput = input(promt)
	
	while not userInput.isdigit():
		userInput = input(promt)
	
	return int(userInput)

def main():
	numOfChars = intInput('Enter the number of characters you would like to input: ')
	charList = getNChars(numOfChars)
	charCountList = sorted(getCharCountFromList(charList), key=lambda d: d['count'])
	print(charCountList)

	if len(charCountList) == 0:
		print('No data provided')
	elif len(charCountList) == 1:
		print('No data provided')
	elif charCountList[-1]["count"] < 2:
		print('Data was multimodal.')
	else:
		print(f'\nMost Frequently Entered: {charCountList[-1]["char"]}\nEntered {charCountList[-1]["count"]} time(s)\n')


if __name__ == '__main__':
	main()
