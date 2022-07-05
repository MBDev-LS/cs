
for i in range(1, 19):
	output = ''
	output += 'Fizz' if i % 3 == 0 else ''
	output += 'Buzz' if i % 5 == 0 else ''

	print(f'{i}: {i if len(output) == 0 else output}')