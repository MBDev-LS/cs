NumberIn = int(input("Enter a positive whole number: "))
NumberOut = 0
Count = 0
while NumberIn > 0:
	Count += 1
	PartValue = NumberIn % 2
	NumberIn = NumberIn // 2
	for i in range(1, Count):
		PartValue = PartValue * 10
	
	NumberOut += PartValue

print(f'The result is: {NumberOut}')