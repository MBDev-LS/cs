
def isAHarshadNumber(num: int) -> bool:
	digitList = [char for char in str(num)]

	digitSum = sum(int(charStr) for charStr in digitList)

	return num % digitSum == 0


def getNthHarshadNumber(n: int) -> int:
	harshadCount = 0
	numberBeingTested = 1
	
	while harshadCount < n:
		if isAHarshadNumber(numberBeingTested) is True:
			harshadCount += 1

			if harshadCount == n:
				return numberBeingTested
		
		numberBeingTested += 1


def intInput(prompt: str) -> int:
	userInput = input(prompt)

	while not userInput.isdigit():
		userInput = input(prompt)
	
	return int(userInput)


def main():
	nTarget = intInput('Enter a number: ')
	nthHarshadNumber = getNthHarshadNumber(nTarget)

	print(f'Harshad Number No. {nTarget}: {nthHarshadNumber}')


if __name__ == '__main__':
	main()
