
numOfDigits = int(input('Enter the number of numeric digits you would like to enter: '))

digitList = []
for i in range(numOfDigits):
	digitList.append(int(input('Enter a digit: ')))

frequencies = []

for digit in set(digitList):
	frequencies.append(digitList.count(digit))

frequencies.sort()

if numOfDigits == 0:
	print("Really?")
elif numOfDigits == 1:
	print(frequencies[-1])
else:
	print(frequencies[-1] if frequencies[-1] != frequencies[-2] else 'Data was multimodal')

# Watch out for edge cases, numOfDigits == 1
# caught me out here, despite the fact 
# I realised it may cause issues when
# I was writing the code.

# For numOfDigits == 0, I was unsure
# what the program should do, so, if
# numOfDigits == 0, it does nothing.