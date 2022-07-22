
def add(num1, num2):
	res = 0
	counter1 = 0
	while counter1 < num1:
		res += 1
		counter1 += 1

	counter2 = 0
	while counter2 < num2:
		res += 1
		counter2 += 1
	
	return res

print(add(100, 100))