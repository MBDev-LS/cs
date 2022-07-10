
numOfDigits = int(input('Enter the number of numeric digits you would like to enter: '))

digitList = [int(input('Enter a digit: ')) for i in range(numOfDigits)]
frequencies = [digitList.count(digit) for digit in set(digitList)]

frequencies.sort()

if numOfDigits == 1:
	print(frequencies[-1])
elif numOfDigits > 1:
	print(frequencies[-1] if frequencies[-1] != frequencies[-2] else 'Data was multimodal')
