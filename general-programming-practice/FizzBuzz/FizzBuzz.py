
import time

maxNum = 100

counters = {
	'fizz': 0,
	'buzz': 0,
	'fizzbuzz': 0
}

t0 = time.perf_counter()

for i in range(1, maxNum+1):
	output = ''
	output += 'Fizz' if i % 3 == 0 else ''
	output += 'Buzz' if i % 5 == 0 else ''

	if output == 'Fizz':
		counters['fizz'] += 1
	elif output == "Buzz":
		counters['buzz'] += 1
	elif output == 'FizzBuzz':
		counters['fizzbuzz'] += 1

	print(f'{str(i).rjust(len(str(maxNum)))}: {i if len(output) == 0 else output}')

t1 = time.perf_counter()

print('\n', t1-t0, counters)


#  To 1 million (with print): 11.432852125 {'fizz': 266667, 'buzz': 133334, 'fizzbuzz': 66666}
#  To 1 million (without print): 0.681378125 {'fizz': 266667, 'buzz': 133334, 'fizzbuzz': 66666}